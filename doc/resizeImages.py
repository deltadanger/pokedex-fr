import os
from PIL import Image


# count = 100
# for root, dirs, files in os.walk("image"):
    # for file in files:
        # if count < 0: break
        # count -= 1
        # i = Image.open("image/"+file)
        # # i = i.resize((i.size[0], i.size[1]), Image.ANTIALIAS)
        # i.convert("P")
        # i.save("image-small/"+file.split(".")[0]+".png", optimize=True, quality=10)



count = 5

for root, dirs, files in os.walk("image"):
    for file in files:
        # if count < 0: break
        count -= 1
        os.system("pngquant --ext _new.png image/"+file)
        os.rename("image/" + file.split(".")[0] + "_new.png", "image-small/"+file)