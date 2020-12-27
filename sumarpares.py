"""
Complete the function that takes a sequence of numbers as single parameter. Your function must return the sum of the even values of this sequence.

Only numbers without decimals like 4 or 4.0 can be even.

The input is a sequence of numbers: integers and/or floats.
@test.describe("Simple integers input.")
def example_tests():
    test.assert_equals(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
    test.assert_equals(sum_even_numbers([]), 0)

"""
def sum_even_numbers(seq): 
    lista_de_pares=[]
    for i in seq:
        if i % 2==0:
            lista_de_pares.append(i)
        else:
            pass
    return sum(lista_de_pares)

#Mas votado

def sum_even_numbers(seq): 
    return sum(x for x in seq if x%2==0) # la suma de cada termino para cada termino en seq si el termino es par