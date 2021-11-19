def run():
    contador = 0
    print("\"BIENVENIDO, Verificaremos si el DNI ingresado es correto :) \"\n")
    dni=input("Ingrese su número de DNI: ") 
    print(f"Dígitos ingresados : {len(dni)}")
    for i in range(len(dni)):
        contador += 1
    
    if contador == 8 :
        print("EL DNI ingresado es \" correcto \"")
    else :
        print("EL DNI ingresado es \" incorrecto \"")
        

if __name__ == '__main__':
    run()
