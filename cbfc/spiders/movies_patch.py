# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest
from cbfc.items import Movie
import json
import datetime

class MoviesPatchSpider(scrapy.Spider):
    name = 'movies_patch'

    start_urls = ["https://www.cbfcindia.gov.in"]

    error = open("./errors.log","a+")
    error.write("\n\n\n######## CBFC Movies Crawler "+str(datetime.datetime.now())+" ###########\n" )


    #start_urls = ['https://www.cbfcindia.gov.in/main/search_page_call.php?title=&lang1=&dt1=01/01/1920&dt2=01/01/1960']

    def parse(self, response):

        with open("data/missed.json") as f:
            m_list = json.load(f)

        for each in m_list:
            form_data = {
                "movie_id": str(each['m_id']),
                "lang_id": str(each['l_id'])
            }
            yield FormRequest(
                url = "https://www.cbfcindia.gov.in/main/search-result",
                formdata = form_data,
                meta = {
                    'dont_redirect': True,
                    'handle_httpstatus_list': [302],
                    'mid': each['m_id'],
                    'lid': each['l_id'],
                },
                callback = self.parse_details_page,
                errback = self.error_handler,
            )

    def parse_details_page(self, response):
        details = response.css("table")[0].css("tr")
        m_name = details[1].css("td")[1].css("::text").extract_first()
        m_lang = details[2].css("td")[1].css("::text").extract_first()
        m_category = details[3].css("td")[1].css("::text").extract_first()
        c_office = details[4].css("td")[1].css("::text").extract_first()
        c_no = details[5].css("td")[1].css("::text").extract_first()
        c_date = details[6].css("td")[1].css("::text").extract_first()
        m_leng = details[7].css("td")[1].css("::text").extract_first()
        m_producer = details[8].css("td")[1].css("::text").extract_first()
        c_applicant = details[9].css("td")[1].css("::text").extract_first()

        cutsList = list()
        
        if len(response.css("table")) == 2:
            cuts = response.css("table")[1].css("tr")    
            if len(cuts) > 2:
                for cut in cuts[2:]:
                    each = dict()
                    each['where'] = cut.css("td")[1].css("::text").extract_first()
                    each['desc'] = cut.css("td")[2].css("::text").extract_first()
                    each['guidline'] = cut.css("td")[3].css("::text").extract_first()
                    cutsList.append(each)
            
        yield Movie (
            m_id = response.meta['mid'],
            movie_name = m_name,
            movie_language = m_lang,
            movie_category = m_category,
            certificate_reg_office = c_office,
            certificate_no = c_no,
            certificate_date = c_date,
            movie_length = m_leng,
            movie_producer = m_producer,
            certificate_applicant = c_applicant,
            cuts = cutsList
        )

    def error_handler(self,failure):
        error_message = {
            "m_id" : failure.request.meta['mid'],
            "l_id": failure.request.meta['lid']
        }
        self.error.write(json.dumps(error_message) + "\n")