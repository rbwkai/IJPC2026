# XORnacci

Problem Setter: [Jannatul Fardus Rakhi](https://codeforces.com/profile/sectumsemprra)

Estimated Difficulty: 1200

Tag(s): Bitmasks

<details>
<summary>Hint</summary>
Use these properties of XOR:

- $a \oplus b = b \oplus a $
- $a \oplus 0 = a$
- $a \oplus a = 0$
</details>

<details>
<summary>Solution</summary>

The sequence is extended using the rule $a_i = a_{i-2} \oplus a_{i-1}$ for $i > m$. Let’s check the first few terms after the given elements:

- $a_{m+1} = a_{m-1} \oplus a_m$
- $a_{m+2} = a_m \oplus a_{m+1} = a_m \oplus (a_{m-1} \oplus a_m) = a_{m-1}$
- $a_{m+3} = a_{m+1} \oplus a_{m+2} = (a_{m-1} \oplus a_m) \oplus a_{m-1} = a_m$
- $a_{m+4} = a_{m+2} \oplus a_{m+3} = a_{m-1} \oplus a_m$

We can observe that from index $m-1$ onward, the sequence repeats with period $3$. So the entire sequence is:  
$\displaystyle a_1, \dots, a_{m-2}, \underbrace{a_{m-1},\ a_m,\ (a_{m-1}\oplus a_m),\ a_{m-1},\ a_m,\ (a_{m-1}\oplus a_m),\ \dots}_{\text{period }3}$

Let a complete block be three consecutive elements of the repeating portion of the sequence. The XOR of one full block is $a_{m-1}\oplus a_m\oplus(a_{m-1}\oplus a_m)=0$.

Therefore, every complete block contributes nothing to the total XOR sum, and we only need to consider the first $m-2$ elements and the final incomplete block.

The repeating section runs from index $m-1$ through $n$, so it contains $K=n-m+2$ elements. Let $R=K \bmod 3$. This is the size of the final incomplete block.

- If $R = 0$: all elements form complete blocks, so they cancel out. The final answer is the XOR of the first $m-2$ elements:  
  $\displaystyle \bigoplus_{i=1}^{m-2} a_i$

  ![R0](./img/XORnacci-Diagram-0.png 'R = 0')

- If $R = 1$: one extra element $a_{m-1}$ remains. The final answer is  
  $\displaystyle \left(\bigoplus_{i=1}^{m-2} a_i\right)\oplus a_{m-1}=\bigoplus_{i=1}^{m-1} a_i$

  ![R1](./img/XORnacci-Diagram-1.png 'R = 1')

- If $R = 2$: two extra elements $a_{m-1}$ and $a_m$ remain. The final answer is  
  $\displaystyle \left(\bigoplus_{i=1}^{m-2} a_i\right)\oplus a_{m-1}\oplus a_m=\bigoplus_{i=1}^{m} a_i$

  ![R2](./img/XORnacci-Diagram-2.png 'R = 2')

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
    int i, n, m;
    cin >> n >> m;

    vector<int> v(m + 1);
    for(i = 1; i <= m; i++) cin >> v[i];

    vector<int> prefXor(m + 1);
    prefXor[0] = 0;
    for(i = 1; i <= m; i++) prefXor[i] = prefXor[i - 1] ^ v[i];

    int K = n - m + 2;
    int R = K % 3;

    if(R == 0) cout << prefXor[m - 2];
    else if(R == 1) cout << prefXor[m - 1];
    else cout << prefXor[m];
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
