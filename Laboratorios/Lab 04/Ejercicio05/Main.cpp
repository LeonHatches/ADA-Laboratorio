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
