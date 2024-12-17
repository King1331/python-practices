## Lab continue, comedor de vocales

palabra = input("Digita una palabra: ")

for x in palabra:
    if x == "a"  or x == "e" or x == "i" or x == "o" or x == "u":
     continue
    print(x.upper())


