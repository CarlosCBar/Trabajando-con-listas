#Hacer listas

peliculas = ["Batman", "Spiderman", "El santo contra la tetona Mendoza", "Paprika"]
Cantantes = list(("Bad Bunny", "Eminem", "Porfirio", "Paquita la del Barrio"))
años = list(range(2021,2051))
variada = ["Victor", 324, 39.09, False, not False]

#modificar

peliculas[0]= "Casino"

#INDICES


print(variada[0:])
print(variada[:4])
print(peliculas[-2])
print(variada[1:3])


Cantantes.append("Kase O")
peliculas.append("Chrismas caroll")

#Recorrer lista
print("\n LISTADO DE PELICULAS \n")

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Agrega una pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

# Lista multidimensional (listas dentro de listas)

print("\n LISTADO DE CONTACTOS \n")

contactos = [
    [
        "Antonio", "antonio@toñito.com"
        ],
     [   "Pedro", "caradePedro@holi.com"

      ],[  "Salvador", "Chavapero@notuya.com"
        ]
    ]
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:   
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")

#IMPRMIR LA LSITA EN EL INDICE 1 Y EL VALOR EN EL IDICE 1
print(contactos[1][1]) 

numeros = [1,99,3,12,2,5,7,6,1,4]

#ORDENAR LISTAS

numeros.sort()
print(numeros)

# AÑADIR ELEMENTOS
Cantantes.insert(1, "Maria Conchita")

# ELIMINAR ELEMENTOS
Cantantes.pop(0)
print(Cantantes)
Cantantes.remove("Paquita la del Barrio")

# INVERTIR LISTAS
numeros.reverse()
print(numeros)

# BUSCAR DENTRO DE UNA LISTA

print("Batman" in peliculas)

# CUANTAS VECES APARECE UN ELEMENTO DENTRO DE UNA LSITA

print(numeros.count(1))

#UNIR LISTAS

numeros.extend(variada)
print(numeros)


