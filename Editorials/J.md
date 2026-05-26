# The Grand Fleet’s Logbook

Problem Setter: [Saom Bin Khaled](https://codeforces.com/profile/greenbinjack)

Estimated Difficulty: 1400

Tag(s): Implementation

<details>
<summary>Solution</summary>

👉 [Open Solution PDF](pdf/Grand%20Fleets%20Logbook.pdf)

</details>

<details>
<summary>Code</summary>

<details>
<summary>C Solution</summary>

```c
#include <stdio.h>
#include <string.h>

bool isLeapYear(int y) {
    if (y % 400 == 0) return true;
    if (y % 100 == 0) return false;
    return y % 4 == 0;
}

int daysInMonth(int m, int y) {
    if (m == 2) {
        if (isLeapYear(y)) return 29;
        else return 28;
    }
    if (m == 4 || m == 6 || m == 9 || m == 11) return 30;
    return 31;
}

// Converts DD/MM/YYYY to total days elapsed since 01/01/2000
int getAbsoluteDay(int d, int m, int y) {
    int days = 0;
    for (int i = 2000; i < y; i++) {
        if (isLeapYear(i)) days += 366;
        else days += 365;
    }
    for (int i = 1; i < m; i++) {
        days += daysInMonth(i, y);
    }
    days += (d - 1);
    return days;
}

// Converts absolute days back to DD/MM/YYYY and prints it
void printDate(int total_days) {
    int y = 2000;
    while (1) {
        int days_in_year = isLeapYear(y) ? 366 : 365;
        if (total_days >= days_in_year) {
            total_days -= days_in_year;
            y++;
        } else {
            break;
        }
    }

    int m = 1;
    while (1) {
        int dim = daysInMonth(m, y);
        if (total_days >= dim) {
            total_days -= dim;
            m++;
        } else {
            break;
        }
    }

    int d = total_days + 1;
    // printf handles leading zeros natively
    printf("%02d/%02d/%04d\n", d, m, y);
}

int main() {
    int K;
    if (scanf("%d", &K) != 1) return 0;

    char crew_names[55][25];
    int crew_start_days[55];
    char crew_patterns[55][105];
    int crew_pat_lens[55];

    for (int i = 0; i < K; i++) {
        int d, m, y;
        scanf("%s %d/%d/%d %s", crew_names[i], &d, &m, &y, crew_patterns[i]);

        crew_start_days[i] = getAbsoluteDay(d, m, y);

        // Find length of string
        int len = 0;
        while (crew_patterns[i][len] != '\0') {
            len++;
        }
        crew_pat_lens[i] = len;
    }

    int Q;
    scanf("%d", &Q);

    while (Q > 0) {
        Q--;
        int type;
        scanf("%d", &type);

        if (type == 1) {
            int d, m, y;
            char target_act;
            scanf("%d/%d/%d %c", &d, &m, &y, &target_act);

            int target_day = getAbsoluteDay(d, m, y);

            char active_crews[55][25];
            int active_count = 0;

            for (int i = 0; i < K; i++) {
                if (target_day >= crew_start_days[i]) {
                    int delta = target_day - crew_start_days[i];

                    // MODULO REPLACEMENT: Loop subtraction to wrap around the pattern
                    while (delta >= crew_pat_lens[i]) {
                        delta -= crew_pat_lens[i];
                    }
                    int idx = delta;

                    if (crew_patterns[i][idx] == target_act) {
                        strcpy(active_crews[active_count], crew_names[i]);
                        active_count++;
                    }
                }
            }

            if (active_count == 0) {
                printf("NONE\n");
            } else {
                // BUBBLE SORT ALGORITHM
                for (int i = 0; i < active_count - 1; i++) {
                    for (int j = 0; j < active_count - i - 1; j++) {
                        if (strcmp(active_crews[j], active_crews[j+1]) > 0) {
                            // Swap strings using a temporary buffer
                            char temp[25];
                            strcpy(temp, active_crews[j]);
                            strcpy(active_crews[j], active_crews[j+1]);
                            strcpy(active_crews[j+1], temp);
                        }
                    }
                }

                // Print sorted names
                for (int i = 0; i < active_count; i++) {
                    printf("%s", active_crews[i]);
                    if (i < active_count - 1) {
                        printf(" ");
                    }
                }
                printf("\n");
            }

        }
        else if (type == 2) {
            char target_name[25];
            int m, y;
            scanf("%s %d %d", target_name, &m, &y);

            int c_idx = -1;
            for (int i = 0; i < K; i++) {
                if (strcmp(crew_names[i], target_name) == 0) {
                    c_idx = i;
                    break;
                }
            }

            int start_day = getAbsoluteDay(1, m, y);
            int dim = daysInMonth(m, y);
            int s_count = 0, f_count = 0, p_count = 0;

            for (int i = 0; i < dim; i++) {
                int current_day = start_day + i;
                if (current_day >= crew_start_days[c_idx]) {
                    int delta = current_day - crew_start_days[c_idx];

                    // MODULO REPLACEMENT
                    while (delta >= crew_pat_lens[c_idx]) {
                        delta -= crew_pat_lens[c_idx];
                    }
                    int idx = delta;

                    char act = crew_patterns[c_idx][idx];
                    if (act == 'S') s_count++;
                    else if (act == 'F') f_count++;
                    else if (act == 'P') p_count++;
                }
            }

            printf("%d %d %d\n", s_count, f_count, p_count);

        }
        else if (type == 3) {
            char name1[25], name2[25];
            int d, m, y;
            scanf("%s %s %d/%d/%d", name1, name2, &d, &m, &y);

            int c1 = -1, c2 = -1;
            for (int i = 0; i < K; i++) {
                if (strcmp(crew_names[i], name1) == 0) c1 = i;
                if (strcmp(crew_names[i], name2) == 0) c2 = i;
            }

            int start_day = getAbsoluteDay(d, m, y);
            int found = 0;

            for (int i = 0; i < 69; i++) {
                int current_day = start_day + i;

                if (current_day >= crew_start_days[c1] && current_day >= crew_start_days[c2]) {
                    int delta1 = current_day - crew_start_days[c1];
                    int delta2 = current_day - crew_start_days[c2];

                    // MODULO REPLACEMENT FOR C1
                    while (delta1 >= crew_pat_lens[c1]) {
                        delta1 -= crew_pat_lens[c1];
                    }
                    int idx1 = delta1;

                    // MODULO REPLACEMENT FOR C2
                    while (delta2 >= crew_pat_lens[c2]) {
                        delta2 -= crew_pat_lens[c2];
                    }
                    int idx2 = delta2;

                    char act1 = crew_patterns[c1][idx1];
                    char act2 = crew_patterns[c2][idx2];

                    if (act1 == 'F' && act2 == 'F') {
                        printDate(current_day);
                        found = 1;
                        break;
                    }
                }
            }

            if (found == 0) {
                printf("PEACE\n");
            }
        }
    }

    return 0;
}
```

</details>

<details>
<summary>C++ Solution</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

bool isLeapYear(int y) {
    if (y % 400 == 0) return true;
    if (y % 100 == 0) return false;
    return y % 4 == 0;
}

int daysInMonth(int m, int y) {
    if (m == 2) {
        if (isLeapYear(y)) return 29;
        else return 28;
    }
    if (m == 4 || m == 6 || m == 9 || m == 11) return 30;
    return 31;
}

// Converts DD/MM/YYYY to total days elapsed since 01/01/2000
int getAbsoluteDay(int d, int m, int y) {
    int days = 0;
    for (int i = 2000; i < y; i++) {
        if (isLeapYear(i)) days += 366;
        else days += 365;
    }
    for (int i = 1; i < m; i++) {
        days += daysInMonth(i, y);
    }
    days += (d - 1);
    return days;
}

// Converts absolute days back to DD/MM/YYYY and prints it
void printDate(int total_days) {
    int y = 2000;
    while (true) {
        int days_in_year = isLeapYear(y) ? 366 : 365;
        if (total_days >= days_in_year) {
            total_days -= days_in_year;
            y++;
        } else {
            break;
        }
    }

    int m = 1;
    while (true) {
        int dim = daysInMonth(m, y);
        if (total_days >= dim) {
            total_days -= dim;
            m++;
        } else {
            break;
        }
    }

    int d = total_days + 1;
    cout << setfill('0') << setw(2) << d << "/"
         << setfill('0') << setw(2) << m << "/"
         << setw(4) << y << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int K;
    cin >> K;

    string crew_names[55];
    int crew_start_days[55];
    string crew_patterns[55];

    for (int i = 0; i < K; i++) {
        string date_str;
        cin >> crew_names[i] >> date_str >> crew_patterns[i];

        int d = stoi(date_str.substr(0, 2));
        int m = stoi(date_str.substr(3, 2));
        int y = stoi(date_str.substr(6, 4));

        crew_start_days[i] = getAbsoluteDay(d, m, y);
    }

    int Q;
    cin >> Q;
    while (Q--) {
        int type;
        cin >> type;

        if (type == 1) {
            // QUERY 1: Find all crews doing specific activity on a date
            string date_str;
            char target_act;
            cin >> date_str >> target_act;

            int d = stoi(date_str.substr(0, 2));
            int m = stoi(date_str.substr(3, 2));
            int y = stoi(date_str.substr(6, 4));
            int target_day = getAbsoluteDay(d, m, y);

            vector<string> active_crews;

            for (int i = 0; i < K; i++) {
                if (target_day >= crew_start_days[i]) { // Crew is active
                    int delta = target_day - crew_start_days[i];
                    char current_act = crew_patterns[i][delta % crew_patterns[i].length()];
                    if (current_act == target_act) {
                        active_crews.push_back(crew_names[i]);
                    }
                }
            }

            if (active_crews.empty()) {
                cout << "NONE\n";
            } else {
                sort(active_crews.begin(), active_crews.end());
                for (size_t i = 0; i < active_crews.size(); i++) {
                    cout << active_crews[i] << (i + 1 == active_crews.size() ? "" : " ");
                }
                cout << "\n";
            }

        }
        else if (type == 2) {
            // QUERY 2: Count S, F, P days for a specific crew in a given month
            string name;
            int m, y;
            cin >> name >> m >> y;

            int crew_index = -1;
            for (int i = 0; i < K; i++) {
                if (crew_names[i] == name) {
                    crew_index = i;
                    break;
                }
            }

            int start_day = getAbsoluteDay(1, m, y);
            int dim = daysInMonth(m, y);
            int s_count = 0, f_count = 0, p_count = 0;

            for (int i = 0; i < dim; i++) {
                int current_day = start_day + i;
                if (current_day >= crew_start_days[crew_index]) { // Check if active
                    int delta = current_day - crew_start_days[crew_index];
                    char act = crew_patterns[crew_index][delta % crew_patterns[crew_index].length()];

                    if (act == 'S') s_count++;
                    else if (act == 'F') f_count++;
                    else if (act == 'P') p_count++;
                }
            }

            cout << s_count << " " << f_count << " " << p_count << "\n";

        }
        else if (type == 3) {
            // QUERY 3: Find first common 'F' day within a 69-day window
            string name1, name2, date_str;
            cin >> name1 >> name2 >> date_str;

            int d = stoi(date_str.substr(0, 2));
            int m = stoi(date_str.substr(3, 2));
            int y = stoi(date_str.substr(6, 4));

            int c1 = -1, c2 = -1;
            for (int i = 0; i < K; i++) {
                if (crew_names[i] == name1) c1 = i;
                if (crew_names[i] == name2) c2 = i;
            }

            int start_day = getAbsoluteDay(d, m, y);
            bool found = false;

            // Brute force check the exactly 69 days
            for (int i = 0; i < 69; i++) {
                int current_day = start_day + i;

                // Check if both crews have started their journeys
                if (current_day >= crew_start_days[c1] && current_day >= crew_start_days[c2]) {
                    int delta1 = current_day - crew_start_days[c1];
                    int delta2 = current_day - crew_start_days[c2];

                    char act1 = crew_patterns[c1][delta1 % crew_patterns[c1].length()];
                    char act2 = crew_patterns[c2][delta2 % crew_patterns[c2].length()];

                    if (act1 == 'F' && act2 == 'F') {
                        printDate(current_day);
                        found = true;
                        break;
                    }
                }
            }

            if (!found) {
                cout << "PEACE\n";
            }
        }
    }

    return 0;
}
```

</details>

</details>
