#include <cstdio>
#include <vector>
#include <algorithm>

struct rect {
    int w;
    int h;
    int x;
    int y;
};

int does_overlap(const rect &r1, const rect &r2)
{
    int xr1 = r1.x + r1.w, yb1 = r1.y + r1.h;
    int xr2 = r2.x + r2.w, yb2 = r2.y + r2.h;
    return !(r1.x >= xr2 or r2.x >= xr1 or r1.y >= yb2 or r2.y >= yb1);
}

int n;
std::vector<rect> rects;
std::vector<int> areas;
std::vector<int> overlaps;
std::vector<int> selected;

int solve(
    int ii,
    int area
)
{
    if (ii == n)
        return area;
    bool valid = true;
    for (int jj = 0; jj < ii; ++jj)
    {
        if (selected[jj] && overlaps[n * ii + jj])
        {
            valid = false;
            break;
        }
    }
    int r1 = -1;
    if (valid)
    {
        selected[ii] = 1;
        r1 = solve(ii + 1, area + areas[ii]);
        selected[ii] = 0;
    }
    return std::max(r1, solve(ii + 1, area));
}

int main()
{
    scanf("%d", &n);
    while (n)
    {
        rects.clear();
        areas.clear();
        overlaps.clear();
        selected.clear();

        overlaps.resize(n * n);
        selected.resize(n);
        for (int ii = 0; ii < n; ++ii)
        {
            int w, h, x, y;
            scanf("%d %d %d %d", &w, &h, &x, &y);
            rect r {w, h, x, y};
            rects.push_back(r);
            areas.push_back(w * h);
            for (int jj = 0; jj < ii; ++jj)
            {
                overlaps[n * ii + jj] = does_overlap(r, rects[jj]);
            }
        }
        printf("%d\n", solve(0, 0));
        scanf("%d", &n);
    }
    return 0;
}