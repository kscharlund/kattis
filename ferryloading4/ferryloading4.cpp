#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;

int main()
{
    int nCases;
    scanf("%d", &nCases);
    for (int ii = 0; ii < nCases; ++ii)
    {
        int maxCap, nCars;
        scanf("%d %d", &maxCap, &nCars);
        maxCap *= 100; // cm
        queue<int> lq;
        queue<int> rq;
        for (int jj = 0; jj < nCars; ++jj)
        {
            int len;
            char buf[10];
            scanf("%d %s", &len, buf);
            if (!strcmp(buf, "left"))
                lq.push(len);
            else
                rq.push(len);
        }

        bool leftSide = true;
        int trips = 0;
        queue<int> *cq = &lq;
        while (!lq.empty() || !rq.empty())
        {
            int cap = maxCap;
            while (!cq->empty() && cap > cq->front())
            {
                cap -= cq->front();
                cq->pop();
            }
            ++trips;
            leftSide = !leftSide;
            cq = leftSide ? &lq : &rq;
        }
        printf("%d\n", trips);
    }
    return 0;
}