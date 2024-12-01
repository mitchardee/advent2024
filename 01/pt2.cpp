#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
using namespace std;

int main(){
    ifstream file("input");

    string line;
    int tot = 0, a, b;
    vector<int> aa;
    unordered_map<int, int> bb;

    while (getline(file, line)){ 
        a = stoi(line.substr(0, 5));
        b = stoi(line.substr(8));
        aa.push_back(a);
        bb[b]++;
    }

    for(int i = 0; i < aa.size(); i++) {
        tot += aa[i] * bb[aa[i]];
    }

    cout<<tot<<endl;
    file.close();

    return 0;
}