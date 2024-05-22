from binarytree import Node
from hashlib import md5
import os

def create_tree():
    root = Node(500000, None)

    media_list = os.listdir()
    cwd = os.getcwd()
    for media in media_list:
        mini_media_list = os.listdir(os.path.join(cwd, media))
        for mini_media in mini_media_list:
            for file in os.listdir(os.path.join(cwd, media, mini_media)):
                as_int = hash_generator(os.path.join(cwd, media, mini_media, file))
                root.insert(as_int, file)
    return root

def menu():
    os.chdir(os.path.join(os.getcwd(), "Media_Root"))
    print("1. Insert")
    print("2. Delete")
    print("3. Tree Traversal")
    print("4. Search")
    choice = int(input("Enter choice: "))
    
    match choice:
        case 1:
            choice = int(input("[1] Music\n[2] Photos\n[3] Videos\nEnter Choise: "))
            match choice:
                case 1:
                    choice = int(input("[1] Pop\n[2] Jazz\nEnter Choise: "))
                    match choice:
                        case 1:
                            os.chdir(os.path.join(os.getcwd(), "Music", "Pop"))
                        case 2:
                            os.chdir(os.path.join(os.getcwd(), "Music", "Jazz"))
                    with open(f'track{len(os.listdir()) + 1}.mp3', 'w') as fp: pass
                case 2:
                    choice = int(input("[1] Events\n[2] Vacation\nEnter Choise: "))
                    match choice:
                        case 1:
                            os.chdir(os.path.join(os.getcwd(), "Photos", "Events"))
                        case 2:
                            os.chdir(os.path.join(os.getcwd(), "Photos", "Vacation"))
                    with open(f'photo{len(os.listdir()) + 1}.jpg', 'w') as fp: pass
                case 3:
                    choice = int(input("[1] Documentaries\n[2] Movies\nEnter Choise: "))
                    match choice:
                        case 1:
                            os.chdir(os.path.join(os.getcwd(), "Videos", "Documentaries"))
                            with open(f'doc{len(os.listdir()) + 1}.mp4', 'w') as fp: pass
                        case 2:
                            os.chdir(os.path.join(os.getcwd(), "Videos", "Movies"))
                            with open(f'movie{len(os.listdir()) + 1}.mp4', 'w') as fp: pass
        case 2:
            path = input("Enter the absolute path to the file: ")
            if os.path.exists(path):
                os.remove(path)
                print("File deleted successfully")
            else:
                print("File not found")
        case 3:
            root = create_tree()
            choice = int(input("[1] Preorder\n[2] Inorder\n[3] Postorder\nEnter Choise: "))
            ordered = []
            match choice:
                case 1:
                    ordered = root.PreorderTraversal(root)
                case 2:
                    ordered = root.inorderTraversal(root)
                case 3:
                    ordered = root.PostorderTraversal(root)
            for i in ordered:
                if i != "500000 - None":
                    print(i)
        case 4:
            root = create_tree()
            data = input("Enter the file path to search: ")
            hash_data = hash_generator(data)
            found = root.search(root, hash_data)
            if not found:
                print("File not found")
            else:
                print(f"File found: {found.file} - {found.data}")
        case _:
            exit()

def hash_generator(file):
    a = md5(file.encode())
    b = a.hexdigest()
    as_int = int(b, 16) % 999983
    return as_int

if __name__ == "__main__":
    menu()