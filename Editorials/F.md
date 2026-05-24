# Still a Group Project??

Problem Setter: [MD. Mahiul Kabir](https://codeforces.com/profile/rbwkai)

Estimated Difficulty: 1200

Tag(s): Greedy, Implementation

<details>
<summary>Solution</summary>

The problem asks whether we can transform an initial array $a$ into a target array $b$ by swapping elements that are exactly $m$ indices apart.

When you can only swap elements at positions $i$ and $i+m$, an element at index $i$ can only ever move to $i \pm m$, $i \pm 2m$, $i \pm 3m$, and so on. In other words, the array is divided into $m$ completely independent groups based on the index modulo $m$ ($i \pmod m$). 

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
#include <iostream>
#include <vector>
#include <algorithm>

void solve() {
    long long n, k; 
    std::cin >> n >> k; 
    
    std::vector<long long> a(n); 
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }
    
    std::vector<long long> b(n); 
    for (int i = 0; i < n; ++i) {
        std::cin >> b[i];
    }

    // 2D vectors for separating elements into independent congruence classes
    std::vector<std::vector<long long>> ga(k);
    std::vector<std::vector<long long>> gb(k);
    
    // Populate based on index modulo k
    for (int i = 0; i < n; ++i) {
        ga[i % k].push_back(a[i]);
        gb[i % k].push_back(b[i]);
    }
    
    // Sort independent classes to check if they contain the exact same elements
    for (int i = 0; i < k; ++i) {
        std::sort(ga[i].begin(), ga[i].end());
        std::sort(gb[i].begin(), gb[i].end());
    }

    // Direct comparison of 2D vectors and conditional output
    if (ga == gb) {
        std::cout << "Yes\n";
    } else {
        std::cout << "No\n";
    }
}

int main() {
    // Optimize standard I/O operations for performance
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int tt = 1; 
    std::cin >> tt;
    for (int i = 0; i < tt; ++i) {
        solve();
    }
    
    return 0;
}
```
</details>

<details>
<summary>Cool Alt solution</summary>
Create an array of pairs for each arrangement, where the first element of the pair is the value of the array, and the second element is the *group number* of that element, i.e., index modulo $m$ ($i \pmod m$), then sort (with any transitive comparator of your choice!). Check for the final array becomes same for both $a$ and $b$. *But, why this works?* 

Kudos to [Rafio](https://codeforces.com/profile/Rafio) for coming up with this one..:D
    
</details>
</details>
