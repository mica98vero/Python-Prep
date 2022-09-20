#Creo un diccionario:
mi_diccionario = { 'Colores Primarios': ['Rojo', 'Azul','Amarillo'],
                   'Colores secundarios': ['Naranja','Violeta','Verde'],
                   'Clave3': 10,
                   'Clave4': False}

#imprimir un diccionario
print(mi_diccionario)

#Imprimir un valor a través de su clave 
print(mi_diccionario['Colores secundarios'])

#Agregar un valor
mi_diccionario['Clave5']='Otro ejemplo'

#Cambiar un valor
mi_diccionario['Clave3']=2

#Eliminar un elemento a través de su clave.
del mi_diccionario['Clave4']
print(mi_diccionario)

#Utilizar una tupla como clave de un diccionario.
mi_tupla=('Argentina','Italia','Inglaterra')
mi_diccionario={mi_tupla[0]:'Buenos Aires',
                mi_tupla[1]:'Roma',
                mi_tupla[2]:'Londres'}
print(mi_diccionario)

#Colocar una (tupla) dentro de un diccionario
mi_diccionario={'clave1':'Valor1','Clave2':(1,2,3,4,5)}
print(mi_diccionario)

#Colocar una [lista] dentro de un diccionario.
mi_diccionario={'clave1':'Valor1','Clave2':[1,2,3,4,5]}
print(mi_diccionario)

#Colocar un diccionario dentro de un diccionario
mi_diccionario={'Clave1':'Valor1', ' Clave2':{'numeros':[1,2,3,4,5]}}
print(mi_diccionario)

#Imprimir las clves del diccionario
print(mi_diccionario.keys())

#Imprimir los valores del diccionario
print(mi_diccionario.values())

#Imprimir la longitud del diccionario
print(len(mi_diccionario))