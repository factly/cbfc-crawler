import json

with open("data/search_page.json") as f:
    exp = json.load(f)

final = list()

allIDs = set()

notThere = list()

for i in range(1951, 2020):
    print(i)
    filename = "data/"+str(i)+".json"
    with open(filename) as f:
        temp = json.load(f)
        final = final + temp

for each in final:
    allIDs.add(each['m_id'])

for every in exp['aaData']:
    if every['m_id'] not in allIDs:
        notThere.append(every)


print(len(notThere))

with open('data/missed.json', 'w', encoding='utf-8') as f:
    json.dump(notThere, f, ensure_ascii=False, indent=4)