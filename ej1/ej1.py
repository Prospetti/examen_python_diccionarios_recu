notas = {
    "Arveja": [],
    "Pobrione": [],
    "Tocino": [],
    "Yano": [],
    "Hombre Lobo": [],
}

while True:

    print("-Seleccione una opcion-")
    print("1: Ver todas la notas")
    print("2: Ver notas por alumno")
    print("3: Cargar notas")
    print("4: Ver promedio")
    print("5: Salir")

    pre = int(input("Elija una opcion (1-5): "))

    if pre == 1:
        for apellido in notas:
            print(f"Notas de {apellido}: {notas[apellido]}")

    elif pre == 2:
        apellido = input("Ingrese el apellido del alumno: ")
        if apellido in notas:
            print(f"Notas de {apellido}: {notas[apellido]}")
        else:
            print("Error, vuelva a intentar")

    elif pre == 3:
        apellido = input("Ingrese el apellido del alumno: ")
        if apellido in notas:
            if len(notas[apellido]) == 0:
                for i in range(5):
                    nota = int(input(f"Ingrese la nota {i+1}: "))
                    notas[apellido].append(nota)
                    print("Fueron cargadas las notas de: ", apellido)
        else:
            print("Error, vuelva a intentar")
    
    elif pre == 4:
        apellido = input("Ingrese el apellido del alumno: ")
        if apellido in notas:
            if len(notas[apellido]) == 5:
                suma = 0
            for nota in notas[apellido]:
                suma = suma + nota
            promedio = suma / 5
            print(f"Promedio de {apellido}: ", {promedio})
        else:
            print("Error, vuelva a intentar")
    
    elif pre == 5:
        print("Chau")
        break

    else:
        print("Ingrese una opion valida")