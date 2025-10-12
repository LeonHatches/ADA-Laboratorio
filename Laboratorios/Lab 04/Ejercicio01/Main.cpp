#include <iostream>
#include "../graph.h"
#include <vector>
#include <algorithm>
#include <limits>
#include <queue>
#include <map>
#include <ctime>

using namespace std;

// -------------- ALGORITMO KRUSKAL --------------

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


// -------------- ALGORITMO PRIM --------------

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

// -------------- MAIN --------------

int main () {
    const int VERTICES = 6;
    const int ARISTAS  = 10;
    const int PESO_MAX = 20;

    srand(time(0));

    GraphLink<int> grafo;

    for (int i = 1 ; i <= VERTICES ; i++) {
        grafo.insertVertex(i);
    }

    for (int i = 0 ; i < ARISTAS ; i++) {
        int from, to, weight;
        
        do {
            from = 1 + rand() % VERTICES;
            to   = 1 + rand() % VERTICES;
            
        } while (from == to || grafo.getEdgeWeight(from, to) != -1);

        weight = 1 + rand() % PESO_MAX;

        grafo.insertEdge(from, to, weight);
        grafo.insertEdge(to, from, weight);
    }

    cout << "Grafo original:\n";
    grafo.printGraph();

    cout << "\nÁrbol de expansión mínima (Kruskal):\n";
    auto arbolK = kruskal(grafo);
    arbolK.printGraph();

    cout << "\nÁrbol de expansión mínima (Prim):\n";
    auto arbolP = prim(grafo, 2);
    arbolP.printGraph();

    return 0;
}