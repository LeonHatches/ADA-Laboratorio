#include <iostream>
#include <vector>
#include <limits>

template <typename T>
class Graph {
    private: 
        std::vector<T> vertices;
        std::vector<std::vector<int>> matriz;

        const int INF = std::numeric_limits<int>::max();

    private:
        int searchVertexIndex(T value) {
            for (int i = 0; i < vertices.size(); i++) {
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
            }

            for (int i = 0; i < matriz.size(); i++) {
                if (i == 0) {
                    std::cout << "\t";
                    for (auto value : vertices)
                        std::cout << value << "\t";
                    std::cout << "\n";
                }
                for (int j = 0; j < matriz[i].size(); j++) {
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
};

int main() {
    Graph<std::string> graph;
}