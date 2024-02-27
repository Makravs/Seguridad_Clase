from cryptography.fernet import Fernet

#propio
key = Fernet.generate_key()
print("llave",key)
f = Fernet(key)
token = f.encrypt(b"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
print ("token", token)

#compañero
d= Fernet(b'xqk2t7om_UeIkryuFxwzJAyLHMjbjKFwVPrLRz_0AWs=')
print("resultado",d.decrypt(b'gAAAAABluw2oenyRLxrbgD-CpuPngKzI1p9D9nG9NDEmgPlmsb5e2xG8gI_4v4rogR881xVqvY9_UC8r-bxLyqNHM8PYI66SeA=='))
      
