import csv
import os

def read_csv_file(file_path):
    data = []
    hash_table_title = {}
    hash_table_author = {}
    with open(file_path, 'r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    for row in data:
        hash_table_title[row['Book Title'][0:2]] = row
        hash_table_author[row['Author'][0:2]] = row
    return data, hash_table_title, hash_table_author

def linear_search(csv_data, book, author):
    data = []
    if csv_data is None:
        return None
    elif book is None and author is None:
        return None
    
    for row in csv_data:
        if row['Book Title'] == book or row['Author'] == author:
            data.append(row)
    return data

def hash_table_search(hash_table, key):
    if key not in hash_table:
        print("No result found!")
    else:
        print(hash_table[key])

if __name__ == '__main__':
    file_path = os.path.join(os.getcwd(), 'tr_books.csv') 
    csv_data, hash_table_title, hash_table_author = read_csv_file(file_path)
    choise = input("[1] Linear Search\n[2] HashTable Search\nChoise: ")
    choise2 = input("[1] Search by book\n[2] Search by author\nChoise: ")
    book = None
    author = None
    match choise:
        case '1':
            match choise2:
                case '1':
                    book = input("Enter book name: ")
                case '2':
                    author = input("Enter author name: ")
            result = linear_search(csv_data, book, author[0:2])
            if result == []:
                print("No result found!")
            else:
                print(result)
        case '2':
             match choise2:
                case '1':
                    book = input("Enter book name: ")
                    hash_table_search(hash_table_title, book[0:2])
                case '2':
                    author = input("Enter author name: ")
                    hash_table_search(hash_table_author, author[0:2])
                
        case _:
            print("Invalid choise!")

