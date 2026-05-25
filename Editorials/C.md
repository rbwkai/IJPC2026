# Strong Password

Problem Setter: [Md. Wasi Ul Habib](https://codeforces.com/profile/CodingPariNaa)

Estimated Difficulty: 1400

Tag(s): Constructive, Number Theory

### The Problem in a Nutshell
We are given an integer $n$ and a digit $d$. Our goal is to find a positive number that is divisible by $n$, uses only the digit $d$ and $0$ and contains at most $n$ digits.

<details>
<summary>Hint 1</summary>

How many unique remainders can there be if we divide any number by $n$?
</details>

<details>
<summary>Hint 2</summary>

If $a \equiv r \pmod n$ and $b \equiv r \pmod n$, then $n \mid a-b$.
</details>

<details>
<summary>Hint 3</summary>

If you generate $n$ numbers and divide all of them by $n$, it is guaranteed that at least one of them will be divisible by $n$ or at least two of them will have the same remainder when they are divided by $n$. Why?
</details>

<details>
<summary>Hint 4</summary>

What should the sequence of $n$ numbers look like if you want to make sure that the absolute difference of any two contains only the digit $d$ and $0$?
</details>

<details>
<summary>Solution</summary>

### Observation 1: The Set of Possible Remainders
When we divide any number by $n$, the remainder must fall within the range $[0, 1, 2, ..., n-1]$. This means there are exactly $n$ possible unique remainders.

### Observation 2: Generating a Sequence
Let's construct a sequence of $n$ numbers, where each number is formed entirely of the digit $d$:
* $S_{1}=d$
* $S_{2}=dd$
* $S_{3}=ddd$
* $S_{n}=dd...d$ ($n$ occurrences of $d$)

Now, let's look at the remainders of these $n$ numbers when divided by $n$.

**Case 1: We hit a 0 remainder.**
If any $S_{i} \equiv 0 \pmod n$, we are done! The number $S_{i}$ is already a multiple of $n$ and consists only of the digit $d$.

**Case 2: We never hit a 0 remainder.**
If none of the numbers are divisible by $n$, then the remainder 0 is never used. This leaves us with $n-1$ possible remainders: $[1, 2, ..., n-1]$.

### Using Pigeonhole Principle
We have $n$ numbers in our sequence $(S_{1}, S_{2}, ..., S_{n})$, but only $n-1$ possible remainders available. By the Pigeonhole Principle, at least two different numbers in our sequence must yield the exact same remainder when divided by $n$.

Let's assume $S_{i}$ and $S_{j}$ (where $i>j$) have the same remainder $r$. Using modular arithmetic properties:
* $S_{i} \equiv r \pmod n$
* $S_{j} \equiv r \pmod n$

If we subtract the smaller number from the larger one:
* $S_{i}-S_{j} \equiv (r-r) \pmod n$
* $S_{i}-S_{j} \equiv 0 \pmod n$

This proves that $S_{i}-S_{j}$ is perfectly divisible by $n$.

**What does $S_{i}-S_{j}$ look like?**

Because of how we constructed our sequence, subtracting a smaller sequence from a larger one always leaves a trail of $d$'s followed by a trail of 0's.

*Example:* Let $i=6$ and $j=3$,
$$S_{6}-S_{3}=ddddd-ddd=ddd000$$

The resulting number consists of exactly $(i-j)$ occurrences of $d$, followed by exactly $j$ occurrences of 0. This perfectly satisfies the problem's conditions!

### Implementation Details
Generating massive numbers and checking their remainders would cause integer overflow. Instead, we can build the remainders iteratively using modular arithmetic.

If we know the remainder of $S_{i-1}$, we can find the remainder of $S_{i}$ by appending the digit $d$:
$$R_{i} = (R_{i-1} \times 10 + d) \pmod n$$

**Algorithm:**
1.  Maintain an array `seen` of size $n$, initialized to -1, to track which sequence length produced which remainder.
2.  Initialize a running remainder $R=0$.
3.  Loop $i$ from 1 to $n$:
    * Update the remainder: $R=(R\times 10+d) \pmod n$.
    * If $R==0$: Your answer is $i$ occurrences of $d$. Stop.
    * If `seen[R]` is already filled: Let $j = seen[R]$. Your answer is $(i-j)$ occurrences of $d$, followed by $j$ occurrences of 0. Stop.
    * Otherwise, record the current length: `seen[R]=i`.

**Complexity Assessment**
* **Time Complexity:** $\mathcal{O}(n)$. We iterate at most $n$ times before the Pigeonhole Principle guarantees a collision.
* **Space Complexity:** $\mathcal{O}(n)$. We need an array of size $n$ to store the first occurrence of each remainder.

</details>

<details>
<summary>Code</summary> 

```cpp
#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(0); cin.tie(0)

void pre()
{
    fastio;
}

void solve(int tc)
{
    int n, d;
    cin >> n >> d;
    
    int R = 0;
    // Maintain an array seen of size n, initialized to -1
    vector<int> seen(n, -1);
    
    // Loop i from 1 to n:
    for(int i = 1; i <= n; i++)
    {
        // Update the remainder
        R = (R * 10 + d) % n;
        
        // If R == 0: Our answer is i occurrences of d. Stop.
        if (R == 0)
        {
            string ans(i, d + '0');
            cout << ans << "\n";
            return;
        }
        
        // If seen[R] is already filled: 
        if (seen[R] != -1)
        {
            // Let j = seen[R]. 
            int j = seen[R];
            
            // Our answer is (i - j) occurrences of d, followed by j occurrences of 0. Stop.
            string ans(i - j, d + '0');
            ans.append(j, '0');
            
            cout << ans << "\n";
            return;
        }
        
        // Otherwise, record the current length
        seen[R] = i;
    }
}

signed main()
{
    pre();
    int tc, tt = 1;
    cin >> tt;
    for (tc = 1; tc <= tt; tc++)
    {
        // cout << "Case " << tc << ": ";
        solve(tc);
    }
    return 0;
}
