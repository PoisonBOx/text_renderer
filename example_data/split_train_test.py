import os, json
import random
import re

root_path = "output/eng_word_data_v2/"
json_file = "labels.json"

with open(os.path.join(root_path, json_file), "r", encoding="utf-8") as fin:
    label_info = json.loads(fin.read())["labels"]

train_num = 500000

sample_list = []
for image_basename in label_info:
    label = label_info[image_basename]
    sample_list.append((image_basename + ".jpg", label))

os.mkdir(os.path.join(root_path, "rec"))
os.mkdir(os.path.join(root_path, "rec", "train"))
os.mkdir(os.path.join(root_path, "rec", "train", "imgs"))
os.mkdir(os.path.join(root_path, "rec", "eval"))
os.mkdir(os.path.join(root_path, "rec", "eval", "imgs"))

fout_train = open(os.path.join(root_path, "rec", "train", "train_list.txt"), "w", encoding="utf-8")
fout_eval = open(os.path.join(root_path, "rec", "eval", "eval_list.txt"), "w", encoding="utf-8")
for i in range(len(sample_list)):
    image_name = sample_list[i][0]
    label = sample_list[i][1]
    label = re.sub("\s+", " ", label)
    if i < train_num:
        fout_train.write(image_name + "\t" + label + "\n")
        # os.system("cp %s %s" % (os.path.join(root_path, "images", image_name), os.path.join(root_path, "rec", "train", "imgs")))
    else:
        fout_eval.write(image_name + "\t" + label + "\n")
        os.system("cp %s %s" % (os.path.join(root_path, "images", image_name), os.path.join(root_path, "rec", "eval", "imgs")))
fout_train.close()
fout_eval.close()
