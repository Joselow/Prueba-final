def run():
    print("\"BIENVENIDO, Determinaremos si el número es par o impar :) \"\n")
    numero_p_i =  int(input("Ingrese el número a comprobar: "))
    if numero_p_i % 2 == 0 :
        print(f"El número \" {numero_p_i} \" es par")
    else :
        print(f"El número \" {numero_p_i }\" es impar")

if __name__ == '__main__':
    run()