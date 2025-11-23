import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from typing import List, Dict, Tuple
import calendar

class Tarea:
    def __init__(self, id_tarea: int, nombre: str, duracion_minutos: int, 
                 prioridad: int, fecha_entrega: datetime, tipo: str, descripcion: str = ""):
        self.id = id_tarea
        self.nombre = nombre
        self.duracion_minutos = duracion_minutos
        self.prioridad = prioridad
        self.fecha_entrega = fecha_entrega
        self.tipo = tipo
        self.descripcion = descripcion
        self.urgencia = self.calcular_urgencia()
        self.valor = self.calcular_valor()
        self.dias_restantes = self.calcular_dias_restantes()
        self.categoria_prioridad = self.determinar_categoria_prioridad()
    
    def calcular_urgencia(self) -> float:
        """Calcula la urgencia basada en la fecha de entrega"""
        hoy = datetime.now()
        dias_restantes = (self.fecha_entrega - hoy).days
        
        if dias_restantes <= 0:
            return 10.0
        elif dias_restantes <= 1:
            return 9.0
        elif dias_restantes <= 3:
            return 8.0
        elif dias_restantes <= 7:
            return 6.0
        else:
            return max(1.0, 10.0 - (dias_restantes / 7))
    
    def calcular_dias_restantes(self) -> int:
        """Calcula los días restantes para la entrega"""
        hoy = datetime.now()
        return max(0, (self.fecha_entrega - hoy).days)
    
    def calcular_valor(self) -> float:
        """Calcula el valor compuesto de la tarea"""
        return (self.prioridad * 0.6 + self.urgencia * 0.4) * 10
    
    def determinar_categoria_prioridad(self) -> str:
        """Determina la categoría de prioridad para la tarea"""
        puntuacion = (self.prioridad * 0.4) + (self.urgencia * 0.6)
        
        if puntuacion >= 8.5:
            return "HACER YA"
        elif puntuacion >= 7.0:
            return "PRÓXIMAS"
        elif puntuacion >= 5.0:
            return "PUEDE ESPERAR"
        else:
            return "BAJA PRIORIDAD"
    
    def obtener_color_prioridad(self) -> str:
        """Devuelve el color según la categoría de prioridad"""
        colores_prioridad = {
            "HACER YA": "#FF4444",      
            "PRÓXIMAS": "#FF8800",      
            "PUEDE ESPERAR": "#FFBB33", 
            "BAJA PRIORIDAD": "#00C851" 
        }
        return colores_prioridad.get(self.categoria_prioridad, "#95A5A6")
    
    def obtener_color_tipo(self) -> str:
        """Devuelve colores específicos por tipo de tarea"""
        colores_tipo = {
            "estudio": "#4285F4",      
            "trabajo": "#EA4335",      
            "ejercicio": "#34A853",    
            "personal": "#FBBC05",     
            "organizacion": "#8E44AD", 
            "creativo": "#FF6B6B",     
            "reunion": "#17A2B8",     
            "urgente": "#E74C3C"  
        }
        return colores_tipo.get(self.tipo, "#95A5A6")

class AlgoritmoOptimizacionTareas:
    """Algoritmos para optimizar la selección y secuenciación de tareas"""
    
    @staticmethod
    def algoritmo_greedy_seleccion(tareas: List[Tarea], tiempo_disponible: int = 480) -> List[Tarea]:
        """GREEDY MEJORADO: Balance entre valor/tiempo y prioridad"""
        
        def puntuacion_balanceada(tarea: Tarea) -> float:
            # Factor 1: Valor por minuto (50%)
            valor_por_minuto = tarea.valor / tarea.duracion_minutos
            
            # Factor 2: Prioridad absoluta (30%)
            factor_prioridad = tarea.prioridad / 10.0
            
            # Factor 3: Urgencia (20%)
            factor_urgencia = tarea.urgencia / 10.0
            
            # Combinación balanceada
            return (valor_por_minuto * 0.5 + factor_prioridad * 0.3 + factor_urgencia * 0.2) * 100
        
        # Ordenar por puntuación balanceada
        tareas_ordenadas = sorted(tareas, key=puntuacion_balanceada, reverse=True)
        
        # Selección por tiempo disponible
        tareas_seleccionadas = []
        tiempo_usado = 0
        
        for tarea in tareas_ordenadas:
            if tiempo_usado + tarea.duracion_minutos <= tiempo_disponible:
                tareas_seleccionadas.append(tarea)
                tiempo_usado += tarea.duracion_minutos
        
        return tareas_seleccionadas
    
    @staticmethod
    def programacion_dinamica_optimizacion(tareas: List[Tarea], tiempo_maximo: int = 480) -> List[Tarea]:
        """PROGRAMACIÓN DINÁMICA: Problema de la mochila para selección óptima"""
        n = len(tareas)
        dp = [0] * (tiempo_maximo + 1)
        seleccion = [[] for _ in range(tiempo_maximo + 1)]
        
        for tarea in tareas:
            for t in range(tiempo_maximo, tarea.duracion_minutos - 1, -1):
                if dp[t] < dp[t - tarea.duracion_minutos] + tarea.valor:
                    dp[t] = dp[t - tarea.duracion_minutos] + tarea.valor
                    seleccion[t] = seleccion[t - tarea.duracion_minutos] + [tarea]
        
        mejor_tiempo = max(range(tiempo_maximo + 1), key=lambda t: dp[t])
        return seleccion[mejor_tiempo]
    
    @staticmethod
    def algoritmo_camino_corto_secuenciacion(tareas: List[Tarea]) -> List[Tarea]:
        """ALGORITMO CAMINO MÁS CORTO: Optimiza secuencia para minimizar transiciones"""
        if len(tareas) <= 1:
            return tareas
        
        def costo_transicion(tipo1: str, tipo2: str) -> int:
            transiciones_suaves = [("estudio", "ejercicio"), ("ejercicio", "personal")]
            if (tipo1, tipo2) in transiciones_suaves:
                return 1
            elif tipo1 == tipo2:
                return 2
            else:
                return 5
        
        secuencia = [tareas[0]]
        tareas_restantes = tareas[1:]
        
        while tareas_restantes:
            ultima_tarea = secuencia[-1]
            mejor_costo = float('inf')
            mejor_tarea = None
            mejor_indice = -1
            
            for i, tarea in enumerate(tareas_restantes):
                costo = costo_transicion(ultima_tarea.tipo, tarea.tipo)
                if costo < mejor_costo:
                    mejor_costo = costo
                    mejor_tarea = tarea
                    mejor_indice = i
            
            secuencia.append(mejor_tarea)
            tareas_restantes.pop(mejor_indice)
        
        return secuencia

