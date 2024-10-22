import speech_recognition as sr  # Importa el módulo para el reconocimiento de voz.
import pyttsx3  # Importa el módulo para convertir texto a voz.
from utils.utils import talk, process_command  # Importa talk y process_comand desde utils.py.
from config.config import ASSISTANT_NAME  # Importa el nombre del asistente desde config

# Inicializa el reconocimiento de voz y el motor de texto a voz.
listener = sr.Recognizer()
machine = pyttsx3.init()

# Configuración de la voz del asistente.
voices = machine.getProperty('voices')  # Obtiene las voces disponibles en el sistema.
machine.setProperty('voice', voices[0].id)  # Cambia a la primera voz disponible (generalmente masculina).
machine.setProperty('rate', 150)  # Ajusta la velocidad del habla a 150 palabras por minuto.

def input_instruction():
    """Función para escuchar la instrucción de voz del usuario y convertirla a texto."""
    try:
        with sr.Microphone() as source:  # Usa el micrófono como fuente de entrada.
            print("Escuchando...")  # Muestra un mensaje cuando el asistente está escuchando.
            audio = listener.listen(source, phrase_time_limit=10)  # Escucha durante 5 segundos.
            text = listener.recognize_google(audio, language='es-MX')  # Convierte el audio a texto.
            text = text.lower()  # Convierte el texto a minúsculas para facilitar la comparación.

            if ASSISTANT_NAME in text:  # Verifica si el nombre del asistente está en el texto.
                print(text) 
                return text  # Retorna el texto si contiene el nombre del asistente.
            else:
                return None  # Retorna None si no se menciona al asistente.

    except sr.UnknownValueError:
        # Maneja el caso cuando no se entiende el audio.
        print("No se entendió lo que dijiste.")
        return None
    except sr.RequestError as e:
        # Maneja errores relacionados con el servicio de reconocimiento de voz.
        print(f"Error al acceder al servicio de reconocimiento: {e}")
        return None


def run_assistant():
    from functions import play_youtube_song, search_module # importa funciones de busqueda
    from functions import date_module # importa funciones de tiempo

    #Función principal que ejecuta las acciones del asistente según los comandos de voz
    text = input_instruction()  # Llama a la función para escuchar y convertir la instrucción a texto.
    if text:
        processed_data = process_command(text)
        if 'dame la' in text:  # Si el comando contiene 'hora', informa la hora actual.
            date_module(text) # llama la funcion y devuelve la hora
        elif 'reproduce' in processed_data["commands"] and processed_data["entities"]:
            # Llama a la función para reproducir video en YouTube si contiene 'reproduce' y una entidad (canción).
            song = " ".join(processed_data["entities"])
            play_youtube_song(f'reproduce {song}')
        elif "busca en" in text:
            search_module(text)
        else:
            talk("No entendí el comando.")  # Si no reconoce el comando, informa que no lo entendió.
    else:
        talk("No mencionaste el nombre del asistente.")  # Si no se mencionó el nombre del asistente, lo indica.

# Bucle infinito que mantiene el asistente activo.
while True:
    run_assistant()  # Ejecuta continuamente la función del asistente.
