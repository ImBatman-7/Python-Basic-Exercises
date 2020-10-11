
students1 = [
    {'abhinav' : 'score', 'age':24},
    {'ab'      : 'score' ,'age':19},
    {'batman'  : 'score', 'age':23}
]
print(sorted(students1, key = lambda d:d['age']))


# ________________________________________________

students1 = [
    {'abhinav' : 'score', 'age':24},
    {'ab'      : 'score' ,'age':19},
    {'batman'  : 'score', 'age':23}
]
print(sorted(students1, key = lambda d:d['age'], reverse = True))