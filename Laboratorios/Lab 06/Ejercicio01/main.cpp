#include <iostream>
#include <vector>


long fibonacci(int n) {
    if (n < 0)
        std::cout << "No se aceptan números negativos";

    long a = 0, b = 1, c;

    if (n <= 1)
        return n;

    for (int i = 1; i < n; i++) {
        c = a + b;
        a = b;
        b = c;
    }

    return b;
}

int main() {
    for (int i = 0; i <= 80; i++) {
        long f = fibonacci(i);
        std::cout << "Fibonacci(" << i << ")\t= " << f << "\n";
    }
}