#include <iostream>
#include <set>

using namespace std;
int main(){
    int t,n, cas=1;
    cin>>t;
    while (t--){
        cin >> n;
        set<int> all;
        cout << "Case #" << cas++ << ": " << n << " ";
    
        while(n != 1){
            int sum = 0;
            if (all.count(n))
                break;
            all.insert(n);
        
            while(n){
                sum += (n % 10) * (n % 10);
                n /= 10;
            }
            n = sum;
        }
        if (n == 1)
            cout << "is a Happy number." << endl;
        else
            cout << "is an Unhappy number." << endl;
    }
}  