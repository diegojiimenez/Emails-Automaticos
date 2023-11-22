import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_correo(destinatario, asunto, mensaje):
    # Configuración del servidor de correo
    servidor_correo = 'smtp.tu_servidor_de_correo.com'
    puerto = 587
    usuario_correo = 'tu_correo@gmail.com'
    contraseña_correo = 'tu_contraseña'

    # Crear objeto de mensaje
    msg = MIMEMultipart()
    msg['From'] = usuario_correo
    msg['To'] = destinatario
    msg['Subject'] = asunto

    # Agregar cuerpo del mensaje
    msg.attach(MIMEText(mensaje, 'plain'))

    # Iniciar conexión con el servidor de correo
    with smtplib.SMTP(servidor_correo, puerto) as server:
        server.starttls()
        server.login(usuario_correo, contraseña_correo)

        # Enviar correo
        server.send_message(msg)

# Función para obtener las fechas deseadas del usuario
def obtener_fechas_deseadas():
    fechas_deseadas = {}

    while True:
        nombre = input("Ingresa el nombre de la persona (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break

        fecha = input(f"Ingrese la fecha de cumpleaños de {nombre} (YYYY-MM-DD): ")
        fecha_obj = datetime.datetime.strptime(fecha, '%Y-%m-%d').date()

        fechas_deseadas[nombre] = fecha_obj

    return fechas_deseadas

# Llamar a la función para obtener fechas deseadas del usuario
cumpleanios_deseados = obtener_fechas_deseadas()

# Función para enviar correos en fechas específicas
def enviar_correos_programados():
    # Obtener la fecha actual
    fecha_actual = datetime.date.today()

    for persona, fecha_cumpleanios in cumpleanios_deseados.items():
        # Verificar si es la fecha deseada para enviar el correo
        if fecha_actual.month == fecha_cumpleanios.month and fecha_actual.day == fecha_cumpleanios.day:
            asunto = f'¡Feliz cumpleaños, {persona}!'
            mensaje = f'Hoy es la fecha especial para {persona}. ¡Envía tus mejores deseos!'

            # Cambiar el destinatario al correo de la persona
            destinatario = 'correo_de_la_persona@gmail.com'

            # Llamar a la función para enviar el correo
            enviar_correo(destinatario, asunto, mensaje)

# Llamar a la función para enviar correos programados
enviar_correos_programados()
