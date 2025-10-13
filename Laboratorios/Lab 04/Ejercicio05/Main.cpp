#include <iostream>
#include <vector>
#include <tuple>
#include <set>
#include <algorithm>
#include <chrono>
#include <iomanip>
#include <map>
#include <list>
#include <climits>

using namespace std;
using namespace std::chrono;

// Forward declarations
template <typename T>
class Edge;

template <typename T>
class Vertex {
private:
    T data;
    list<Edge<T>> adj;
public:
    Vertex(T d) : data(d) {}
    
    T getData() const { return data; }
    list<Edge<T>>& getAdj() { return adj; }
    const list<Edge<T>>& getAdj() const { return adj; }
    
    void addEdge(Vertex<T>* dest, int weight) {
        adj.push_back(Edge<T>(this, dest, weight));
    }
};

template <typename T>
class Edge {
private:
    Vertex<T>* origin;
    Vertex<T>* dest;
    int weight;
public:
    Edge(Vertex<T>* o, Vertex<T>* d, int w) : origin(o), dest(d), weight(w) {}
    
    Vertex<T>* getOrigin() const { return origin; }
    Vertex<T>* getDest() const { return dest; }
    int getWeight() const { return weight; }
};

template <typename T>
class GraphLink {
private:
    vector<Vertex<T>*> vertices;
public:
    ~GraphLink() {
        for (auto v : vertices) delete v;
    }
    
    void insertVertex(T data) {
        vertices.push_back(new Vertex<T>(data));
    }
    
    void insertEdge(T from, T to, int weight) {
        Vertex<T>* v1 = findVertex(from);
        Vertex<T>* v2 = findVertex(to);
        if (v1 && v2) {
            v1->addEdge(v2, weight);
            v2->addEdge(v1, weight); // Para grafo no dirigido
        }
    }
    
    Vertex<T>* findVertex(T data) {
        for (auto v : vertices) {
            if (v->getData() == data) return v;
        }
        return nullptr;
    }
    
    vector<Vertex<T>*> getListVertex() const {
        return vertices;
    }
    
    // Para debugging
    void printGraph() {
        for (auto v : vertices) {
            cout << "Vertice " << v->getData() << ": ";
            for (const auto& e : v->getAdj()) {
                cout << "-> " << e.getDest()->getData() << "(" << e.getWeight() << ") ";
            }
            cout << endl;
        }
    }
};

// Estructura para Union-Find (usada en Kruskal)
template <typename T>
class UnionFind {
private:
    map<Vertex<T>*, Vertex<T>*> parent;
    map<Vertex<T>*, int> rank;
public:
    void makeSet(Vertex<T>* v) {
        parent[v] = v;
        rank[v] = 0;
    }
    
    Vertex<T>* find(Vertex<T>* v) {
        if (parent[v] != v)
            parent[v] = find(parent[v]);
        return parent[v];
    }
    
    void unionSets(Vertex<T>* a, Vertex<T>* b) {
        Vertex<T>* rootA = find(a);
        Vertex<T>* rootB = find(b);
        
        if (rootA != rootB) {
            if (rank[rootA] < rank[rootB])
                parent[rootA] = rootB;
            else if (rank[rootA] > rank[rootB])
                parent[rootB] = rootA;
            else {
                parent[rootB] = rootA;
                rank[rootA]++;
            }
        }
    }
};

// Algoritmo de Kruskal
template <typename T>
GraphLink<T> kruskal(GraphLink<T>& G) {
    GraphLink<T> mst;
    UnionFind<T> uf;
    vector<pair<int, pair<Vertex<T>*, Vertex<T>*>>> edges;
    
    // Crear vértices en el MST
    for (auto v : G.getListVertex()) {
        mst.insertVertex(v->getData());
        uf.makeSet(v);
    }
    
    // Recoger todas las aristas
    for (auto v : G.getListVertex()) {
        for (const auto& e : v->getAdj()) {
            if (v->getData() < e.getDest()->getData()) { // Evitar duplicados
                edges.push_back({e.getWeight(), {v, e.getDest()}});
            }
        }
    }
    
    // Ordenar aristas por peso
    sort(edges.begin(), edges.end(), 
         [](const auto& a, const auto& b) { return a.first < b.first; });
    
    // Construir MST
    for (const auto& edge : edges) {
        int weight = edge.first;
        Vertex<T>* u = edge.second.first;
        Vertex<T>* v = edge.second.second;
        
        if (uf.find(u) != uf.find(v)) {
            mst.insertEdge(u->getData(), v->getData(), weight);
            uf.unionSets(u, v);
        }
    }
    
    return mst;
}

// Algoritmo de Prim
template <typename T>
GraphLink<T> prim(GraphLink<T>& G, T inicio) {
    GraphLink<T> mst;
    auto vertices = G.getListVertex();
    
    if (vertices.empty()) return mst;
    
    // Crear vértices en el MST
    for (auto v : vertices) {
        mst.insertVertex(v->getData());
    }
    
    map<Vertex<T>*, bool> inMST;
    map<Vertex<T>*, int> key;
    map<Vertex<T>*, Vertex<T>*> parent;
    
    for (auto v : vertices) {
        inMST[v] = false;
        key[v] = INT_MAX;
    }
    
    Vertex<T>* startVertex = G.findVertex(inicio);
    if (!startVertex) return mst;
    
    key[startVertex] = 0;
    parent[startVertex] = nullptr;
    
    for (int i = 0; i < vertices.size(); i++) {
        // Encontrar vértice con key mínimo
        Vertex<T>* u = nullptr;
        int minKey = INT_MAX;
        
        for (auto v : vertices) {
            if (!inMST[v] && key[v] < minKey) {
                minKey = key[v];
                u = v;
            }
        }
        
        if (!u) break;
        
        inMST[u] = true;
        
        // Agregar arista al MST
        if (parent[u] != nullptr) {
            // Encontrar el peso de la arista
            int weight = 0;
            for (const auto& e : parent[u]->getAdj()) {
                if (e.getDest() == u) {
                    weight = e.getWeight();
                    break;
                }
            }
            mst.insertEdge(parent[u]->getData(), u->getData(), weight);
        }
        
        // Actualizar keys de vértices adyacentes
        for (const auto& e : u->getAdj()) {
            Vertex<T>* v = e.getDest();
            int weight = e.getWeight();
            if (!inMST[v] && weight < key[v]) {
                parent[v] = u;
                key[v] = weight;
            }
        }
    }
    
    return mst;
}
