# Strong Password

Problem Setter: [Md. Wasi Ul Habib](https://codeforces.com/profile/CodingPariNaa)

Estimated Difficulty: 1400

Tag(s): Constructive, Number Theory

<details>
<summary>Hint 1</summary>

How many possible remainders can a number have when divided by $n$?

</details>

<details>
<summary>Hint 2</summary>

If two numbers have the same remainder when divided by $n$, what can you say about their difference?

</details>

<details>
<summary>Hint 3</summary>

Try generating $n$ numbers. If none of them has remainder $0$, then two of them must have the same remainder.

</details>

<details>
<summary>Hint 4</summary>

Can you generate the numbers in such a way that the difference of any two generated numbers always contains only the digits $d$ and $0$?

</details>

<details>
<summary>Solution</summary>

When a number is divided by $n$, its remainder must be one of $0, 1, 2, \dots, n - 1$. So there are exactly $n$ possible remainders.

Now, suppose you have two numbers $a$ and $b$ such that $a \bmod n = b \bmod n$. Then their difference is divisible by $n$, because $(a - b) \bmod n = 0$.

This gives a useful direction. If you can find two numbers with the same remainder modulo $n$, then their difference will be divisible by $n$.

However, that difference is not automatically a valid answer. The problem also requires the answer to contain only the digits $d$ and $0$, have no leading zero, and have length at most $n$.

### Idea

Generate the following $n$ numbers: $S_1 = d$, $S_2 = dd$, $S_3 = ddd$, and so on up to $S_n = dd\dots d$ ($n$ occurrences of $d$).

Now, consider the difference between two such numbers $S_i$ and $S_j$, where $i > j$.

For example, if $i = 6$ and $j = 3$, then $S_i - S_j = dddddd - ddd = ddd000$.

In general, $S_i - S_j$ contains exactly $i - j$ occurrences of $d$, followed by exactly $j$ occurrences of $0$. So this difference always satisfies the digit condition and has no leading zero. Also, its length is $i$, which is at most $n$.

So now the goal is clear: among $S_1, S_2, \dots, S_n$, find either one number with remainder $0$, or two numbers with the same remainder.

If some $S_i \bmod n = 0$, then $S_i$ itself is a valid answer.

Otherwise, none of the $n$ numbers has remainder $0$. Then all their remainders are among $1, 2, \dots, n - 1$, which gives only $n - 1$ possible remainders. By the **Pigeonhole Principle**, two of the numbers must have the same remainder. If these numbers are $S_i$ and $S_j$ with $i > j$, then $S_i - S_j$ is divisible by $n$ and satisfies all constraints.

To implement this without constructing huge numbers, maintain only the current remainder. If the remainder of $S_{i-1}$ is $R$, then after appending digit $d$, the new remainder becomes $R = (R \times 10 + d) \bmod n$.

Use an array $seen$ where $seen[r]$ stores the first length that produced remainder $r$. When a repeated remainder is found, construct the answer from the two lengths.

The time complexity is $\mathcal{O}(n)$ per test case, and the space complexity is $\mathcal{O}(n)$.

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

void printRepeated(int cnt, char ch)
{
    for(int i = 0; i < cnt; i++) cout << ch;
}

void solve(int tc)
{
    int n, d;
    cin >> n >> d;

    int R = 0;
    vector<int> seen(n, -1);

    for(int i = 1; i <= n; i++)
    {
        R = (R * 10 + d) % n;

        if(R == 0)
        {
            printRepeated(i, d + '0');
            return;
        }

        if(seen[R] != -1)
        {
            int j = seen[R];
            printRepeated(i - j, d + '0');
            printRepeated(j, '0');
            return;
        }

        seen[R] = i;
    }
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
<summary>Alternative Solution</summary>

If the constraints were extremely low, a natural approach would be to brute-force the problem. We could have generated and checked all possible string combinations of the allowed characters, checking all the numbers like $d$, $0$, $d0$, $dd$, $00$, $0d$, and so on, filtering out those with leading zeros and checking if they are divisible by $n$.

However, this is not an option anymore. The number of combinations grows exponentially ($2^L$ for a string of length $L$), meaning for constraints like $n \le 10^5$, a brute-force approach would immediately result in a **Time Limit Exceeded (TLE)** error.

What we can do instead is optimize this process by realizing we do not need to track the massive numbers themselves. We only care about their remainders when divided by $n$. 

Since there are exactly $n$ possible remainders ($0$ to $n-1$), we can treat these remainders as states in a graph and traverse them using **Breadth-First Search (BFS)**. From any current state with remainder $R$, appending a new digit transitions us to a new state. The mathematical transitions are strictly:

* **Appending 0:** The new remainder becomes $(R \times 10) \bmod n$.
* **Appending d:** The new remainder becomes $(R \times 10 + d) \bmod n$.

By using BFS, we guarantee that the first time we hit the target state (remainder $0$), we have found the shortest possible valid number.

#### Implementation Steps

1.  **Initialize BFS:** Start a queue and push the initial valid remainder: $d \bmod n$. *(We cannot start with `0` because leading zeros are not allowed).*
2.  **Track States:** Use a `parent` array to keep track of the visited states to avoid infinite loops and redundant checks. This array will also store the preceding state so we can retrace our path.
3.  **Track Digits:** Use another array `digit` to remember which character (`0` or `d`) was appended to reach the current remainder.
4.  **Backtrack:** Once we pop a state where $R=0$, we stop the BFS and backtrack through the `parent` array to construct our final answer string.

* **Time Complexity:** $\mathcal{O}(n)$ because we visit at most $n$ states.
* **Space Complexity:** $\mathcal{O}(n)$ to store the queue and tracking arrays.
  
<details>
<Summary>Code</Summary>
    
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
    int n, d;
    cin >> n >> d;

    // Base case: if the single digit 'd' is already divisible by 'n'
    if (d % n == 0)
    {
        cout << d << '\n';
        return;
    }

    vector<int> parent(n, -1);
    vector<char> digit(n, 0);
    queue<int> q;

    int start_R = d % n;
    q.push(start_R);
    parent[start_R] = -2; // Let's use -2 to mark the starting point
    digit[start_R] = d + '0';

    while (!q.empty())
    {
        int R = q.front();
        q.pop();

        if (R == 0) break; // We found a number divisible by n!

        // Option 1: Let's append a '0'
        int next_R1 = (R * 10) % n;
        if (parent[next_R1] == -1) // If we haven't seen this remainder yet
        {
            parent[next_R1] = R;
            digit[next_R1] = '0';
            q.push(next_R1);
        }

        // Option 2: Let's append a 'd'
        int next_R2 = (R * 10 + d) % n;
        if (parent[next_R2] == -1) // If we haven't seen this remainder yet
        {
            parent[next_R2] = R;
            digit[next_R2] = d + '0';
            q.push(next_R2);
        }
    }

    // We will build the final string by walking backward from remainder 0
    if (parent[0] != -1)
    {
        string ans = "";
        int curr = 0;
        
        while (curr != -2) // We must stop when we hit the starting point
        {
            ans += digit[curr];
            curr = parent[curr];
        }
        
        // Since we built the string backward, we must flip it before printing
        reverse(ans.begin(), ans.end());
        cout << ans;
    }
}

int main()
{
    pre();

    int tc, tt = 1;
    cin >> tt;

    for(tc = 1; tc <= tt; tc++)
    {
        solve(tc);
        cout << '\n';
    }

    return 0;
}
```
</details>
</details>
