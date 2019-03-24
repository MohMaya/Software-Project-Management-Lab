#include <iostream>
using namespace std;
int main(){
    int x;
    cin>>x;
    if(x>5){
        cout<<"X is gr8er than 5\n";
    }
    for(int i=0; i<x; i++){
        cout<<i<<"\t";
    }
}