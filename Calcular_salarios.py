def salarioo(porcentaje,descuento1,descuento2,porcentaje2,h_s1):
            salario = round(porcentaje2 * h_s1,1)
            descuento = round(porcentaje * salario,1)
            salario1 = salario - descuento            
            return print(f"\n{descuento1}\nTu salario bruto : S/. {salario}\n{descuento2} {descuento}\nTu salario neto : S/. {salario1}")
            
def run():
    print("\"BIENVENIDO, Calculáremos tu salario bruto :)\"\n")
    turno_trabajo = int(input("¿En qué turno relizaste el trabajo?\n[1]Mañana\n[2]Tarde\n[3]Noche\n: "))
    horas_trabajo = float(input("¿Cuántas horas tienes trabajando?: "))
    
    if turno_trabajo == 1 :
        salarioo(0, "Descuento 0.0 % (Turno Mañana)", "Descuento : S/.",37,horas_trabajo)
        
    elif turno_trabajo == 2 :
        salarioo(0, "Descuento 0.0 % (Turno Tarde)", "Descuento : S/.",38.2,horas_trabajo)
                
    elif turno_trabajo == 3 :
        salario = round(38.5 * horas_trabajo,1)    
        
        if 2000 <=salario <= 5000 :
            salarioo(0.15, "Tu salario ronda entre los S/. 2000  y  S/. 5000, se aplicará un descuento del 15 % (Turno noche)", "Descuento : S/.",38.5,horas_trabajo)
            
        elif 8000 <= salario <= 10000 :
            salarioo(0.17, "Tu salario ronda entre los S/. 8000  y  S/. 10000, se aplicará un descuento del 17 % (Turno noche)", "Descuento : S/.",38.5,horas_trabajo)
            
        else:
            salarioo(0, "Descuento 0.0 % (Turno Noche)", "Descuento : S/.",38.5,horas_trabajo)
    else:
        print("***ERROR***\nElije el N° de salario correcto porfavor.")
        exit()
            

if __name__ == '__main__':
    run()