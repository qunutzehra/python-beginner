# Understanding the offset and appending item to list

states_of_India = ['Goa', 'Madhya Pradesh', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telanga', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
print("\nBefore append\n")
print(states_of_India)
print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")



#**************************************** More on Lists*********************************************************

# Append function is used to adding new state name in list
states_of_India.append('Aruchanachal pradesh')
states_of_India.append('Assam')
states_of_India.append('Himachal Pradesh')
states_of_India.append('Jharkhand')
states_of_India.append('Kerala')
states_of_India.append('Karnataka')
print("\nAfter append\n")
print(states_of_India)
print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")



# list.extend(iterable): Extend the list by appending all the items from the iterable. 
states_of_India.extend(['Bihar', 'Bihar', 'Chattisgarah', 'Gujarat', 'Haryana','Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha'])
print("\n Extensed list of States in india\n",states_of_India)
print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")


#  list.insert(i,x): used to insert an item on a given position (This will remove onli one arguement)
states_of_India.remove('Chattisgarah')
print(states_of_India)
print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")


#  pop([i]): pop() removes and returns the last item in the list. 
a = states_of_India.pop()
b = states_of_India.pop()
c = states_of_India.pop()
d = states_of_India.pop()
e = states_of_India.pop()
f = states_of_India.pop()
print("pop value a is: ",a)
print("pop value b is: ",b)
print("pop value c is: ",c)
print("pop value d is: ",d)
print("pop value e is: ",e)
print("pop value f is: \n",f)
print("The list after pop value\n",states_of_India)
print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")



# listName.index(x[, start[, end]]) is used to insert a item on pacific place in list
states_of_India.index('Bihar')
states_of_India.index('Bihar', 0)
print(states_of_India)
print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")


# remove(x): this function is used to remove first item from the list
states_of_India.remove('Goa')
print(states_of_India)
print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# -------------------------------------------------------------------------
# .count(x) : this is used to return number of times x appears in the list
'''list.count("Bihar")
print(states_of_India)'''
# it shows error because it does not apply for string 
# --------------------------------------------------------------------------


# .sort(*, key=None, reverse=False):Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).'''
states_of_India.sort(reverse=True)
print('After sorted it looks like\n',states_of_India)
print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")


# .reverse(): Reverse the element of the list in place.
states_of_India.reverse()
print("Reverses list is: ")
print(states_of_India)
print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")



# .clear(): Remove all items from the list. Equivalent to del a[:]
states_of_India.clear()
print("you did empty your list using .clear():")
print(states_of_India)

