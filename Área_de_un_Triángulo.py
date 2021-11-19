def run():
    print("\"BIENVENIDO, Calculáremos el área de un triángulo :) \"\n")
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    area = base * altura / 2
    print(f"EL área de un triangulo de base {base} y altura {altura} es : \"{area}\"")


if __name__ == '__main__':
    run()