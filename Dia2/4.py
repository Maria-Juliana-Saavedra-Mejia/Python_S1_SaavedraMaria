## Password generator

def password (n):
    
    import secrets
    import string
    string.ascii_letters
    string.digits
    string.punctuation
    clave= string.ascii_letters + string.digits + string.punctuation
    passr="".join(secrets.choice(clave)for i in range (1,8+n))
    return passr 

n=int(input("Digite la cantidad de caracteres extras de la contraseña():" ))

print ("Su clave es : ", password(n))


##Desarollado por Maria Juliana Saavedra Mejia / T.I 1097100816