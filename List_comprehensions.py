def run():   #list comprehensions
    # squares = []
    
    # for i in range(1,101):
    #     if i %3 != 0 :
    #         squares.append(i**2)
    squares = [i**2 for i in range(1,101) if i % 3 != 0]  #lo mismo que arriba solo que mas rapido y en una linea
    print(squares)

    squares = [i for i in range(1,100000) if i % 36 ==0] #lectura: para i en el rango de 1 a 100000 quiero a i solo si es divisible entre 36
    print(squares)






if __name__ == '__main__' :
    run() 