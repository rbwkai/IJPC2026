# Moushi Is In Trouble

Problem Setter: [Fariya Ahmed](https://codeforces.com/profile/fariyapracticekorena)

Estimated Difficulty: 900

Tag(s): Math

<details>
<summary>Hint1</summary>
How can you find the parity of a Base-10 number?
</details>
<details>
<summary>Hint2</summary>
How does the parity of the base affect the parity of multi-digit numbers?
</details>
<details>
<summary>Hint3</summary>
11, 13, 15, 17, 19, 121, 132 are all even numbers in Base-9.
</details>

<details>
<summary>Solution</summary>
A number in Base-9 can be written as:

```math
a_0 \times 9^0 + a_1 \times 9^1 + a_2 \times 9^2 + \dots
```

9 being an odd number ,every power of 9 is also odd.Therefore,

```math
a_0 \times 9^0 + a_1 \times 9^1 + a_2 \times 9^2 + \dots
```

has the same parity as

```math
a_0 + a_1 + a_2 + \dots
```

because multiplying by an odd number does not change parity.

So a Base-9 number is:

- **even** if the sum of its digits is even
- **odd** if the sum of its digits is odd

Example:

```math
132_9 = 2\times9^0 + 3\times9^1 + 1\times9^2
```

Digit sum:

```math
2+3+1=6
```

Since 6 is even, `132₉` is also even.

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

void solve() {
    int len;
    cin>>len;
    string number;
    cin>>number;
    int ans = 0;
    for(auto &digit: number)
    {
        ans+= (digit - '0');
    }
    if(ans%2)cout<<"NO"<<endl;
    else cout<<"YES"<<endl;
}

int main()
{
    pre();

    int tc, tt = 1;
    cin >> tt;

    for(tc = 1; tc <= tt; tc++)
    {
        // cout << "Case " << tc << ": ";
        solve();
    }

    return 0;
}
```

</details>
</details>
