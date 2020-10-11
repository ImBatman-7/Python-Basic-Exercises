names = ['abhinav', 'abhinavsahu', 'ab']
print(max(names, key = lambda item : len(item)))

# __________________________________________

students = {
    'abhinav' : {'score':50, 'age':24},
    'ab'      : {'score':75, 'age':19},
    'batman'  : {'score':80, 'age':23}
}


print(max(students, key = lambda item : students[item]['age']))

students1 = [
    'abhinav' : {'score':50, 'age':24},
    'ab'      : {'score':75, 'age':19},
    'batman'  : {'score':80, 'age':23}
]
print(sorted(students1, key = lambda d : d['score'])
