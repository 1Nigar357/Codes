#include <bits/stdc++.h>
#define MAX 200000
using namespace std;
vector<int>edges[1001];
int dis_from_s[1001], dis_from_t[1001], visited[1001];
int g[1001][1001];
void bfs(int src, int dis[]){
    queue<int>q;
    q.push(src);
    visited[src] = 1;
    while(!q.empty()){
        int u = q.front();
        for(int i = 0; i < edges[u].size(); i++){
            int v = edges[u][i];
            if(visited[v] == 0){
                dis[v] = dis[u] + 1;
                visited[v] = 1;
                q.push(v);
            }
        }
        q.pop();
    }
}
int main(){
    int n, m, u, v, s, t, ans = 0;
    cin>>n>>m;
    cin>>s>>t;
    for(int i = 1; i <= m; i++){
        cin>>u>>v;
        edges[u].push_back(v);
        edges[v].push_back(u);
        g[u][v] = g[v][u] = 1;
    }
    bfs(s, dis_from_s);
    memset(visited, 0, sizeof(visited));
    bfs(t, dis_from_t);
    int s_to_t = dis_from_s[t];
    for(int i = 1; i < n; i++){
        for(int j = i + 1; j <= n; j++){
            if(g[i][j] == 0 && (dis_from_s[i] + dis_from_t[j] + 1 >= s_to_t &&
               dis_from_s[j] + dis_from_t[i] + 1 >= s_to_t)){
            	ans++;
        	}
        }
    }
    cout<<ans<<endl;
}
