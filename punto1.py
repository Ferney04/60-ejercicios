nombre = input("Por favor ingrese su nombre: ")
cualificativo = input("Escriba su apodo: ")
edad = int(input("Escriba su edad: "))

if edad <= 25:
    print(nombre,cualificativo,", eres un pelaito")
else:
    print(f"{nombre}{cualificativo}, ya estas viejo")