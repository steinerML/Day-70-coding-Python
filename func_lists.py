#Defining a function that takes a LIST as an argument.

def greet_users (names):
    for name in names:
        msg = 'Hello! '+ name
        print(msg)

usernames = ['Nay', 'Yeay', 'Yee', 'Woo']

greet_users(usernames)


#Allowing a function to modify a list
#2 lists: unprinted and printed

def print_models(unprinted,printed):
    while unprinted:
        current = unprinted.pop() #removes last item by default.
        print('Printer currently working on:',current)
        printed.append(current)


unprinted = ['jewel', 'necklace', 'ring', 'engine part']
printed = []
print_models(unprinted,printed)

#Allowing a function to modify a list (a copy)
#In this case 3 lists, unprinted[:], unprinted & printed

def my_printer(unprinted,printed):
    while unprinted:
        current = unprinted.pop()
        print('Printing queue:', current)
        printed.append(current)
        

unprinted = ['3d bolt', 'gasket', 'flange', 'washer']
printed = []

my_printer(unprinted[:],printed)

#Now we verify that the original list hasn't changed
print(unprinted)
#But we do though, have created a fresh new list called printed
print(printed) #In reverse order as pop() starts by the end.

#Remember that unprintend[:] is a copy of unprinted list!
