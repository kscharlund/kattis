#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct bia {
    bool bb;
    bool ii;
    bool aa;
};

bool is_possible(string const &brackets)
{
    unsigned int nn = brackets.length();
    if (nn & 1u)
        return false;

    vector<bia> m1(nn + 1u);
    vector<bia> m2(nn + 1u);
    bia *possible_curr = &(m1[0]);
    bia *possible_prev = &(m2[0]);

    possible_curr[nn / 2].bb = true;
    possible_curr[nn / 2].ii = true;
    possible_curr[nn / 2].aa = true;

    for (int ii = (int)nn - 1; ii >= 0; --ii)
    {
        swap(possible_curr, possible_prev);
        int lim = min((int)nn / 2, ii);
        for (int ll = (ii + 1) / 2; ll <= lim; ++ll)
        {
            possible_curr[ll].aa = possible_prev[ll + (brackets.at(ii) == '(')].aa;
            possible_curr[ll].ii = possible_curr[ll].aa | possible_prev[ll + (brackets.at(ii) == ')')].ii;
            possible_curr[ll].bb = possible_curr[ll].ii | possible_prev[ll + (brackets.at(ii) == '(')].bb;
        }
    }
    return possible_curr[0].bb;
}

int main()
{
    string brackets;
    cin >> brackets;
    cout << (is_possible(brackets) ? "possible" : "impossible") << endl;
    return 0;
}
