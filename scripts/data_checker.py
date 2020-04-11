import json
import requests

for i in range(1951, 2020):
    filename = "patch_data/"+str(i)+".json"
    with open(filename) as f:
        temp = json.load(f)

        URL = "https://www.cbfcindia.gov.in/main/search_page_call.php"
        PARAMS = {
            'title': "",
            'lang1': "",
            'dt1': "01/01/" + str(i),
            "dt2": "12/31/" + str(i)
        }

        r = requests.get(url = URL, params = PARAMS)
  
        # extracting data in json format 
        data = r.json()

        if(len(temp) != data['iTotalRecords']):
            print(i, len(temp), data['iTotalRecords'])

