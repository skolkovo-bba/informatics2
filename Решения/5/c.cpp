#include<bits/stdc++.h>

using namespace std;
typedef long long ll;
#define fast_cin() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
ll timer = 0;
vector<vector<ll>> gr;
vector<ll> tin,fup;
set<ll> points_of_connectebility;
vector<bool> used;

void dfs(ll v,ll p = -1){
    used[v] = true;
    tin[v] = fup[v] = timer++;
    ll children = 0;
    for(auto u : gr[v]){
        if(u == p){
            continue;
        }
        if(used[u]){
            fup[v] = min(fup[v],tin[u]);
        }
        else{
            dfs(u,v);
            fup[v] = min(fup[v],fup[u]);
            if(fup[u] >= tin[v] && p != -1){
                points_of_connectebility.insert(v+1);
            }
            children++;
        }
    }
    if(p == -1 && children > 1){
        points_of_connectebility.insert(v+1);
    }
}

int main() {
    fast_cin();
    ll n, m;
    cin >> n >> m;
    gr.resize(n);
    tin.resize(n);
    fup.resize(n);
    used.resize(n);
    ll v, u;
    for (ll i = 0; i < m; i++) {
        cin >> v >> u;
        v--;
        u--;
        gr[v].push_back(u);
        gr[u].push_back(v);
    }

    for (ll i = 0; i < n; i++)
        if (!used[i])
            dfs(i);

    cout << points_of_connectebility.size() << endl;
    for(auto i : points_of_connectebility){
        cout << i << "\n";
    }
}