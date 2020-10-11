
def reversed_item(l):
    rlist = []
    for i in l: 
        rlist.append(i[::-1])
    return rlist  

items_to_be_reversed = ['batman', 'superman', 'cyborg']
print(reversed_item(items_to_be_reversed))