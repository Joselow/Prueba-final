def porcentaje():
    print("\"BIENVENIDO, Descubre que porcentaje estas invirtiendo en la fundación de una Empresa :) \"\n")
    total = 0
    for i in range(3):
        inversor = float(input(f"Monto invertido del {i+1} inversor: "))
        print(inversor)
                
        if i == 0:
            inversor1 = inversor
        
        elif i == 1:
            inversor2 = inversor
        
        else:
            inversor3 = inversor
        
        total+= inversor

    print(f"\nEL total invertido es {total} que es el 100%\n")

    print(f"El porcentaje invertido en la empresa del primer inversor es  ---> \" {round(inversor1*100/total,1)} %\"")
    
    print(f"El porcentaje invertido en la empresa del segundo inversor es  ---> \" {round(inversor2*100/total,1)} %\"")
    
    print(f"El porcentaje invertido en la empresa del tercer inversor es  ---> \" {round(inversor3*100/total,1)} % \"")

        

if __name__ == '__main__':
    porcentaje()
    
