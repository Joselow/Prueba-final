def run():
    print("\"BIENVENIDO, Determinaremos el numero mayor :) \"\n")
    numero_1 = float(input("Ingrese el primer número:"))
    numero_2 = float(input("Ingrese el segundo número:"))
    numero_3 = float(input("Ingrese el tercer número:"))

    if numero_1 > numero_2 and numero_1 > numero_3 :
        print(f"El número mayor es: {numero_1}")
    
    elif numero_2 > numero_3 :
        print(f"El número mayor es: {numero_2}")
    
    elif numero_1 == numero_2 and numero_1 == numero_3:
        print(f"Los números son iguales: {numero_1} = {numero_2} = {numero_3}")
    
    else :
        print(f"El número mayor es: {numero_3}")


if __name__=='__main__':
    run()