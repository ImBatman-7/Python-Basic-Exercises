numbers = [2,4,6,8,10]

print(all(i%2==0 for i in numbers))

# ____________________________________

numbers = [2,4,777777,8,10]

print(all(i%2==0 for i in numbers))

# ____________________________________

numbers = [2,4,6,8,10]

print(any(i%2==0 for i in numbers))



# ________________________________________



def sum(*args):
    if all((type(arg)==int or type(arg)==float) for arg in args):

        total = 0
        for num in args:
          total += num
        return total    
    else:
        return "wrong input"

print(sum(1,2,3,4,5,5.6, 'hdhsui'))            