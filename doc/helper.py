
def normalize(text):
    return text.strip()\
        .replace("é", "e")\
        .replace("è", "e")\
        .replace("ê", "e")\
        .replace("à", "a")\
        .replace("â", "a")\
        .replace("ï", "i")\
        .replace("ô", "o")\
        .replace("ç", "c")\
        .replace("ç", "c")\
        .replace("œ", "oe")\
        .replace("É", "e")

def toId(text):
    return text.lower()\
        .replace(" ", "_")\
        .replace("-", "_")\
        .replace(".", "")\
        .replace("'", "")\
        .replace("(", "")\
        .replace(")", "")