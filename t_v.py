import pyttsx3

def texto_a_voz(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

# Diccionario de respuestas
respuestas = {
    "hola": "!Hola como estas?",
    "bien": "Me alegra oir eso.",
    "mal": "Lo siento, espero que te sientas bien.",
    "adios": "Adios! Que tengas un buen dia.",
    "que estas haciendo?": "Estoy aqui para ensenarte a programar. Seras el mejor.",
    "gracias": "De nada, estoy aqui para ayudarte."
}

# Bucle para interactuar con el chatbot
while True:
    entrada = input("tu: ").lower()
    if entrada in respuestas:
        respuesta = respuestas[entrada]
        print("bot: ", respuesta)
        texto_a_voz(respuesta)  # Convierte la respuesta a audio
    else:
        respuesta = "No lo entiendo."
        print("bot: ", respuesta)
        texto_a_voz(respuesta)  # Convierte a audio cuando no entiende
    
    if entrada == 'adios master':
        break
