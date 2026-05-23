# XORnacci

Problem Setter: [Jannatul Fardus Rakhi](https://codeforces.com/profile/sectumsemprra)

Estimated Difficulty: 1200

Tag(s): Bitmasks

<details>
<summary>Hint</summary>
A special property of XOR: $a \oplus a = 0$
</details>

<details>
<summary>Solution</summary>
The sequence is extended using the rule $a_i = a_{i-2} \oplus a_{i-1}$ for $i > m$. Let's examine the terms immediately following the given elements to find a pattern:
    
- $a_{m+1} = a_{m-1} \oplus a_m$
- $a_{m+2} = a_m \oplus a_{m+1} = a_m \oplus (a_{m-1} \oplus a_m) = a_{m-1}$
- $a_{m+3} = a_{m+1} \oplus a_{m+2} = (a_{m-1} \oplus a_m) \oplus a_{m-1} = a_m$
- $a_{m+4} = a_{m+2} \oplus a_{m+3} = a_{m-1} \oplus a_m$

Starting from index $m-1$, the sequence traps itself into a repeating cycle of length 3: 
$$\dots, a_{m-1}, \ a_m, \ (a_{m-1} \oplus a_m), \ a_{m-1}, \ a_m, \ (a_{m-1} \oplus a_m), \ \dots$$

The total XOR sum of any single full block of 3 elements in this cycle is $a_{m-1} \oplus a_m \oplus (a_{m-1} \oplus a_m) = 0$. Because full blocks contribute nothing to the total XOR sum, we only need to track the leftover elements at the end of the sequence.

The repeating zone spans from index $m-1$ to $n$, containing $K = n - m + 2$ elements. We find the remainder $R = K \pmod 3$:
* **If $R = 0$**: The repeating zone forms complete blocks of 3. They all cancel out to $0$. The final answer is the prefix sum up to $m-2$: $\bigoplus_{i=1}^{m-2} a_i$.
* **If $R = 1$**: Exactly one element ($a_{m-1}$) is left over. The final answer is $\left(\bigoplus_{i=1}^{m-2} a_i\right) \oplus a_{m-1} = \bigoplus_{i=1}^{m-1} a_i$.
* **If $R = 2$**: Two elements ($a_{m-1} \oplus a_m$) are left over. The final answer is $\left(\bigoplus_{i=1}^{m-2} a_i\right) \oplus a_{m-1} \oplus a_m = \bigoplus_{i=1}^{m} a_i$.

<details>
<summary>Code</summary>

```cpp
#include <iostream>
#include <vector>

using namespace std;

void solve() {
    long long n, m;
    cin >> n >> m;
    
    vector<long long> P(m + 1, 0);
    for (int i = 1; i <= m; ++i) {
        long long val;
        cin >> val;
        P[i] = P[i - 1] ^ val;
    }
    
    long long K = n - m + 2;
    int R = K % 3;
    
    if (R == 0) {
        cout << (m - 2 >= 1 ? P[m - 2] : 0) << "\n";
    } else if (R == 1) {
        cout << P[m - 1] << "\n";
    } else {
        cout << P[m] << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
```

</details>
</details>


