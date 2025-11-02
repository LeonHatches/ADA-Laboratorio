#include <iostream>
#include <vector>
#include <limits>

const int INF = std::numeric_limits<int>::max();

std::vector<int> getPath(int u, int v, std::vector<std::vector<int>>& next) {
    if (next[u][v] == -1) return {};
    std::vector<int> path = {u};
    while (u != v) {
        u = next[u][v];
        path.push_back(u);
    }
    return path;
}

std::pair<int, std::vector<int>> floydWarshall(std::vector<std::vector<int>> matriz, int origin, int dest) {
    int n = matriz.size();

    std::vector<std::vector<int>> dist(n , std::vector<int>(n));
    std::vector<std::vector<int>> next(n, std::vector<int>(n, -1));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dist[i][j] = matriz[i][j];
            if (matriz[i][j] != INF && i != j)
                next[i][j] = j;
        }
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][k] != INF && dist[k][j] != INF &&
                    dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                    next[i][j] = next[i][k];
                }
            }
        }
    }

    int cost = dist[origin][dest];
    std::vector<int> path = getPath(origin, dest, next);

    return {cost, path};
}

void printMatrix(std::vector<std::vector<int>> matrix) {
    for (int i = 0; i < matrix.size(); i++) {
        std::cout << "[";
        for (int j = 0; j < matrix[i].size(); j++) {
            if (matrix[i][j] == INF)
                std::cout << "\tINF";
            else
                std::cout << "\t" << matrix[i][j];
        }
        std::cout << "\t]\n";
    }
}

int main() {
     std::vector<std::vector<int>> matriz = {
        {0,   3, INF,   7},
        {8,   0,   2, INF},
        {5, INF,   0,   1},
        {2, INF, INF,   0}
    };

    std::cout << "Matriz Original\n";
    printMatrix(matriz);

    int origin = 0;
    int dest = 2;


    auto [cost, path] = floydWarshall(matriz, origin, dest);

    std::cout << "Menor costo = " << cost << "\n";
    std::cout << "Camino: ";
    for (auto n : path) {
        std::cout << n << "  ";
    }

    std::cout << "\n";
}