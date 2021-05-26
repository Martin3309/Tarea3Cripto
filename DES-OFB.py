from Crypto.Cipher import DES
from string import Template

#KEY = input('Ingrese la llave: \n')
#IV = input('Ingrese vector (iv): \n')

#Aqui se puede cambiar la llave (KEY), el vector (VI) y el mensaje en la variable plaintext.

KEY = '87654321'
IV = '13245678'
keyb = bytes(KEY, 'Utf-8')
text1 = bytes(IV, 'Utf-8')
a = DES.new(keyb, DES.MODE_OFB, text1)

plaintext = 'HOLAAAAAAAAA MUNDO'
text = bytes(plaintext, 'Utf-8')
#Cifrando el mensaje.
ciphertext = a.encrypt(text)
textocifrado = ciphertext.hex()
print(textocifrado)

#Pasar mensaje encriptado a HTML
f= open('mensaje.html','w')           #  Generando el archivo html.
mensaje = """<!DOCTYPE html>

<html dir="ltr" lang="en">
    <head>
    <meta charset="utf-8"/>
        <title>Mensaje Secreto</title>
        <div class=$DES_OFB id=$encrip></div><div class = $key id=$key1></div><div class=$VEC id=$vector></div>
        <p>$encrip</p>
    </head>
    <body>
        <p>Este sitio contiene un mensaje secreto</p>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js" integrity="sha512-nOQuvD9nKirvxDdvQ9OMqe2dgapbPB7vYAMrzJihw5m+aNcf0dX53m6YxM4LgA9u8e9eg9QX+/+mPu8kCNpV2A==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
        <script src="./DES-OFB.js"></script>
    </body>
</html>"""
insertar=Template(mensaje).safe_substitute(DES_OFB='algoritmo',encrip=textocifrado,key = 'key', key1 = KEY,VEC='vector', vector = IV)
f.write(insertar)
f.close()



#Desencriptar
#b= DES.new(keyb, DES.MODE_OFB, text1)
#print(b.decrypt(ciphertext).decode('Utf-8'))