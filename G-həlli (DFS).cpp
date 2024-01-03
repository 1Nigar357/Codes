#include <bits/stdc++.h>
using namespace std;
int n, m, t;
set<int>g[101];
vector<int>order;
int color[101], gray[101], black[101];
void dfs(int src){
    order.push_back(src);
    color[src] = 1;
    gray[src] = ++t;
    for(auto i = g[src].begin(); i != g[src].end(); i++){
        int x = *i;
        if(color[x] == 0){
            dfs(x);
        }

    }
    color[src] = 2;
    black[src] = ++t;
}
int main()
{
    cin>>n;
    int u, v;
    while(cin>>u>>v){
        g[u].insert(v);
        g[v].insert(u);
    }
    for(int i = 1; i <= n; i++){
        if(color[i] == 0){
            dfs(i);
        }
    }
    for(auto x = order.begin(); x != order.end(); x++){
        cout<<"Vertex: "<<*x<<", Gray "<<gray[*x]<<", Black "<<black[*x]<<endl;
    }
}