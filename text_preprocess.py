import re
from globals import *

def preprocess(raw_Text):
    separated_string = raw_Text.splitlines()
    temp = []
    for i in separated_string:
        if(i != '' and i != ' '):
            temp.append(i)
    temp_1 = []
    for i in temp:
        temp_1.append(i.replace(' ',''))
    for i in temp_1:
        find = re.search("(?P<url>https?://[^\s]+)", i)
        if find:
            preprocessed_text.append(find.group(0))
        else:
            find = re.search(r"(www?[^\s]+)", i)
            if find:
                preprocessed_text.append(find.group(0))
    return preprocessed_text