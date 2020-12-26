#include <cstdio>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <cstdlib>

using namespace std;

typedef pair<int, int> Pos;
static const int xMax = 10000;

double pyt(double hyp, double cat)
{
    return sqrt(hyp*hyp - cat*cat);
}

int main()
{
    vector<multiset<int> > gnomes;
    int nGnomes;
    int nSprinklers;
    
    scanf("%d", &nGnomes);
    gnomes.resize(xMax+1);
    for (int i = 0; i < nGnomes; ++i)
    {
        int x, y;
        scanf("%d %d", &x, &y);
        gnomes[x].insert(y);
    }

    scanf("%d", &nSprinklers);
    for (int i = 0; i < nSprinklers; ++i)
    {
        int sx, sy, sr;
        scanf("%d %d %d", &sx, &sy, &sr);

        for (int x = max(sx - sr, 0); x <= min(sx + sr, xMax); ++x)
        {
            int dx = abs(sx - x);
            double dy = pyt(sr, dx);
            gnomes[x].erase(
                gnomes[x].lower_bound((int)ceil(sy - dy)),
                gnomes[x].upper_bound((int)floor(sy + dy)));
        }
    }

    int left = 0;
    for (int x = 0; x <= xMax; ++x)
    {
        left += gnomes[x].size();
    }

    printf("%d\n", left);
    return 0;
}
