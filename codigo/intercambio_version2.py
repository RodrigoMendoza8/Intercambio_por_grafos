import networkx as nx
import random
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

correos = {
    'Letos': 'xxxx@hotmail.com',
    'Norbert': 'xxxx@hotmail.com',
    'Rodrigo': 'xxxxx@hotmail.com',
    'Karla': 'xxxx@gmail.com',
    'Alberto': 'xxxx@hotmail.com',
    'Lucy': 'xxxx@gmail.com',
    'Conrado': 'xxx@gmail.com',
    'Gina': 'xxxx@hotmail.com',
    'Jesus': 'xxxx@hotmail.com',
    'Lupis': 'xxxx@hotmail.com',
    'Mau': 'xxxx@gmail.com',
    'Carmen': 'xxxx@gmail.com',
    'Gaby': 'xxxx@gmail.com',
    'Javier': 'xxxx@hotmail.com',
    'Oscar': 'xxxx@gmail.com'
}

mendonza = ['Letos','Norbert','Rodrigo','Karla']
chavos = ['Alberto','Lucy']
vidal = ['Conrado','Gina','Jesus']
boston = ['Lupis','Mau','Oscar']
chilangos = ['Carmen','Gaby','Javier']
familia = mendonza + chavos + vidal + boston + chilangos
familias = [mendonza, chavos, vidal, boston, chilangos]

G = nx.Graph()
G.add_nodes_from(familia)

for i in range(len(familias)):
    for j in range(i + 1, len(familias)):
        for persona1 in familias[i]:
            for persona2 in familias[j]:
                G.add_edge(persona1, persona2)

adjM = nx.adjacency_matrix(G)
adjM = adjM.todense()

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

asignaciones = generar_intercambio(G, familia)
assert len(asignaciones) == len(familia), "Alguien se quedó sin asignación."
assert len(set(asignaciones.values())) == len(familia), "Alguien recibe doble regalo."


lista_de_intercambios = open("lista_de_intercambios.txt", "w")

print("🎁 Resultados del intercambio:\n")
for quien, a_quien in asignaciones.items():
    lista_de_intercambios.write((f"{quien} le regala a {a_quien} \n"))


print("Personas en el grafo:", len(G.nodes))
print("Personas en la lista:", len(familia))

'''
load_dotenv()

password = os.getenv('PASSWORD')
email_sender = 'xxxx@gmail.com'  

for quien, a_quien in asignaciones.items():
    email_reciver = correos.get(quien)
    if email_reciver is None:
        print(f"No hay correo registrado para {quien}")
        continue

    subject = '🎁 Intercambio diciembre'
    body = f"""
Hola {quien},

Este es tu resultado del intercambio:
🎅 Tú le vas a regalar a: {a_quien}

¡Rifate con un buen regalo!

Saludos,
Rorrito
"""

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, email_reciver, em.as_string())
        print(f"📧 Correo enviado a {quien} ({email_reciver})")
'''