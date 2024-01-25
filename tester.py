import os

contactos = []

print("----------------AGENDA DE CONTACTOS--------------------")

while True:
    
    def agregar(name, number):
        nuevo = {"Nombre": name, "Numero": number}
        contactos.append(nuevo)
        print(nuevo)
        
    def borrar(name):
        for cont in contactos:
            if cont.get("Nombre") == name:
                contactos.remove(cont)
                
    def actualizar(name):
        for cont in contactos:
            if cont.get("Nombre") == name:
                print(f"Nombre actual: {cont.get('Nombre')}")
                new_name = input("Ingresa el nuevo nombre (o presiona Enter para mantener el actual): ")
                cont['Nombre'] = new_name if new_name else cont['Nombre']
                print(f"Numero actual: {cont.get('Numero')}")
                new_number = input("Ingresa el nuevo numero (o presiona Enter para mantener el actual): ")
                cont['Numero'] = new_number if new_number else cont['Numero']
                print("Contacto actualizado:")
                print(cont)

    print("Que desea hacer \n 1)Agregar \n 2)Borrar \n 3)Actualizar \n 4)Ver contactos")
    option = int(input(": "))

    if option == 1:
        name = input("Ingresa un nombre: ")
        number = input("Ingresa un numero: ")
        agregar(name, number)
    elif option == 2:
        print("------------------CONTACTOS-----------------")
        for cont in contactos:
            print(cont)
        name = input("Ingresa el nombre del usuario que deseas borrar: ")
        borrar(name)
    elif option == 3:
        print("------------------CONTACTOS-----------------")
        for cont in contactos:
            print(cont)
        name = input("Ingresa el nombre del usuario que deseas actualizar: ")
        actualizar(name)
    elif option == 4:
        print("------------------CONTACTOS-----------------")
        for cont in contactos:
            print(cont)
    else:
        print("Opcion invalida")

    menu = int(input("Desea hacer otra operacion?(1/0): "))
    
    if menu == 0:
        os.system("clear")
        break
    else:
        os.system("clear")
