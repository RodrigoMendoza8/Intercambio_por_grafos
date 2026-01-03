import networkx as nx
import random

# ------------------- DATOS -------------------
mendonza = ['Letos','Norbert','Rodrigo','Karla']
chavos = ['Alberto','Lucy']
vidal = ['Conrado','Gina','Jesus']
boston = ['Lupis','Mau','Oscar']
chilangos = ['Carmen','Gaby','Javier']
familia = mendonza + chavos + vidal + boston + chilangos
familias = [mendonza, chavos, vidal, boston, chilangos]

# ------------------- GRAFO -------------------
G = nx.Graph()
G.add_nodes_from(familia)

# Agregar aristas entre familias diferentes
for i in range(len(familias)):
    for j in range(i + 1, len(familias)):
        for persona1 in familias[i]:
            for persona2 in familias[j]:
                G.add_edge(persona1, persona2)

# ------------------- FUNCIÓN DE GENERACIÓN -------------------
def generar_intercambio(G, familia, max_intentos=1000):
    for intento in range(max_intentos):
        disponibles_para_dar = familia.copy()
        asignaciones = {}
        ya_recibieron = set()
        try:
            while disponibles_para_dar:
                persona1 = random.choice(disponibles_para_dar)
                vecinos_validos = [v for v in G.neighbors(persona1) if v not in ya_recibieron]
                if not vecinos_validos:
                    raise ValueError(f"No hay a quién regalar para {persona1}")
                persona2 = random.choice(vecinos_validos)
                asignaciones[persona1] = persona2
                ya_recibieron.add(persona2)
                disponibles_para_dar.remove(persona1)
            return asignaciones
        except ValueError:
            continue
    raise RuntimeError("No se pudo generar una rifa válida en los intentos dados.")

# ------------------- PRUEBAS AUTOMÁTICAS -------------------
num_pruebas = 1000
errores = 0

for i in range(num_pruebas):
    try:
        asignaciones = generar_intercambio(G, familia)
        
        # Validaciones
        assert len(asignaciones) == len(familia), "Alguien se quedó sin asignación."
        assert len(set(asignaciones.values())) == len(familia), "Alguien recibe doble regalo."
        
        # Nadie regala dentro de su propia familia
        for f in familias:
            for persona in f:
                if asignaciones[persona] in f:
                    raise AssertionError(f"{persona} le regaló a alguien de su familia ({asignaciones[persona]})")
                    
    except Exception as e:
        errores += 1
        print(f"❌ Error en la iteración {i+1}: {e}")

print("\n✅ Pruebas completadas.")
print(f"Total de pruebas: {num_pruebas}")
print(f"Errores encontrados: {errores}")
if errores == 0:
    print("🎉 Todo perfecto. Ningún caso falló.")
else:
    print("⚠️ Hubo fallos, revisa los casos impresos arriba.")
