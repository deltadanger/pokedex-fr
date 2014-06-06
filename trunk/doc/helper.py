
def normalize(text):
    return text.strip()\
        .replace("�", "e")\
        .replace("�", "e")\
        .replace("�", "e")\
        .replace("�", "a")\
        .replace("�", "a")\
        .replace("�", "i")\
        .replace("�", "o")\
        .replace("�", "c")\
        .replace("�", "c")\
        .replace("�", "oe")\
        .replace("�", "e")

def toId(text):
    return text.lower()\
        .replace(" ", "_")\
        .replace("-", "_")\
        .replace(".", "")\
        .replace("'", "")\
        .replace("(", "")\
        .replace(")", "")