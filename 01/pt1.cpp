#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main(){
    ifstream file("input");

    string line;
    int tot = 0, a, b;
    vector<int> aa, bb;

    while (getline(file, line)){ 
        a = stoi(line.substr(0, 5));
        b = stoi(line.substr(8));
        aa.push_back(a);
        bb.push_back(b);
    }
    sort(aa.begin(), aa.end());
    sort(bb.begin(), bb.end());

    for(int i = 0; i < aa.size(); i++) {
        tot += abs(aa[i]-bb[i]);
    }

    cout<<tot<<endl;
    file.close();

    return 0;
}