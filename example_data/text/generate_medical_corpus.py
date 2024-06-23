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


possible_units_dict = {
    "x10^3/μL": ["10^3/μL"],
    "x10^3/uL": ["10^3/uL", "x10*3/uL", "10e3/uL", "tsd./uL", "Thousand/uL", "*10^E/L", "10*3/uL", "k/ul", "x10E3/uL", "micl/3*10"],
    "x10^6/uL": ["10^6/uL", "x10*6/uL", "10e6/uL", "Million/uL", "10*6/ul", "mio./ul", "m/ul", "x10e6/ul"],
    "x10^6/L": ["*10^6/L", "10^6/L"],
    "x10^6/μL": ["10^6/μL"],
    "x10^9/L": ["x10*9/L", "×10^9/L", "10^9/L", "*10^9/L", "10*9/L", "X10^9/L"],
    "x10^12/L": ["10^12/L", "×10^12/L", "*10^12/L", "x10*12/L", "10*12/l", "*10^e2/l", ],
    "/HPF": [],
    "/HP": [],
    "/LPF": [],
    "/100 WBCs": ["/100WBC", "/100 WBC"],
    "/100": [],
    "/1000 RBC": [],
    "/uL": [],
    "/nL": [],
    "/min": [],
    "titer": [],
    "index": [],
    "fL": [],
    "pg": [],
    "units": [],
    "kPa": [],
    "COI": [],
    "mmHg": [],
    "%": ["", "ratio"],
    "mmol": [],
    "mL/min/1.73m^2": ["mL/min/1.73m2", "mL/min/1.73m*2", "per 1.73sqm", "ml/min/1.73qm", "1.73/m2", "ml/min/1.73m2", "ml/min^1.73"],
    "umol/L": [],
    "nmol/L": [],
    "μIU/L": [],
    "μIU/mL": [],
    "mIU/L": [],
    "g/L": [],
    "TU/mL": [],
    "ug/L": [],
    "U/mL": [],
    "pmol/L": [],
    "IU/L": [],
    "IU/mL": [],
    "U/L": [],
    "miIU/L": [],
    "mm/h": [],
    "ug/g": [],
    "nmol/t": [],
    "mg/L": [],
    "mU/L": [],
    "pg/L": [],
    "umo/L": [],
    "units/L": [],
    "mmol/mol": [], #"milU/L",
    "mm/hr": [],
    "mmol/L": [],
    "L/L": [],
    "mg/dL": [],
    "AU/mL": [],
    "ng/mL": [],
    "mcg/L": [],
    "mIU/mL": [],
    "pg/mL": [],
    "ng/dL": [],
    "kg/m2": [],
    "ng/L": [],
    "μmol/L": [],
    "kappa/lambda": [],
    "g/dL": [],
    "mmoi/L": [],
    "mL/min": [],
    "ug/dL": [],
    "uIU/mL": [],
    "M/uL": [],
    "mg/mmol": [],
    "kIU/L": [],
    "kU/L": [],
    "mcg/dL": [],
    "mol/L": [],
    "Copies/mL": [],
    "μg/L": [],
    "cells/uL": [],
    "nmol/mL/min": [],
    "mOsm/KgH2O": [],
    "nan": []
}

for key in possible_units_dict:
    unit_list.append(key)
    if u == "nan":
        continue
    p = random.random()
    if p > 0.5:
        u = u.replace("/", " /")
        u = u.replace("/", "/ ")
        u = u.replace("*", " * ")
        u = u.replace("^", " ^ ")
        unit_list.append(u)

    for u in possible_units_dict[key]:
        unit_list.append(u)
        if u == "nan":
            continue
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
        words = random.choices(novel_word_list, k=random.randint(1, 5))
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
    elif p > 0.1 and p < 0.2:
        words = random.choices(symbol_list, k=random.randint(1, 2))

    output_info = ""
    for w in words[:-1]:
        output_info += w
        p = random.random()
        if p > 0.8:
            output_info += " " * random.randint(1, 3)
        else:
            output_info += " "
    output_info += words[-1]
    output_info = output_info.replace("_", "-")
    # fout.write(" ".join(words) + "\n")
    fout.write(output_info + "\n")
fout.close()