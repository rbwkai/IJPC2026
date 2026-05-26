# Glorious Batch-24!

Problem Setter: [Fariya Ahmed](https://codeforces.com/profile/fariyapracticekorena)

Estimated Difficulty: 900

Tag(s): Number Theory

<details>
<summary>Hint 1</summary>

Rewrite $x^2 - 1$ as $(x - 1)(x + 1)$.

</details>

<details>
<summary>Hint 2</summary>

Since $24 = 8 \times 3$, analyze divisibility by $8$ and $3$ separately.

</details>

<details>
<summary>Solution</summary>

An ID $x$ is an impostor if $x^2 - 1$ is divisible by $24$.

Since $24 = 8 \times 3$, we need $x^2 - 1$ to be divisible by both $8$ and $3$. Now,

$x^2 - 1 = (x - 1)(x + 1)$.

First, consider divisibility by $3$.

The numbers $x - 1$, $x$, and $x + 1$ are three consecutive integers. Among any three consecutive integers, exactly one is divisible by $3$.

If $x$ itself is divisible by $3$, then neither $x - 1$ nor $x + 1$ is divisible by $3$. So $(x - 1)(x + 1)$ is not divisible by $3$.

If $x$ is not divisible by $3$, then one of $x - 1$ and $x + 1$ must be divisible by $3$. So $(x - 1)(x + 1)$ is divisible by $3$.

Therefore, $x^2 - 1$ is divisible by $3$ if and only if $x$ is not divisible by $3$.

Now, consider divisibility by $8 = 2^3$.

If $x$ is even, then both $x - 1$ and $x + 1$ are odd. Their product is odd, so it is not even divisible by $2$.

If $x$ is odd, then both $x - 1$ and $x + 1$ are even. They are two consecutive even numbers, so one of them must be divisible by $4$. Their product is therefore divisible by $2 \times 4 = 8$.

Therefore, $x^2 - 1$ is divisible by $8$ if and only if $x$ is odd.

Combining the two observations, $x^2 - 1$ is divisible by $24$ if and only if $x$ is divisible by neither $2$ nor $3$.

So the problem reduces to counting how many integers in the range $[1, N]$ are not divisible by $2$ and not divisible by $3$. You can solve this using the **inclusion-exclusion principle**.

Initially, consider all $N$ integers from $1$ to $N$ as possible impostor IDs.

Now, remove the integers that are divisible by $2$, because they cannot be impostors. There are $\lfloor N / 2 \rfloor$ such integers.

Then, remove the integers that are divisible by $3$, because they also cannot be impostors. There are $\lfloor N / 3 \rfloor$ such integers.

However, integers divisible by both $2$ and $3$ have now been removed twice. These are exactly the integers divisible by $6$, and there are $\lfloor N / 6 \rfloor$ of them. So, add them back once.

Thus, the final answer is $N - \lfloor N / 2 \rfloor - \lfloor N / 3 \rfloor + \lfloor N / 6 \rfloor$.

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

void solve(int tc)
{
    LL N;
    cin >> N;

    cout << N - N / 2 - N / 3 + N / 6;
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

<details>
<summary>Hint 3</summary>

Check which IDs from $1$ to $24$ are impostors. What happens to the pattern after every $24$ IDs?

</details>

<details>
<summary>Alternate Solution</summary>

Another way to solve the problem is to use the periodic nature of remainders modulo $24$.

The value of $x^2 - 1$ modulo $24$ depends only on $x$ modulo $24$. So, if an ID $x$ is an impostor, then $x + 24$ is also an impostor. Similarly, if $x > 24$, then $x$ is an impostor if and only if $x - 24$ is an impostor.

Here is a simplified proof: Since $x + 24 \equiv x \pmod {24}$, we also have $(x + 24)^2 \equiv x^2 \pmod {24}$. Subtracting $1$ from both sides gives $(x + 24)^2 - 1 \equiv x^2 - 1 \pmod {24}$. Therefore, $x^2 - 1$ is divisible by $24$ if and only if $(x + 24)^2 - 1$ is divisible by $24$.

Therefore, the pattern of impostor IDs repeats every $24$ numbers.

Since $24$ is small, you can first check all IDs from $1$ to $24$ and mark which remainders are impostors. Then split the range $[1, N]$ into full blocks of length $24$ and one remaining suffix.

Let $g = \lfloor N / 24 \rfloor$. If there are $k$ impostors in the first block from $1$ to $24$, then there are $g \times k$ impostors in the first $24g$ IDs.

After that, only the IDs from $24g + 1$ to $N$ remain. There are at most $23$ of them, so you can check them one by one.

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

void solve(int tc)
{
    LL N, i;
    cin >> N;

    vector<int> isImpostor(25, 0);
    int k = 0;

    for(i = 1; i <= 24; i++)
    {
        if(((i * i - 1) % 24) == 0)
        {
            isImpostor[i % 24] = 1;
            k++;
        }
    }

    LL g = N / 24;
    LL ans = g * k;

    for(i = 24 * g + 1; i <= N; i++) if(isImpostor[i % 24]) ans++;

    cout << ans;
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
