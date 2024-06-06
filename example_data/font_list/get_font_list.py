import os, glob

font_path_list = glob.glob(os.path.join("../font/", "*.ttf"))

fout = open("font_eng_list.txt", "w")
for font_path in font_path_list:
    basename = os.path.basename(font_path)
    fout.write(basename + "\n")
fout.close()