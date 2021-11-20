menu=""" |     Marca    |  Precio    |
 -----------------------------
 | 1.Salsa      |  S/. 56.00 |
 | 2.Rock       |  S/. 63.00 |
 | 3.Pop        |  S/. 87.00 |
 | 4.Folclore   |  S/. 120.50|
    \nSuper Oferta
 |   Cantidad   |  (%)Descuento    |
 -----------------------------------
 | 1 a 3        |  No hay descuento|
 | 4            |  6.0%            |
 | 5 a 10       |  8.0%           |
 | Más de 10    |  10.2%           | 
 -----------------------------------
 |  De 7 a más  | +1 POSTER  gratis| """


def nudiscos(Costo,dsct,poster,posterr,numero_discos,precioo):
        total = precioo * numero_discos
        descuento = round(Costo * total,1)
        total1 = round(total - descuento,1)   
        print(f"{dsct}\nIMPORTE:\n1.Precio: S/. {total}\n2.Descuento: S/. {descuento}\n3.Total a pagar: S/. {total1}\n{poster} \"POSTER\"{posterr}")
        return "♣♣ Hasta luego ♣♣ "


def precio(precioo,numero_discos):    
    if 0 < numero_discos < 4:        
        return nudiscos(0, "No hay descuento :c", "---No te toca el ", "---", numero_discos,precioo)
        
    elif numero_discos == 4 :
        return nudiscos(.06, "Descuento 6.0 % :)", "---No te toca el ", "---", numero_discos,precioo)
                  
    elif  6 < numero_discos < 11  :
        return nudiscos(.08, "Descuento 8.0 % :)", "¡¡¡Te llevas un ", "gratis!!!", numero_discos,precioo)
            
    elif  4 < numero_discos < 7  :
        return nudiscos(.08, "Descuento 8.0 % :)", "---No te toca el ", "---", numero_discos,precioo)
              
    elif numero_discos > 10:    
        return nudiscos(.102, "Descuento 10.2 % :)", "¡¡¡Te llevas un ", "gratis!!!", numero_discos,precioo)              
        

def discoo(disco,costo,Precio,numero_discos):
        print(f"\nDisco : {disco} S/. {Precio}\n ")
        if 0 < numero_discos < 4:
            return (precio(costo,numero_discos))
        elif numero_discos == 4 :
            return (precio(costo,numero_discos))

        elif  6 < numero_discos < 11  :
            return (precio(costo,numero_discos))

        elif  4 < numero_discos < 11  :
            return (precio(costo,numero_discos))
        
        elif numero_discos > 10:
            return (precio(costo,numero_discos))
        else :
            return print(f"***ERROR***\n{numero_discos}??? Cantidad de discos imposibles.")
            

def run():
    print("\"BIENVENIDO a \"La Tienda de Músicas \" :) \"\n\nCompra nuestros mejores Discos:")
    print(menu)
    disco = int(input("\nElige el N° de disco que quieres comprar: "))
    numero_discos = int(input("Cuántos discos quieres comprar: "))
    
    if disco == 1 :
        print(discoo("Salsa", 56, "56.00",numero_discos))
        
    elif disco == 2 :
        print(discoo("Rock", 63, "63.00",numero_discos))

    elif disco == 3 :
        print(discoo("Pop", 87, "87.00",numero_discos))
    
    elif disco == 4 :
        print(discoo("Folclore", 120.5, "120.5.00",numero_discos))
    else:
        print(f"***ERROR***\n{disco}??? N° de Disco no disponible")
    

if __name__ == '__main__' :
    run()
    
