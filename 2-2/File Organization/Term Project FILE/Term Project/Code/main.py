import os
from datetime import datetime
from hashlib import sha256, md5, sha1

def get_non_duplicated_passwords():
    non_duplicated_passwords = dict()
    os.chdir(os.getcwd().replace("Code", "Unprocessed-Passwords"))
    files = os.listdir()
    
    for file in files:
        with open(file, "r", encoding="utf8") as open_file:
            for line in open_file:
                line = line.strip("\n")
                non_duplicated_passwords[line] = open_file.name

    if len(files) == 0:
        print("Unprocessed-Passwords klasöründe hiç dosya bulunamadı.")
        exit()
        
    for f in files:
        old_path = os.path.join(os.getcwd(), f)
        new_path = os.path.join(os.getcwd().replace("Unprocessed-Passwords", "Processed"), f)
        os.replace(old_path, new_path)
    
    return non_duplicated_passwords

def create_index_files():
    len_dict = dict()
    pass_dict = get_non_duplicated_passwords()
    os.chdir(os.getcwd().replace("Unprocessed-Passwords", "Index"))
    for key in pass_dict:
        first_char = str(ord(key[0]))
        dir_contents = os.listdir()
        if first_char not in dir_contents:
            if not os.path.exists(first_char):
                os.mkdir(first_char)
                len_dict[first_char] = 1
        index = len_dict[first_char] // 10000
        with open(f"{first_char}/{index}.txt", "a") as open_file:
            open_file.write(f"{key}|{md5(key.encode()).hexdigest()}|{sha1(key.encode()).hexdigest()}|{sha256(key.encode()).hexdigest()}|{pass_dict[key]}\n")
            len_dict[first_char] += 1

def add_new_password(key):
    password_list = os.listdir()
    with open(f"{password_list[len(password_list) - 1]}", "a") as open_file:
        open_file.write(f"{key}|{md5(key.encode()).hexdigest()}|{sha1(key.encode()).hexdigest()}|{sha256(key.encode()).hexdigest()}|User Input\n")


def find_password():
    input_password = input("Aranacak parolayı giriniz:")
    start_time = datetime.now()
    end_time = 0
    first_char = str(ord(input_password[0]))
    os.chdir(os.getcwd().replace("Code", "Index"))
    os.chdir(os.path.join(os.getcwd(), first_char))
    files = os.listdir()
    for file in files:
        with open(file, "r", encoding="utf8") as open_file:
            for line in open_file:
                line = line.strip("\n").split("|")
                if line[0] == input_password:
                    print()
                    print("PAROLA BULUNDU!\n")
                    print(f"Parola: {line[0]}\nMD5: {line[1]}\nSHA1: {line[2]}\nSHA256: {line[3]}\nKaynak Dosya: {line[4]}\n")
                    end_time = datetime.now()
                    print(f"Geçen süre: {end_time - start_time}")
                    exit()
    print()
    print("Parola bulunamadı.")
    end_time = datetime.now()
    print(f"Geçen süre: {end_time - start_time}")
    add_new_password(input_password)

if __name__ == "__main__":
    print("[1] Parolaları oku ve Index dosyalarını oluştur\n[2] Parola Arama\n[4] Çıkış yap")
    choise = input("Seçiminizi yapınız:")
    
    match choise:
        case "1":
            print("Parolalar okunuyor ve index dosyaları oluşturuluyor...")
            start_time = datetime.now()
            create_index_files()
            end_time = datetime.now()
            print(f"Geçen süre: {end_time - start_time}")
        case "2":
            find_password()
        case "4":
            print("Çıkış yapılıyor...")
            exit()
        case _:
            print("Geçersiz seçim yaptınız. Lütfen tekrar deneyiniz.")
