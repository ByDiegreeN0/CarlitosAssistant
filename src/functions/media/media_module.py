import pywhatkit
from utils.utils import talk  # Importa talk desde utils.py.
from config.config import ASSISTANT_NAME  # Importa el nombre del asistente desde config
import webbrowser # modulo para buscar en google
import spacy  # Importa spaCy para procesamiento de lenguaje natural

# Carga el modelo de lenguaje de spaCy
nlp = spacy.load("es_core_news_sm")  

def play_youtube_song(text):
    # Procesa el texto usando spaCy
    doc = nlp(text)
    
    # Filtrar las palabras clave que no queremos en el nombre de la canción
    keywords = {ASSISTANT_NAME.lower(), "reproduce"}
    
    # Extraer el nombre de la canción omitiendo las palabras clave
    song = " ".join([token.text for token in doc if token.text.lower() not in keywords]).strip()

    if song:  # Asegúrate de que haya una canción en el texto.
        talk(f'Reproduciendo {song}')  # Informa al usuario qué canción va a reproducir.
        pywhatkit.playonyt(song)  # Usa pywhatkit para reproducir la canción en YouTube.
    else:
        talk("No mencionaste ninguna canción para reproducir.")  # Responde si no se detecta el nombre de la canción.
        
        
def search_on_google(text):
    doc = nlp(text)

    # Define las palabras clave a eliminar
    keywords = {ASSISTANT_NAME.lower(), "busca en google"}

    # Extrae el término de búsqueda eliminando las palabras clave
    search_term = " ".join([token.text for token in doc if token.text.lower() not in keywords]).strip()
    
    if search_term:  # Verifica si hay un término de búsqueda
        talk(f"Buscando '{search_term}' en Google...")  # Informa al usuario que está buscando.
        webbrowser.open(f"https://www.google.com/search?q={search_term}")  # Abre la página web con la búsqueda.
    else:
        talk("No mencionaste ningún término para buscar.")  # Informa al usuario si no se encontró un término válido.

