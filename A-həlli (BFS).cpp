#include <bits/stdc++.h>
using namespace std;
int g[101][101];
int color[101], dis[101];
int n;

void bfs(int s){
    queue<int>q;
    color[s] = 1;
    dis[s] = 0;
    q.push(s);
    while(!q.empty()){
        int u = q.front();

for(int i = 1; i <= n; i++){
            if(g[u][i] == 1 && !color[i]){
                color[i] = 1;
                dis[i] = dis[u] + 1;
                q.push(i);
            }
        }
        q.pop();
        color[u] = 2;
    }
}
int main()
{
    int u, v;
    cin>>n>>u>>v;
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            cin>>g[i][j];
        }
    }
    bfs(u);
    cout<<dis[v]<<endl;
}