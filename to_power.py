def to_power(num, *args):
  output = [i ** num for i in args] if args else 'hey please enter list data'
  return output

nums = [1,2,3,4]
print(to_power(3, *nums))









