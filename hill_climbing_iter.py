#TSP con Hill Climbing Iterativo
import math
import random

def distancia(coord1, coord2):
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

#Calcular la distancia correcta por una ruta
def evalua_ruta(ruta):
    total = 0
    for i in range(0, len(ruta) - 1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        total += distancia(coord[ciudad1], coord[ciudad2])
    ciudad1 = ruta[-1]  
    ciudad2 = ruta[0]
    total += distancia(coord[ciudad1], coord[ciudad2])
    return total

def i_hill_climbing():
     #Crear ruta inicial aleatoria
    ruta = list(coord.keys())
    mejor_ruta = ruta[:]
    max_iteraciones = 10

    while max_iteraciones > 0:
        mejora = False
        #Generar nueva ruta aleatoria
        random.shuffle(ruta)
        for i in range(0, len(ruta)):
            if mejora:
                break
            # Evitar permutaciones duplicadas
            for j in range(i + 1, len(ruta)):  
                ruta_tmp = ruta[:]
                # Realizar intercambio
                ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i] 
                dist = evalua_ruta(ruta_tmp)
                if dist < evalua_ruta(ruta):
                    mejora = True
                    ruta = ruta_tmp
                    break
        max_iteraciones -= 1  # Decrementar max_iteraciones

    return mejor_ruta

if __name__ == "__main__":
    coord = {
        'Jilotepec': (19.984146, -99.519127),
        'Toluca': (19.283389, -99.651294),
        'Atlacomulco': (19.797032, -99.875878),
        'Guadalajara': (20.666006, -103.343649),
        'Monterrey': (25.687299, -100.315655),
        'Cancun': (21.080865, -86.773482),
        'Morelia': (19.706167, -101.191413),
        'Aguascalientes': (21.861534, -102.321629),
        'Querétaro': (20.614858, -100.392965),
        'CDMX': (19.432361, -99.133111),
    }

    ruta = i_hill_climbing()
    print("Ruta óptima:", ruta)
    print("Distancia total:", evalua_ruta(ruta))
