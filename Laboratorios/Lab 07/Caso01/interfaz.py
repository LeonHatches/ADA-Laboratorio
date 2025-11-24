import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import ttk
from ordenar_pacientes import merge_sort_pacientes
from asignacion import mochila_pacientes
from gráficos import mapa_hospital, mostrar_ruta, embed_figure_in_window

# PACIENTES

pacientes = [
    {"nombre": "Juan", "gravedad": 8, "tiempo": 3},
    {"nombre": "Jose", "gravedad": 4, "tiempo": 2},
    {"nombre": "Carl", "gravedad": 10, "tiempo": 4},
    {"nombre": "Aron", "gravedad": 2, "tiempo": 1},
    {"nombre": "Mark", "gravedad": 5, "tiempo": 5}
]

# TABLAS
tabla_global = None

asignacion = {
    "Cama1": "Jaic",
    "Cama2": None,
    "Cama3": None,
    "Cama4": None,
    "Cama5": None,
    "Cama6": None
}

# MODAL PARA MENSAJES
def mostrar_modal(root, titulo, contenido):
    win = tb.Toplevel(root)
    win.title(titulo)
    win.geometry("420x300")
    win.resizable(False, False)

    frame = tb.Frame(win, padding=20)
    frame.pack(fill="both", expand=True)

    tb.Label(frame, text=titulo, font=("Segoe UI", 16, "bold")).pack(pady=10)

    text = tk.Text(frame, wrap="word", height=10, font=("Segoe UI", 12))
    text.insert("1.0", contenido)
    text.configure(state="disabled", bg="#f8f9fa", relief="flat")
    text.pack(fill="both", expand=True, pady=10)

    tb.Button(frame, text="Aceptar", bootstyle="primary", command=win.destroy).pack(pady=10)


# ACTUALIZACION DE LA TABLA
def actualizar_tabla(tabla):
    tabla.delete(*tabla.get_children())
    ordenados = merge_sort_pacientes(pacientes)
    for p in ordenados:
        tabla.insert("", tk.END, values=(p["nombre"], p["gravedad"], p["tiempo"]))


# MODAL PARA AGREGAR PACIENTE
def agregar_paciente_modal(root, tabla):

    win = tb.Toplevel(root)
    win.title("Agregar paciente")
    win.geometry("350x400")
    win.resizable(False, False)

    frame = tb.Frame(win, padding=20)
    frame.pack(fill="both", expand=True)

    tb.Label(frame, text="Nuevo paciente", font=("Segoe UI", 18, "bold")).pack(pady=10)

    # ENTRADAS
    tb.Label(frame, text="Nombre:", font=("Segoe UI", 12, "bold")).pack(anchor="w")
    nombre_entry = tb.Entry(frame)
    nombre_entry.pack(fill="x", pady=5)

    tb.Label(frame, text="Gravedad (1–10):", font=("Segoe UI", 12, "bold")).pack(anchor="w")
    gravedad_entry = tb.Entry(frame)
    gravedad_entry.pack(fill="x", pady=5)

    tb.Label(frame, text="Tiempo (horas):", font=("Segoe UI", 12, "bold")).pack(anchor="w")
    tiempo_entry = tb.Entry(frame)
    tiempo_entry.pack(fill="x", pady=5)

    def guardar(*args):
        try:
            nombre = nombre_entry.get().strip()
            gravedad = int(gravedad_entry.get())
            tiempo = int(tiempo_entry.get())

            if not nombre:
                mostrar_modal(root, "Error", "El nombre está vacío.")
                return
            if not 1 <= gravedad <= 10:
                mostrar_modal(root, "Error", "La gravedad debe ser entre 1 y 10.")
                return
            if tiempo <= 0:
                mostrar_modal(root, "Error", "El tiempo debe ser mayor a 0.")
                return

            pacientes.append({"nombre": nombre, "gravedad": gravedad, "tiempo": tiempo})
            actualizar_tabla(tabla)
            win.destroy()

        except:
            mostrar_modal(root, "Error", "Los datos ingresados no son válidos.")

    # BOTÓN FINAL
    btn = tb.Button(frame, text="Guardar", bootstyle="success", width=18, command=guardar)
    btn.pack(pady=15)

    # ASOCIAR ENTER A GUARDAR
    win.bind("<Return>", guardar)


