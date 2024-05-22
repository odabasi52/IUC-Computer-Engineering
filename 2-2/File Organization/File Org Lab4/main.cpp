#include <iostream>
#include <fstream>
#include <chrono>

using namespace std::chrono;


void selectionSort(int arr[], int n)
{
    int minindex;
    for (int i = 0; i < n; i++)
    {
        minindex = i;
        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[minindex])
                minindex = j; 
        }
        if (minindex != i)
        {
            int temp = arr[i];
            arr[i] = arr[minindex];
            arr[minindex] = temp;
        }
    }
}

void insertionSort(int arr[], int n)
{
    for (int i = 1; i < n; i++)
    {
        int j = i;
        int key = arr[i];
        while (key < arr[--j] && j >= 0)
            arr[j + 1] = arr[j];
        arr[j + 1] = key;
    }
}

void merge(int left[], int right[], int mai[], int size)
{
    int l = 0;
    int r = 0;
    int i = 0;
    int lmax = size / 2;
    int rmax = size - lmax;
    while (l < lmax && r < rmax)
    {
        if (left[l] < right[r])
            mai[i++] = left[l++];
        else
            mai[i++] = right[r++];
    }
    while (l < lmax)
        mai[i++] = left[l++];
    while (r < rmax)
        mai[i++] = right[r++];
}

void merge_sort(int arr[], int n)
{
    int mid = n / 2;
    int left[mid];
    int right[n - mid];

    if (n <= 1) return ;
		//fill arrays
    for (int i = 0; i < n; i++)
    {
        if (i < mid)
            left[i] = arr[i];
        else
            right[i - mid] = arr[i];
    }
    merge_sort(left, mid);
    merge_sort(right, n - mid);
    merge(left, right, arr, n);
}

void print_array(int arr[])
{
    for (int i = 0; i < 1000; i++)
        std::cout << arr[i] << ", ";
    std::cout << std::endl;
}

int main()
{
    std::ifstream file("numbers.txt");
    std::string line;
    microseconds duration;
    _V2::system_clock::time_point start_time, end_time;
    int arr[1000];
    int i = 0;
    int n = 1000;

    if (file.is_open()){
        while (std::getline(file, line)){
            arr[i++] = std::stoi(line);
        }
        file.close();
        std::cout << "Original Array:\n";
        print_array(arr);
        
        int a;
        std::cout << "[1] Selection Sort\n[2] Insertion Sort\n[3] Merge Sort\nSelect an option: ";
        std::cin >> a;
        

        switch(a){
            case 1:
                start_time = high_resolution_clock::now();
                selectionSort(arr, n);
                end_time = high_resolution_clock::now();
                duration = duration_cast<microseconds>(end_time - start_time);
                std::cout << "Selection Sort took " << (double)(duration.count() / 1000.0) << " microseconds\n\n";
                std::cout << "Selection Sort:\n";
                print_array(arr);
                break;
            case 2:
                start_time = high_resolution_clock::now();
                insertionSort(arr, n);
                end_time = high_resolution_clock::now();
                duration = duration_cast<microseconds>(end_time - start_time);
                std::cout << "Insertion Sort took " << (double)(duration.count() / 1000.0) << " microseconds\n\n";
                std::cout << "Insertion Sort:\n";
                print_array(arr);
                break;
            case 3:
                start_time = high_resolution_clock::now();
                merge_sort(arr, n);
                end_time = high_resolution_clock::now();
                duration = duration_cast<microseconds>(end_time - start_time);
                std::cout << "Merge Sort took " << (double)(duration.count() / 1000.0) << " microseconds\n\n";
                std::cout << "Merge Sort:\n";
                print_array(arr);
                break;
            default:
                std::cout << "Invalid option" << std::endl;
                break;
        }
    }
    else
        std::cout << "File could not be opened" << std::endl;
}
