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
    
    GraphLink<int> G;

    G.insertVertex(1);
    G.insertVertex(2);
    G.insertVertex(3);
    G.insertVertex(4);

    G.insertEdge(1, 2, 3);
    G.insertEdge(1, 3, 1);
    G.insertEdge(2, 3, 7);
    G.insertEdge(2, 4, 5);
    G.insertEdge(3, 4, 2);

    cout << "Grafo original:\n";
    G.printGraph();

    GraphLink<int> tree = prim(G, 1);

    cout << "\nArbol de expansion minima (Prim):\n";
    tree.printGraph();
}