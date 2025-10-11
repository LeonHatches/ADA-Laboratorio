#include <iostream>
#include "graph.h"
#include <limits>
#include <queue>
#include <map>

using namespace std;

template <typename T>
GraphLink<T> prim (GraphLink<T>& G, T start) {
    
    GraphLink<T> tree;
    map<T, int>  distance;
    map<T, T>    father;
    map<T, bool> inQueue;

    const int INFINITO = numeric_limits<int>::max();

    for (auto v : G.getListVertex()) {
        tree.insertVertex(v->getData());
        
        distance [v->getData()] = INFINITO;
        father   [v->getData()] = T();
        inQueue  [v->getData()] = true;
    }

    priority_queue<pair<int, T>, vector<pair<int, T>>, greater<pair<int, T>>> queue;

    distance[start] = 0;
    queue.push( {0, start} );

    while (!queue.empty()) {
        T u = queue.top().second;
        queue.pop();

        if (!inQueue[u]) continue;
        inQueue[u] = false;

        Vertex<T>* vertU = G.searchVertex(u);
        if (!vertU) continue;

        for (const auto& e : vertU->getAdj()) {
            T v = e.getDest()->getData();
            int peso = e.getWeight();

            if (inQueue[v] && peso < distance[v]) {
                distance[v] = peso;
                father[v]   = u;
                queue.push({distance[v], v});
            }
        }
    }

    for (auto& p : father)
        if (p.second != T())
            tree.insertEdge(p.second, p.first, distance[p.first]);

    return tree;
}

int main() {
}