# utils.py
import pyttsx3
import spacy  # Importa spaCy para procesamiento de lenguaje natural


machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()


# Intenta cargar el modelo de lenguaje de spaCy
try:
    nlp = spacy.load("en_core_web_sm")
except OSError as e:
    print(f"Error al cargar el modelo: {e}")
    exit()  # Sale del programa si no se puede cargar el modelo

def process_command(text): # esta funcion se encarga de procesar y entender el texto pasado como parametro
    """Procesa el texto usando spaCy para extraer entidades y verbos importantes."""
    doc = nlp(text)  # Procesa el texto usando spaCy
    command_data = {
        "commands": [],
        "entities": []
    }
    
    # Extrae verbos (acciones) y entidades (personas, organizaciones, etc.)
    for token in doc:
        if token.pos_ == "VERB":  # Busca los verbos (como 'reproduce')
            command_data["commands"].append(token.text)
        if token.ent_type_:  # Busca entidades como nombres de canciones, fechas, etc.
            command_data["entities"].append(token.text)

    return command_data