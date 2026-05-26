# Moushi Is In Trouble

Problem Setter: [Fariya Ahmed](https://codeforces.com/profile/fariyapracticekorena)

Estimated Difficulty: 900

Tag(s): Math

<details>
<summary>Hint 1</summary>

How can you find the parity of a Base-10 number?

</details>

<details>
<summary>Hint 2</summary>

How does the parity of the base affect the parity of multi-digit numbers?

</details>

<details>
<summary>Hint 3</summary>

Take all the numbers from $1_9$ to $25_9$ and check which numbers are even. Then take some random $9$-based numbers and test whether they are odd or even. Try to notice a pattern, and then try to prove whether it will always work.

</details>

<details>
<summary>Solution</summary>

Let the $9$-based number be $X = a_{n-1}a_{n-2}\dots a_1a_0$. Its decimal value is  
$\displaystyle\sum_{i=0}^{n-1} a_i \times 9^i = a_0 \times 9^0 + a_1 \times 9^1 + \dots + a_{n-1} \times 9^{n-1}$.

Since $9$ is odd, every power of $9$ is also odd. Multiplying a digit by an odd number does not change its parity. Therefore, the parity of $X$ is the same as the parity of $\displaystyle\sum_{i=0}^{n-1} a_i = a_0 + a_1 + \dots + a_{n-1}$.

So a $9$-based number is:

- **even** if the sum of its digits is even
- **odd** if the sum of its digits is odd

Example:

$132_9 = 1 \times 9^2 + 3 \times 9^1 + 2 \times 9^0$ and the digit sum is $1 + 3 + 2 = 6$.

Since $6$ is even, $132_9$ is also even.

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
    int n;
    string X;
    cin >> n >> X;

    int digitSum = 0;
    for(auto digit: X)
    {
        digitSum += digit - '0';
    }

    if(digitSum % 2 == 0) cout << "YES";
    else cout << "NO";
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
