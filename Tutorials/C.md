Problem Setter: [Md. Wasi Ul Habib](https://codeforces.com/profile/CodingPariNaa)

Estimated Difficulty: 1400

Tag(s): Constructive, Number Theory

<details>
<summary>Hint 1</summary>

How many possible remainders can a number have when divided by $n$?

</details>

<details>
<summary>Hint 2</summary>

If two numbers have the same remainder when divided by $n$, what can you say about their difference?

</details>

<details>
<summary>Hint 3</summary>

Try generating $n$ numbers. If none of them has remainder $0$, then two of them must have the same remainder.

</details>

<details>
<summary>Hint 4</summary>

Can you generate the numbers in such a way that the difference of any two generated numbers always contains only the digits $d$ and $0$?

</details>

<details>
<summary>Solution</summary>

When a number is divided by $n$, its remainder must be one of $0, 1, 2, \dots, n - 1$. So there are exactly $n$ possible remainders.

Now, suppose you have two numbers $a$ and $b$ such that $a \bmod n = b \bmod n$. Then their difference is divisible by $n$, because $(a - b) \bmod n = 0$.

This gives a useful direction. If you can find two numbers with the same remainder modulo $n$, then their difference will be divisible by $n$.

However, that difference is not automatically a valid answer. The problem also requires the answer to contain only the digits $d$ and $0$, have no leading zero, and have length at most $n$.

### Idea

Generate the following $n$ numbers: $S_1 = d$, $S_2 = dd$, $S_3 = ddd$, and so on up to $S_n = dd\dots d$ ($n$ occurrences of $d$).

Now, consider the difference between two such numbers $S_i$ and $S_j$, where $i > j$.

For example, if $i = 6$ and $j = 3$, then $S_i - S_j = dddddd - ddd = ddd000$.

In general, $S_i - S_j$ contains exactly $i - j$ occurrences of $d$, followed by exactly $j$ occurrences of $0$. So this difference always satisfies the digit condition and has no leading zero. Also, its length is $i$, which is at most $n$.

So now the goal is clear: among $S_1, S_2, \dots, S_n$, find either one number with remainder $0$, or two numbers with the same remainder.

If some $S_i \bmod n = 0$, then $S_i$ itself is a valid answer.

Otherwise, none of the $n$ numbers has remainder $0$. Then all their remainders are among $1, 2, \dots, n - 1$, which gives only $n - 1$ possible remainders. By the **Pigeonhole Principle**, two of the numbers must have the same remainder. If these numbers are $S_i$ and $S_j$ with $i > j$, then $S_i - S_j$ is divisible by $n$ and satisfies all constraints.

To implement this without constructing huge numbers, maintain only the current remainder. If the remainder of $S_{i-1}$ is $R$, then after appending digit $d$, the new remainder becomes $R = (R \times 10 + d) \bmod n$.

Use an array $seen$ where $seen[r]$ stores the first length that produced remainder $r$. When a repeated remainder is found, construct the answer from the two lengths.

The time complexity is $\mathcal{O}(n)$ per test case, and the space complexity is $\mathcal{O}(n)$.

<details>
<summary>Code</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(0); cin.tie(0)
using LL = long long;

void pre()
{
    fastio;
}

void printRepeated(int cnt, char ch)
{
    for(int i = 0; i < cnt; i++) cout << ch;
}

void solve(int tc)
{
    int n, d;
    cin >> n >> d;

    int R = 0;
    vector<int> seen(n, -1);

    for(int i = 1; i <= n; i++)
    {
        R = (R * 10 + d) % n;

        if(R == 0)
        {
            printRepeated(i, d + '0');
            return;
        }

        if(seen[R] != -1)
        {
            int j = seen[R];
            printRepeated(i - j, d + '0');
            printRepeated(j, '0');
            return;
        }

        seen[R] = i;
    }
}

int main()
{
    pre();

    int tc, tt = 1;
    cin >> tt;

    for(tc = 1; tc <= tt; tc++)
    {
        // cout << "Case " << tc << ": ";
        solve(tc);
        cout << '\n';
    }

    return 0;
}
```

</details>
</details>
