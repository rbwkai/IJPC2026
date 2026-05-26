# Still a Group Project??

Problem Setter: [MD. Mahiul Kabir](https://codeforces.com/profile/rbwkai)

Estimated Difficulty: 1200

Tag(s): Greedy, Implementation, Sorting

<details>
<summary>Solution</summary>

The problem asks whether you can transform the initial array $a$ into the target array $b$ by swapping elements that are exactly $m$ indices apart.

If an element starts at index $i$, then it can only move to indices $i - m$, $i + m$, $i - 2m$, $i + 2m$, and so on. In other words, it can only move to positions with the same remainder modulo $m$.

So the indices are divided into $m$ independent groups, one for each possible value of $i \bmod m$ from $0$ to $m - 1$.

No operation can move an element from one group to another.

Within one group, the allowed swaps are between neighboring elements of that group. So, just like Bubble Sort, the elements inside the same group can be rearranged in any order.

Therefore, the transformation is possible if and only if, for every remainder $r$, the multiset of values at indices $i \bmod m = r$ is the same in both arrays $a$ and $b$.

Now the solution is simple. For each remainder $r$, collect all values from array $a$ whose indices have remainder $r$, and do the same for array $b$. Sort both groups and compare them. If all groups match, output `YES`; otherwise, output `NO`.

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
    int n, m;
    cin >> n >> m;

    vector<int> a(n), b(n);
    for(int i = 0; i < n; i++) cin >> a[i];
    for(int i = 0; i < n; i++) cin >> b[i];

    vector<vector<int>> ga(m), gb(m);

    for(int i = 0; i < n; i++)
    {
        ga[i % m].push_back(a[i]);
        gb[i % m].push_back(b[i]);
    }

    for(int r = 0; r < m; r++)
    {
        sort(ga[r].begin(), ga[r].end());
        sort(gb[r].begin(), gb[r].end());

        if(ga[r] != gb[r])
        {
            cout << "NO";
            return;
        }
    }

    cout << "YES";
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
<summary>Alternate Solution</summary>

There is another way to express the same idea.

For each element, store two pieces of information:

1. the value of the element
2. the group it belongs to, which is its index modulo $m$

So every element becomes a pair $(\text{value}, \text{group})$.

If the transformation is possible, then after sorting these pairs, the list built from array $a$ must be exactly the same as the list built from array $b$.

So the solution is to build these two lists of pairs, sort them, and compare them directly.

<details>
<summary>Code</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(0); cin.tie(0)
using LL = long long;
using PII = pair<int, int>;

void pre()
{
    fastio;
}

void solve(int tc)
{
    int n, m;
    cin >> n >> m;

    vector<int> a(n), b(n);
    for(int i = 0; i < n; i++) cin >> a[i];
    for(int i = 0; i < n; i++) cin >> b[i];

    vector<PII> itemsA, itemsB;

    for(int i = 0; i < n; i++)
    {
        itemsA.push_back({a[i], i % m});
        itemsB.push_back({b[i], i % m});
    }

    sort(itemsA.begin(), itemsA.end());
    sort(itemsB.begin(), itemsB.end());

    if(itemsA == itemsB) cout << "YES";
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