class SistemaGestionTareas:
    def __init__(self):
        self.lista_tareas = []
        self.proximo_id = 1
        self.algoritmo_optimizacion = AlgoritmoOptimizacionTareas()
    
    def agregar_tarea(self, nombre: str, duracion_minutos: int, prioridad: int, 
                     fecha_entrega: datetime, tipo: str, descripcion: str = "") -> Tarea:
        tarea = Tarea(self.proximo_id, nombre, duracion_minutos, prioridad, fecha_entrega, tipo, descripcion)
        self.lista_tareas.append(tarea)
        self.proximo_id += 1
        return tarea
    
    def obtener_tareas_por_fecha(self) -> Dict[datetime, List[Tarea]]:
        """Agrupa las tareas por fecha de entrega"""
        tareas_por_fecha = {}
        for tarea in self.lista_tareas:
            fecha = tarea.fecha_entrega.date()
            if fecha not in tareas_por_fecha:
                tareas_por_fecha[fecha] = []
            tareas_por_fecha[fecha].append(tarea)
        return tareas_por_fecha
    
    def obtener_tareas_para_fecha(self, fecha: datetime) -> List[Tarea]:
        """Obtiene todas las tareas para una fecha específica"""
        fecha_date = fecha.date()
        return [tarea for tarea in self.lista_tareas if tarea.fecha_entrega.date() == fecha_date]
    
    def generar_plan_optimizado(self) -> Dict[str, List[Tarea]]:
        """Genera un plan optimizado usando todos los algoritmos"""
        if not self.lista_tareas:
            return {}
        
        tareas_greedy = self.algoritmo_optimizacion.algoritmo_greedy_seleccion(self.lista_tareas)
        tareas_optimas = self.algoritmo_optimizacion.programacion_dinamica_optimizacion(tareas_greedy)
        secuencia_final = self.algoritmo_optimizacion.algoritmo_camino_corto_secuenciacion(tareas_optimas)
        
        tareas_por_prioridad = {
            "HACER YA": [t for t in self.lista_tareas if t.categoria_prioridad == "HACER YA"],
            "PRÓXIMAS": [t for t in self.lista_tareas if t.categoria_prioridad == "PRÓXIMAS"],
            "PUEDE ESPERAR": [t for t in self.lista_tareas if t.categoria_prioridad == "PUEDE ESPERAR"],
            "BAJA PRIORIDAD": [t for t in self.lista_tareas if t.categoria_prioridad == "BAJA PRIORIDAD"]
        }
        
        return {
            'secuencia_optimizada': secuencia_final,
            'por_prioridad': tareas_por_prioridad,
            'total_tareas': len(self.lista_tareas)
        }

