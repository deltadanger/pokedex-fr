import os


def main():
    for root, dirs, files in os.walk("miniat/"):
        for file in files:
            os.rename("miniat/"+file, "miniat/"+file.replace("miniat_",""))
            #~ print "miniat/"+file, "miniat/miniat-"+file
main()