import os

BOOK_PATH = os.path.join('book')
USED_BOOKS_PATH = os.path.join('used_books')
print(BOOK_PATH)
BOOKS_NAME_LIST = os.listdir(BOOK_PATH)


def find_books_by_name(name):
    print(f'书名包含"{name}"的书有：')
    name = name.lower()
    num = 0
    books = []
    for idx, book in enumerate(BOOKS_NAME_LIST):
        if name in book.lower():
            num += 1
            print(num, f"列表中的索引：{idx}\t书名：", book)
            books.append(book)
    return books


cet6_name = "cet6"
cet6_books_list = find_books_by_name(cet6_name)
import zipfile


def unzip_books_by_name(books_list):
    for book in books_list:
        used_book_path = os.path.join(USED_BOOKS_PATH,book.replace(".zip",""))
        os.mkdir(used_book_path)

        book_path = os.path.join(BOOK_PATH, book)
        book_zip = zipfile.ZipFile(book_path)

        print(book_zip.namelist())
        book_zip.extractall(used_book_path)


unzip_books_by_name(cet6_books_list)