class VistaDiaria:
    def __init__(self, parent, sistema_gestion):
        self.parent = parent
        self.sistema = sistema_gestion
        self.fecha_actual = datetime.now()
        self.configurar_interfaz()
    
    def configurar_interfaz(self):
        # Frame principal
        self.frame_principal = tk.Frame(self.parent, bg='white')
        self.frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        self.configurar_header()
        
        # Contenido principal
        self.configurar_contenido_principal()
        
        self.actualizar_vista_diaria()
    
    def configurar_header(self):
        frame_header = tk.Frame(self.frame_principal, bg='white', height=80)
        frame_header.pack(fill=tk.X, pady=(0, 20))
        frame_header.pack_propagate(False)
        
        # Título y fecha
        frame_titulo = tk.Frame(frame_header, bg='white')
        frame_titulo.pack(side=tk.LEFT, padx=20)
        
        logo_text = tk.Label(frame_titulo, text="", font=("Montserrat", 24), 
                           bg='white', fg='#5F6368')
        logo_text.pack(side=tk.LEFT)
        
        self.label_fecha = tk.Label(frame_titulo, text="", 
                                  font=("Montserrat", 20, "bold"), bg='white', fg='#3C4043')
        self.label_fecha.pack(side=tk.LEFT, padx=10)
        
        # Controles de navegación
        frame_controles = tk.Frame(frame_header, bg='white')
        frame_controles.pack(side=tk.RIGHT, padx=20)
        
        estilo_boton = {
            'font': ('Montserrat', 10), 
            'bg': '#F1F3F4', 
            'fg': '#3C4043',
            'relief': 'flat',
            'bd': 0,
            'padx': 15,
            'pady': 8
        }
        
        btn_hoy = tk.Button(frame_controles, text="Hoy", 
                           command=self.ir_a_hoy, **estilo_boton)
        btn_hoy.pack(side=tk.LEFT, padx=5)
        
        btn_anterior = tk.Button(frame_controles, text="‹ Ayer", 
                                command=self.dia_anterior, **estilo_boton)
        btn_anterior.pack(side=tk.LEFT, padx=5)
        
        btn_siguiente = tk.Button(frame_controles, text="Mañana ›", 
                                 command=self.dia_siguiente, **estilo_boton)
        btn_siguiente.pack(side=tk.LEFT, padx=5)
    
    def configurar_contenido_principal(self):
        """Configura el contenido principal de la vista diaria"""
        frame_contenido = tk.Frame(self.frame_principal, bg='white')
        frame_contenido.pack(fill=tk.BOTH, expand=True)
        
        # Columna izquierda - Tareas del día organizadas por prioridad
        self.configurar_columna_tareas(frame_contenido)
        
        # Columna derecha - Estadísticas y recomendaciones
        self.configurar_columna_estadisticas(frame_contenido)
    
    def configurar_columna_tareas(self, parent):
        """Configura la columna de tareas organizadas por prioridad"""
        frame_tareas = tk.Frame(parent, bg='white')
        frame_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        
        # Título
        titulo_tareas = tk.Label(frame_tareas, text="SECUENCIA OPTIMIZADA DEL DÍA", 
                               font=("Montserrat", 14, "bold"), bg='white', fg='#3C4043')
        titulo_tareas.pack(pady=(0, 20))
        
        # Frame para las tareas ordenadas
        self.frame_secuencia_diaria = tk.Frame(frame_tareas, bg='white')
        self.frame_secuencia_diaria.pack(fill=tk.BOTH, expand=True)
    
    def configurar_columna_estadisticas(self, parent):
        """Configura la columna de estadísticas y recomendaciones"""
        frame_estadisticas = tk.Frame(parent, bg='#F8F9FA', width=350)
        frame_estadisticas.pack(side=tk.RIGHT, fill=tk.Y, padx=(15, 0))
        frame_estadisticas.pack_propagate(False)
        
        # Título
        titulo_estadisticas = tk.Label(frame_estadisticas, text="RESUMEN DEL DÍA", 
                                     font=("Montserrat", 14, "bold"), bg='#F8F9FA', fg='#3C4043')
        titulo_estadisticas.pack(pady=20)
        
        # Estadísticas
        self.frame_estadisticas = tk.Frame(frame_estadisticas, bg='#F8F9FA')
        self.frame_estadisticas.pack(fill=tk.X, padx=20, pady=10)
        
        # Recomendaciones de optimización
        self.frame_recomendaciones = tk.Frame(frame_estadisticas, bg='#F8F9FA')
        self.frame_recomendaciones.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        titulo_recomendaciones = tk.Label(self.frame_recomendaciones, text="RECOMENDACIONES", 
                                        font=("Montserrat", 12, "bold"), bg='#F8F9FA', fg='#3C4043')
        titulo_recomendaciones.pack(anchor='w', pady=(0, 10))
        
        self.label_recomendaciones = tk.Label(self.frame_recomendaciones, 
                                            font=("Montserrat", 10), bg='#F8F9FA', fg='#5F6368',
                                            justify=tk.LEFT, wraplength=300)
        self.label_recomendaciones.pack(anchor='w')
    
    def actualizar_vista_diaria(self):
        """Actualiza toda la vista diaria"""
        # Actualizar fecha
        self.actualizar_fecha_display()
        
        # Actualizar tareas del día en ORDEN ÓPTIMO
        self.actualizar_secuencia_optimizada_dia()
        
        # Actualizar estadísticas
        self.actualizar_estadisticas()
        
        # Actualizar recomendaciones
        self.actualizar_recomendaciones()
    
    def actualizar_fecha_display(self):
        """Actualiza el display de la fecha"""
        formato_fecha = self.fecha_actual.strftime("%A, %d de %B de %Y")
        # Capitalizar el día de la semana
        formato_fecha = formato_fecha[0].upper() + formato_fecha[1:]
        self.label_fecha.config(text=formato_fecha)
    
    def actualizar_secuencia_optimizada_dia(self):
        """Actualiza las tareas del día en ORDEN ÓPTIMO de ejecución"""
        # Limpiar frame anterior
        for widget in self.frame_secuencia_diaria.winfo_children():
            widget.destroy()
        
        # Obtener tareas para la fecha actual
        tareas_dia = self.sistema.obtener_tareas_para_fecha(self.fecha_actual)
        
        if not tareas_dia:
            # Mostrar mensaje de día libre
            frame_vacio = tk.Frame(self.frame_secuencia_diaria, bg='white')
            frame_vacio.pack(fill=tk.BOTH, expand=True)
            
            label_vacio = tk.Label(frame_vacio, 
                                 text=" ¡No hay tareas programadas para hoy!\n\nPuedes agregar nuevas tareas o disfrutar de un día productivo organizando tus próximos objetivos.",
                                 font=("Montserrat", 12), bg='white', fg='#95A5A6',
                                 justify=tk.CENTER)
            label_vacio.pack(expand=True)
            return
        
        # Generar secuencia optimizada para las tareas del día
        secuencia_optimizada = self.generar_secuencia_optimizada_dia(tareas_dia)
        
        # Mostrar encabezado de la secuencia
        frame_encabezado = tk.Frame(self.frame_secuencia_diaria, bg='#E8F0FE')
        frame_encabezado.pack(fill=tk.X, pady=(0, 15))
        
        label_encabezado = tk.Label(frame_encabezado, 
                                  text=f" ORDEN RECOMENDADO",
                                  font=("Montserrat", 12, "bold"), bg='#E8F0FE', fg="#2D15B8")
        label_encabezado.pack(pady=10)
        
        # Mostrar cada tarea en orden con número de secuencia
        for i, tarea in enumerate(secuencia_optimizada, 1):
            self.crear_tarjeta_tarea_ordenada(self.frame_secuencia_diaria, tarea, i)
    
    def generar_secuencia_optimizada_dia(self, tareas_dia: List[Tarea]) -> List[Tarea]:
        """Genera la secuencia optimizada para las tareas del día usando los algoritmos"""
        if not tareas_dia:
            return []
        
        # Usar el algoritmo greedy para ordenar las tareas del día
        tiempo_disponible = 480  # 8 horas
        secuencia_greedy = self.sistema.algoritmo_optimizacion.algoritmo_greedy_seleccion(
            tareas_dia, tiempo_disponible
        )
        
        # Aplicar optimización de secuenciación para mejor flujo
        secuencia_final = self.sistema.algoritmo_optimizacion.algoritmo_camino_corto_secuenciacion(
            secuencia_greedy
        )
        
        return secuencia_final
    
    def crear_tarjeta_tarea_ordenada(self, parent, tarea: Tarea, numero_orden: int):
        """Crea una tarjeta de tarea con número de orden en la secuencia"""
        frame_tarjeta = tk.Frame(parent, bg='white', 
                                relief='solid', borderwidth=1,
                                highlightbackground=tarea.obtener_color_prioridad(),
                                highlightthickness=2)
        frame_tarjeta.pack(fill=tk.X, pady=6, padx=5)
        
        # Contenido principal
        frame_contenido = tk.Frame(frame_tarjeta, bg='white', padx=15, pady=12)
        frame_contenido.pack(fill=tk.X)
        
        # Línea 1: Número de orden y nombre
        frame_linea1 = tk.Frame(frame_contenido, bg='white')
        frame_linea1.pack(fill=tk.X)
        
        # Número de orden
        frame_orden = tk.Frame(frame_linea1, bg='#F5422A')
        frame_orden.pack(side=tk.LEFT)
        
        label_orden = tk.Label(frame_orden, text=f"{numero_orden}", 
                             font=("Montserrat", 12, "bold"), bg="#F5422A", fg='white',
                             padx=10, pady=5)
        label_orden.pack()
        
        # Nombre de la tarea
        label_nombre = tk.Label(frame_linea1, text=tarea.nombre, 
                              font=("Montserrat", 11, "bold"), bg='white', fg='#3C4043',
                              wraplength=450, justify=tk.LEFT, anchor='w')
        label_nombre.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))
        
        # Badge de prioridad
        frame_badge = tk.Frame(frame_linea1, bg=tarea.obtener_color_prioridad())
        frame_badge.pack(side=tk.RIGHT, padx=(10, 0))
        
        label_prioridad = tk.Label(frame_badge, text=f"P{tarea.prioridad}", 
                                 font=("Montserrat", 9, "bold"), bg=tarea.obtener_color_prioridad(), fg='white',
                                 padx=8, pady=2)
        label_prioridad.pack()
        
        # Línea 2: Detalles principales
        frame_linea2 = tk.Frame(frame_contenido, bg='white')
        frame_linea2.pack(fill=tk.X, pady=(8, 0))
        
        # Calcular valor por minuto para mostrar por qué está en esta posición
        valor_por_minuto = tarea.valor / tarea.duracion_minutos
        
        detalles_principales = [
            f"⏱️ {tarea.duracion_minutos} min",
            f"{tarea.categoria_prioridad}",
            f"Valor/min: {valor_por_minuto:.1f}",
            f"{tarea.dias_restantes}d restantes"
        ]
        
        for detalle in detalles_principales:
            label_det = tk.Label(frame_linea2, text=detalle,
                               font=("Montserrat", 9), bg='white', fg='#5F6368')
            label_det.pack(side=tk.LEFT, padx=(0, 15))
        
        # Línea 3: Descripción (si existe)
        if tarea.descripcion and tarea.descripcion.strip():
            frame_linea3 = tk.Frame(frame_contenido, bg='white')
            frame_linea3.pack(fill=tk.X, pady=(6, 0))
            
            label_desc = tk.Label(frame_linea3, text=f"📝 {tarea.descripcion}",
                                font=("Montserrat", 9), bg='white', fg='#7F8C8D',
                                wraplength=500, justify=tk.LEFT, anchor='w')
            label_desc.pack(fill=tk.X)
        
        # Línea 4: Razón de la posición (solo para las primeras tareas)
        if numero_orden <= 3:
            frame_linea4 = tk.Frame(frame_contenido, bg='white')
            frame_linea4.pack(fill=tk.X, pady=(6, 0))
    
    def actualizar_estadisticas(self):
        # Limpiar estadísticas anteriores
        for widget in self.frame_estadisticas.winfo_children():
            widget.destroy()
        
        # Obtener tareas del día
        tareas_dia = self.sistema.obtener_tareas_para_fecha(self.fecha_actual)
        
        if not tareas_dia:
            # Estadísticas para día sin tareas
            stats = [
                "Tareas totales: 0",
                "Tiempo total: 0 min",
                "Tareas críticas: 0",
                "Tareas completables: 0"
            ]
        else:
            # Generar secuencia optimizada para calcular estadísticas reales
            secuencia_optimizada = self.generar_secuencia_optimizada_dia(tareas_dia)
            tiempo_total = sum(t.duracion_minutos for t in tareas_dia)
            tareas_criticas = len([t for t in tareas_dia if t.categoria_prioridad == "HACER YA"])
            tareas_rapidas = len([t for t in tareas_dia if t.duracion_minutos <= 15])
            
            horas = tiempo_total // 60
            minutos = tiempo_total % 60
            tiempo_text = f"{horas}h {minutos}min" if horas > 0 else f"{minutos}min"
            
            stats = [
                f"Tareas totales: {len(tareas_dia)}",
                f"Tiempo total: {tiempo_text}",
                f"Tareas críticas: {tareas_criticas}",
                f"Tareas rápidas (<15min): {tareas_rapidas}",
                f"Orden optimizado: {len(secuencia_optimizada)} tareas"
            ]
        
        # Mostrar estadísticas
        for stat in stats:
            label_stat = tk.Label(self.frame_estadisticas, text=stat,
                                font=("Montserrat", 10, "bold"), bg='#F8F9FA', fg='#3C4043',
                                anchor='w')
            label_stat.pack(fill=tk.X, pady=3)
    
    def actualizar_recomendaciones(self):
        """Actualiza las recomendaciones basadas en las tareas del día"""
        tareas_dia = self.sistema.obtener_tareas_para_fecha(self.fecha_actual)
        
        if not tareas_dia:
            recomendaciones = [
                "Este día está libre de tareas programadas",
                "Es un buen momento para planificar la semana",
                "Puedes adelantar tareas futuras o dedicar tiempo a proyectos personales"
            ]
        else:
            # Generar secuencia optimizada para recomendaciones específicas
            secuencia_optimizada = self.generar_secuencia_optimizada_dia(tareas_dia)
            tareas_rapidas = [t for t in secuencia_optimizada if t.duracion_minutos <= 15]
            tareas_largas = [t for t in secuencia_optimizada if t.duracion_minutos > 120]
            
            recomendaciones = []
            
            if tareas_rapidas:
                recomendaciones.append(f"Comienza con {tareas_rapidas[0].nombre} ({tareas_rapidas[0].duracion_minutos}min)")           
            
            if tareas_largas:
                recomendaciones.append(f"Programa descansos durante tarea(s) larga(s)")
            
            # Tiempo total
            tiempo_total = sum(t.duracion_minutos for t in tareas_dia)
            if tiempo_total > 480:
                recomendaciones.append("Considera delegar o reprogramar algunas tareas")
            elif tiempo_total < 240:
                recomendaciones.append("Tienes tiempo disponible, agrega tareas pendientes")
        
        texto_recomendaciones = "\n".join(recomendaciones)
        self.label_recomendaciones.config(text=texto_recomendaciones)
    
    def dia_anterior(self):
        """Navega al día anterior"""
        self.fecha_actual -= timedelta(days=1)
        self.actualizar_vista_diaria()
    
    def dia_siguiente(self):
        """Navega al día siguiente"""
        self.fecha_actual += timedelta(days=1)
        self.actualizar_vista_diaria()
    
    def ir_a_hoy(self):
        """Vuelve al día actual"""
        self.fecha_actual = datetime.now()
        self.actualizar_vista_diaria()

