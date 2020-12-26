#include <cstdio>
#include <map>

using namespace std;

int main()
{
    int nCases;
    scanf("%d", &nCases);
    for (int ii = 0; ii < nCases; ++ii)
    {
        map<int, int> sellOrders;
        map<int, int, greater<int> > buyOrders;
        int stockPrice = -1;
        int nOrders;
        scanf("%d", &nOrders);
        for (int jj = 0; jj < nOrders; ++jj)
        {
            char buf[5];
            int nShares;
            int orderPrice;
            scanf("%s %d shares at %d", buf, &nShares, &orderPrice);
            if (buf[0] == 'b')
            {
                // Buy
                while (nShares && !sellOrders.empty())
                {
                    auto sellOrder = sellOrders.begin();

                    if (sellOrder->first > orderPrice)
                    {
                        // No more sell orders at acceptable price.
                        break;
                    }

                    // Transaction occurs, stock price is current ask price.
                    stockPrice = sellOrder->first;

                    if (sellOrder->second <= nShares)
                    {
                        nShares -= sellOrder->second;
                        sellOrders.erase(sellOrder);
                    }
                    else
                    {
                        sellOrder->second -= nShares;
                        nShares = 0;
                    }
                }

                if (nShares)
                {
                    auto it = buyOrders.lower_bound(orderPrice);
                    if (it->first == orderPrice)
                    {
                        it->second += nShares;
                    }
                    else
                    {
                        buyOrders.insert(it, pair<int, int>(orderPrice, nShares));
                    }
                }
            }
            else
            {
                // Sell
                while (nShares && !buyOrders.empty())
                {
                    auto buyOrder = buyOrders.begin();

                    if (buyOrder->first < orderPrice)
                    {
                        // No more buy orders at acceptable price.
                        break;
                    }

                    // Transaction occurs, stock price is current ask price.
                    stockPrice = orderPrice;

                    if (buyOrder->second <= nShares)
                    {
                        nShares -= buyOrder->second;
                        buyOrders.erase(buyOrder);
                    }
                    else
                    {
                        buyOrder->second -= nShares;
                        nShares = 0;
                    }
                }

                if (nShares)
                {
                    auto it = sellOrders.lower_bound(orderPrice);
                    if (it->first == orderPrice)
                    {
                        it->second += nShares;
                    }
                    else
                    {
                        sellOrders.insert(it, pair<int, int>(orderPrice, nShares));
                    }
                }
            }

            if (sellOrders.empty())
                printf("- ");
            else
                printf("%d ", sellOrders.begin()->first);

            if (buyOrders.empty())
                printf("- ");
            else
                printf("%d ", buyOrders.begin()->first);

            if (stockPrice < 0)
                printf("-\n");
            else
                printf("%d\n", stockPrice);
        }
    }
    return 0;
}