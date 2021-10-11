num = float(input("Por favor ingrese un numero decimal: "))

entera = num//1
num %= 1
print(f"la parte entera es {entera}")
print(f"la parte decimal es {num:.3f}")