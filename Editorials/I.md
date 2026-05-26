# Iris Out

Problem Setter: [Irfanur Rahman Rafio](https://codeforces.com/profile/Rafio)

Estimated Difficulty: 800

Tag(s): Ad-hoc, Graphs

<details>
<summary>Hint</summary>

Analyze the effect of pressing one switch. Then check it for all four switches.

</details>

<details>
<summary>Solution</summary>

Let the four rooms be denoted by $A$ (top-left), $B$ (top-right), $C$ (bottom-left), and $D$ (bottom-right).

- Pressing the switch in room $A$ toggles the lights of room $B$ and $C$.
- Pressing the switch in room $B$ toggles the lights of room $A$ and $D$.
- Pressing the switch in room $C$ toggles the lights of room $A$ and $D$.
- Pressing the switch in room $D$ toggles the lights of room $B$ and $C$.

It is easy to observe that the four switches reduce to two independent operations:

1. Toggle the lights in the primary diagonal (room $A$ and $D$).
2. Toggle the lights in the secondary diagonal (room $B$ and $C$).

Now, consider the two diagonals separately.  
If the two lights on a diagonal are in different states (one is ON and another is OFF), then it is impossible to turn them both OFF at the same time. Because if Denji tries to turn one OFF, the other one will be turned ON.  
If the two lights on a diagonal are in the same state, then it is always possible to turn them both OFF. If they are both OFF, Denji doesn't have to do anything on that diagonal. If they are both ON, Denji can simply toggle them once to turn them both OFF.

So the final solution is to simply check whether rooms $A$ and $D$ have the same initial state and whether rooms $B$ and $C$ have the same initial state. If both conditions hold, output `YES`, otherwise, output `NO`.

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
    char a, b, c, d;
    cin >> a >> b >> c >> d;

    if(a == d and b == c) cout << "YES";
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

<details>
<summary>Alternate Solution</summary>

The building has four rooms, and each room can be either ON or OFF. So, the entire building can be in $2^4 = 16$ different configurations.

Next, consider what happens when Denji presses switches. Pressing switches changes the configuration of the building, moving it from one configuration to another. Since the number of possible configurations is finite, pressing switches can only move among these $16$ configurations. If Denji keeps pressing switches, eventually a configuration must repeat, and from that point onward, the same sequence of configurations will cycle forever.

Because of this, there is no benefit in pressing switches forever. Since there are only $16$ possible configurations, if Denji cannot reach the all-OFF configuration within $15$ steps, then he will never reach it at all.

With this in mind, you can think of the solution as follows. Starting from the initial configuration, try all possible choices of switch presses, while keeping track of the configurations. At each step, choose one of the rooms and press its switch, which leads to a new configuration. If at any point the configuration becomes the all-OFF configuration, then the answer is `YES`.

If all possible sequences of switch presses up to length $15$ are explored and none of them lead to the all-OFF configuration, then the answer must be `NO`. This is because every reachable configuration has already been considered, and the target configuration was not among them.

<details>
<summary>Code (TLE)</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(0); cin.tie(0)
using LL = long long;

int gridToMask(const vector<string>& grid)
{
    int mask = 0;
    mask |= (grid[0][0] - '0') << 3;
    mask |= (grid[0][1] - '0') << 2;
    mask |= (grid[1][0] - '0') << 1;
    mask |= (grid[1][1] - '0');
    return mask;
}

vector<string> maskToGrid(int mask)
{
    vector<string> grid(2, string(2, '0'));

    grid[0][0] = ((mask >> 3) & 1) + '0';
    grid[0][1] = ((mask >> 2) & 1) + '0';
    grid[1][0] = ((mask >> 1) & 1) + '0';
    grid[1][1] = ((mask >> 0) & 1) + '0';

    return grid;
}

bool found(int mask, int remainingMoves)
{
    if(mask == 0) return 1;
    if(remainingMoves == 0) return 0;

    auto grid = maskToGrid(mask);

    vector<string> grid1, grid2, grid3, grid4;

    // Press the switch of room A
    grid1 = grid;
    grid1[0][1] ^= 1;
    grid1[1][0] ^= 1;
    if(found(gridToMask(grid1), remainingMoves - 1)) return 1;

    // Press the switch of room B
    grid2 = grid;
    grid2[0][0] ^= 1;
    grid2[1][1] ^= 1;
    if(found(gridToMask(grid2), remainingMoves - 1)) return 1;

    // Press the switch of room C
    grid3 = grid;
    grid3[0][1] ^= 1;
    grid3[1][0] ^= 1;
    if(found(gridToMask(grid3), remainingMoves - 1)) return 1;

    // Press the switch of room D
    grid4 = grid;
    grid4[0][0] ^= 1;
    grid4[1][1] ^= 1;
    if(found(gridToMask(grid4), remainingMoves - 1)) return 1;

    return 0;
}



void pre()
{
    fastio;


}

void solve(int tc)
{
    vector<string> grid(2);
    cin >> grid[0] >> grid[1];

    int mask = gridToMask(grid);

    if(found(mask, 15)) cout << "YES";
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

---

However, there is a problem! From each configuration of the building, you can press $4$ different switches. Even if you limit yourself to at most $15$ switch presses, the total number of possible sequences is around $4^{15}$, which is greater than one billion. It is not feasible to try all of them within time limit for $1$ test case, let alone $30$.

To resolve this issue, you can use a clever technique called **"Meet in the Middle"**. The observation is simple. If there exists a sequence of switch presses that transforms the initial configuration into the target configuration in at most $15$ moves, then there must be some intermediate configuration that can be reached from the start in at most $8$ moves and also reached from the target in at most $7$ moves. In other words, the two sets of reachable configurations must have at least one configuration in common.

Now, generate all configurations that can be reached using at most $8$ switch presses from the initial configuration. Separately, starting from the target configuration, generate all configurations that can be reached using at most $7$ switch presses.

After generating both sets, you simply check whether their intersection is non-empty. If you find at least one common configuration, then it is possible to turn all the lights OFF, and the answer is `YES`. If there is no common configuration, then no sequence of switch presses can achieve the target configuration, and the answer is `NO`.

<details>
<summary>Code</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(0); cin.tie(0)
using LL = long long;

int gridToMask(const vector<string>& grid)
{
    int mask = 0;

    mask |= (grid[0][0] - '0') << 3;
    mask |= (grid[0][1] - '0') << 2;
    mask |= (grid[1][0] - '0') << 1;
    mask |= (grid[1][1] - '0');

    return mask;
}

vector<string> maskToGrid(int mask)
{
    vector<string> grid(2, string(2, '0'));

    grid[0][0] = ((mask >> 3) & 1) + '0';
    grid[0][1] = ((mask >> 2) & 1) + '0';
    grid[1][0] = ((mask >> 1) & 1) + '0';
    grid[1][1] = ((mask >> 0) & 1) + '0';

    return grid;
}

void explore(int mask, int remainingMoves, set<int>& st)
{
    st.insert(mask);
    if(remainingMoves == 0) return;

    auto grid = maskToGrid(mask);

    vector<string> grid1, grid2, grid3, grid4;

    // Press the switch of room A
    grid1 = grid;
    grid1[0][1] ^= 1;
    grid1[1][0] ^= 1;

    // Press the switch of room B
    grid2 = grid;
    grid2[0][0] ^= 1;
    grid2[1][1] ^= 1;

    // Press the switch of room C
    grid3 = grid;
    grid3[0][1] ^= 1;
    grid3[1][0] ^= 1;

    // Press the switch of room D
    grid4 = grid;
    grid4[0][0] ^= 1;
    grid4[1][1] ^= 1;

    explore(gridToMask(grid1), remainingMoves - 1, st);
    explore(gridToMask(grid2), remainingMoves - 1, st);
    explore(gridToMask(grid3), remainingMoves - 1, st);
    explore(gridToMask(grid4), remainingMoves - 1, st);
}



void pre()
{
    fastio;


}

void solve(int tc)
{
    vector<string> grid(2);
    cin >> grid[0] >> grid[1];

    int startMask = gridToMask(grid), targetMask = 0;

    set<int> forwardMasks, backwardMasks;
    explore(startMask, 8, forwardMasks);
    explore(targetMask, 7, backwardMasks);

    for(auto fm: forwardMasks)
    {
        if(backwardMasks.count(fm) == 1)
        {
            cout << "YES";
            return;
        }
    }

    cout << "NO";
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

You begin with the same basic observation as before: the building has only $4$ rooms, and each room can be either ON or OFF. Therefore, there are only $16$ possible configurations of the building.

Next, you think about what happens when you press switches. From any given configuration, you can press any one of the four switches, which takes you to another configuration. This means you can think of each switch press as a transition from one configuration to another.

At this point, notice an important fact. If you ever reach a configuration that you have already seen before, there is no point in exploring further from that configuration. Any sequence of switch presses starting from it will behave exactly the same way as it did the first time you reached it. Visiting the same configuration again cannot give you anything new.

This observation changes the solution approach. Instead of thinking in terms of sequences of switch presses, you now think in terms of configurations and transitions between them. Since there are only $16$ configurations in total, and from each configuration there are only $4$ possible switch presses, there are at most $16 \times 4 = 64$ meaningful transitions to consider.

Now the solution is simple. Starting from the initial configuration, you apply all possible switch presses, but you keep track of which configurations you have already visited. Whenever you reach a configuration that has been visited before, you skip exploring from there. In this way, you systematically explore all configurations that are reachable from the starting configuration, without doing unnecessary work.

Once this exploration is complete, you simply check whether the configuration in which all lights are OFF has been visited. If it has, then it is possible to turn all the lights OFF, and the answer is `YES`. If it has not, then no sequence of switch presses can reach that configuration, and the answer is `NO`.

<details>
<summary>Code</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(0); cin.tie(0)
using LL = long long;

int gridToMask(const vector<string>& grid)
{
    int mask = 0;
    mask |= (grid[0][0] - '0') << 3;
    mask |= (grid[0][1] - '0') << 2;
    mask |= (grid[1][0] - '0') << 1;
    mask |= (grid[1][1] - '0');
    return mask;
}

vector<string> maskToGrid(int mask)
{
    vector<string> grid(2, string(2, '0'));

    grid[0][0] = ((mask >> 3) & 1) + '0';
    grid[0][1] = ((mask >> 2) & 1) + '0';
    grid[1][0] = ((mask >> 1) & 1) + '0';
    grid[1][1] = ((mask >> 0) & 1) + '0';

    return grid;
}

void dfs(int mask, vector<int>& visited)
{
    if(visited[mask]) return;
    visited[mask] = 1;

    auto grid = maskToGrid(mask);

    vector<string> grid1, grid2, grid3, grid4;

    // Press the switch of room A
    grid1 = grid;
    grid1[0][1] ^= 1;
    grid1[1][0] ^= 1;

    // Press the switch of room B
    grid2 = grid;
    grid2[0][0] ^= 1;
    grid2[1][1] ^= 1;

    // Press the switch of room C
    grid3 = grid;
    grid3[0][1] ^= 1;
    grid3[1][0] ^= 1;

    // Press the switch of room D
    grid4 = grid;
    grid4[0][0] ^= 1;
    grid4[1][1] ^= 1;

    dfs(gridToMask(grid1), visited);
    dfs(gridToMask(grid2), visited);
    dfs(gridToMask(grid3), visited);
    dfs(gridToMask(grid4), visited);
}



void pre()
{
    fastio;


}

void solve(int tc)
{
    vector<string> grid(2);
    cin >> grid[0] >> grid[1];

    int mask = gridToMask(grid);

    vector<int> visited(16, 0);
    dfs(mask, visited);

    if(visited[0]) cout << "YES";
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
