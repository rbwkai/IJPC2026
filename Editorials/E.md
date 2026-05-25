# AutoCAD Mayhem

Problem Setter: [Mishkat Ahmed Khan](https://codeforces.com/profile/C01d)  

Estimated Difficulty: 900  

Tag(s): Math, Sorting

<details>
<summary> Hint 1</summary>

Think of the properties of similar triangles.

</details>

<details>
<summary> Hint 2</summary>

Observe that the given side lengths are not necessarily sorted.

</details>

<details>
<summary>Solution</summary>

This is the more elegant solution. However, there's an alternative solution coming.

Two triangles are similar if their corresponding side lengths are proportional.

Let the first triangle have sides:

\[
(a,b,c)
\]

and the second triangle have sides:

$$
(d,e,f)
$$

Since the order of the sides is unknown, we first sort both triples in non-decreasing order.

Suppose after sorting we get:

$$
x_1 \le x_2 \le x_3
$$

and

$$
y_1 \le y_2 \le y_3
$$


If the triangles are similar, then the ratios of corresponding sides must be equal:

$$
\frac{x_1}{y_1} = \frac{x_2}{y_2} = \frac{x_3}{y_3}
$$

Instead of using floating point division (which may cause precision issues), we compare the ratios using cross multiplication:

$$
x_1 \times y_2 = y_1 \times x_2
$$

and

$$
x_2 \times y_3 = y_2 \times x_3
$$

If both conditions are true, the triangles are similar; otherwise, they are not.

Time Complexity = $\mathcal{O}(1)$

<details>

<summary>Code</summary>

```cpp
#include<bits/stdc++.h>
using namespace std;

#define ll long long

void solve() {
    vector<ll> labib(3);
    for(ll i=0; i<3; i++) cin >> labib[i];

    vector<ll> jehad(3);
    for(ll i=0; i<3; i++) cin >> jehad[i];

    sort(labib.begin(), labib.end());
    sort(jehad.begin(), jehad.end());

    if(labib[0] * jehad[1] == labib[1] * jehad[0] and
        labib[1] * jehad[2] == labib[2] * jehad[1] and
        labib[0] * jehad[2] == labib[2] * jehad[0]) {
        cout << "YES\n";
        return;
    }

    cout << "NO\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll T = 1;
    // cin >> T;

    while (T--) {
        solve();
    }

    return 0;
}
```

</details>
</details>

<details>
<summary>Alternative Solution</summary>

There's an interesting alternative solution for this problem.

Instead of sorting the side lengths, we can directly try every possible correspondence between the sides of the second triangle and the first triangle.

Let the first triangle have sides:

$$
(a,b,c)
$$

and the second triangle have sides:

$$
(d,e,f)
$$

Two triangles are similar if there exists some arrangement of the second triangle’s sides such that:

$$
\frac{a}{x} = \frac{b}{y} = \frac{c}{z}
$$

where

$$
(x,y,z)
$$

is a permutation of

$$
(d,e,f)
$$

Since a triangle has exactly:

$$
3! = 6
$$

possible permutations, we can simply test all six arrangements.

For each permutation, we check whether the corresponding side ratios are equal.

To avoid floating point precision issues, we compare ratios using cross multiplication:

$$
a \times y = b \times x
$$

$$
b \times z = c \times y
$$

$$
a \times z = c \times x
$$

If all three conditions hold for any permutation, then the triangles are similar.

Time Complexity = $\mathcal{O}(1)$

```cpp
#include<bits/stdc++.h>
using namespace std;

#define ll long long

bool similar(ll a, ll b, ll c, ll x, ll y, ll z) {
    return (a * y == b * x) &&
           (b * z == c * y) &&
           (a * z == c * x);
}

void solve() {

    ll a, b, c;
    cin >> a >> b >> c;

    ll d, e, f;
    cin >> d >> e >> f;

    vector<vector<ll>> perm = {
        {d, e, f},
        {d, f, e},
        {e, d, f},
        {e, f, d},
        {f, d, e},
        {f, e, d}
    };

    for(auto p : perm) {
        if(similar(a, b, c, p[0], p[1], p[2])) {
            cout << "YES\n";
            return;
        }
    }

    cout << "NO\n";
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll T = 1;
    // cin >> T;

    while(T--) {
        solve();
    }

    return 0;
}
```
