def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return round(num1 / num2,2)
    

def multiplica(num1, num2):
    return num1 * num2

if __name__ == '__main__':
    print("\"BIENVENIDO, Resolveremos una pequeña operación :) \"\n")
    numero_1 = float(input("Ingrese un número: "))
    numero_2 = float(input("Ingrese otro número: "))       
    operacion = int(input("Elige la operacion que deseas realizar: \n[1]Suma\n[2]Resta\n[3]Multiplicación\n[4]Divición\n \n"))
 
    if operacion == 1:
        print(f"El resultado de la suma es: \" {suma(numero_1, numero_2)} \"")

    elif operacion == 2:
        print(f"El resultado de la resta es: \" {resta(numero_1, numero_2)} \"")

    elif operacion == 3:
        print(f"El resultado de la multiplicación es: \" {multiplica(numero_1, numero_2)} \"")

    elif operacion == 4:
        print(f"El resultado de la división es: \" {divide(numero_1, numero_2)} \"")
    else:
        print("ERRONEO")