#include <cstdio>

using namespace std;

/*

  1  1  1  1
  1 -1  1 -1
  1  1 -1 -1
  1 -1 -1  1

*/

int hadamard(long long nn, long long xx, long long yy, bool flip = false)
{
    if (nn == 1)
        return flip ? -1 : 1;

    long long nh = nn >> 1;
    if (xx < nh)
    {
        if (yy < nh)
        {
            return hadamard(nh, xx, yy, flip);
        }
        else
        {
            return hadamard(nh, xx, yy - nh, flip);
        }
    }
    else
    {
        if (yy < nh)
        {
            return hadamard(nh, xx - nh, yy, flip);
        }
        else
        {
            return hadamard(nh, xx - nh, yy - nh, !flip);
        }
    }
}

int main()
{
    int ncases;
    scanf("%d", &ncases);
    for (int ii = 0; ii < ncases; ++ii)
    {
        long long nn, xx, yy, ww, hh;
        scanf("%lld %lld %lld %lld %lld", &nn, &xx, &yy, &ww, &hh);
        for (long long jj = 0; jj < hh; ++jj)
        {
            printf("%d", hadamard(nn, xx, yy + jj));
            for (long long ii = 1; ii < ww; ++ii)
            {
                printf(" %d", hadamard(nn, xx + ii, yy + jj));
            }
            printf("\n");
        }
        printf("\n");
    }
    return 0;
}