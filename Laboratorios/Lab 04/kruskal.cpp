#include <iostream>
#include "graph.h"
#include <vector>

using namespace std;

template <typename T>
GraphLink<T> kruskal (GraphLink<T>& G) {
    
    vector<Vertex<T>*> set;
    for (auto v : G.getListVertex()) {
        set.push_back(v);
    }

    vector<tuple<Vertex<T>*, Vertex<T>*, int>> Q;
    for (auto v : set) {
        for (const auto& e : v->getAdj()) {
            Q.push_back({v, e.getDest(), e.getWeight()});
        }
    }

    sort(Q.begin(), Q.end(),
        [](const auto& a, const auto& b) {
        return get<2>(a) < get<2>(b);
    });

    int n = set.size();
    GraphLink<T> tree;

    return G;
}

int main () {

}