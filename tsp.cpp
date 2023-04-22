#include <bits/stdc++.h>
#include <iostream>
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int MAXN = 23;
const int INF = INT_MAX;

int n;
vvi dist;
int memo[MAXN][1 << MAXN];
int parent[MAXN][1 << MAXN];

void read_matrix() {
    vvi ret;
    ifstream file;
    file.open("matrix1.txt", ios::in);
    for (int i = 0; i < n; i++) {
        vi row;
        for (int j = 0; j < n; j++) {
            int x; file >> x;
            row.push_back(x);
        }
        ret.push_back(row);
    }
    dist = ret;
}

int tsp(int pos, int mask) {
    if (mask == (1 << n) - 1) {
        return dist[pos][0];
    }
    if (memo[pos][mask] != -1) {
        return memo[pos][mask];
    }
    int ans = INF;
    for (int next = 0; next < n; next++) {
        if ((mask & (1 << next)) == 0) {
            int newMask = mask | (1 << next);
            int newDist = dist[pos][next] + tsp(next, newMask);
            if (newDist < ans) {
                ans = newDist;
                parent[pos][mask] = next;
            }
        }
    }
    return memo[pos][mask] = ans;
}

void printPath(int pos, int mask) {
    if (pos == 0) {}
    ofstream file;
    file.open("route1.txt", ios::out | ios::app);
    if (pos == 0) {
        file << "0" << endl;
    }
    if (mask == (1 << n) - 1) {
        file << "0" << endl;
        return;
    }
    int next = parent[pos][mask];
    file << next << endl;
    printPath(next, mask | (1 << next));
}

int main() {
    n = 23;
    read_matrix();
    memset(memo, -1, sizeof(memo));
    memset(parent, -1, sizeof(parent));
    int ans = tsp(0, 1);
    cout << "The cost of most efficient tour = " << ans << "\n";
    printPath(0, 1);
    return 0;
}