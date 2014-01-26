import os


def main():
    for root, dirs, files in os.walk("image/"):
        for file in files:
            os.rename("image/"+file, "image/"+file.replace("_","-"))
            #~ print "image/"+file, "image/image-"+file
main()