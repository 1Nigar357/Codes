#include <bits/stdc++.h>
using namespace std;

#define ll long long

int main ()
{
    int n;
    while(cin >> n){
        if(n==0) return 0;
        
        cout << n - (n&(n-1)) << endl;
    }
}
