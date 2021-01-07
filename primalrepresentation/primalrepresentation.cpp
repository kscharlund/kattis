#include <cmath>
#include <cstdio>
#include <vector>
#include <cstdint>

using namespace std;

vector<uint32_t> create_primes(const uint32_t max_p)
{
    vector<bool> is_prime(max_p+1, true);
    vector<uint32_t> primes;
    primes.push_back(2u);
    uint32_t pi = 3u;

    while (pi <= max_p)
    {
        primes.push_back(pi);

        // Mark multiples of pi as composite
        for (uint32_t ci = pi * pi; ci < is_prime.size(); ci += 2u * pi)
        {
            is_prime[ci] = false;
        }

        // Advance to next prime
        do
        {
            pi += 2u;
        }
        while (pi < is_prime.size() && !is_prime[pi]);
    }
    return primes;
}

vector<uint32_t> factorize(vector<uint32_t> const &primes, uint32_t n)
{
    vector<uint32_t> factors;
    uint32_t i = 0;
    while (n > 1u)
    {
        while (i < primes.size() && n % primes[i])
        {
            ++i;
        }
        if (i < primes.size())
        {
            factors.push_back(primes[i]);
            n /= primes[i];
        }
        else
        {
            factors.push_back(n);
            n = 1;
        }
    }
    return factors;
}

/*
vector<uint32_t> factorize(uint32_t n)
{
    vector<uint32_t> factors;
    uint32_t f;
    f = 2u;
    while (n % 2u == 0u)
    {
        factors.push_back(f); n /= 2u;
    }
    f = 3u;
    while (n % 3u == 0u)
    {
        factors.push_back(f); n /= 3u;
    }
    f = 5u;
    uint32_t ac = 9u, temp = 16u;
    do
    {
        ac += temp;
        if (ac > n)
            break; 
        if (n % f == 0)
        {
            factors.push_back(f);
            n /= f;
            ac -= temp;
        }
        else
        {
            f += 2;
            temp += 8;
        }
    } while (1);

    if (n != 1)
        factors.push_back(n);

    return factors;
}
*/

int main()
{
    vector<uint32_t> primes = create_primes((uint32_t) sqrt((double)INT32_MAX) + 1u);
    int n;
    while (scanf("%d", &n) != EOF)
    {
        if (n < 0)
        {
            printf("-1 ");
            n = -n;
        }
        vector<uint32_t> factors = factorize(primes, (uint32_t) n);
        uint32_t cf = 0u;
        uint32_t ce = 0u;
        for (int i = 0; i < (int)factors.size(); ++i)
        {
            if (factors[i] == cf)
            {
                ++ce;
            }
            else
            {
                if (cf)
                {
                    if (ce > 1u)
                        printf("%u^%u ", cf, ce);
                    else
                        printf("%u ", cf);
                }
                cf = factors[i];
                ce = 1u;
            }
        }
        if (ce > 1u)
            printf("%u^%u\n", cf, ce);
        else
            printf("%u\n", cf);
    }
    return 0;
}
