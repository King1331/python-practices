###Espatifilio (elif brinda la capacidad del poner varias condiciones,
## el else al final es el que aniquila todo, si ningul elif se cumple
## El else entra en accion)

palabra= input("Digite el nombre de una planta: ")

if palabra == "Espatifilo" :
    print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")

elif palabra == "espatifilo" :
    print("No, ¡quiero un gran Espatifilo!")
    
elif  palabra == "ESPATIFILO" :
    print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")

    
else:
    print("¡Espatifilo!, ¡No!", palabra , "!")





