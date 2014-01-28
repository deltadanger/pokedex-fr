import os
from PIL import Image

for root, dirs, files in os.walk("image"):
    for file in files:
        i = Image.open("image/"+file)
        i = i.resize((i.size[0]/2, i.size[1]/2), Image.ANTIALIAS)
        i.save("image-small/"+file, optimize=True, quality=90)

