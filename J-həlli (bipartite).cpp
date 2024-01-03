#include <bits/stdc++.h>
using namespace std;
int n, m, g[101][101], u, v, color[101];
void dfs(int s){
    for(int i = 1; i <= n; i++){
        if(g[s][i] && color[i] == 0){
            color[i] = -color[s];
            dfs(i);
        }
    }
}
int main()
{
    cin>>n>>m;
    while(m--){
        cin>>u>>v;
        g[u][v] = g[v][u] = 1;
    }
    for(int i = 1; i <= n; i++){
        if(color[i] == 0){
            color[i] = 1;
            dfs(i);
        }
    }
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            if(g[i][j] && color[i] == color[j]){
                cout<<"NO";
                return 0;
            }
        }
    }
    cout<<"YES";
}