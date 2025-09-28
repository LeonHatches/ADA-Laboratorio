#include <vector>
#include <iostream>
using namespace std;

class Producto {
    private:
        int id;
        string nombre;
        double precio;

    public:
        Producto (int id, string nombre, double precio) {
            this->id = id;
            this->nombre = nombre;
            this->precio = precio;
        }

        bool operator >(const Producto& producto) {
            return (this->precio > producto.precio);
        }

        bool operator <(const Producto& producto) {
            return (this->precio < producto.precio);
        }

        int getId () { return id; }
        string getNombre () { return nombre; }
        double getPrecio () { return precio; }

        string toStr() const {
            return "| "+to_string(id)+", "+nombre+", "+to_string(precio)+" |";
        }
};