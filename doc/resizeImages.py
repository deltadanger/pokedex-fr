import os
from PIL import Image

SRC = "image_tmp"
DEST = "image_tmp"
HEIGHT = 200

def resize():
    for root, dirs, files in os.walk(SRC):
        for file in files:
            i = Image.open(SRC + "/"+file)
            i.thumbnail((i.size[0]*HEIGHT/i.size[1], i.size[1]), Image.ANTIALIAS)
            i.convert("P")
            i.save(DEST + "/"+file.split(".")[0]+".png", optimize=True, quality=10)

def compress():
    for root, dirs, files in os.walk(SRC):
        for file in files:
            os.system("pngquant --ext _new.png " + SRC + "/"+file)

def rename():
    for root, dirs, files in os.walk(SRC):
        for file in files:
            # Remove "_new.png", 8 characters
            os.rename(SRC + "/" + file, DEST + "/"+file[:-8]+".png")

rename()