def run():
    print("\"BIENVENIDO, Encontraremos el promedio de tus números :) \"")
    
    promedio = 0
    
    for i in range(4):
        numero_1= float(input(f"Ingresa el {i+1}° número: "))
        promedio+=numero_1

    promedio = round(promedio/4,2)

    print(f"\nEL promedio de los números ingresados  es ---> \"{promedio}\"")


if __name__=='__main__':
    run()