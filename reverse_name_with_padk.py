def caprev(name,**rev):
    return[ (i[::-1]).title()  if (rev.get('rev_str') == True) else i.title() for i in name]


names = ['abhinav', 'batman']
print(caprev(names, rev_str = True))

