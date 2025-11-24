class Edge:
    def __init__(self, dest, weight):
        self.dest = dest
        self.weight = weight

    def __str__(self):
         return f"({self.dest.data}, {self.weight})"

class Vertex:
    def __init__(self, data):
        self.data = data
        self.adj_list : list[Edge] = []
    
    def add_edge(self, dest, weight):
        if any(e.dest == dest for e in self.adj_list):
            return
        self.adj_list.append(Edge(dest, weight))

    def __lt__(self, other):
        return self.data < other.data  

class GraphLink:
    def __init__(self):
        self.vertices : list[Vertex] = []

    def search_vertex(self, data):
        for v in self.vertices:
            if v.data == data:
                return v
        return None

    def insert_vertex(self, data):
        if self.search_vertex(data):
            print("Vertice ya esta en el grafo")
            return
        self.vertices.append(Vertex(data))

    def insert_edge(self, vFrom, vTo, weight):
        v_from = self.search_vertex(vFrom)
        v_to = self.search_vertex(vTo)

        if v_from and v_to:
            v_from.add_edge(v_to, weight)
            v_to.add_edge(v_from, weight)
        else:
            print("Algún vértice ingresado no existe")

    def insert_edge_directed(self, vFrom, vTo, weight):
        v_from = self.search_vertex(vFrom)
        v_to = self.search_vertex(vTo)

        if v_from and v_to:
            v_from.add_edge(v_to, weight)
        else:
            print("Algún vértice ingresado no existe")

    def get_edge_weight(self, vFrom, vTo):
        v = self.search_vertex(vFrom)
        if not v:
            return -1
        for e in v.adj_list:
            if e.dest.data == vTo:
                return e.weight
        return -1

    def print_graph(self):
        for vertex in self.vertices:
            edges = " ".join(str(e) for e in vertex.adj_list)
            print(f"{vertex.data} -> {edges}")
    
class GraphLinkDirected(GraphLink):
    
    def insert_edge(self, vFrom, vTo, weight):
        v_from = self.search_vertex(vFrom)
        v_to = self.search_vertex(vTo)

        if v_from and v_to:
            v_from.add_edge(v_to, weight)
        else:
            print("Algún vértice ingresado no existe")