# VENTANA DIVIDIDA
def ventana_mapa_y_ruta(root):
    global asignacion, tabla_global

    win = tb.Toplevel(root)
    win.title("Mapa y Ruta - Vista dividida")
    win.state("zoomed")
    win.resizable(True, True)

    # Frame maestro con 2 columnas
    master_frame = tb.Frame(win, padding=10)
    master_frame.pack(fill="both", expand=True)

    master_frame.columnconfigure(0, weight=1, uniform="col")
    master_frame.columnconfigure(1, weight=1, uniform="col")

    # PANEL IZQ.
    left_frame = tb.Labelframe(master_frame, text="Mapa del Hospital", padding=10)
    left_frame.grid(row=0, column=0, sticky="nsew", padx=10)

    # Frame superior
    top_controls = tb.Frame(left_frame)
    top_controls.pack(fill="x", pady=5)

    # Frame inferior para el mapa
    map_container = tb.Frame(left_frame)
    map_container.pack(fill="both", expand=True)

    # ASIGNAR CAMA: FUNCIÓN
    def asignar_cama():
        modal = tb.Toplevel(win)
        modal.title("Asignar cama")
        modal.geometry("350x350")
        modal.resizable(False, False)

        frame = tb.Frame(modal, padding=20)
        frame.pack(fill="both", expand=True)

        tb.Label(frame, text="Asignar cama", font=("Segoe UI", 16, "bold")).pack(pady=10)

        disponibles = [p["nombre"] for p in pacientes]
        tb.Label(frame, text="Paciente:", font=("Segoe UI", 12)).pack(anchor="w")
        cb_pac = tb.Combobox(frame, values=disponibles, width=25)
        cb_pac.pack(pady=5)

        libres = [c for c, n in asignacion.items() if n is None]
        tb.Label(frame, text="Cama:", font=("Segoe UI", 12)).pack(anchor="w")
        cb_cama = tb.Combobox(frame, values=libres, width=25)
        cb_cama.pack(pady=5)

        def confirmar():
            pac = cb_pac.get().strip()
            cama = cb_cama.get().strip()
            if pac == "" or cama == "":
                mostrar_modal(root, "Error", "Seleccione paciente y cama.")
                return

            asignacion[cama] = pac

            for p in pacientes:
                if p["nombre"] == pac:
                    pacientes.remove(p)
                    break

            actualizar_tabla(tabla_global)

            # redibujar mapa
            new_fig = mapa_hospital(asignacion)
            embed_figure_in_window(new_fig, map_container)

            modal.destroy()

        tb.Button(frame, text="Asignar", bootstyle="success",
                width=20, command=confirmar).pack(pady=15)

    # BOTON ASIGNAR CAMAS
    tb.Button(top_controls, text="Asignar cama", bootstyle="success",
            width=20, command=asignar_cama).pack()

    # DIBUJAR MAPA
    fig_mapa = mapa_hospital(asignacion)
    embed_figure_in_window(fig_mapa, map_container)

    # PANEL DER.
    right_frame = tb.Labelframe(master_frame, text="Ruta Ambulancia a Cama", padding=10)
    right_frame.grid(row=0, column=1, sticky="nsew", padx=10)

    # ETIQUETAS
    cb_label = tb.Label(
        right_frame,
        text="Seleccione cama destino:",
        font=("Segoe UI", 14, "bold")
    )
    cb_label.pack(pady=10)

    # COMBOBOX
    cb = tb.Combobox(
        right_frame,
        values=["Cama1", "Cama2", "Cama3", "Cama4", "Cama5", "Cama6"],
        width=20,
        font=("Segoe UI", 12)
    )
    cb.pack(pady=5)

    # BOTÓN CAMA SELECCIONADA
    boton_ruta = tb.Button(
        right_frame,
        text="Buscar ruta",
        bootstyle="danger",
        width=20
    )
    boton_ruta.pack(pady=10)

    # FRAME GRÁFICO INCRUSTAR
    route_plot_frame = tb.Frame(right_frame, width=600, height=500)
    route_plot_frame.pack(fill="both", expand=True, pady=10)

    route_plot_frame.pack_propagate(False)
    route_plot_frame.update()

    # FUNCIÓN BOTON CALCULAR RUTA
    def calcular_ruta():
        cama = cb.get().strip()
        if cama == "":
            mostrar_modal(root, "Error", "Seleccione una cama.")
            return

        fig_route = mostrar_ruta(cama)

        # LIMPIAR RUTA
        for child in route_plot_frame.winfo_children():
            child.destroy()

        embed_figure_in_window(fig_route, route_plot_frame)

    # ASIGNAR FUNCIÓN AL BOTÓN
    boton_ruta.config(command=calcular_ruta)


