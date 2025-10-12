#include <iostream>
#include "../graph.h"
#include <vector>
#include <algorithm>
#include <limits>
#include <queue>
#include <map>

using namespace std;

// -------------- ALGORITMO KRUSKAL --------------

template <typename T>
GraphLink<T> kruskal (GraphLink<T>& G) {
    
    vector<Vertex<T>*> vertices;
    for (auto v : G.getListVertex()) {
        vertices.push_back(v);
    }

    vector<tuple<Vertex<T>*, Vertex<T>*, int>> Q;
    for (auto v : vertices) {
        for (const auto& e : v->getAdj()) {
            Q.push_back({v, e.getDest(), e.getWeight()});
        }
    }

    sort(Q.begin(), Q.end(),
        [](const auto& a, const auto& b) {
        return get<2>(a) < get<2>(b);
    });

    int n = vertices.size();
    vector<int> comp (n);
    for (size_t i = 0; i < n; ++i) {
        comp[i] = i;
    }
    
    auto findIndex = [&](Vertex<T>* v) {
        for (int i = 0; i < n ; ++i)
            if (vertices[i] == v)
                return i;
        
        return -1;
    };

    GraphLink<T> tree;
    for (auto v : G.getListVertex()) {
        tree.insertVertex(v->getData());
    }

    for (const auto& [u, v, w] : Q) {
        int iU = findIndex(u);
        int iV = findIndex(v);

        if(comp[iU] != comp[iV]) {
            tree.insertEdge(u->getData(), v->getData(), w);

            int oldComp = comp[iV];
            int newComp = comp[iU];

            for(auto& c : comp)
                if(c == oldComp)
                    c = newComp;
        }
    }
    
    return tree;
}


// -------------- ALGORITMO PRIM --------------

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

// -------------- MAIN --------------

int main () {

}