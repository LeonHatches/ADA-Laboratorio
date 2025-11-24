from graph import GraphLink

def get_graph():
    g = GraphLink()

    nodes = [
        "Fabrica_ParqueIndustrial",
        "Uchumayo",
        "Tiabaya",
        "Sachaca",
        "Yanahuara",
        "Arequipa_Centro",
        "Av_Independencia",
        "Miraflores",
        "Alto_Selva_Alegre",
        "Cayma_Chilina",
        "Cayma_Plaza",
        "Zamacola",
        "Cerro_Colorado",
        "Ciudad_Municipal",
        "Socabaya",
        "Hunter",
        "Paucarpata",
        "Sabandia",
        "Characato",
        "Chiguata"
    ]

    for n in nodes:
        g.insert_vertex(n)

    edges = [
        # Salida del Parque Industrial
        ("Fabrica_ParqueIndustrial", "Uchumayo", 6),
        ("Fabrica_ParqueIndustrial", "Socabaya", 7),

        # Zona oeste / camino hacia Sachaca / Tiabaya
        ("Uchumayo", "Tiabaya", 5),
        ("Tiabaya", "Sachaca", 4),
        ("Sachaca", "Yanahuara", 6),
        ("Yanahuara", "Arequipa_Centro", 4),

        # Zona norte
        ("Uchumayo", "Zamacola", 9),
        ("Zamacola", "Cerro_Colorado", 4),
        ("Cerro_Colorado", "Ciudad_Municipal", 3),

        # Zona este - centro
        ("Arequipa_Centro", "Miraflores", 3),
        ("Miraflores", "Alto_Selva_Alegre", 4),
        ("Alto_Selva_Alegre", "Cayma_Chilina", 5),
        ("Cayma_Chilina", "Cayma_Plaza", 2),

        # Zona sur / Paucarpata - Sabandia - Characato
        ("Arequipa_Centro", "Paucarpata", 7),
        ("Paucarpata", "Sabandia", 5),
        ("Sabandia", "Characato", 6),
        ("Characato", "Chiguata", 12),

        # Conexiones urbanas y de retorno
        ("Socabaya", "Hunter", 3),
        ("Hunter", "Av_Independencia", 4),
        ("Av_Independencia", "Arequipa_Centro", 2),

        # Conexiones transversales
        ("Ciudad_Municipal", "Cayma_Plaza", 6),
        ("Cayma_Plaza", "Yanahuara", 3),

        # Conexiones adicionales para conectar zonas remotas
        ("Cerro_Colorado", "Paucarpata", 9),
        ("Socabaya", "Paucarpata", 8)
    ]

    for a, b, w in edges:
        g.insert_edge(a, b, w)

    return g



def get_posiciones():
    pos = {
        "Fabrica_ParqueIndustrial": (2.0, -4.0),
        "Uchumayo": (0.0, -2.0),
        "Tiabaya": (-1.0, -1.0),
        "Sachaca": (-1.0, 0.5),
        "Yanahuara": (-0.5, 2.2),
        "Arequipa_Centro": (0.2, 3.0),
        "Av_Independencia": (0.5, 2.0),
        "Miraflores": (1.2, 4.2),
        "Alto_Selva_Alegre": (1.6, 5.0),
        "Cayma_Chilina": (0.5, 5.2),
        "Cayma_Plaza": (-0.2, 4.8),
        "Zamacola": (-2.0, 3.0),
        "Cerro_Colorado": (-2.3, 4.0),
        "Ciudad_Municipal": (-1.5, 5.0),
        "Socabaya": (2.5, -1.0),
        "Hunter": (2.4, 0.5),
        "Paucarpata": (3.0, 2.0),
        "Sabandia": (4.0, 1.0),
        "Characato": (5.0, 1.0),
        "Chiguata": (6.0, 2.5)
    }
    return pos

