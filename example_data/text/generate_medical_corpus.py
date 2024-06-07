import os, glob
import json
import random

random.seed(random.random())

### get sysnonyms corpus ###
fin = open("medical_corpus/revised_synonyms.json", "r", encoding="utf-8")
synonyms_info_json_list = json.load(fin)
fin.close()

parameter_name_list = []
for ele in synonyms_info_json_list:
    abbr = ele["Abbreviation"]
    parameter_name_list.append(abbr)
    synonyms = ele["Synonyms"]
    for syn in synonyms:
        parameter_name_list.append(syn)

### get units corpus ###
fin = open("medical_corpus/health_api_parameter_unit_mapping_raw.json", "r", encoding="utf-8")
health_api_info_json = json.load(fin)
fin.close()

unit_list = []
for key in health_api_info_json:
    units = health_api_info_json[key]["units"]
    for u in units:
        if u == "nan":
            continue
        unit_list.append(u)
        p = random.random()
        if p > 0.5:
            u = u.replace("/", " /")
            u = u.replace("/", "/ ")
            u = u.replace("*", " * ")
            u = u.replace("^", " ^ ")
            unit_list.append(u)



symbol_list = ["^", "-", "*", ">", "<", ">=", "<=", ":",
               "&", "@", "#", "~", "+", "%", "(", ")",
               "[", "]", "{", "}", "'", ",", ".", ";",
               ":", "/", "?", "|"]

novel_word_list = []
novel_path_list = glob.glob(os.path.join("novels", "*.txt"))

for novel_path in novel_path_list:
    fin = open(novel_path, "r")
    lines = fin.readlines()
    fin.close()
    for l in lines:
        l = l.strip().split()
        for word in l:
            novel_word_list.append(word)
novel_word_list = list(set(novel_word_list))
print(novel_word_list)

total_corpus_num = 1000000

fout = open("medical_corpus.txt", "w", encoding="utf-8")
for _ in range(total_corpus_num):
    words = []
    p = random.random()
    if p < 0.4:
        words = random.choices(novel_word_list, k=random.randint(1, 3))
    elif p >= 0.5 and p < 0.65:
        float_data_list = ["%.2f" % random.random() for _ in range(10)]
        float_data_list += ["%.2f" % random.uniform(0, 1000) for _ in range(5)]
        int_data_list = [str(random.randint(1, 1000)) for _ in range(10)]
        words = random.choices(float_data_list + int_data_list, k=random.randint(1, 2))
    elif p >= 0.65 and p < 0.85:
        words = random.choices(unit_list, k=1)
    else:
        words = random.choices(parameter_name_list, k=1)
    p = random.random()
    if p < 0.1:
        words += random.choices(symbol_list, k=random.randint(1, 2))
        random.shuffle(words)

    fout.write(" ".join(words) + "\n")
fout.close()