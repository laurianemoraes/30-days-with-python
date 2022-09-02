numbers=[3, 5, 90, 30, 56]
friends= ["Laura", "Dona", "Jhonna", "Anna"]

friends.extend(numbers)#extend the information to the numbers 

friends.append("Tom")#put the element refer after the others
friends.insert(2, "Jhonn")#put the element refer after the refer position
friends.remove("Dona")#remove one element, clean remove all elements
friends.pop()
print(friends.index("Laura"))#set up the position of the element
print(friends.count("Anna"))

numbers.sort()#reverse switch the position of the elements
print(numbers)

friends2 = numbers.copy()
print(friends2)
