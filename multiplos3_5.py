"""
 If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
 Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)

Buscamos solventar el problema de sumar todos los multiplos de 3 y 5 a partir de un numero dado, para este caso, el numero dado sera 10
"""


# test.describe("Multiples of 3 and 5")
# test.it("should handle basic cases")
# test.assert_equals(solution(10), 23)


def solution(number):
    multiplos_3_5=[] #creamos una lista vacia
    lista=range(1,number) 
    for elementos in lista:         #para cada valor en la lista, revisamos si son multiplos de 3 y 5, si son, lo agregamos a la lista
        if elementos % 3==0:
            multiplos_3_5.append(elementos)
        elif elementos % 5==0:
             multiplos_3_5.append(elementos)
        else:
              pass
    return(sum(multiplos_3_5))

# mejor solución de la comunidad

    def solution(number):
        return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


# test.describe("Multiples of 3 and 5")
# test.it("should handle basic cases")
# test.assert_equals(solution(10), 23)

