#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <queue>

class DisjointSet {
    private:
        std::vector<int> parent;

    public: 
        DisjointSet(int size) {
            parent.resize(size);
            for (int i = 0; i < size; i++) {
                parent[i] = i;
            }
        }

        int find(int i) {
            if (parent[i] == i) {
                return i;
            }

            return find(parent[i]);
        }

        void unite(int i, int j) {
            int irep = find(i);
            int jrep = find(j);

            parent[irep] = jrep;
        }
};



template <typename T>
class MatrixGraph {
    private: 
        std::vector<T> vertices;
        std::vector<std::vector<int>> matriz;

        const int INF = std::numeric_limits<int>::max();

    private:
        int searchVertexIndex(T value) {
            for (size_t i = 0; i < vertices.size(); i++) {
                if (vertices[i] == value)
                    return i;
            }
            return -1;
        }

    public: 
        void addVertex(T value) {

            vertices.push_back(value);
            int n = vertices.size();

            for (auto& vector : matriz)
                vector.push_back(INF);

            matriz.push_back(std::vector<int>(n, INF));
        }

        void addEdge(T vFrom, T vTo, int weight) {
            if (weight <= 0) {
                std::cout << "No se aceptan pesos negativos\n";
                return;
            }

            int vFromIndex = searchVertexIndex(vFrom);
            int vToIndex = searchVertexIndex(vTo);

            if (vFromIndex == -1 || vToIndex == -1) {
                std::cout << "Algunos de los vertices no estan disponibles";
                return;
            }

            matriz[vFromIndex][vToIndex] = weight;
            matriz[vToIndex][vFromIndex] = weight;
        }

        void printGraph() {
            if (vertices.size() == 0) {
                std::cout << "No hay ninguna vértice incluida";
                return;
            }

            for (size_t i = 0; i < matriz.size(); i++) {
                if (i == 0) {
                    std::cout << "\t";
                    for (auto value : vertices)
                        std::cout << value << "\t";
                    std::cout << "\n";
                }
                for (size_t j = 0; j < matriz[i].size(); j++) {
                    if (j == 0) {
                        std::cout << vertices[i] << "\t";
                    }

                    if (matriz[i][j] == INF) 
                        std::cout << "INF" << "\t";
                    else 
                        std::cout << matriz[i][j] << "\t";
                }
                std::cout << "\n";
            }
        }

        struct Edge {
            int u, v, weight;

            Edge(int u, int v, int weight) {
                this->u = u;
                this->v = v;
                this->weight = weight;
            }

            bool operator<(const Edge& other) const {
                return this->weight < other.weight;
            }
        };

        void kruskal() {
            std::vector<T> vertices = this->vertices;

            std::vector<Edge> aristas;
            int n = vertices.size();

            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    if (matriz[i][j] != INF) {
                        aristas.push_back(Edge(i, j, matriz[i][j]));
                    }
                }
            }

            std::sort(aristas.begin(), aristas.end());

            MatrixGraph<T> mst;
            for (T vertice : vertices)
                mst.addVertex(vertice);

            DisjointSet dSet = DisjointSet(n);

            int totalEdges = 0;
            for (size_t i = 0; i < aristas.size() && totalEdges < (int)vertices.size() - 1; i++) {
                if (dSet.find(aristas[i].u) != dSet.find(aristas[i].v)) {
                    mst.addEdge(vertices[aristas[i].u], vertices[aristas[i].v], aristas[i].weight);
                    dSet.unite(aristas[i].u, aristas[i].v);
                }
            }

            mst.printGraph();
        }

        void prim() {
            const int NUL = -1;
            int size = vertices.size();

            std::vector<int> parent(size, NUL);
            std::vector<int> key(size, INF);
            std::vector<bool> inMST(size, false);

            key[0] = 0;
            parent[0] = NUL;

            for (int i = 0; i < size - 1; i++) {
                int minKey = INF;
                int u = NUL;

                for (int j = 0; j < size; j++) {
                    if (!inMST[i] && key[i] < minKey) {
                        minKey = key[i];
                        u = i;
                    }
                }

                if (u == -1) 
                    break;

                inMST[u] = true;

                for (int j = 0; j < size; j++) {
                    if (matriz[u][j] != INF && !inMST[j] && matriz[u][j] < key[j]) {
                        key[j] = matriz[u][j];
                        parent[j] = u;
                    }
                }
            }

            MatrixGraph<T> mst;

            for (T vertice : vertices)
                mst.addVertex(vertice);

            for (int i = 1; i < size; i++) {
                if (parent[i] != NUL)
                    mst.addEdge(vertices[parent[i]], vertices[i], matriz[parent[i]][i]);
            }

            mst.printGraph();
        }
};

int main() {
    MatrixGraph<std::string> graph;

    graph.addVertex("A");
    graph.addVertex("B");
    graph.addVertex("C");
    graph.addVertex("D");
    graph.addVertex("E");
    graph.addVertex("F");
    graph.addVertex("G");

    graph.addEdge("A", "B", 10);
    graph.addEdge("B", "D", 11);
    graph.addEdge("C", "D", 12);
    graph.addEdge("A", "C", 13);
    graph.addEdge("B", "G", 14);
    graph.addEdge("D", "G", 15);
    graph.addEdge("D", "E", 16);
    graph.addEdge("C", "E", 17);
    graph.addEdge("E", "F", 18);
    graph.addEdge("G", "F", 19);

    graph.printGraph();
    std::cout << "\n";
    graph.prim();
}