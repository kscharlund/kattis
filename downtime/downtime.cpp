#include <cstdio>
#include <deque>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    deque<int> fifo;
    int n;
    int k;
    size_t max_size = 0;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; ++i)
    {
        int t;
        scanf("%d", &t);
        while (!fifo.empty() && fifo.front() <= (t - 1000))
        {
            fifo.pop_front();
        }
        fifo.push_back(t);
        max_size = max(max_size, fifo.size());
    }
    printf("%d\n", (int)ceil(((double)max_size) / ((double)k)));
    return 0;
}
