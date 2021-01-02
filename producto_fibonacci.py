def productFib(prod):  
    x=0 #iniciadores
    y=1
    while prod> x*y: #mientras que no sea igual al producto
        x=y  #a sera el proximo numero
        y=x+y  #b es la suma del anterior con el actual
    return [x, y, prod==x*y]
    







