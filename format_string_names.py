def namelist(names):
    if len(names) == 0:   #Making sure program work if entry is empty   
        return ''
    if len(names) == 1:  #making sure program work with only one name in list
        return names[0]['name']
    return ", ".join([n['name'] for n in names[:-1]]) + " & " + names[-1]['name']  # ', '.join() agregamos la coma para cada [diccionario['key]] dentro de diccionario  names[:-1]] hasta la penultima




# Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge',
# "Must work with many names")
# Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
# "Must work with many names")
# Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa', 
# "Must work with two names")
# Test.assert_equals(namelist([{'name': 'Bart'}]), 'Bart', "Wrong output for a single name")
# Test.assert_equals(namelist([]), '', "Must work with no names")
