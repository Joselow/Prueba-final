def run():
    print("\"BIENVENIDO, Calculáremos tu salario :) \"\n")
    nombre = input("Por favor, ingresa tu nombre completo:  ")
    salario_hora = float(input("Ingresa el salario basico por hora: "))
    horas_trabajo = int(input("Ingresa las horas que tienes trabajando: "))

    nombre=nombre.capitalize()

    sueldo = salario_hora * horas_trabajo
    print(f"\nBueno {nombre}\nTu sueldo sin aumento es de : {sueldo}")
    sueldo +=.15*sueldo
    print(f"Tu sueldo con aumento del 15% asciende a: {sueldo}")


if __name__ == '__main__':
    run() 