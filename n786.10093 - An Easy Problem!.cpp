#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    string n;

    while(cin >> n){

        int total = 0;
        int max_digit = 0;
        int value = 0;

        for (char c : n){
            if ('0' <= c && c <= '9')
                value = c - '0';
            else if('A' <= c && c <= 'Z')
                value = c - 'A' + 10;
            else 
                value = c - 'a' + 36;

            total += value;
            max_digit = max(max_digit, value);
        }


        int answer = -1;


        for(int i = max_digit + 1; i <= 62; i++){
            if (total % (i-1) == 0){
                answer = i;
                break;
            }
        }
        if (answer == -1)
            cout << "such number is impossible!" << endl;
        else
            cout << answer << endl;
    }
}
