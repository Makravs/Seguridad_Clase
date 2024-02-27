from cryptography.fernet import Fernet

key_alice = Fernet.generate_key()
key_bob = Fernet.generate_key()
key_eve = Fernet.generate_key()

f_alice = Fernet(key_alice)
f_bob = Fernet(key_bob)
f_eve = Fernet(key_eve)

m_alice = b"Mensaje no.1"
m_c_alice = f_alice.encrypt(m_alice)

interceptado_eve = f_alice.decrypt(m_c_alice)
mensaje_m_eve = b"Mensaje Interceptado por Eve"
mensaje_re_cifrado= f_bob.encrypt(mensaje_m_eve)

mensaje_final = f_bob.decrypt(mensaje_re_cifrado)

print("Mensaje original:", m_alice.decode())
print("Mensaje interceptado", mensaje_m_eve.decode())
print("Mensaje modificado final por eve", mensaje_final.decode())