name = "sam"
surname = "sistem"

fullname = (f"\t{name} {surname}\n Sam Sistem") #tabulador y salto de linea
print(fullname.title())#imprime la primera letra en mayuscula
print(fullname.upper())#imprime todo en mayuscula
print(fullname.lower())#imprime todo en minuscula
print("lenguajes:\n\tpython\n\tc\n\tjavaScript")#salto de linea y tabulador
print("lenguajes:\n\tpython\n\tc\n\tjavaScript".title())#imprime la primera letra en mayuscula
favorite_language = "python "
favorite_language.rstrip()#elimina el espacio en blanco una vez
print(favorite_language)
favorite_language = " python "
favorite_language.lstrip()#elimina el espacio en blanco izquierdo
favorite_language = favorite_language.rstrip()#elimina el espacio en blanco derecho
favorite_language.strip()#elimina el espacio en blanco de ambos lados

#Eliminar prefijo https de una url
nostarch_url = 'https://nostrach.com'
nostarch_url.removeprefix('https://')
print(nostarch_url)