import os, json
import random

root_path = "output/eng_word_data_multi_transform/"
json_file = "labels.json"

with open(os.path.join(root_path, json_file), "r", encoding="utf-8") as fin:
    label_info = json.loads(fin.read())["labels"]


train_num = 100000

sample_list = []
for image_basename in label_info:
    label = label_info[image_basename]
    sample_list.append((image_basename + ".jpg", label))

random.shuffle(sample_list)

fout = open(os.path.join(root_path, "train_samples.txt"), "w", encoding="utf-8")
for i in range(len(sample_list))[:train_num]:
    image_name = sample_list[i][0]
    label = sample_list[i][1]
    fout.write(image_name + "\t" + label + "\n")
fout.close()


fout = open(os.path.join(root_path, "eval_samples.txt"), "w", encoding="utf-8")
for i in range(len(sample_list))[train_num:]:
    image_name = sample_list[i][0]
    label = sample_list[i][1]
    fout.write(image_name + "\t" + label + "\n")
fout.close()