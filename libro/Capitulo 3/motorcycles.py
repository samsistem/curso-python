"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' # Cambia el valor de la primera posición de la lista
print(motorcycles) 

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati') # Añade un valor al final de la lista
print(motorcycles)

entrada_usuario = input("Introduce una moto: ")
motorcycles.append(entrada_usuario) # Añade un valor al final de la lista
print(motorcycles)

motorcycles = [] # Crea una lista vacía
question = input("dime una marca de moto: ")
motorcycles.append(question) # Añade un valor al final de la lista con el input del usuario.
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(4, 'ducati') # Añade un valor en la posición 0 de la lista
print(motorcycles)
"""
mortorcycles = ['honda', 'yamaha', 'suzuki']
print(mortorcycles)

del mortorcycles[2] # Elimina el valor de la posición 2 de la lista
print(mortorcycles)

mortorcycles = ['honda', 'yamaha', 'suzuki']
print(mortorcycles)

popped_motorcycle = mortorcycles.pop() # Elimina el último valor de la lista
print(mortorcycles)

print(popped_motorcycle)

mortorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = mortorcycles.pop() # Elimina el último valor de la lista
print(f"The last motorcycle I owned was a {last_owned.title()}.")  # Imprime el valor eliminado

mortorcycles = ['honda', 'yamaha', 'suzuki']
print(mortorcycles)

remove_items = input("Introduce una moto a eliminar: ")
mortorcycles.remove(remove_items) # Elimina el valor 'yamaha' de la lista segun el input del usuario
print(mortorcycles)
