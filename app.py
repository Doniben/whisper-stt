import whisper
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Función para guardar el output en un archivo txt
def guardar_output(texto, nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        archivo.write(texto)

# Función para enviar un correo electrónico
def enviar_correo(desde, para, asunto, cuerpo, servidor_smtp, puerto_smtp, usuario_smtp, contrasena_smtp):
    mensaje = MIMEMultipart()
    mensaje["From"] = desde
    mensaje["To"] = para
    mensaje["Subject"] = asunto
    mensaje.attach(MIMEText(cuerpo, "plain"))

    try:
        servidor = smtplib.SMTP(servidor_smtp + ": " + str(puerto_smtp))
        servidor.starttls()
        servidor.login(usuario_smtp, contrasena_smtp)
        servidor.sendmail(mensaje)
        servidor.quit()
        print("Correo enviado correctamente.")
    except Exception as e:
        print("Error al enviar el correo:", str(e))

def transcribir_archivos(archivos):
    model = whisper.load_model("large")

    for archivo in archivos:
        result = model.transcribe(archivo)
        texto_transcrito = result["text"]
        print(texto_transcrito)

        # Guardar el output en un archivo txt
        nombre_archivo_output = archivo.split(".")[0] + ".txt"
        guardar_output(texto_transcrito, nombre_archivo_output)

        # Enviar correo electrónico
        enviar_correo("doniben6@gmail.com", "tao_toons@yahoo.es", "Transcripción de audio " + nombre_archivo_output, texto_transcrito,
                      "smtp.gmail.com", 587, "doniben6@gmail.com", "kmzwa8awaaaAAA")

# Agregar varios archivos a una lista
archivos_audio = ["Asley0507.m4a"]  # Agregar más archivos según sea necesario

# Llamar a la función para transcribir los archivos
transcribir_archivos(archivos_audio)
