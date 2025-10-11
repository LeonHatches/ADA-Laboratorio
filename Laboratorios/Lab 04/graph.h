#include <iostream>
#include <list>

template <typename T>
class Vertex;

template <typename T>
class Edge;

template <typename T>
class Edge {
    private:
        Vertex<T>* refDest;
        int weight;

    public:
        Edge(Vertex<T>* refDest, int weight) {
            this->refDest = refDest;
            this->weight = weight;
        }

        int getWeight() const {
            return this->weight;
        }

        Vertex<T>* getDest() const {
            return this->refDest;
        }

        std::string toString() const {
            return "(" + std::to_string(refDest->getData()) + ", " + std::to_string(weight) + ")";
        }
};

template <typename T>
class Vertex {
    private:
        T data;
        std::list<Edge<T>> listAdj;

    public:
        Vertex(T data) {
            this->data = data;
        }

        void addEdge(Vertex<T>* dest, int weight) {
            for (const auto& e : listAdj)
                if (e.getDest() == dest)
                    return;

            listAdj.push_front(Edge<T>(dest, weight));
        }

        T getData() const {
            return data;
        }

        const std::list<Edge<T>>& getAdj() const {
            return listAdj;
        }
};

template <typename T>
class GraphLink {
    private:
        std::list<Vertex<T>*> listVertex;
    
    public:
        GraphLink() {}

        const std::list<Vertex<T>*>& getListVertex () const {
            return listVertex;
        }

        Vertex<T>* searchVertex(T data) const {
            for (Vertex<T>* v : listVertex) {
                if (v->getData() == data)
                    return v;
            }
            return nullptr;
        }

        void insertVertex(T data) {
            Vertex<T>* vertex = searchVertex(data);
            if (vertex) {
                std::cout << "Vertice ya esta en el grafo\n";
                return;
            }
            listVertex.push_front(new Vertex<T>(data));
        }

        void insertEdge(T from, T to, int weight) {
            Vertex<T>* vFrom = searchVertex(from);
            Vertex<T>* vTo = searchVertex(to);

            if (vFrom && vTo) {
                vFrom->addEdge(vTo, weight);
                return;
            }

            std::cout << "Alguna vertice ingresada no existe\n";
        }
    
        void printGraph() {
            for (Vertex<T>* vertex : listVertex) {
                std::cout << vertex->getData() << " -> ";
                for (const Edge<T>& edge : vertex->getAdj())
                    std::cout << edge.toString() << " ";

                std::cout << "\n";
            }
        }
};
