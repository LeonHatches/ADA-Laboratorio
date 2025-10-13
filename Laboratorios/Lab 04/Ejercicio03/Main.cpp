GraphLink<int> generarGrafoAleatorio(int numVertices) {
    GraphLink<int> G;
    srand(time(nullptr));

    // Inserta vértices del 1 al n
    for (int i = 1; i <= numVertices; i++) 
        G.insertVertex(i);

    // Asegura que el grafo sea conexo uniendo en cadena
    for (int i = 1; i < numVertices; i++) 
        G.insertEdge(i, i + 1, rand() % 20 + 1);

    // Agrega aristas adicionales aleatorias
    int aristasExtras = numVertices * 2;
    for (int i = 0; i < aristasExtras; i++) {
        int a = rand() % numVertices + 1;
        int b = rand() % numVertices + 1;
        if (a != b) 
            G.insertEdge(a, b, rand() % 20 + 1);
    }
    return G;
}
