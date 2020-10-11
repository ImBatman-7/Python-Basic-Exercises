def num_to_list(l):
    return [str(i) for i in l if type(i) == int or type(i) == float ]
    

print(num_to_list([1,1.0,'abhinav', 0.1,100]))