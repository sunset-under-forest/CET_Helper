import os
from pprint import pprint

USED_BOOKS_PATH = os.path.join('used_books')


def find_books_json_by_name(name):
    name = name.lower()
    books_json_path = []
    for root,dirs,files in os.walk(USED_BOOKS_PATH):
        for f in files:
            if name in  f.lower():
                books_json_path.append(os.path.join(root,f))
        # print(root,dirs,files)
    return books_json_path

cet6_name = "cet6_3"
cet6_books_list = find_books_json_by_name(cet6_name)
print(cet6_books_list)

import json
book_path = cet6_books_list[0]
word_jsons = []
with open(book_path,"r",encoding="utf-8") as bk:
    for word_json in bk.readlines():
        word_jsons.append(json.loads(word_json))
pprint(word_jsons[1])