#################LISTAS####################
###########################################

my_lista = ["Rojo", "Azul", "Amarillo", "Naranja", "Violeta", "Verde"] #se crea una lista de strings
#input()
print(my_lista) # Muestra la lista en pantalla
print(type(my_lista)) #Imprime el tipo de variable my_lista
print(my_lista[2]) #muestra lo que se encuentra en la posicion 2 de la lista

print("my_lista size: ", len(my_lista)) #muestra el tamaño de la lista
print(my_lista[0:2]) #muestra desde la posicion 0 hasta el 1, la posicion 2 se excluye
print(my_lista[:2]) # Muestra los elementos dwe la lista desde el indice 0 hasta el indice 2 excluido

my_lista.append('Blanco')      #Agrega elemento al final de la lista
print(my_lista) #muestra la lista actualizada

my_lista.insert(3, 'Negro') #agrega a la posicion 3 el color negro moviendo los siguientes 
print(my_lista) #muestra la lista

my_lista.extend(['Marron', 'Gris'])   #Concatena a otra lista
print(my_lista)# muestra la lista

print(my_lista.index('Azul')) #Muestra la posicion de la busqueda realizada en el argumento de la funcion

#my_lista.remove('Magenta') #elimina 
my_lista.remove('Marron') #elimina el index de la lista
print(my_lista)

my_lista.insert(8, 'Marron') #Vuelve a ingresar el index marron a la lista, esta vez en la posicion 8 de la misma   
print(my_lista) #muestra la lista

print(my_lista.pop()) #muestra el objeto que se encuentra al funal de la lista
size = len(my_lista) #se define la longitud de la lista en la variable size
print("size = ", size) #muestra el tamaño de la lista de otra manera
#print(my_lista.pop(size))

my_lista_3 = my_lista*3 #repite la lista 3 veces guardandola en la variable my_lista_3
print("my_lista_3: ", my_lista_3) #muestra la nueva lista

print("Sort: ") #imprime la palabra short
print() #imprime una linea vacia
my_listaSort = my_lista.sort() #Organiza la lista de manera ascendente y no devuelve nada o "none"
print(my_listaSort) # imprime none

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1] #Crea una lista numerica
print("Ordering my_NumList: ") #imprime un mensaje  
my_NumList.sort() #ordena la lista
print(my_NumList) #muestra la lista ordenada de manera ascendente
#OrderedLList = my_NumList.sort()
#print(my_listaSort)

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True) #el argumento "reverse = true" organiza la lista de manera descendente
print("De menor a mayor: ", my_NumList) #imprime en pantalla la lista reordenada



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################") #Muestra como mensaje ###########################
print("###########################") #Muestra como mensaje ###########################
print("###########################") #Muestra como mensaje ###########################
print("############TUPLAS#########") #Muestra como mensaje ############TUPLAS#########
my_tupla = tuple(my_lista) #convierte la lista en una tupla
print() #imprime una linea vacia
print() #imprime una linea vacia
print("my_tuple: ", my_tupla) #muestra la tupla

print(my_tupla[0]) #muestra la posicion 0 de la tupla
print(my_tupla[2]) #muestra la posicion 2 de la tupla


print('Rojo' in my_tupla) #Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print(my_tupla.count('Rojo')) #evalua cuantos elementos coinciden con el argumento

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria) #muestra el contenido de la tupla

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla) #imprime la tupla


nombre, dia, mes, año = my_tupla #Desempaquetado de tupla, se guardan los valores en orden de las variables
print(nombre) #imprime lo que este almacenado en la variable
print(dia) #imprime lo que este almacenado en la variable
print(mes) #imprime lo que este almacenado en la variable
print(año) #imprime lo que este almacenado en la variable

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año) #imprime un mensaje seguido de un elemento almacenado en cada una de las variables (Ejemplo: "Nombre: ", 'Daniel'; siendo Daniel el elemento almacenado en "nombre")


my_lista2=list(my_tupla) #Convertir una tupla en una lista
print(my_lista2) #imprime la lista proveniente de la tupla