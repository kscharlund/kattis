#include <iostream>
#include <string>

using namespace std;

int main()
{
    int height;
    string path;
    cin >> height >> path;
    int root = (1 << (height + 1)) - 1;
    int num = root;
    //cerr << "Root num: " << num << endl;
    int num_r = 0;
    for (size_t ii = 0; ii < path.length(); ++ii)
    {
        char choise = path.at(ii);
        if (choise == 'R')
        {
            num_r = 2 * num_r + 1;
        }
        else
        {
            num_r = 2 * num_r;
        }

        num = root - (1 << (ii + 1)) + 1 - num_r;
        //cerr << "num at level " << (ii + 1) << ": " << num << endl;
        //cerr << "num_r at level " << (ii + 1) << ": " << num_r << endl;
    }
    cout << num << endl;
    return 0;
}
