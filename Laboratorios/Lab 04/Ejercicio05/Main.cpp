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

// Funcion para obtener aristas únicas (evita duplicados)
template <typename T>
vector<tuple<T, T, int>> obtenerAristasUnicas(GraphLink<T>& G) {
    vector<tuple<T, T, int>> lista;
    for (auto v : G.getListVertex()) {
        T a = v->getData();
        for (const auto& e : v->getAdj()) {
            T b = e.getDest()->getData();
            int w = e.getWeight();
            if (a < b) lista.push_back({a, b, w});
        }
    }
    sort(lista.begin(), lista.end(),
         [](const auto& x, const auto& y){
             if (get<0>(x) != get<0>(y)) return get<0>(x) < get<0>(y);
             if (get<1>(x) != get<1>(y)) return get<1>(x) < get<1>(y);
             return get<2>(x) < get<2>(y);
         });
    return lista;
}

// Calcula el peso total de las aristas del grafo
template <typename T>
int pesoTotal(GraphLink<T>& G) {
    int total = 0;
    for (auto v : G.getListVertex()) {
        T a = v->getData();
        for (const auto& e : v->getAdj()) {
            T b = e.getDest()->getData();
            int w = e.getWeight();
            if (a < b) total += w;
        }
    }
    return total;
}

// Compara si dos listas de aristas son idénticas
template <typename T>
bool mismasAristas(const vector<tuple<T,T,int>>& a, const vector<tuple<T,T,int>>& b) {
    return a == b;
}

// Imprime las aristas del grafo
template <typename T>
void imprimirAristas(const vector<tuple<T,T,int>>& lista) {
    for (const auto& t : lista)
        cout << "  " << get<0>(t) << " - " << get<1>(t) << "  (peso = " << get<2>(t) << ")\n";
}

// Ejemplo 1: Red de transporte urbano
GraphLink<string> crearRedTransporte() {
    GraphLink<string> R;
    vector<string> estaciones = {"Central","Avenida","Parque","Universidad","Museo","Terminal"};
    for (auto& s : estaciones) R.insertVertex(s);

    R.insertEdge("Central", "Avenida", 5);
    R.insertEdge("Central", "Parque", 7);
    R.insertEdge("Avenida", "Parque", 3);
    R.insertEdge("Avenida", "Universidad", 10);
    R.insertEdge("Parque", "Universidad", 4);
    R.insertEdge("Parque", "Museo", 8);
    R.insertEdge("Universidad", "Museo", 6);
    R.insertEdge("Museo", "Terminal", 9);
    R.insertEdge("Universidad", "Terminal", 12);
    R.insertEdge("Avenida", "Terminal", 14);

    return R;
}

// Ejemplo 2: Red de fibra optica
GraphLink<int> crearRedFibra() {
    GraphLink<int> F;
    for (int i = 1; i <= 8; ++i) F.insertVertex(i);

    F.insertEdge(1, 2, 10);
    F.insertEdge(1, 3, 12);
    F.insertEdge(2, 3, 8);
    F.insertEdge(2, 4, 20);
    F.insertEdge(3, 5, 15);
    F.insertEdge(4, 5, 7);
    F.insertEdge(4, 6, 30);
    F.insertEdge(5, 6, 10);
    F.insertEdge(5, 7, 6);
    F.insertEdge(6, 8, 25);
    F.insertEdge(7, 8, 12);
    F.insertEdge(3, 7, 18);

    return F;
}

// Funcion para aplicar y comparar los algoritmos
template <typename T>
void aplicarYCompararMST(GraphLink<T>& red, T inicio, const string& nombreRed) {
    cout << "\n" << string(50, '=') << "\n";
    cout << "RED: " << nombreRed << "\n";
    
    cout << "Grafo original:\n";
    red.printGraph();

    auto t0 = high_resolution_clock::now();
    GraphLink<T> mstK = kruskal(red);
    auto t1 = high_resolution_clock::now();
    double msK = duration_cast<microseconds>(t1 - t0).count() / 1000.0;

    auto t2 = high_resolution_clock::now();
    GraphLink<T> mstP = prim(red, inicio);
    auto t3 = high_resolution_clock::now();
    double msP = duration_cast<microseconds>(t3 - t2).count() / 1000.0;

    auto aristasK = obtenerAristasUnicas(mstK);
    auto aristasP = obtenerAristasUnicas(mstP);
    int pesoK = pesoTotal(mstK);
    int pesoP = pesoTotal(mstP);

    cout << fixed << setprecision(3);
    cout << "\n ALGORITMO KRUSKAL \n";
    cout << "Tiempo de ejecucion: " << msK << " ms\n";
    cout << "Peso total del MST: " << pesoK << "\n";
    cout << "Aristas del MST:\n"; 
    imprimirAristas(aristasK);

    cout << "\n ALGORITMO PRIM (inicio: " << inicio << ") \n";
    cout << "Tiempo de ejecucion: " << msP << " ms\n";
    cout << "Peso total del MST: " << pesoP << "\n";
    cout << "Aristas del MST:\n"; 
    imprimirAristas(aristasP);

    cout << "\n COMPARACION \n";
    if (pesoK == pesoP)
        cout << "Ambos algoritmos obtuvieron el mismo peso total: " << pesoK << "\n";
    else
        cout << "Los algoritmos obtuvieron pesos diferentes (Kruskal: " << pesoK << ", Prim: " << pesoP << ")\n";

    if (mismasAristas(aristasK, aristasP))
        cout << "Ambos MST contienen exactamente las mismas aristas.\n";
    else
        cout << "Los MST difieren en el conjunto de aristas.\n";

}

int main() {
    cout << "COMPARACION DE ALGORITMOS KRUSKAL Y PRIM\n";

    // Red de transporte urbano
    auto redTransporte = crearRedTransporte();
    aplicarYCompararMST<string>(redTransporte, "Central", "RED DE TRANSPORTE URBANO");

    // Red de fibra óptica
    auto redFibra = crearRedFibra();
    aplicarYCompararMST<int>(redFibra, 1, "RED DE FIBRA OPTICA");

    cout << "\nFin de la comparacion.\n";
    return 0;
}
