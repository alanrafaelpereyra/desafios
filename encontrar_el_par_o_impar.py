# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and returns this "outlier" N.

# test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
# test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
# test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)

# Solucion en funcion
def find_outlier1(integers):  #Buscamos contar los pares e impares para saber que buscar
    pares=0
    impares=0
    for i in integers:
        if i % 2==0: 
            pares+=1
        else:
            impares+=1
    if pares ==1 :               #Si sabemos que solo hay un par, lo buscamos y entregamos
        for i in integers:
            if i % 2 ==0:
                return (i)
            else:
                pass
    if impares == 1 :          # Si sabemos que hay solo un impar, lo buscamos y entregamos
        for i in integers:
            if i %2 !=0:
                return (i)
            else:
                pass


#mejor solucion de la comunidad 

def find_outlier(int):
    odds = [x for x in int if x%2!=0]  #crear una lista con impares   # x es cada elemento para cada elemento de la lista si son impares
    evens= [x for x in int if x%2==0]  #crear una lista con pares     # x es cada elemento para cada elemento de la lista si son pares  
    return odds[0] if len(odds)<len(evens) else evens[0]    # devuelve el primer valor de la lista impar si el tamaño de los impares es menor, 
                                                            #de otra forma devuelve el primer elemento en la lista de los pares