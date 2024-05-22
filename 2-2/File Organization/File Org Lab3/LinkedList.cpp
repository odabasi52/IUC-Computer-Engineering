#include <stdio.h>

struct Student{
    int ogr_no;
    char ad[20];
    char soyad[20];
    char bolum[40];

} typedef student;

class linkedList{
    private:
        struct node{
            student data;
            node* next;
        };
        node* head;
        node* tail;
    public:
        linkedList(){
            head = NULL;
            tail = NULL;
        }
        void addNode(student data){
            node* temp = new node;
            temp->data = data;
            temp->next = NULL;
            if(head == NULL){
                head = temp;
                tail = temp;
            }else{
                tail->next = temp;
                tail = tail->next;
            }
        }

        void printNodes(){
            node* temp = head;
            while(temp != NULL){
                printf("Ogrenci No: %d\n", temp->data.ogr_no);
                printf("Ogrenci Ad: %s\n", temp->data.ad);
                printf("Ogrenci Soyad: %s\n", temp->data.soyad);
                printf("Ogrenci BOlum: %s\n", temp->data.bolum);
                printf("\n");
                temp = temp->next;
            }
        }

        void deleteNode(student data){
            node* temp = head;
            node* prev = NULL;
            while(temp != NULL){
                if(temp->data.ogr_no == data.ogr_no){
                    if(prev == NULL){
                        head = temp->next;
                        delete temp;
                        return;
                    }else{
                        prev->next = temp->next;
                        delete temp;
                        return;
                    }
                }
                prev = temp;
                temp = temp->next;
            }
        }
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

void ogrenciGuncelle_3(FILE *f, student &blank, linkedList *studentList){
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
    studentList->deleteNode(blank);
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
    linkedList *studentList = new linkedList();
    FILE *students;
    student blank = {-1, "", "", ""};

    students = fopen("students.bin", "rb+");
    if (!students)
        return 0;
    else{
        rewind(students);
        fread(&blank, sizeof(student), 1, students);
        while (!feof(students)){
            studentList->addNode(blank);
            fread(&blank, sizeof(student), 1, students);
        }
        rewind(students);

        int choise = getchoise();
        
        switch (choise){
            case 1:
                ogrenciEkle_1(students, blank);
                studentList->addNode(blank);
                break;
            case 2:
                ogrenciSil_2(students, blank);
                studentList->deleteNode(blank);
                break;
            case 3:
                ogrenciGuncelle_3(students, blank, studentList);
                studentList->addNode(blank);
                break;
        }
    }
    printf("\n\n");
    studentList->printNodes();
    fclose(students);
}
