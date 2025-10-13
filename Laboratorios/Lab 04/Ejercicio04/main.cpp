#include <iostream>
#include "../graph.h"
#include "graph.h"
#include <vector>
#include <algorithm>
#include <limits>
#include <queue>
#include <map>
#include <ctime>

using namespace std;

template <typename T>
GraphLink<T> kruskal (GraphLink<T>& G) {
    int kruskalSteps = 0;
    
    vector<Vertex<T>*> vertices;
    for (auto v : G.getListVertex()) {
        vertices.push_back(v);
    }

    vector<tuple<Vertex<T>*, Vertex<T>*, int>> Q;
    for (auto v : vertices) {
        for (const auto& e : v->getAdj()) {
            if (v->getData() < e.getDest()->getData())
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
    
    map<Vertex<T>*, int> vertexIndex;
    for (int i = 0; i < n; ++i) {
        vertexIndex[vertices[i]] = i;
    }

    GraphLink<T> tree;
    for (auto v : G.getListVertex()) {
        tree.insertVertex(v->getData());
    }

    for (const auto& [u, v, w] : Q) {
        kruskalSteps++;
        
        int iU = vertexIndex[u];
        int iV = vertexIndex[v];

        if(comp[iU] != comp[iV]) {
            tree.insertEdge(u->getData(), v->getData(), w);
            tree.insertEdge(v->getData(), u->getData(), w);
        
            int oldComp = comp[iV];
            int newComp = comp[iU];

            for(auto& c : comp)
                if(c == oldComp)
                    c = newComp;
        }
    }
    
    cout << "Kruskal procesó " << kruskalSteps << " aristas.\n";
    return tree;
}


template <typename T>
GraphLink<T> prim (GraphLink<T>& G, T start) {
    
    int primSteps = 0;
    GraphLink<T> tree;
    map<T, int>  distance;
    map<T, T>    father;
    map<T, bool> visited;


    const int INFINITO = numeric_limits<int>::max();

    for (auto v : G.getListVertex()) {
        tree.insertVertex(v->getData());
        
        distance [v->getData()] = INFINITO;
        father   [v->getData()] = T();
        visited  [v->getData()] = false;
    }

    distance[start] = 0;
    priority_queue<pair<int, T>, vector<pair<int, T>>, greater<pair<int, T>>> queue;
    queue.push( {0, start} );

    while (!queue.empty()) {

        int dist = queue.top().first;
        T u = queue.top().second;
        queue.pop();

        if (visited[u]) continue;
        visited[u] = true;

        if (u != start) {
            tree.insertEdge(father[u], u, distance[u]);
            tree.insertEdge(u, father[u], distance[u]);
        }

        Vertex<T>* vertU = G.searchVertex(u);
        if (!vertU) continue;

        for (const auto& e : vertU->getAdj()) {
            primSteps++;
            T v = e.getDest()->getData();
            int peso = e.getWeight();

            if (!visited[v] && peso < distance[v]) {
                distance[v] = peso;
                father[v]   = u;
                queue.push({distance[v], v});
            }
        }
    }

    cout << "Prim procesó " << primSteps << " aristas.\n";
    return tree;
}

int main() {
    GraphLink<int> graphLink;
    MatrixGraph<int> matrixGraph;

    for (int i = 0; i < 15; i++) {
        graphLink.insertVertex(i);
        matrixGraph.addVertex(i);
    }

    std::vector<std::tuple<int,int,int>> edges = {
        {0,1,4}, {0,7,8}, {1,2,8}, {1,7,11}, {2,3,7},
        {2,8,2}, {3,4,9}, {3,5,14}, {4,5,10}, {5,6,2},
        {6,7,1}, {6,8,6}, {7,8,7}, {8,9,3}, {9,10,5},
        {10,11,8}, {11,12,6}, {12,13,4}, {13,14,7}, {0,14,12}
    };

    for (auto [u,v,w] : edges) {
        graphLink.insertEdge(u,v,w);
        graphLink.insertEdge(v,u,w);
        matrixGraph.addEdge(u,v,w);
    }

    std::cout << "Grafo con Listas de Adyacencia\n";
    graphLink.printGraph();

    std::cout << "\n";

    std::cout << "Grafo con Matriz de Adyacencia\n";
    matrixGraph.printGraph();

    std::cout << "\nKRUSKAL\n";
    kruskal(graphLink).printGraph();

    std::cout << "\n";

    matrixGraph.kruskal();


    std::cout << "\nPRIM\n";
    prim(graphLink, 0).printGraph();

    std::cout << "\n";

    matrixGraph.printGraph();
}
