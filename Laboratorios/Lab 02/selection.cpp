#include <iostream>
#include <vector>
#include <utility>
using namespace std;

void selection (vector <int> &arr) {

    for (int min, i = 0 ; i < arr.size()-2 ; i++) {
        
        for (int j = i ; i < arr.size()-1 ; i++) {
            
            if (arr[i] > arr[j])
                min = j;
        }
        swap(arr[i], arr[min]);
    }
}

int main () {
    
}