#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

#if 0
// Old code
void createPrimes(vector<size_t> &primes)
{
    size_t maxPrime = (size_t)floor(sqrt(1000000000.0));
    vector<bool> isPrimeVec(maxPrime+1, true);
    primes.push_back(2);
    size_t pi = 3;

    while (pi <= maxPrime)
    {
        primes.push_back(pi);

        // Mark multiples of pi as composite
        for (size_t ci = pi * pi; ci < isPrimeVec.size(); ci += 2 * pi)
        {
            isPrimeVec[ci] = false;
        }

        // Advance to next prime
        do
        {
            pi += 2;
        }
        while (pi < isPrimeVec.size() && !isPrimeVec[pi]);
    }
}

size_t sopf(size_t nn, const vector<size_t> &primes)
{
    size_t sum = 0;
    size_t prod = 1;

    for (auto pi = primes.begin(); pi != primes.end(); ++pi)
    {
        size_t prime = *pi;
        while ((nn % prime) == 0)
        {
            sum += prime;
            prod *= prime;
            nn /= prime;
        }
        if (nn == 1)
        {
            break;
        }
    }

    return sum;
}

int main()
{
    vector<size_t> primes;
    createPrimes(primes);

    size_t nn;
    while (cin >> nn)
    {
        if (nn == 4)
        {
            break;
        }

        int count = 1;
        while (true)
        {
            size_t ss = sopf(nn, primes);
            if (ss == nn)
            {
                break;
            }
            else
            {
                nn = ss;
                ++count;
            }
        }

        cout << nn << " " << count << endl;
    }

    return 0;
}
#endif

bool is_prime(int nn)
{
    if (nn <= 2)
    {
        return true;
    }
    if (nn % 2 == 0)
    {
        return false;
    }
    for (int ii = 3; ii*ii <= nn; ii += 2)
    {
        if (nn % ii == 0)
        {
            return false;
        }
    }
    return true;
}

int sum_of_prime_factors(int nn)
{
    int sum = 0;

    while (nn % 2 == 0)
    {
        nn /= 2;
        sum += 2;
    }

    for (int ii = 3; ii*ii <= nn; ii += 2)
    {
        if (nn % ii == 0 && is_prime(ii))
        {
            while (nn % ii == 0)
            {
                nn /= ii;
                sum += ii;
            }
        }
    }

    if (nn > 1)
    {
        sum += nn;
    }

    return sum;
}

void prime_reduction(int nn)
{
    int count = 1;
    while (!is_prime(nn))
    {
        nn = sum_of_prime_factors(nn);
        ++count;
    }
    cout << nn << " " << count << endl;
}

int main()
{
    int nn;
    while (cin >> nn)
    {
        if (nn == 4)
        {
            break;
        }
        prime_reduction(nn);
    }
    return 0;
}
