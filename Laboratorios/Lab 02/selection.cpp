#include <iostream>
#include <vector>
#include <utility>
using namespace std;

void selection (vector <int> &arr) {

    for (int min, i = 0 ; i < arr.size()-1 ; i++) {
        
        min = i;
        for (int j = min+1 ; j < arr.size() ; j++) {
            
            if (arr[j] < arr[min])
                min = j;
        }
        swap(arr[i], arr[min]);
    }
}

int main () {
    
    vector <int> arr = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
    
    cout<<"El arreglo desordenado es: "<<ends;
    for (int num : arr)
        cout<<num<<" ";
    
    selection(arr);

    cout<<"\nEl arreglo ordenado es: "<<ends;
    for (int num : arr)
        cout<<num<<" ";
}