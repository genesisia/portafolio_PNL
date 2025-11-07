from textblob import TextBlob
import random
from deep_translator import GoogleTranslator

usuario=["hola",
         "hola chat",
         "buen dia",]

preguntas=["como te sientes hoy?",
           "que tal estas hoy?",
           "como vas el dia de hoy?",]
respuestas=["me siento triste",
            "me siento feliz",
            "me siento enojado",
            "estoy normal"]
positivo=["que bien que te sientas bien el dia de hoy",
          "que bien que te sientas feliz el dia de hoy"]
negativo=["lamento que te sientas triste hoy",
          "lamento mucho lo que sientes mis mejores deseos"]
neutro=["okey escelente",
        "bien echale ganas"]
while True:
    texto = input("Ingresa una texto: ")
    ingles = GoogleTranslator(source='es', target='en').translate(texto)
    analizar = TextBlob(ingles)
    sentimiento = analizar.sentiment.polarity

    if texto in usuario:
        print("Chatbot: ",random.choice(preguntas))
    if texto in respuestas:
        if sentimiento >= 0.5:
            print(random.choice(positivo))
        if sentimiento ==0:
            print(random.choice(neutro))
        if sentimiento <0:
            print(random.choice(negativo))