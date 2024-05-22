#include <stdio.h>

struct Student{
    int ogr_no;
    char ad[20];
    char soyad[20];
    char bolum[40];

} typedef student;

class hashTable{
    public:
        hashTable(){
            for (int i = 0; i < 100; i++)
                table[i] = NULL;
        }
        void addNode(student &s){
            int index = s.ogr_no % 100;
            if (!table[index]){
                table[index] = new node(s);
            }
            else{
                node *tmp = table[index];
                while (tmp->next)
                    tmp = tmp->next;
                tmp->next = new node(s);
            }
        }
        void deleteNode(student &s){
            int index = s.ogr_no % 100;
            if (!table[index])
                return;
            node *tmp = table[index];
            if (tmp->data.ogr_no == s.ogr_no){
                table[index] = tmp->next;
                delete tmp;
                return;
            }
            while (tmp->next){
                if (tmp->next->data.ogr_no == s.ogr_no){
                    node *tmp2 = tmp->next;
                    tmp->next = tmp->next->next;
                    delete tmp2;
                    return;
                }
                tmp = tmp->next;
            }
        }
        void printNodes(){
            for (int i = 0; i < 100; i++){
                node *tmp = table[i];
                while (tmp){
                    printf("\nOgrenci No: %d\n", tmp->data.ogr_no);
                    printf("Ogrenci Ad: %s\n", tmp->data.ad);
                    printf("Ogrenci Soyad: %s\n", tmp->data.soyad);
                    printf("Ogrenci Bolum: %s\n", tmp->data.bolum);
                    tmp = tmp->next;
                }
            }
        }
    private:
        struct node{
            student data;
            node *next;
            node(student &s){
                data = s;
                next = NULL;
            }
        } *table[100];
};

int getchoise(){
    int a;
        
    printf("[1] Ogrenci Ekle\n"
        "[2] Ogrenci Sil\n"
        "[3] Ogrenci Guncelle\n"
        "Seciminiz >> ");
    scanf("%d", &a);
    while (!(a >= 1 && a <= 3))
    {
        fflush(stdout);
        printf("1-4 arasi secim giriniz >> ");
        scanf("%d", &a);
    }
    return (a);
}

void ogrenciEkle_1(FILE *f, student& blank){
    fflush(stdout);
    printf("Ogrenci No: ");
    scanf("%d", &(blank.ogr_no));
    fflush(stdout);
    printf("Ogrenci Ad: ");
    scanf("%s", blank.ad);
    fflush(stdout);
    printf("Ogrenci Soyad: ");
    scanf("%s", &(blank.soyad));
    fflush(stdout);
    printf("Ogrenci BOlum: ");
    scanf("%s", blank.bolum);

    fseek(f, 0, SEEK_END);
    fwrite(&blank, sizeof(student), 1, f);
}

void ogrenciSil_2(FILE *f, student& blank){
    int a;  
    
    printf("Ogrenci No >> ");
    scanf("%d", &a);

    FILE *tmp_f = fopen("tmp.bin", "wb");
    fread(&blank, sizeof(student), 1, f);
    while(!feof(f)){
        if (blank.ogr_no != a){
            fwrite(&blank, sizeof(student), 1, tmp_f);
        }
        fread(&blank, sizeof(student), 1, f);
    }
    fclose(tmp_f);
    remove("students.bin");
    rename("tmp.bin", "students.bin");
}

void ogrenciGuncelle_3(FILE *f, student &blank, hashTable *studentTable){
    int a;
    int index;
    
    printf("Ogrenci No >> ");
    scanf("%d", &a);

    index = 0;
    fseek(f, 0, SEEK_SET);
    fread(&blank, sizeof(student), 1, f);
    while (!feof(f)){
        if (blank.ogr_no == a)
            break;
        fread(&blank, sizeof(student), 1, f);
        index++;
    }
    if (blank.ogr_no != a){
        printf("ogrenci bulunamadi"); return;
    }
    studentTable->deleteNode(blank);
    fflush(stdout);
    printf("Ogrenci Ad: ");
    scanf("%s", blank.ad);
    fflush(stdout);
    printf("Ogrenci Soyad: ");
    scanf("%s", &(blank.soyad));
    fflush(stdout);
    printf("Ogrenci BOlum: ");
    scanf("%s", blank.bolum);
    fseek(f, sizeof(student) * index, SEEK_SET);
    fwrite(&blank, sizeof(student), 1, f);
}


int main(){
    FILE *students;
    hashTable *studentTable = new hashTable();
    student blank = {-1, "", "", ""};

    students = fopen("students.bin", "rb+");
    if (!students)
        return 0;
    else{
        rewind(students);
        fread(&blank, sizeof(student), 1, students);
        while (!feof(students)){
            studentTable->addNode(blank);
            fread(&blank, sizeof(student), 1, students);
        }
        rewind(students);

        int choise = getchoise();
        
        switch (choise){
            case 1:
                ogrenciEkle_1(students, blank);
                studentTable->addNode(blank);
                break;
            case 2:
                ogrenciSil_2(students, blank);
                studentTable->deleteNode(blank);
                break;
            case 3:
                ogrenciGuncelle_3(students, blank, studentTable);
                studentTable->addNode(blank);
                break;
        }
    }
    printf("\n\n");
    studentTable->printNodes();
    fclose(students);
}
