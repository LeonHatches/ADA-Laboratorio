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
};

// Función para crear un grafo aleatorio conexo
GraphLink<int> generarGrafoAleatorio(int numVertices) {
    GraphLink<int> G;
    srand(time(nullptr));

    // Crear los vértices
    for (int i = 1; i <= numVertices; i++)
        G.insertVertex(i);

    // Agregar aristas aleatorias para asegurar conexidad
    for (int i = 1; i < numVertices; i++) {
        int peso = rand() % 20 + 1;
        G.insertEdge(i, i + 1, peso);
    }

    // Agregar más aristas aleatorias para densidad
    int aristasExtras = numVertices * 2;
    for (int i = 0; i < aristasExtras; i++) {
        int a = rand() % numVertices + 1;
        int b = rand() % numVertices + 1;
        if (a != b) {
            int peso = rand() % 20 + 1;
            G.insertEdge(a, b, peso);
        }
    }

    return G;
}
