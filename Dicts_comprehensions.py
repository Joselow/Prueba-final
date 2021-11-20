def run(): #dicts comprehensions
    # my_dict = {}
#Agregando un comentario ramdom desde GitHub para practicar lo dle profe Fredy xddddd ajjsasa
    # for i in range(1,101):
    #     if i % 3 != 0 :
    #         my_dict[i] = i**3  #i es la llave y i ** 3 es el valor

    # my_dict ={i : i**3 for i in range(1,101) if i % 3 != 0}  #lo mismo que arriba en unba linea
    # print(my_dict)

    my_new_dict = {i : round(i**0.5,2) for i in range(1,1001)} #lectura: para i en el rango de 1 a 1000 quiero que la llave sea i y su valor sea la raiz de i .
    print(my_new_dict)

if __name__ == '__main__':
    run()
