# states = {
#     'Oregon': 'OR',
#     'Florida': 'FL',
#     'California': 'CA',
#     'New York': 'NY',
#     'Michigan': 'MI'
# }
# 
# 
# # create a basic set of states and some cities in them
# cities = {
#     'CA': 'San Fransisco',
#     'MI': 'Detroit',
#     'FL': 'Jacksonville'
# }
# 
# # add some cities
# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'
# 
# # print out some cities
# print('-' * 10)
# print("NY State has: ", cities['NY'])
# print("OR State has: ", cities['OR'])
# 
# # print some states
# print('-' * 10)
# print("Michigan has: ", cities[states['Michigan']])
# print("Florida has: ", cities[states['Florida']])
# 
# # print every state abbreviation
# print('-' * 10)
# for state, abbrev in list(states.items()):
#     print(f"{state} is abbreviated {abbrev}")
# 
# # now do both at the same time
# print('-' * 10)
# for state, abbrev in list(states.items()):
#     print(f"{state} state is abbreviated {abbrev}.")
#     print(f"and has city {cities[abbrev]}")
# 
# print('-' * 10)
# # safely get an abbreviation that might not be there
# state = states.get('Texas')
# if not state:
#     print('Sorry, no Texas.')
# # get a city with a default value 
# city = cities.get('TX', 'Does not exist')
# print(f"The city for state 'TX' is: {city}.")

states = {
    "Washington": 'WA',
    "South Dakota": 'SD',
    'Hawaii': 'HI'
}

cities = {
    'WA': ['Seattle', 'Bellingham'],
    'SD': 'Sioux',
    'HI': 'Honolulu'
}

cities['WA'] = 'Bellingham'
cities['SD'] = 'Rapid City'
cities['HI'] = 'Maui'

print("WA State has: ", cities['WA'])

cities_states = dict([('WA', 'Seattle'), ('SD', 'Rapid City'), ('HI', 'Honolulu')])
cities_states.update({'OR': 'Portland'})
cities_states.update({'Vermont': 'Burlington'})
del(cities_states['Vermont'])
listed_cities = list(cities)
print(cities_states)
print(cities)

grades = {"Jordan": 95, "Darby": 97, "Kaiju": 91, "Bastet": 89}


word_freq = {
    "hello": 56,
    "at": 23,
    "test": 43,
    "this": 78,
    "hi": 99
}
values = word_freq.values()
print(values)
print("Iterate over all values")
for elem in word_freq.values():
    print(elem)


# Get all values from a dictionary
word_freq['hello'] = 100
word_freq['at'] = 200
print('Values of dictionary: ')
print(values)

wordlen = len(listed_cities)
print(wordlen)

gradelen = len(grades)
print(gradelen)


for value in grades:
    if grades[value] > 90:
        print(value)

