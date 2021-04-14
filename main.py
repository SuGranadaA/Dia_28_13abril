#Importamos la librería Matplotlib.pyplot para los gráficos
import matplotlib.pyplot as plt

#Importamos la librería Matplotlib.colors para los colores
import matplotlib.colors as colors

#Abrimos el archivo en modo lectura
pers = open('personeria.txt', 'r')

#Leemos las lineas del archivo
lista = pers.readlines()

#Cerramos el archivo
pers.close()

#Imprimimos el contenido del archivo
print(
    "\nEn un colegio se hicieron las votaciones a personería, y los resultados fueron los siguientes: \n",
    lista, "\n")

#Relacionamos las líneas con una variable para operar a continuación
nom1 = (lista[0].rstrip())
num1 = (lista[1].rstrip())
nom2 = (lista[2].rstrip())
num2 = (lista[3].rstrip())
nom3 = (lista[4].rstrip())
num3 = (lista[5].rstrip())
nom4 = (lista[6].rstrip())
num4 = (lista[7].rstrip())
nom5 = (lista[8].rstrip())
num5 = (lista[9].rstrip())

#Creamos el diccionario y relacionamos las variables
votos1 = {
    nom1: int(num1),
    nom2: int(num2),
    nom3: int(num3),
    nom4: int(num4),
    nom5: int(num5)
}

#Imprimimos el diccionario
print("\nEl resumen de los votos es: \n", votos1, "\n")

#Definimos los colores a utilizar en la gráfica
colores = ["lightblue", "lightgreen", "lightyellow", "pink", "orange"]

#Creamos la gráfica y relacionamos los valores y colores
plt.bar(votos1.keys(), votos1.values(), color=colores)

#Damos nombre al eje X
plt.xlabel('Candidatos')

#Damos nombre al eje Y
plt.ylabel('Cantidad de votos a favor')

#Damos nombre a la gráfica
plt.title('Votaciones a personería')

#Guardamos el nuevo archivo en formato PNG
plt.savefig("RESpersoneria.png")

#Cerramos el nuevo archivo
plt.close()

#Abrimos el archivo en modo lectura
exam = open('examen.txt', 'r')

#Leemos las lineas del archivo
listita = exam.readlines()

#Cerramos el archivo
exam.close()

#Imprimimos el contenido del archivo
print(
    "\nA final de curso se realizó un exámen, y los resultados fueron los siguientes: \n",
    listita, "\n")

#Relacionamos las líneas con una variable para operar a continuación
dat1 = (listita[0].rstrip())
val1 = (listita[1].rstrip())
dat2 = (listita[2].rstrip())
val2 = (listita[3].rstrip())
dat3 = (listita[4].rstrip())
val3 = (listita[5].rstrip())
dat4 = (listita[6].rstrip())
val4 = (listita[7].rstrip())

#Creamos el diccionario y relacionamos las variables
datitos = {
    dat1: float(val1),
    dat2: float(val2),
    dat3: float(val3),
    dat4: float(val4)
}

#Imprimimos el diccionario
print("\nLos datos del diccionario son: \n", datitos, "\n")

#Definimos los colores a utilizar en la gráfica
col = ["brown", "lightgreen", "lightblue", "lightyellow"]

#Creamos la gráfica y relacionamos los valores y colores
plt.pie(datitos.values(),
        labels=datitos.keys(),
        colors=col,
        autopct=("%0.2f%%"))

#Damos nombre a la gráfica
plt.title('Calificaciones del exámen final')

#Guardamos el nuevo archivo en formato PNG
plt.savefig("RESexamen.png")

#Cerramos el nuevo archivo
plt.close()
