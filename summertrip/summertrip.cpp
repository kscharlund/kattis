#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<uint32_t> vu;

int set_bits(uint32_t i)
{
     i = i - ((i >> 1) & 0x55555555u);
     i = (i & 0x33333333u) + ((i >> 2) & 0x33333333u);
     return (((i + (i >> 4)) & 0x0F0F0F0Fu) * 0x01010101u) >> 24;
}

int main()
{
    cin.sync_with_stdio(false);
    cin.tie(NULL);

    uint32_t ahead = 0u;
    vu pairs(26);
    string events;
    cin >> events;

    int count = 0;
    for (auto event : events) {
        int e = event - 'a';
        for (int i = 0; i < 26; ++i) {
            if (i != e) {
                pairs[i] |= 1 << e;
            } else {
                count += set_bits(pairs[i]);
                pairs[i] = 0u;
            }
        }
    }
    cout << count << endl;

    return 0;
}
