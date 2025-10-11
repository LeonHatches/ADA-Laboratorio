#include <iostream>
#include "graph.h"
#include <vector>

using namespace std;

template <typename T>
GraphLink<T> kruskal (GraphLink<T>& G) {
    
    vector<Vertex<T>*> set;
    for (auto v : G.listVertex) {
        set.push_back(v);
    }

    vector<Edge<T>*> Q;
    for (auto v : set) {
        for (auto& e : v->getAdj()) {
            Q.push_back(new Edge (v, e.getWeight(), e.getDest()));
        }
    }

    GraphLink<T> tree;

    return G;
}

int main () {

}