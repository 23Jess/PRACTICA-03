#1. Crea un programa en Python que simule una lista de compras. El programa 
#debe permitir al usuario agregar productos al final de la lista, eliminar 
#productos del inicio de la lista y mostrar todos los productos en la lista en 
#orden de compra.
 
#creamos una lista vacia
lista_articulos = list()
 
#funcion para agregar articulos a nuestra lista
def agregar_producto():
	print("Lista de compras")
	articulos = input("Agrega tu producto: ")
	#Utilizamos string.capitaliza() para convertir nuestra primera letra en mayuscula
	lista_articulos.append(articulos.capitalize())
	print("Articulo agregados")
 
#Funcion para borrar elementos de nuestra lista
def borrar_producto():
	articulo = input("Producto a eliminar: ")
	#Agregamos de nuevo string.capitaliza()para que python no marque error
	lista_articulos.remove(articulo.capitalize())
	print("El articulo se ha borrado con exito!")
 
 
#Funcion para imprimir los artculos de nuestra lista
def ver_lista():
	#muestra los articulos en forma de lista de python
	#print(lista_articulos)
	print("Articulos en tu lista")
	for articulos in lista_articulos:
		print(articulos)
	print()
 
 
while  True:
	try:
		print("Menú de opciones")
		print ("1. Agregar producto al inicio")
		print ("2. Eliminar el primer producto")
		print ("3. Ver lista de productos")
		print ("4. Salir")
 
		opcion = int(input("Que deseas hacer: "))
	except ValueError:
		print("Favor de ingresar una opcion valida")
	else:
		#si no es ninguna de las 4 opciones validas
		if opcion < 0 or opcion > 4:
				print ("Opcion no válida")
				continue
		if opcion == 1:
			agregar_producto()
		elif opcion == 2:
			borrar_producto()
		elif opcion == 3:
			ver_lista()
		else:
			break
print("Fin")