# VENTANA PRINCIPAL 
def interfaz():

    global tabla_global

    root = tb.Window(themename="flatly")
    root.title("Sistema de Gestión Hospitalaria - ADA")
    root.state("zoomed")

    # TOOLBAR
    toolbar = tb.Frame(root, bootstyle="light", padding=10)
    toolbar.pack(fill="x")

    # TÍTULO
    tb.Label(root, text="Pacientes Ordenados por Gravedad",
             font=("Segoe UI", 20, "bold")).pack(pady=5)

    tabla_frame = tb.Frame(root)
    tabla_frame.pack(pady=10)

    columnas = ("Nombre", "Gravedad", "Tiempo")
    tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings", height=8)

    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Gravedad", text="Gravedad")
    tabla.heading("Tiempo", text="Tiempo (horas)")

    tabla.column("Nombre", width=200, anchor="center")
    tabla.column("Gravedad", width=100, anchor="center")
    tabla.column("Tiempo", width=120, anchor="center")

    tabla.pack()
    actualizar_tabla(tabla)

    tabla_global = tabla

    # BOTONES TOOLBAR
    tb.Button(toolbar, text="+ Agregar paciente",
              bootstyle="success", width=30,
              command=lambda: agregar_paciente_modal(root, tabla)).pack(side="left", padx=10)
    
    tb.Button(toolbar, text="Mapa + Ruta (Vista dividida)",
          bootstyle="dark-outline",
          width=30,
          command=lambda: ventana_mapa_y_ruta(root)).pack(side="left", padx=10)

    # MOCHILA PANEL
    caja = tb.Labelframe(root, text="Según tiempo disponible",
                         padding=15, bootstyle="info")
    caja.pack(pady=20, padx=20, fill="x")

    tb.Label(caja, text="Tiempo máximo disponible (horas):",
             font=("Segoe UI", 12)).pack()

    tiempo_entry = tb.Entry(caja, width=15)
    tiempo_entry.pack(pady=8)

    def resolver_mochila():
        try:
            t = int(tiempo_entry.get())
        except ValueError:
            mostrar_modal(root, "Error", "Ingrese un número válido.")
            return

        seleccion, total = mochila_pacientes(merge_sort_pacientes(pacientes), t)

        if not seleccion:
            mostrar_modal(root, "Resultado", "No se puede atender ningún paciente con ese tiempo.")
            return

        texto = "\n".join([
            f"- {p['nombre']} (G:{p['gravedad']}, T:{p['tiempo']}h)"
            for p in seleccion
        ])
        texto += f"\n\nGravedad total: {total}"

        mostrar_modal(root, "Resultado Mochila 0/1", texto)

    tb.Button(caja, text="Calcular", bootstyle="success",
              command=resolver_mochila).pack(pady=8)

    # PANEL PARA LIBERAR CAMA
    caja_liberar = tb.Labelframe(root, text="Liberar cama ocupada",
                                padding=15, bootstyle="warning")
    caja_liberar.pack(pady=10, padx=20, fill="x")

    tb.Label(caja_liberar,
            text="Seleccione la cama a liberar:",
            font=("Segoe UI", 12)).pack()

    # COMBOBOX DE CAMAS OCUPADAS
    cb_liberar = tb.Combobox(
        caja_liberar,
        values=[c for c, p in asignacion.items() if p is not None],
        width=20
    )
    cb_liberar.pack(pady=8)

    def liberar_cama():
        cama = cb_liberar.get().strip()
        if cama == "":
            mostrar_modal(root, "Error", "Seleccione una cama para liberar.")
            return

        asignacion[cama] = None

        cb_liberar["values"] = [c for c, p in asignacion.items() if p is not None]

        mostrar_modal(root, "Éxito", f"La {cama} ha sido liberada correctamente.")

    tb.Button(caja_liberar, text="Liberar",
            bootstyle="danger", width=15,
            command=liberar_cama).pack(pady=5)

    
    root.mainloop()