def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count    

mixed = [[7], 4,  [4], [3]]
print(sublist_counter(mixed))