#!/usr/bin/python3

print("welcome back")
fruits = ['apples','bananas','grapes','mangos','nectarines', 'pears',]


i = 0;
for fruit in fruits :
    print(fruits[i])
    i += 1


i = 0

while i < len(fruits) :
    if fruits[i] == 'nectarines' :
        i +=1
        continue
    print(fruits[i])
    i +=1