class CalendarioTareas:
    def __init__(self, parent, sistema_gestion):
        self.parent = parent
        self.sistema = sistema_gestion
        self.fecha_actual = datetime.now()
        self.configurar_calendario()
    
    def configurar_calendario(self):
        # Frame principal del calendario con fondo blanco
        self.frame_calendario = tk.Frame(self.parent, bg='white')
        self.frame_calendario.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.configurar_header()
        self.configurar_leyenda_prioridades()
        
        # Frame principal para calendario y sidebar
        frame_principal = tk.Frame(self.frame_calendario, bg='white')
        frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Área del calendario (izquierda)
        self.frame_dias = tk.Frame(frame_principal, bg='white')
        self.frame_dias.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=15)
        
        self.configurar_sidebar_recomendaciones()
        self.configurar_panel_prioridades()
        self.actualizar_calendario()
    
    def configurar_header(self):
        """Header del calendario"""
        frame_header = tk.Frame(self.frame_calendario, bg='white', height=80)
        frame_header.pack(fill=tk.X, pady=(0, 10))
        frame_header.pack_propagate(False)
        
        # Logo y título
        frame_titulo = tk.Frame(frame_header, bg='white')
        frame_titulo.pack(side=tk.LEFT, padx=20)
        
        logo_text = tk.Label(frame_titulo, text="", font=("Montserrat", 24), 
                           bg='white', fg='#5F6368')
        logo_text.pack(side=tk.LEFT)
        
        titulo = tk.Label(frame_titulo, text="Mi calendario", 
                         font=("Montserrat", 20, "bold"), bg='white', fg='#3C4043')
        titulo.pack(side=tk.LEFT, padx=10)
        
        # Controles de navegación
        frame_controles = tk.Frame(frame_header, bg='white')
        frame_controles.pack(side=tk.RIGHT, padx=20)
        
        estilo_boton = {
            'font': ('Montserrat', 10), 
            'bg': '#F1F3F4', 
            'fg': '#3C4043',
            'relief': 'flat',
            'bd': 0,
            'padx': 15,
            'pady': 8
        }
        
        btn_hoy = tk.Button(frame_controles, text="Hoy", 
                           command=self.ir_a_hoy, **estilo_boton)
        btn_hoy.pack(side=tk.LEFT, padx=5)
        
        btn_anterior = tk.Button(frame_controles, text="‹", 
                                command=self.mes_anterior, **estilo_boton)
        btn_anterior.pack(side=tk.LEFT, padx=5)
        
        btn_siguiente = tk.Button(frame_controles, text="›", 
                                 command=self.mes_siguiente, **estilo_boton)
        btn_siguiente.pack(side=tk.LEFT, padx=5)
        
        self.label_mes_actual = tk.Label(frame_controles, 
                                        font=("Montserrat", 16, "bold"), 
                                        bg='white', fg='#3C4043')
        self.label_mes_actual.pack(side=tk.LEFT, padx=20)
    
    def configurar_leyenda_prioridades(self):
        """Leyenda de PRIORIDADES con más énfasis"""
        frame_leyenda = tk.Frame(self.frame_calendario, bg='white')
        frame_leyenda.pack(fill=tk.X, pady=10)
        
        tk.Label(frame_leyenda, text="NIVELES DE PRIORIDAD:", 
                font=("Montserrat", 11, "bold"), bg='white', fg='#3C4043').pack(side=tk.LEFT, padx=10)
        
        prioridades_leyenda = [
            ("HACER YA", "#FF4444"),      # Rojo intenso
            ("PRÓXIMAS", "#FF8800"),      # Naranja
            ("PUEDE ESPERAR", "#FFBB33"), # Amarillo
            ("BAJA PRIORIDAD", "#00C851"),# Verde
        ]
        
        for texto, color in prioridades_leyenda:
            frame_color = tk.Frame(frame_leyenda, bg='white')
            frame_color.pack(side=tk.LEFT, padx=12)
            
            canvas = tk.Canvas(frame_color, width=20, height=20, bg=color, 
                              highlightthickness=1, highlightbackground="#DADCE0")
            canvas.pack(side=tk.LEFT, padx=2)
            canvas.create_text(10, 10, text="!", fill="white", font=("Montserrat", 12, "bold"))
            
            tk.Label(frame_color, text=texto, font=("Montserrat", 10, "bold"), 
                   bg='white', fg='#3C4043').pack(side=tk.LEFT)
    
    def configurar_panel_prioridades(self):
        "Panel de prioridades"
        frame_prioridades = tk.Frame(self.frame_calendario, bg='#F8F9FA', 
                                   relief='solid', borderwidth=2)
        frame_prioridades.pack(fill=tk.X, pady=15, padx=10)
        
        # Título del panel
        titulo_prioridades = tk.Label(frame_prioridades, text="PANEL DE PRIORIDADES: TAREAS ORGANIZADAS", 
                                    font=("Montserrat", 14, "bold"), bg='#F8F9FA', fg='#3C4043')
        titulo_prioridades.pack(pady=15)
        
        # Frame para las categorías de prioridad
        self.frame_categorias = tk.Frame(frame_prioridades, bg='#F8F9FA')
        self.frame_categorias.pack(fill=tk.X, padx=20, pady=10)
        
        self.actualizar_panel_prioridades()
    
    def actualizar_panel_prioridades(self):
        # Limpiar panel anterior
        for widget in self.frame_categorias.winfo_children():
            widget.destroy()
        
        # Obtener plan optimizado
        plan = self.sistema.generar_plan_optimizado()
        tareas_por_prioridad = plan.get('por_prioridad', {})
        
        # Crear una sección para cada categoría de prioridad
        categorias = [
            ("HACER YA: Realizar inmediatamente", "HACER YA", "#FF4444"),
            ("PRÓXIMAS: Tareas importantes para los próximos días", "PRÓXIMAS", "#FF8800"),
            ("PUEDE ESPERAR: Tareas que pueden planificarse para más adelante", "PUEDE ESPERAR", "#FFBB33"),
            ("BAJA PRIORIDAD: Tareas opcionales sin urgencia", "BAJA PRIORIDAD", "#00C851")
        ]
        
        for titulo, clave, color in categorias:
            # Frame para toda la categoría
            frame_categoria = tk.Frame(self.frame_categorias, bg='#F8F9FA')
            frame_categoria.pack(fill=tk.X, pady=12, padx=5)
            
            # Header de la categoría con color más destacado
            frame_header = tk.Frame(frame_categoria, bg=color, relief='raised', borderwidth=2)
            frame_header.pack(fill=tk.X, padx=2, pady=2)
            
            label_titulo = tk.Label(frame_header, text=titulo, 
                                font=("Montserrat", 12, "bold"), 
                                bg=color, fg='white', padx=15, pady=8,
                                anchor='w')
            label_titulo.pack(fill=tk.X)
            
            # Frame para las tarjetas de esta categoría
            frame_tareas_categoria = tk.Frame(frame_categoria, bg='#F8F9FA')
            frame_tareas_categoria.pack(fill=tk.X, padx=8, pady=8)
            
            tareas_categoria = tareas_por_prioridad.get(clave, [])
            
            if not tareas_categoria:
                # Mostrar mensaje si no hay tareas
                label_vacio = tk.Label(frame_tareas_categoria, 
                                     text="¡No hay tareas en esta categoría!",
                                     font=("Montserrat", 10, "italic"), 
                                     bg='#F8F9FA', fg='#95A5A6', 
                                     pady=20)
                label_vacio.pack()
            else:
                # Mostrar contador de tareas más destacado
                contador_frame = tk.Frame(frame_tareas_categoria, bg='#F8F9FA')
                contador_frame.pack(fill=tk.X, pady=(0, 8))
                
                label_contador = tk.Label(contador_frame, 
                                        text=f"{len(tareas_categoria)} tarea(s) en esta categoría",
                                        font=("Montserrat", 10, "bold"), 
                                        bg='#F8F9FA', fg='#5F6368')
                label_contador.pack(anchor='w')
                
                # Mostrar cada tarea como tarjeta
                for tarea in tareas_categoria:
                    self.crear_item_prioridad(frame_tareas_categoria, tarea, color)
    
    def crear_item_prioridad(self, parent, tarea, color_categoria):
        "Tarjeta de tarea para el panel de prioridades"
        frame_tarjeta = tk.Frame(parent, bg='white', 
                                relief='solid', borderwidth=1,
                                highlightbackground=color_categoria,
                                highlightthickness=2)
        frame_tarjeta.pack(fill=tk.X, pady=6, padx=5)
        
        # Barra lateral de color según la PRIORIDAD (no el tipo)
        frame_color = tk.Frame(frame_tarjeta, bg=color_categoria, width=6)
        frame_color.pack(side=tk.LEFT, fill=tk.Y)
        
        # Contenido de la tarjeta
        frame_contenido = tk.Frame(frame_tarjeta, bg='white', padx=12, pady=10)
        frame_contenido.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Nombre de la tarea
        frame_header = tk.Frame(frame_contenido, bg='white')
        frame_header.pack(fill=tk.X)
        
        label_nombre = tk.Label(frame_header, text=tarea.nombre, 
                            font=("Montserrat", 11, "bold"), bg='white', fg='#3C4043',
                            wraplength=300, justify=tk.LEFT, anchor='w')
        label_nombre.pack(fill=tk.X)
        
        # Detalles de la tarea MÁS DESTACADOS
        frame_detalles = tk.Frame(frame_contenido, bg='white')
        frame_detalles.pack(fill=tk.X, pady=(8, 0))
        
        # Primera línea de detalles
        frame_linea1 = tk.Frame(frame_detalles, bg='white')
        frame_linea1.pack(fill=tk.X)
        
        detalles_linea1 = [
            f"{tarea.fecha_entrega.strftime('%d/%m/%Y')}",
            f"{tarea.duracion_minutos}min",
            f"Prioridad: {tarea.prioridad}/10"
        ]
        
        for detalle in detalles_linea1:
            label_det = tk.Label(frame_linea1, text=detalle,
                               font=("Montserrat", 9), bg='white', fg='#5F6368')
            label_det.pack(side=tk.LEFT, padx=(0, 15))
        
        # Segunda línea de detalles
        frame_linea2 = tk.Frame(frame_detalles, bg='white')
        frame_linea2.pack(fill=tk.X, pady=(3, 0))
        
        # Mostrar días restantes con color según urgencia
        dias_color = "#E74C3C" if tarea.dias_restantes <= 1 else "#F39C12" if tarea.dias_restantes <= 3 else "#27AE60"
        label_dias = tk.Label(frame_linea2, text=f"Días restantes: {tarea.dias_restantes}",
                            font=("Montserrat", 9, "bold"), bg='white', fg=dias_color)
        label_dias.pack(side=tk.LEFT, padx=(0, 15))
        
        label_urgencia = tk.Label(frame_linea2, text=f"Urgencia: {tarea.urgencia:.1f}/10",
                                font=("Montserrat", 9), bg='white', fg='#5F6368')
        label_urgencia.pack(side=tk.LEFT)
        
        # Descripción (si existe)
        if tarea.descripcion and tarea.descripcion.strip():
            frame_descripcion = tk.Frame(frame_contenido, bg='white')
            frame_descripcion.pack(fill=tk.X, pady=(8, 0))
            
            label_descripcion = tk.Label(frame_descripcion, text=f"📝 {tarea.descripcion}",
                                    font=("Montserrat", 9), bg='white', fg='#7F8C8D',
                                    wraplength=300, justify=tk.LEFT, anchor='w')
            label_descripcion.pack(fill=tk.X)
    
    def mes_anterior(self):
        self.fecha_actual = self.fecha_actual.replace(day=1) - timedelta(days=1)
        self.fecha_actual = self.fecha_actual.replace(day=1)
        self.actualizar_calendario()
    
    def mes_siguiente(self):
        if self.fecha_actual.month == 12:
            self.fecha_actual = self.fecha_actual.replace(year=self.fecha_actual.year + 1, month=1, day=1)
        else:
            self.fecha_actual = self.fecha_actual.replace(month=self.fecha_actual.month + 1, day=1)
        self.actualizar_calendario()
    
    def ir_a_hoy(self):
        self.fecha_actual = datetime.now()
        self.actualizar_calendario()
    
    def actualizar_calendario(self):
        # Actualizar label del mes
        nombre_mes = calendar.month_name[self.fecha_actual.month]
        año = self.fecha_actual.year
        self.label_mes_actual.config(text=f"{nombre_mes} {año}")
        
        # Limpiar frame de días
        for widget in self.frame_dias.winfo_children():
            widget.destroy()
        
        # Actualizar panel de prioridades
        self.actualizar_panel_prioridades()
        
        # Actualizar recomendaciones
        self.actualizar_recomendaciones()
        
        # Configurar grid del calendario
        self.configurar_grid_calendario()
    
    def configurar_grid_calendario(self):
        # Obtener tareas agrupadas por fecha
        tareas_por_fecha = self.sistema.obtener_tareas_por_fecha()
        
        # Crear encabezados de días de la semana
        dias_semana = ["LUN", "MAR", "MIÉ", "JUE", "VIE", "SÁB", "DOM"]
        for i, dia in enumerate(dias_semana):
            frame_dia_header = tk.Frame(self.frame_dias, bg='white', height=30)
            frame_dia_header.grid(row=0, column=i, sticky="nsew", padx=1, pady=1)
            frame_dia_header.grid_propagate(False)
            
            label = tk.Label(frame_dia_header, text=dia, 
                           font=("Montserrat", 10, "bold"), bg='white', fg='#5F6368')
            label.pack(expand=True)
        
        # Obtener primer día del mes y número de días
        primer_dia = self.fecha_actual.replace(day=1)
        num_dias = calendar.monthrange(self.fecha_actual.year, self.fecha_actual.month)[1]
        dia_inicio = primer_dia.weekday()
        
        # Configurar pesos del grid
        for i in range(7):
            self.frame_dias.columnconfigure(i, weight=1)
        for i in range(6):
            self.frame_dias.rowconfigure(i + 1, weight=1)
        
        # Crear celdas del calendario
        fila, columna = 1, dia_inicio
        hoy = datetime.now().date()
        
        for dia in range(1, num_dias + 1):
            fecha_actual = self.fecha_actual.replace(day=dia).date()
            
            # Crear frame para el día
            bg_color = '#FFFFFF'
            if fecha_actual == hoy:
                bg_color = '#E8F0FE'
            elif fecha_actual.weekday() >= 5:
                bg_color = '#F8F9FA'
            
            frame_dia = tk.Frame(self.frame_dias, bg=bg_color, 
                                relief="solid", borderwidth=0.5, 
                                highlightbackground='#DADCE0',
                                width=120, height=100)
            frame_dia.grid(row=fila, column=columna, sticky="nsew", padx=0.5, pady=0.5)
            frame_dia.grid_propagate(False)
            
            # Configurar contenido del día
            self.configurar_contenido_dia(frame_dia, fecha_actual, dia, hoy, tareas_por_fecha)
            
            # Actualizar posición
            columna += 1
            if columna == 7:
                columna = 0
                fila += 1
    
    def configurar_contenido_dia(self, frame_dia, fecha, numero_dia, hoy, tareas_por_fecha):
        # Número del día
        day_color = '#3C4043'
        if fecha == hoy:
            canvas_dia = tk.Canvas(frame_dia, width=25, height=25, 
                                 bg=frame_dia['bg'], highlightthickness=0)
            canvas_dia.place(x=5, y=5)
            canvas_dia.create_oval(2, 2, 23, 23, fill='#1A73E8', outline='')
            canvas_dia.create_text(12.5, 12.5, text=str(numero_dia), 
                                 fill='white', font=("Montserrat", 10, "bold"))
        else:
            label_numero = tk.Label(frame_dia, text=str(numero_dia), 
                                  font=("Montserrat", 11), bg=frame_dia['bg'], fg=day_color)
            label_numero.place(x=8, y=5)
        
        # Mostrar tareas para esta fecha
        if fecha in tareas_por_fecha:
            tareas_dia = tareas_por_fecha[fecha]
            
            frame_tareas = tk.Frame(frame_dia, bg=frame_dia['bg'])
            frame_tareas.place(x=5, y=35, width=110, height=60)
            
            for i, tarea in enumerate(tareas_dia[:3]):
                if i < 2:
                    self.crear_widget_tarea(frame_tareas, tarea, i)
                else:
                    label_extra = tk.Label(frame_tareas, 
                                         text=f"+{len(tareas_dia) - 2} más",
                                         font=("Montserrat", 8), bg=frame_dia['bg'],
                                         fg='#5F6368')
                    label_extra.pack(fill=tk.X, pady=(2, 0))
                    break
    
    def crear_widget_tarea(self, parent, tarea, index):
        """Crea un widget de tarea para el calendario"""
        color_tarea = tarea.obtener_color_tipo()
        
        frame_tarea = tk.Frame(parent, bg=color_tarea, height=16)
        frame_tarea.pack(fill=tk.X, pady=1)
        frame_tarea.pack_propagate(False)
        
        frame_contenido = tk.Frame(frame_tarea, bg=color_tarea)
        frame_contenido.pack(fill=tk.X, padx=4)
        
        nombre_abreviado = tarea.nombre[:14] + "..." if len(tarea.nombre) > 14 else tarea.nombre
        label = tk.Label(frame_contenido, text=nombre_abreviado, 
                        font=("Montserrat", 8), bg=color_tarea, fg='white',
                        anchor='w')
        label.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def configurar_sidebar_recomendaciones(self):
        """Configura el sidebar con recomendaciones de tareas"""
        # Frame lateral
        frame_sidebar = tk.Frame(self.frame_calendario, bg='#F8F9FA', width=300)
        frame_sidebar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 20), pady=20)
        frame_sidebar.pack_propagate(False)
        
        # Título del sidebar
        titulo_sidebar = tk.Label(frame_sidebar, text="Tareas recomendadas", 
                                font=("Montserrat", 14, "bold"), bg='#F8F9FA', fg='#3C4043')
        titulo_sidebar.pack(pady=20)
        
        # Frame para las recomendaciones
        self.frame_recomendaciones = tk.Frame(frame_sidebar, bg='#F8F9FA')
        self.frame_recomendaciones.pack(fill=tk.BOTH, expand=True, padx=15)
        
        self.actualizar_recomendaciones()

    def actualizar_recomendaciones(self):
        """Actualiza las recomendaciones en el sidebar"""
        # Limpiar recomendaciones anteriores
        for widget in self.frame_recomendaciones.winfo_children():
            widget.destroy()
        
        # Obtener tareas ordenadas por prioridad
        tareas_ordenadas = sorted(self.sistema.lista_tareas, 
                                key=lambda x: (-x.urgencia, -x.prioridad))
        
        # Tomar las top 5 recomendaciones
        recomendaciones = tareas_ordenadas[:5]
        
        if not recomendaciones:
            label = tk.Label(self.frame_recomendaciones, 
                        text="No hay tareas pendientes\n¡Agrega algunas tareas!",
                        font=("Montserrat", 11), fg="#5F6368", bg='#F8F9FA',
                        justify=tk.CENTER)
            label.pack(pady=20)
            return
        
        for i, tarea in enumerate(recomendaciones, 1):
            self.crear_tarjeta_recomendacion(tarea, i)

    def crear_tarjeta_recomendacion(self, tarea, numero):
        """Crea una tarjeta de recomendación para el sidebar"""
        frame_tarjeta = tk.Frame(self.frame_recomendaciones, bg='white', 
                                relief='solid', borderwidth=1,
                                highlightbackground='#DADCE0')
        frame_tarjeta.pack(fill=tk.X, pady=5, padx=5)
        
        # Barra lateral de color
        frame_color = tk.Frame(frame_tarjeta, bg=tarea.obtener_color_prioridad(), width=5)
        frame_color.pack(side=tk.LEFT, fill=tk.Y)
        
        # Contenido de la tarjeta
        frame_contenido = tk.Frame(frame_tarjeta, bg='white', padx=10, pady=8)
        frame_contenido.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Número y nombre
        frame_header = tk.Frame(frame_contenido, bg='white')
        frame_header.pack(fill=tk.X)
        
        label_numero = tk.Label(frame_header, text=f"{numero}.", 
                            font=("Montserrat", 10, "bold"), bg='white', fg='#3C4043')
        label_numero.pack(side=tk.LEFT)
        
        label_nombre = tk.Label(frame_header, text=tarea.nombre, 
                            font=("Montserrat", 10, "bold"), bg='white', fg='#3C4043',
                            wraplength=200, justify=tk.LEFT)
        label_nombre.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Detalles
        frame_detalles = tk.Frame(frame_contenido, bg='white')
        frame_detalles.pack(fill=tk.X, pady=(5, 0))
        
        detalles_text = (f"📅 {tarea.fecha_entrega.strftime('%d/%m')} | "
                    f"⏱️ {tarea.duracion_minutos}min | "
                    f"⭐ {tarea.prioridad}/10 | "
                    f"🚨 {tarea.dias_restantes}d")
        
        label_detalles = tk.Label(frame_detalles, text=detalles_text,
                                font=("Montserrat", 8), bg='white', fg='#5F6368')
        label_detalles.pack(anchor='w')

