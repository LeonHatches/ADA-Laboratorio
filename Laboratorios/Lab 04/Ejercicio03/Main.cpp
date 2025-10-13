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
