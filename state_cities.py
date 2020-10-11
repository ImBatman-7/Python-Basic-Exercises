states = {
    'maharashtra': 'mh',
    'madhya pradesh' : 'mp',
    'rajasthan' : 'rj',
    'delhi' : 'dl',
    'haryana': 'hr'
}

cities = {
    'rj' : 'kota',
    'mp' : 'bhopal',
    'mh' : 'nagpur'
}

cities['dl'] = 'new delhi'
cities['hr'] = 'gurgaon'
print('-'*20)

print('mp has: ', cities['mp'])
print('dl has: ', cities['dl'])
print('-'*20)

print('nagpur is in : ', states['maharashtra'])
print('bhopal is in : ', states['madhya pradesh'])
print('-'*20)


print('haryana has :',cities[states['haryana']])
print('rajasthan has :',cities[states['rajasthan']])
print('-'*20)

for every_state,every_abb in states.items():
    print(f'{every_state} : {every_abb}')
print('-'*20)

for every_state,every_city in cities.items():
    print(f'{every_state} : {every_city}')    
print('-'*20)

for every_state,every_abb in states.items():
        print(f'{every_state} : {every_abb}')
        print(f'{every_state} : {cities[every_abb]}')
        print('---')


state=states.get('telangana')
if state not in states.items():
    print('not found')
else:
    print(state)