class InterfazSistemaGestionTareas:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Sistema de Gestión de Tareas con Algoritmos")
        self.ventana_principal.geometry("1400x900")
        self.ventana_principal.configure(bg='white')
        
        self.centrar_ventana()
        
        self.sistema = SistemaGestionTareas()
        self.configurar_interfaz()
        
        # EJEMPLO
        self.tareas_ejemplo()
    
    def centrar_ventana(self):
        self.ventana_principal.update_idletasks()
        ancho = self.ventana_principal.winfo_width()
        alto = self.ventana_principal.winfo_height()
        x = (self.ventana_principal.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.ventana_principal.winfo_screenheight() // 2) - (alto // 2)
        self.ventana_principal.geometry(f'+{x}+{y}')
    
    def configurar_interfaz(self):
        # Frame principal con pestañas
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background='white')
        style.configure('TNotebook.Tab', font=('Montserrat', 10, 'bold'), padding=[15, 5])
        
        notebook = ttk.Notebook(self.ventana_principal)
        notebook.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        # Pestaña 1: Vista Diaria (NUEVA)
        self.frame_diario = tk.Frame(notebook, bg='white')
        notebook.add(self.frame_diario, text="Vista diaria")
        
        # Pestaña 2: Calendario
        self.frame_calendario = tk.Frame(notebook, bg='white')
        notebook.add(self.frame_calendario, text="Calendario mensual")
        
        # Pestaña 3: Gestión de Tareas
        self.frame_gestion = tk.Frame(notebook, bg='white')
        notebook.add(self.frame_gestion, text="+ Gestionar tareas")
        
        # Configurar todas las pestañas
        self.configurar_pestana_diaria()
        self.configurar_pestana_calendario()
        self.configurar_pestana_gestion()
    
    def configurar_pestana_diaria(self):
        """Configura la nueva pestaña de vista diaria"""
        self.vista_diaria = VistaDiaria(self.frame_diario, self.sistema)
    
    def configurar_pestana_calendario(self):
        """Configura la pestaña de calendario mensual"""
        self.calendario = CalendarioTareas(self.frame_calendario, self.sistema)
    
    def configurar_pestana_gestion(self):
        """Configura la pestaña de gestión de tareas"""
        # Frame principal con layout moderno
        frame_principal = tk.Frame(self.frame_gestion, bg='white')
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Título
        titulo = tk.Label(frame_principal, text="Gestión de Tareas", 
                         font=("Montserrat", 24, "bold"), bg='white', fg='#3C4043')
        titulo.pack(pady=(0, 20))
        
        # Dos columnas: formulario y lista
        frame_contenido = tk.Frame(frame_principal, bg='white')
        frame_contenido.pack(fill=tk.BOTH, expand=True)
        
        # Columna izquierda - Formulario
        frame_formulario = tk.Frame(frame_contenido, bg='white')
        frame_formulario.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 20))
        
        self.configurar_formulario_moderno(frame_formulario)
        
        # Columna derecha - Lista
        frame_lista = tk.Frame(frame_contenido, bg='white')
        frame_lista.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.configurar_lista_tareas_moderna(frame_lista)
    
    def configurar_formulario_moderno(self, parent):
        # Frame del formulario
        frame_form = tk.Frame(parent, bg='#F8F9FA', relief='solid', 
                             borderwidth=1, padx=20, pady=20)
        frame_form.pack(fill=tk.BOTH, pady=(0, 20))
        
        titulo_form = tk.Label(frame_form, text="Nueva Tarea", 
                              font=("Montserrat", 16, "bold"), bg='#F8F9FA', fg='#3C4043')
        titulo_form.pack(pady=(0, 20))
        
        # Campos del formulario
        campos = [
            ("Nombre de la tarea:", "entry_nombre", "entry"),
            ("Duración (minutos):", "spinbox_duracion", "spinbox"),
            ("Prioridad (1-10):", "spinbox_prioridad", "spinbox"),
            ("Fecha de entrega:", "frame_fecha", "fecha"),
            ("Tipo de tarea:", "combobox_tipo", "combobox"),
            ("Descripción:", "text_descripcion", "textarea")
        ]
        
        for i, (label_text, var_name, tipo) in enumerate(campos):
            frame_campo = tk.Frame(frame_form, bg='#F8F9FA')
            frame_campo.pack(fill=tk.X, pady=8)
            
            label = tk.Label(frame_campo, text=label_text, 
                           font=("Montserrat", 10), bg='#F8F9FA', fg='#5F6368')
            label.pack(anchor='w')
            
            if tipo == "entry":
                widget = tk.Entry(frame_campo, font=("Montserrat", 10), 
                                 relief='solid', borderwidth=1)
                widget.pack(fill=tk.X, pady=2)
                setattr(self, var_name, widget)
                
            elif tipo == "spinbox":
                valores = {"duracion": (15, 480, 15), "prioridad": (1, 10, 1)}
                min_val, max_val, inc_val = valores[var_name.split('_')[1]]
                widget = ttk.Spinbox(frame_campo, from_=min_val, to=max_val, 
                                   increment=inc_val, width=15)
                widget.set("60" if "duracion" in var_name else "5")
                widget.pack(anchor='w', pady=2)
                setattr(self, var_name, widget)
                
            elif tipo == "fecha":
                frame_fecha = tk.Frame(frame_campo, bg='#F8F9FA')
                frame_fecha.pack(anchor='w', pady=2)
                
                fecha_default = datetime.now() + timedelta(days=7)
                self.spinbox_dia = ttk.Spinbox(frame_fecha, from_=1, to=31, width=3)
                self.spinbox_dia.set(str(fecha_default.day))
                self.spinbox_dia.pack(side=tk.LEFT)
                
                tk.Label(frame_fecha, text="/", bg='#F8F9FA').pack(side=tk.LEFT)
                
                self.spinbox_mes = ttk.Spinbox(frame_fecha, from_=1, to=12, width=3)
                self.spinbox_mes.set(str(fecha_default.month))
                self.spinbox_mes.pack(side=tk.LEFT)
                
                tk.Label(frame_fecha, text="/", bg='#F8F9FA').pack(side=tk.LEFT)
                
                año_actual = datetime.now().year
                self.spinbox_año = ttk.Spinbox(frame_fecha, from_=año_actual, 
                                             to=año_actual+1, width=5)
                self.spinbox_año.set(str(fecha_default.year))
                self.spinbox_año.pack(side=tk.LEFT)
                
            elif tipo == "combobox":
                widget = ttk.Combobox(frame_campo, values=[
                    "estudio", "trabajo", "ejercicio", "personal", 
                    "organizacion", "creativo", "reunion", "urgente"
                ], width=18)
                widget.set("trabajo")
                widget.pack(anchor='w', pady=2)
                setattr(self, var_name, widget)
                
            elif tipo == "textarea":
                frame_text = tk.Frame(frame_campo, bg='#F8F9FA')
                frame_text.pack(fill=tk.X, pady=2)
                
                widget = tk.Text(frame_text, height=3, font=("Montserrat", 10),
                               relief='solid', borderwidth=1)
                widget.pack(fill=tk.X)
                setattr(self, var_name, widget)
        
        # Botón de agregar
        btn_agregar = tk.Button(frame_form, text="➕ Agregar Tarea", 
                               font=("Montserrat", 12, "bold"), bg='#34A853', fg='white',
                               relief='flat', padx=20, pady=10,
                               command=self.agregar_tarea)
        btn_agregar.pack(pady=20)
    
    def configurar_lista_tareas_moderna(self, parent):
        # Frame de la lista
        frame_lista = tk.Frame(parent, bg='white')
        frame_lista.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo_lista = tk.Label(frame_lista, text="Todas las Tareas", 
                               font=("Montserrat", 16, "bold"), bg='white', fg='#3C4043')
        titulo_lista.pack(pady=(0, 15))
        
        # Treeview
        frame_tree = tk.Frame(frame_lista, bg='white')
        frame_tree.pack(fill=tk.BOTH, expand=True)
        
        # Configurar estilo del treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", 
                       background="white", 
                       fieldbackground="white",
                       foreground="#3C4043",
                       rowheight=25)
        style.configure("Custom.Treeview.Heading", 
                       background="#F8F9FA",
                       foreground="#3C4043",
                       font=('Montserrat', 10, 'bold'))
        
        columnas = ("ID", "Nombre", "Duración", "Prioridad", "Urgencia", 
                   "Días", "Fecha", "Tipo", "Prioridad")
        
        self.treeview_tareas = ttk.Treeview(frame_tree, columns=columnas, 
                                          show="headings", style="Custom.Treeview",
                                          height=15)
        
        # Configurar columnas
        anchos = [40, 200, 70, 70, 70, 50, 90, 80, 100]
        for col, ancho in zip(columnas, anchos):
            self.treeview_tareas.heading(col, text=col)
            self.treeview_tareas.column(col, width=ancho)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_tree, orient=tk.VERTICAL, 
                                 command=self.treeview_tareas.yview)
        self.treeview_tareas.configure(yscrollcommand=scrollbar.set)
        
        self.treeview_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Botones de acción
        frame_botones = tk.Frame(frame_lista, bg='white')
        frame_botones.pack(fill=tk.X, pady=15)
        
        btn_eliminar = tk.Button(frame_botones, text="🗑️ Eliminar Seleccionada",
                               font=("Montserrat", 10), bg='#EA4335', fg='white',
                               relief='flat', padx=15, pady=8,
                               command=self.eliminar_tarea)
        btn_eliminar.pack(side=tk.LEFT, padx=5)
        
        btn_actualizar = tk.Button(frame_botones, text="🔄 Actualizar Vista",
                                 font=("Montserrat", 10), bg='#4285F4', fg='white',
                                 relief='flat', padx=15, pady=8,
                                 command=self.actualizar_vistas)
        btn_actualizar.pack(side=tk.LEFT, padx=5)
    
    def tareas_ejemplo(self):
        hoy = datetime.now()
        
        tareas_ejemplo = [
            # HACER YA (Alta prioridad + Urgencia) - HOY
            ("Entregar proyecto final", 180, 10, hoy, "trabajo", "Últimas correcciones antes de las 18:00"),
            ("Diapositivas expo", 120, 7, hoy, "reunion", "Preparar slides para junta directiva"),
            ("Pagar recibos de agua y luz", 5, 8, hoy, "personal", "Luz, agua e internet - EVITAR CORTES"),
            ("Hacer ejercicio", 30, 5, hoy, "ejercicio", "30 min cardio + estiramientos"),

            # PRÓXIMAS (Mañana)
            ("Estudiar para examen parcial", 120, 8, hoy + timedelta(days=1), "estudio", "Repasar capítulos 1-5"),
            ("Informe de avance mensual", 90, 7, hoy + timedelta(days=1), "trabajo", "Completar métricas del equipo"),
            
            # PUEDE ESPERAR (Próximos días)
            ("Limpiar y organizar oficina", 60, 5, hoy + timedelta(days=2), "organizacion", "Archivar documentos antiguos"),
            ("Hacer ejercicio cardiovascular", 45, 5, hoy + timedelta(days=2), "ejercicio", "30 min cardio + estiramientos"),
            
            # BAJA PRIORIDAD (Futuro)
            ("Organizar fotos digitales", 120, 3, hoy + timedelta(days=7), "personal", "Clasificar fotos de vacaciones"),
            ("Aprender nuevo software", 90, 2, hoy + timedelta(days=10), "estudio", "Tutoriales básicos"),
            
            # TAREAS REGULARES
            ("Hacer mercado semanal", 90, 4, hoy + timedelta(days=3), "personal", "Lista de supermercado"),
            ("Revisar correos pendientes", 45, 5, hoy + timedelta(days=1), "trabajo", "Responder mensajes importantes"),
        ]
        
        for tarea in tareas_ejemplo:
            self.sistema.agregar_tarea(*tarea)
        
        self.actualizar_vistas()
    
    def obtener_fecha_desde_controles(self) -> datetime:
        """Obtiene la fecha desde los controles de entrada"""
        try:
            dia = int(self.spinbox_dia.get())
            mes = int(self.spinbox_mes.get())
            año = int(self.spinbox_año.get())
            return datetime(año, mes, dia)
        except ValueError:
            messagebox.showerror("Error", "Fecha inválida")
            return datetime.now()
    
    def agregar_tarea(self):
        """Agrega una nueva tarea al sistema"""
        try:
            nombre = self.entry_nombre.get().strip()
            if not nombre:
                messagebox.showerror("Error", "El nombre de la tarea es obligatorio")
                return
            
            duracion = int(self.spinbox_duracion.get())
            prioridad = int(self.spinbox_prioridad.get())
            fecha_entrega = self.obtener_fecha_desde_controles()
            tipo = self.combobox_tipo.get()
            descripcion = self.text_descripcion.get("1.0", tk.END).strip()
            
            tarea = self.sistema.agregar_tarea(nombre, duracion, prioridad, fecha_entrega, tipo, descripcion)
            self.actualizar_vistas()
            
            # Limpiar campos
            self.entry_nombre.delete(0, tk.END)
            self.text_descripcion.delete("1.0", tk.END)
            
            messagebox.showinfo("Éxito", f"Tarea '{nombre}' agregada correctamente")
            
        except ValueError as e:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos para duración y prioridad")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    
    def eliminar_tarea(self):
        """Elimina la tarea seleccionada"""
        seleccion = self.treeview_tareas.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar")
            return
        
        item = seleccion[0]
        valores = self.treeview_tareas.item(item, 'values')
        id_tarea = int(valores[0])
        
        # Encontrar y eliminar la tarea
        for i, tarea in enumerate(self.sistema.lista_tareas):
            if tarea.id == id_tarea:
                del self.sistema.lista_tareas[i]
                break
        
        self.actualizar_vistas()
        messagebox.showinfo("Éxito", "Tarea eliminada correctamente")
    
    def actualizar_lista_tareas(self):
        """Actualiza la lista visual de tareas"""
        # Limpiar treeview
        for item in self.treeview_tareas.get_children():
            self.treeview_tareas.delete(item)
        
        # Agregar tareas
        for tarea in self.sistema.lista_tareas:
            self.treeview_tareas.insert("", tk.END, values=(
                tarea.id,
                tarea.nombre,
                f"{tarea.duracion_minutos} min",
                tarea.prioridad,
                f"{tarea.urgencia:.1f}",
                tarea.dias_restantes,
                tarea.fecha_entrega.strftime("%d/%m/%Y"),
                tarea.tipo,
                tarea.categoria_prioridad
            ))
    
    def actualizar_vistas(self):
        """Actualiza todas las vistas del sistema"""
        self.actualizar_lista_tareas()
        if hasattr(self, 'vista_diaria'):
            self.vista_diaria.actualizar_vista_diaria()
        if hasattr(self, 'calendario'):
            self.calendario.actualizar_calendario()

def main():
    root = tk.Tk()
    app = InterfazSistemaGestionTareas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
