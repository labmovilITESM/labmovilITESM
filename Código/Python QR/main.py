# Primero instalamos esta librería en la terminal con el comando
# pip install qrcode
import qrcode

# En esta variable vamos a poner la liga a la que queremos que
# nuestro código qr nos mande
url = "https://github.com/labmovilITESM/labmovilITESM#pr%C3%A1cticas-%EF%B8%8F"

# Generar el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Crear una imagen del código QR
imagen_qr = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen del código QR. se puede guargar en cualquier folder,
# pero debemos especificar cual desde el disco duro
imagen_qr.save("qr/practicas.png")
