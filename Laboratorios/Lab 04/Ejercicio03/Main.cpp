#include <iostream>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <vector>
#include <map>
#include <list>
#include <algorithm>
#include <climits>
using namespace std;
using namespace std::chrono;

template <typename T> class Vertex;
template <typename T> class Edge;
template <typename T> class GraphLink;

// Clase Edge
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

// Clase Vertex
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

// Clase GraphLink
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
            // Para evitar duplicados exactos, podrías comprobar existencia antes; aquí lo insertamos directamente
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

// Estructura para Union-Find (usado en Kruskal)
template <typename T>
class UnionFind {
private:
    // Usar punteros como claves/valores
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
    // vector de: (peso, (vertex*, vertex*))
    vector<pair<int, pair<Vertex<T>*, Vertex<T>*>>> edges;
    
    // Crear vértices en el MST (copia solo los datos)
    for (auto v : G.getListVertex()) {
        mst.insertVertex(v->getData());
        uf.makeSet(v); 
    }
    
    // Recoger todas las aristas 
    for (auto v : G.getListVertex()) {
        for (const auto& e : v->getAdj()) {
            // Asegurarse de agregar cada arista solo una vez en el caso no dirigido
            // (esto asume que T soporta operator<, con int funciona)
            if (v->getData() < e.getDest()->getData()) { 
                edges.push_back({e.getWeight(), {v, e.getDest()}});
            }
        }
    }
    
    // Ordenar aristas por peso de forma ascendente
    sort(edges.begin(), edges.end(), 
         [](const auto& a, const auto& b) { return a.first < b.first; });
    
    // Construir MST
    for (const auto& edge : edges) {
        int weight = edge.first;
        Vertex<T>* u_original = edge.second.first;
        Vertex<T>* v_original = edge.second.second;
        
        // si los vértices no estan ya en la misma componente
        if (uf.find(u_original) != uf.find(v_original)) {
            // agrega la arista al MST (usa los datos, insertEdge buscará los vértices copiados en mst)
            mst.insertEdge(u_original->getData(), v_original->getData(), weight);
            // unir
            uf.unionSets(u_original, v_original);
        }
    }
    
    return mst;
}

// Algoritmo de Prim (implementación simple O(V^2))
template <typename T>
GraphLink<T> prim(GraphLink<T>& G, T start) {
    GraphLink<T> mst;
    auto vertices = G.getListVertex();
    
    if (vertices.empty()) return mst;
    
    // Crear vértices en el MST (copiar solo los datos)
    for (auto v : vertices) {
        mst.insertVertex(v->getData());
    }
    
    map<Vertex<T>*, bool> inMST;
    map<Vertex<T>*, int> key;    
    map<Vertex<T>*, Vertex<T>*> parent; 
    
    for (auto v : vertices) {
        inMST[v] = false;
        key[v] = INT_MAX;
        parent[v] = nullptr;
    }
    
    Vertex<T>* startVertex = G.findVertex(start);
    if (!startVertex) return mst;
    
    key[startVertex] = 0; 

    for (int i = 0; i < (int)vertices.size(); i++) {
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
        
        if (parent[u] != nullptr) {
            mst.insertEdge(parent[u]->getData(), u->getData(), key[u]);
        }
        
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

// Función para crear un grafo aleatorio conexo
GraphLink<int> generarGrafoAleatorio(int numVertices) {
    GraphLink<int> G;

    // Crear los vértices
    for (int i = 1; i <= numVertices; i++)
        G.insertVertex(i);

    // Agregar aristas para asegurar la conexidad inicial
    for (int i = 1; i < numVertices; i++) {
        int peso = rand() % 20 + 1; // Pesos entre 1 y 20
        G.insertEdge(i, i + 1, peso);
    }

    // Agregar más aristas aleatorias para aumentar la densidad del grafo
    int aristasExtras = numVertices;
    for (int i = 0; i < aristasExtras; i++) {
        int a = rand() % numVertices + 1;
        int b = rand() % numVertices + 1;
        // evitar autobucles y aristas existentes (comprobación simple)
        if (a != b) {
            int peso = rand() % 20 + 1;
            G.insertEdge(a, b, peso);
        }
    }

    return G;
}

// Funcion para calcular el peso total de un MST
template <typename T>
int calcularPeso(GraphLink<T>& G) {
    int total = 0;
    for (auto v : G.getListVertex()) {
        for (const auto& e : v->getAdj()) {
            // sumar el peso de cada arista una sola vez
            if (v->getData() < e.getDest()->getData()) 
                total += e.getWeight();
        }
    }
    return total;
}

int main() {
    srand((unsigned)time(nullptr));

    vector<int> tamanos = {10, 50, 100}; 

    for (int n : tamanos) {
        cout << "\nGRAFO CON " << n << " VERTICES\n";
        cout << "=====================\n";

        GraphLink<int> G = generarGrafoAleatorio(n);

        // Medir tiempo de Kruskal
        auto inicioK = high_resolution_clock::now();
        GraphLink<int> mstK = kruskal(G);
        auto finK = high_resolution_clock::now();
        auto tiempoK = duration_cast<milliseconds>(finK - inicioK).count();

        // Medir tiempo de Prim
        auto inicioP = high_resolution_clock::now();
        GraphLink<int> mstP = prim(G, 1); // Asumimos que el vértice 1 siempre existe
        auto finP = high_resolution_clock::now();
        auto tiempoP = duration_cast<milliseconds>(finP - inicioP).count();

        // Calcular pesos totales
        int pesoK = calcularPeso(mstK);
        int pesoP = calcularPeso(mstP);

        cout << "Tiempo Kruskal: " << tiempoK << " ms\n";
        cout << "Tiempo Prim: " << tiempoP << " ms\n";
        cout << "Peso total Kruskal: " << pesoK << "\n";
        cout << "Peso total Prim: " << pesoP << "\n";

        if (pesoK == pesoP)
            cout << "Ambos algoritmos producen el mismo costo total\n";
        else
            cout << "ERROR: Los algoritmos generaron MST con diferentes costos!\n";
    }

    return 0;
}
