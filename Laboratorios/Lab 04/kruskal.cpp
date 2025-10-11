#include <iostream>
#include "graph.h"
#include <vector>
#include <algorithm>

using namespace std;

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

int main () {
    GraphLink<int> g;
    g.insertVertex(1);
    g.insertVertex(2);
    g.insertVertex(3);
    g.insertVertex(4);

    g.insertEdge(1, 2, 3);
    g.insertEdge(1, 3, 1);
    g.insertEdge(2, 3, 7);
    g.insertEdge(2, 4, 5);
    g.insertEdge(3, 4, 2);

    cout << "Grafo original:\n";
    g.printGraph();

    auto mst = kruskal(g);
    cout << "\nÁrbol de expansión mínima (Kruskal):\n";
    mst.printGraph();
}