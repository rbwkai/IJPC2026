# Still a Group Project??

Problem Setter: [MD. Mahiul Kabir](https://codeforces.com/profile/rbwkai)

Estimated Difficulty: 1200

Tag(s): Greedy, Implementation

<details>
<summary>Solution</summary>
The problem asks whether we can transform an initial array $a$ into a target array $b$ by swapping elements that are exactly $m$ indices apart. This is a trivial problem involving **independent equivalence classes** created by a fixed step size.

When you can only swap elements at positions $i$ and $i+m$, an element at index $i$ can only ever move to $i \pm m$, $i \pm 2m$, $i \pm 3m$, and so on. In other words, the array is partitioned into $m$ completely independent groups based on the index modulo $m$ ($i \pmod m$). 

For example, if $m=3$:
* Elements at positions $0, 3, 6, 9 \dots$ can swap with each other.
* Elements at positions $1, 4, 7, 10 \dots$ can swap with each other.
* Elements at positions $2, 5, 8, 11 \dots$ can swap with each other.

No operation can ever move an element from the first group into the second or third group. Within any single group, because we can swap adjacent elements inside that group (since their distance is exactly $1 \times m$), we can reorder the elements of that group into **any arbitrary permutation** we want (similar to standard Bubble Sort).

Thus, a valid transformation from $a$ to $b$ is possible if and only if, for every remainder $r$ from $0$ to $m-1$, the multiset of elements at indices $i \equiv r \pmod m$ in array $a$ is identical to the multiset of elements at indices $i \equiv r \pmod m$ in array $b$.

### Algorithm
1. Separate the elements of array $a$ and array $b$ into $m$ buckets based on $i \pmod m$.
2. Sort the elements within each bucket for both arrays.
3. Compare the corresponding sorted buckets of $a$ and $b$. If all pairs of buckets match perfectly, output `YES`. Otherwise, output `NO`.
<details>
<summary>Code</summary>

```cpp
//#pragma GCC optimize("Ofast,unroll-loops")
//#pragma GCC target("avx2,popcnt,lzcnt,abm,bmi,bmi2,fma,tune=native")

#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;
using ll = long long;
using vi = vector<ll>;
using pi = pair<ll, ll>;
using grid = vector<vi>;
 
template<class T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, 
                         tree_order_statistics_node_update>; 
#define en "\n"
#define ln " \n"[i==n-1]
#define F first
#define S second
#define pb push_back
#define all(_O) _O.begin(), _O.end() 
#define rall(_O) _O.rbegin(), _O.rend() 
#define badret return void(cout<<-1<<en)
#define boolret(_O) return void(cout<<(_O? "Yes":"No")<<en) 
#define fir(_O) for(int i=0, ii=(_O)-1; i<(_O); ++i, --ii)
#define fjr(_O) for(int j=0, jj=(_O)-1; j<(_O); ++j, --jj)



// 一心不乱
ll const N = 2e6+6;
ll const inf = 1e18; //0x3f3f3f3f3f3f;
ll const mod = 1e9+7; //998244353;

void solve(){
  ll n, k; cin>>n>>k; 
  vi a(n); fir(n) cin>>a[i];
  vi b(n); fir(n) cin>>b[i];                      //taking input

  grid ga(k), gb(k);                              //2d arrays for separating each independent class
  fir(n) ga[i%k].pb(a[i]), gb[i%k].pb(b[i]);      //populating based on index modulo k.
  fir(k) sort(all(ga[i])), sort(all(gb[i]));      //sorting independent classes to check if they're equal.

  boolret(ga==gb);                                //prints "Yes" if passed boolen is true, "No" otherwise, and returns.
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  int tt = 1; cin>>tt;
  fir(tt) solve();
}
```
</details>
</details>
