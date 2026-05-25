# Glorious Batch-24!

Problem Setter: [Fariya Ahmed](https://codeforces.com/profile/fariyapracticekorena)

Estimated Difficulty: 900

Tag(s): Number Theory

<details>
<summary>Hint1</summary>
Rewrite the expression:

```math
x^2 - 1 = (x-1)(x+1)
```

Now think about what conditions are needed for this product to be divisible by `24`.

</details>

<details>
<summary>Hint2</summary>
The product must be divisible by both 8 and 3. Try analyzing them separately.

</details>

<details>
<summary>Hint3</summary>
What happens if x is even? Can their product be divisible by 8? What happens if it's odd?

</details>

<details>
<summary>Hint4</summary>
If x is odd, then (x-1) and (x+1) are two consecutive even numbers. Among any two consecutive even numbers:

- one is divisible by `2`
- the other is divisible by `4`

So their product is always divisible by `8`.

</details>

<details>
<summary>Hint5</summary>
Among any three consecutive integers:

```math
x-1,\ x,\ x+1
```

exactly one is divisible by 3. Since (x^2-1) must be divisible by 3, x cannot be divisible by `3`.


</details>

<details>
<summary>Solution</summary>
Thus our solution is - every odd number that is not divisible by 3.

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
    LL n;
    cin>>n;
    cout<< n- n/2 - n/3 + n/6 <<endl;
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
