# D. Glass Bridge

**Problem Setter:** [Nayeem Hossain Ahad](https://codeforces.com/profile/flying_saucer)  
**Estimated Difficulty:** 1400  
**Tag(s):** Probability, Combinatorics, Math  

---

### Hint 1
<details>
<summary>View Hint</summary>
Who is the last person in the queue to have a non-zero probability of winning?
</details>

### Hint 2
<details>
<summary>View Hint</summary>
For the i-th person in the queue to win, exactly how many previous players must be eliminated? In how many different configurations can these eliminations occur across the bridge?
</details>

### Hint 3
<details>
<summary>View Hint</summary>
What is the probability of one specific sequence of guesses occurring where the i-th person wins?
</details>

---

### Solution

For the $i$-th person to win, all $(i - 1)$ players that started before them must be eliminated. A player is eliminated when they step on a fragile panel.

Notice that regardless of who wins or dies, exactly $M$ panel guesses will be made in total across the bridge (one for each of the $M$ steps). Since each guess has a $50\%$ (or $\frac{1}{2}$) chance of being correct or incorrect, any specific sequence of $M$ guesses has a probability of $\frac{1}{2^M}$.

For the $i$-th person to be the winner, exactly $(i - 1)$ wrong guesses must be made by their predecessors, and the remaining $M - (i - 1)$ guesses must be correct. The number of ways to choose which $(i - 1)$ steps out of the $M$ steps result in a wrong guess is given by the binomial coefficient $\binom{M}{i - 1}$.

Therefore, the probability of the $i$-th person winning is:

$$P(i) = \frac{\binom{M}{i - 1}}{2^M}$$

From this equation, it is evident that the winning chance follows a binomial distribution. Because $2^M$ is constant for a given bridge, the probability depends entirely on the value of $\binom{M}{i - 1}$.

To maximize the winning probability, we need to maximize $\binom{M}{i - 1}$. The binomial coefficient $\binom{n}{k}$ reaches its maximum when $k = \lfloor \frac{n}{2} \rfloor$.  
Therefore, we want:

$$i - 1 = \lfloor \frac{M}{2} \rfloor$$

$$i = \lfloor \frac{M}{2} \rfloor + 1$$

> **Note:** Because $\binom{n}{k} = \binom{n}{n - k}$, both the floor and ceiling of $\frac{M}{2}$ yield the same maximum probability. So picking either is fine.

However, it is not always possible to pick the $(\lfloor \frac{M}{2} \rfloor + 1)$-th position if the total number of players $N$ is less than $\lfloor \frac{M}{2} \rfloor + 1$. Because $\binom{M}{k}$ is strictly increasing for $k \le \lfloor \frac{M}{2} \rfloor$, if $N < \lfloor \frac{M}{2} \rfloor + 1$, the optimal choice is simply the last available person in the queue, which is $N$.

Thus, the optimal position to choose is $\min(N, \lfloor \frac{M}{2} \rfloor + 1)$.

---

### Code (C++)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    
    int t;
    cin >> t;
    while(t--){
        int n, m; 
        cin >> n >> m;
        cout << min(n, m / 2 + 1) << '\n';
    }

    return 0;
}
