# Exercise 39: Dictionaries

# A Dictionary (or dict) is a way to store data just like a list, but instead of using only numbers
#   to get the data, you can use almost anything.  This lets you treat a dict like it's a database
#   for storing and organizing data.

# # Let's compare what dicts can do to what lists can do.  You see, a list lets you do this:
# things = ['a', 'b','c','d']
# print(things[1])    # prints 'b'

# things[1] = 'z' # reassigns list item [1] to 'z'
# print(things[1]) # prints 'z'

# things  # ['a', 'z','c','d']

# # You can use numbers to index into a list, meaning you can use numbers to find out what's in a list.
# # Make sure you understand that you can ONLY use numbers to get items out of a list.


# # A dict lets you use anything, not just numbers.  Yes, a dict associates one thing to another, no matter what.

# stuff = {'name': 'Gary', 'age:': 31, 'height': 6 * 12 + 4}
# print(stuff['name']) # printing the value associated with the key 'name' in the dict variable stuff
#     # Gary
# print(stuff['age']) # same as above, but for the key 'age'
#     # 31
# print(stuff['height']) # 76

# stuff['city'] = "NY"    # adding a key, 'city', with the value = "NY"
# print(stuff['city'])
#     # NY


# # You will see that instead of just numbers we're using strings to say what we want from the stuff dictionary.
# # We can also put new things into the dictionary with strings.  It doesn't have to be strings, though.

# # We can also do this:

# stuff[1] = "Wow"    
# stuff[2] = "Neato"
# print(stuff[1])
# print(stuff[2])

# # In this code I used numbers, and then you can see there are numbers and strings as keys in the dict when printed.

# # Delete things with the  del  keyword:

# del stuff['city']
# del stuff[1]
# del stuff[2]
# stuff   # {'name': 'Gary', 'age': 31, 'height: 76}


#       A Dictionary Example

# Take note of when you put things in a dict, get them from a hash, and all the operations you use.
# Notice how this example is mapping states to their abbreviations and then the abbreviations
#   to cities in the states.  Remember, mapping (or associating) is the key concept in a dictionary.


# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Fracisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities 
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by ussing the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has the city {cities[abbrev]}")

print('-' * 10)
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")