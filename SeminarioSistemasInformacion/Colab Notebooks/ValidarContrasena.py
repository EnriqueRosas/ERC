while True:
    print("///////////////////////////////////////////////////////////////////////////////")
    print("Debe ingresar una contraseña de al menos 8 caracteres, al menos una minúscula,")
    print("al menos una mayúscula, al menos un número y sin espacios en blanco")
    print("////////////////////////////////////////////////////////////////////////////")
    contrasena = input("Ingrese una contraseña: ")

    # Verificar la longitud de la contraseña
    if len(contrasena) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        continue

    # Verificar si hay al menos una letra minúscula
    if not any(c.islower() for c in contrasena):
        print("La contraseña debe contener al menos una letra minúscula.")
        continue

    # Verificar si hay al menos una letra mayúscula
    if not any(c.isupper() for c in contrasena):
        print("La contraseña debe contener al menos una letra mayúscula.")
        continue

    # Verificar si hay al menos un número
    if not any(c.isdigit() for c in contrasena):
        print("La contraseña debe contener al menos un número.")
        continue

    # Verificar si no contiene espacios en blanco
    if ' ' in contrasena:
        print("La contraseña no debe contener espacios en blanco.")
        continue

    # Si la contraseña cumple con todos los requisitos, imprimir un mensaje y salir del bucle
    print("¡Contraseña segura!")
    break
