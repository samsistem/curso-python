my_string = "Mi string"
my_other_string = 'Mi otro string'

print (len(my_string))
print (len(my_other_string))

print (len(my_string) + len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string =" Este es un string \n con salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string ="\\tEste es un String \n escapado"
print(my_scape_string)

my_scape_string ="\\tEste es un String \\n escapado"
print(my_scape_string)

#formateo de strings

name, surname, age = "Juan", "Perez", 25
print("Mi nombre es {}{} y tengo {} años".format(name, surname, age))#si queremos formatear datos
print("Mi nombre es %s %s y tengo %s años" % (name, surname, age))
print(f"Mi nombre es {name} {surname} y tengo {age} años")#manera estandar

#desempaquetado de strings

language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

#reverse

reversed_language = language[::-1]
print(reversed_language)

#Funciones

print(language.capitalize())#primera letra en mayuscula
print(language.upper())#todas las letras en mayuscula
print(language.lower())#todas las letras en minuscula
print(language.count("t"))#cuenta cuantas veces aparece la letra t
print("1".isnumeric())#devuelve si es numerico
print(language.lower().isupper())#devuelve si es mayuscula
print(language.startswith("Py"))#devuelve si empieza con Py




