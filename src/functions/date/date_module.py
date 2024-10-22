from datetime import datetime
from utils.utils import talk

def get_current_fulldate(text):
    if 'fecha' in text and 'hora' in text:
        current_datetime = datetime.now().strftime('%d de %B de %Y, %H:%M') 
        talk(f'La fecha y hora actual son {current_datetime}')  

def get_current_hour(text):
    if 'hora' in text:  # Si el comando contiene 'hora', informa la hora actual.
        time = datetime.now().strftime('%H:%M')  # Obtiene la hora actual en formato HH:MM.
        talk(f'Son las {time}')  # Usa la función talk para decir la hora.

def get_current_date(text):
    if 'fecha' in text:  # Si el comando contiene 'fecha'
        fecha = datetime.today().strftime('%d de %B de %Y')  # Formato: "día de mes de año"
        talk(f'hoy es {fecha}')  # Usa la función talk para decir la fecha.

def  date_module(text):
    if 'fecha' in text or 'hora' in text:
        if 'fecha' in text and 'hora' in text:
            get_current_fulldate(text)
        elif 'hora' in text:
            get_current_hour(text)
        elif 'fecha' in text:
            get_current_date(text)