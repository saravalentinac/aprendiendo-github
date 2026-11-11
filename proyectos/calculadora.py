def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

a = float(input("Primer número: "))
b = float(input("Segundo número: "))

print("Suma:", sumar(a, b))
print("Resta:", restar(a, b))
print("Multiplicación:", multiplicar(a, b))
print("División:", dividir(a, b))