#ejemplo chatbot con listas basico
import random

#listas de saludos y respuestas
saludos=["como te llamas","que tal","buenos dias","buenas tardes","buenas noches","hola"]
respuesta=["hola, como estas?",
            "me llamo chato",
            "hola como te va",
            "que hay?"
]



despedida=["adios","bye","gracias","nos vemos","hasta luego"]
respuesta_despedida=[
    "adios,hasta pronto",
    "fue un placer ayudarte",
    "cuidate",
    "nos vemos luego",
    "bye",
]

preguntas=["que vamos a comer hoy ","que cenamos","a ti que te gustaria?","buenas tardes","buenas noches"]
respuesta_comida=[
            "pollo con mole?",
            "pizza",
            "hamburguesas",
            "comida china?"
]

#mensaje de bienvenida del chatbot
print("hola soy Chato, tu chatbot de confianza, si deseas"
      "terminar recibe 'salir'")

while True:
    usuario=input("Tu:").lower().strip()

    if usuario in saludos:
       print("chatbot:",random.choice(respuesta))

    elif usuario in preguntas:
        print("chatbot:",random.choice(respuesta_comida))

    elif usuario in despedida:
        print("chatbot:", random.choice(respuesta_despedida))
        break


