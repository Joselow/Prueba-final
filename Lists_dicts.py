def run():
    my_list = [1,"Hi",True,4.5]
    my_dict = {"firts name":"Joshepi","Last name" : "Macha"}
    
    super_list = [
        {"firtsname":"Joshepi","Lastname" : "Macha"},
        {"firtsname":"Dante","Lastname" : "Mayki"},
        {"firtsname":"Luis","Lastname" : "Bravo"},
        {"firtsname":"Carlos","Lastname" : "Dan"},
        {"firtsname":"Estefano","Lastname" : "Fabian"},
    ]

    big_list = [
        {"nick":"Joshepi",3: "yasuo","range" : "challenger"},
        {"nick":"Dante",3: "yasuo","range" : "Maestro"},
        {"nick":"Luis",3: "yasuo","range" : "Broncexd"},
        {"nick":"Carlos",3: "yasuo","range" : "Mitico(MBBB:)"},
        {"nick":"Estefano",3: "yasuo","range" : "Epico(MBBB:)"},
    ]
    lol = [
        {"JOshep":"Yasuo"},
        {"JOshep":"Garen"},
    ]

    super_dict ={
        "natural_nums" : [1,2,3,4,5],
        "integer_nums" : [-1,-2,0,1,2],
        "floating_nums" : [1.1,4.5,6.32],
    }
    
    big_dict ={
        "asesinos": ["fizz","zeed","quiyana"],
        "magos":["lisandra","oriana","anie"],
    }
    
    #super_list
    for item in super_list:        #para items(diccionarios),imprime los valores de las llaves(en todos los dicc debe aver la misma llave)
        print(item["firtsname"],"--->",
        item["Lastname"])
    
    for values in super_list:      #para values(dicts),otro ciclo for y ahi si utilizamos el .items()
        for key,value in values.items():
            print(f"{key} ---> {value}")
            
    #big_list
    for i in big_list:           #para i(dicts),imprime los valores de las llaves con el mismo name
        print(i["nick"],"--->",i["range"],i[3])
    
    for i in big_list:           #para i(dicts),for y ahi aplicamos .items()
        for k,v in i.items():
            print(k ,"-->",v)

    #lol
    for i in lol:                #para i(dicts),for y ahi aplicamos .items()
        for t,i in i.items():
            print(t,"--->",i)
    for i in lol:                #para i(dicts),imprime los valores de las llaves con el mismo name
        print(i["JOshep"])

    #super_dict
    for key,value in super_dict.items():  #para k,v aplicamos el .items() porque es un dict 
        print(key,"--->",value)
    
    #big_dict
    for k, v in big_dict.items():         #para k,v aplicamos el .items() porque es un dict 
        print(k,"--->",v)

    

    
if __name__ == '__main__':
    run()