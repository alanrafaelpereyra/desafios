# Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings,
# ordered from shortest to longest.
# For example, if this array were passed as an argument:
# ["Telescopes", "Glasses", "Eyes", "Monocles"]
# Your function would return the following array:
# ["Eyes", "Glasses", "Monocles", "Telescopes"]
# All of the strings in the array passed to your function will be different lengths, 
# so you will not have to decide how to order multiple strings of the same length.

def sort_by_length(arr):   #this is the bubble sorting method from the all life, just change the parameter, nevertheless is a nice practice
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)

            if len(arr[j]) > len(arr[j + 1]):   # se comparan si los elementos adyancentes estan ordenados
                arr[j], arr[j + 1] = arr[j + 1], arr[j]           #los intercambiadelugar en caso que no esten ordenados

    return arr                                                                  