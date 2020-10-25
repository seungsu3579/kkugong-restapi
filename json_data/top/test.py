import json
import os


path = "."
file_names = os.listdir(path)

# total item list
for file in file_names:
    all_item = list()
    file = path + "/" + file
    with open(file, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)
        for _, data in json_data.items():
            all_item.append({_: data})

    # save test_sample to json
    with open(file, "w", encoding="utf-8") as make_file:
        json.dump(all_item, make_file, ensure_ascii=False, indent="\t")
