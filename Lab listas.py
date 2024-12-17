#### Paso1: Lista viacia
beatles = []

#### Paso2: Agregar elementos a la lista
beatles.append('John Lennon')

beatles.append('Paul McCartney')

beatles.append('George Harrison')

print(beatles)

### Paso3: Agregar nombre de la lista con un for
nombre= input("Digita un nombre: ")
nombre2= input("Digita otro nombre: ")

for i in range(len(beatles)-2):
    
    beatles.append(nombre)
    beatles.append(nombre2)

    
    print(beatles)
    
##Paso 4 del Stu Sutcliffe y Pete best de la lista
print("Deleting")
beatles.remove("Stu Sutcliffe")
beatles.remove("Pete best")
print(beatles)

#### Insert Ringo
print("Inserting")
beatles.insert(0,"Ringo Starr")
print(beatles)

