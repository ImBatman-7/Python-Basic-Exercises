def cube_finder(int):
    numbers = {}
    for i in range(1, int+1):
       numbers[i] = i**3
    return numbers

print(cube_finder(10))
