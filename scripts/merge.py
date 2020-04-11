import json


final = list()

for i in range(1950, 2020):
    print(i)
    filename = "data/"+str(i)+".json"
    with open(filename) as f:
        temp = json.load(f)
        final = final + temp

with open('data/final_end.json', 'w', encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=4)