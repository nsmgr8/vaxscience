# coding=utf-8import sysimport jsondef transform(d):    demographic_list = ["Humans", "Male", "Female", "Young Adult", "Middle Aged", "Adolescent", "Child", "Aged, 80 and over", "Aged", "Adult"]    for row in d:#         if row["MeSH"].exists():        if row["MeSH"] is not None:           row["MeSH"] = row["MeSH"].split("; ")        if row["Affiliation"] is not None:           row["Affiliation"] = row["Affiliation"].split("; ")        if row["Author(s)"] is not None:           row["Author(s)"] = row["Author(s)"].split("; ")    for row in d:        if row["MeSH"] is not None:            for item in row["MeSH"]:                if "*" in item:                    # item_main = item.replace('\*', '')                    item_main = item.split("/")[0]                    row.setdefault("Main_Topic", []).append(item_main)                if item in demographic_list:                    row["MeSH"].remove(item)                    row.setdefault("Demographics", []).append(item)    yield dif __name__ == "__main__":    # Opening JSON file    f = open('r19articles.json')    data = json.load(f)    print(json.dumps(list(transform(data))))