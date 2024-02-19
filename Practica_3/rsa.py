from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Util import number

# Generación de llaves para Alice y Bob
bits = 1024

# Generación de primos y cálculo de n y phi para Alice (A) y Bob (B)
pA = number.getPrime(bits, randfunc=Random.get_random_bytes)
qA = number.getPrime(bits, randfunc=Random.get_random_bytes)
nA = pA * qA
phiA = (pA - 1) * (qA - 1)
e = 65537
dA = number.inverse(e, phiA)

pB = number.getPrime(bits, randfunc=Random.get_random_bytes)
qB = number.getPrime(bits, randfunc=Random.get_random_bytes)
nB = pB * qB
phiB = (pB - 1) * (qB - 1)
dB = number.inverse(e, phiB)

# Creación de las llaves RSA
keyA_private = RSA.construct((nA, e, dA))
keyA_public = keyA_private.publickey()
keyB_private = RSA.construct((nB, e, dB))
keyB_public = keyB_private.publickey()

# Mensaje a firmar
mensaje = "Hola mundo"
mensaje_bytes = mensaje.encode('utf-8')  # Convertir el mensaje a bytes

# Hash del mensaje
hash_mensaje = SHA256.new(mensaje_bytes)

# Firma del hash del mensaje con la llave privada de Alice
firma = pkcs1_15.new(keyA_private).sign(hash_mensaje)

# Verificación de la firma con la llave pública de Alice
try:
    pkcs1_15.new(keyA_public).verify(hash_mensaje, firma)
    verificacion = "La firma es válida."
except (ValueError, TypeError):
    verificacion = "La firma es inválida."

# Imprimir los resultados
print(verificacion)
print("Longitud del mensaje en bytes:", len(mensaje_bytes))