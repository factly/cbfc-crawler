import json

with open("data/patch.json") as f:
    patch = json.load(f)

for i in range(1951, 2020):
    print(i)
    filename = "data/"+str(i)+".json"

    with open(filename) as f:
        year = json.load(f)
        
        year_final = list(filter(lambda x: x['certificate_date'].split("-")[2] == str(i), year))
        
        year_patch = list(filter(lambda x: x['certificate_date'].split("-")[2] == str(i), patch))

        year_final = year_final + year_patch

        newFilename = "patch_data/"+str(i)+".json"
        
        with open(newFilename, 'w', encoding='utf-8') as f:
            json.dump(year_final, f, ensure_ascii=False, indent=4)


#496212
#502575