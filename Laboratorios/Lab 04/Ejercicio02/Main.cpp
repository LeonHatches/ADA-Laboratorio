#include <iostream>
#include "../graph.h"
#include <vector>
#include <algorithm>
#include <limits>
#include <queue>
#include <map>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <cstdlib>
using namespace std;
namespace fs = filesystem;

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

    int step = 0;
    vector<tuple<T, T, int>> cycleEdges;
    
    for (const auto& [u, v, w] : Q) {
        
        int iU = vertexIndex[u];
        int iV = vertexIndex[v];

        if(comp[iU] != comp[iV]) {
            tree.insertEdge(u->getData(), v->getData(), w);

            int oldComp = comp[iV];
            int newComp = comp[iU];

            for(auto& c : comp)
                if(c == oldComp)
                    c = newComp;

            step++;
            saveDot(tree, "kruskalImages/step" + to_string(step) + ".dot",
                {u->getData(), v->getData()}, cycleEdges, w);
        
        } else {

            cycleEdges.push_back({u->getData(), v->getData(), w});
            step++;
            saveDot(tree, "kruskalImages/step" + to_string(step) + ".dot",
                {-1,-1}, cycleEdges, -1);
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
    map<T, bool> hasFather;


    const int INFINITO = numeric_limits<int>::max();

    for (auto v : G.getListVertex()) {
        tree.insertVertex(v->getData());
        
        distance [v->getData()] = INFINITO;
        father   [v->getData()] = T();
        inQueue  [v->getData()] = true;
        hasFather[v->getData()] = false;
    }

    priority_queue<pair<int, T>, vector<pair<int, T>>, greater<pair<int, T>>> queue;

    distance[start] = 0;
    queue.push( {0, start} );

    int step = 0;

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
                hasFather[v] = true;
                queue.push({distance[v], v});
            }
        }
    }

    for (auto& p : father)
        if (hasFather[p.first]) {
            tree.insertEdge(p.second, p.first, distance[p.first]);
            step++;
            saveDot(tree, "primImages/step" + to_string(step) + ".dot",
                {p.second, p.first}, {}, distance[p.first]);
        }

    return tree;
}
// -------------- GRAPHVIZ --------------


void clearFolder (const string& folder) {
    
    if (fs::exists(folder)) {
        for (auto& f : fs::directory_iterator(folder))
            fs::remove_all(f.path());
    
    } else {
        fs::create_directory(folder);
    }
}

template <typename T>
void saveDot(GraphLink<T>& g, const string& filename,
    pair<T,T> newEdge = {-1, -1}, 
    const vector<tuple<T,T,int>>& cycleEdges = {},
    int newEdgeWeight = -1) {
    
    ofstream file(filename);
    file << "graph G {\n";
    
    // VÉRTICES
    for (auto v : g.getListVertex()) {
        file << "  " << v->getData()
             << " [style = filled, fillcolor=lightblue];\n";
    }

    // ARISTAS
    for (auto v : g.getListVertex()) {
        for (auto& e : v->getAdj()) {
            T u = v->getData();
            T w = e.getDest()->getData();

            if (u < w) {
                string color = "black";
                string style = "";
                
                // Resaltar nueva arista agregada
                if ((u == newEdge.first && w == newEdge.second) ||
                    (u == newEdge.second && w == newEdge.first)) {
                    color = "red";
                    style = ", penwidth=2";
                }
                
                file << "  " << u << " -- " << w
                     << " [label=\"" << e.getWeight() 
                     << "\", color=" << color << style << "];\n";
            }
        }
    }

    for (auto& ce : cycleEdges) {
        T u = get<0>(ce);
        T w = get<1>(ce);
        int peso = get<2>(ce);
        
        if (u < w) {
            file << "  " << u << " -- " << w 
                 << " [label=\"" << peso
                 << "\", color=gray, style=dashed];\n";
        }
    }

    file << "}\n";
    file.close();
    
    string cmd = "dot -Tpng \"" + filename + "\" -o \"" + filename.substr(0, filename.size()-4) + ".png\"";
    system(cmd.c_str());
}


// -------------- MAIN --------------

int main () {
    clearFolder("kruskalImages");
    clearFolder("primImages");

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
    kruskal(grafo);
    prim(grafo, 1);

    return 0;
}