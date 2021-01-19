#include <iostream>

using namespace std;

void heapify(int arr[], int n, int i, int arr2[])
{
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;

    if (l < n && arr[l] > arr[largest])
        largest = l;

    if (r < n && arr[r] > arr[largest])
        largest = r;

    if (largest != i) {
        swap(arr[i], arr[largest]);
        swap(arr2[i], arr2[largest]);
        heapify(arr, n, largest, arr2);
    }
}

void heapSort(int arr[], int n, int arr2[])
{
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i, arr2);

    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        swap(arr2[0], arr2[i]);
        heapify(arr, i, 0, arr2);
    }
}

int main(){
    int T, N, i;
    int m[100], n[100];
    int x=0;

    cin >> T;

    for(int t=0;t<T;t++){
        cin >> N;
        for(i=0;i<N;i++){
            cin >> m[i] >> n[i];
        }

        heapSort(n, N, m);


        for(i=0;i<N;i++){ //sorted array
            cout<<m[i]<<" "<<n[i]<<endl;
        }

        x=1;
        i=0;
        for(int j=1;j<N;j++){
            if(m[j] >= n[i]){
                i=j;
                x++;
            }
        }
        cout<<x<<endl;

    }

}
