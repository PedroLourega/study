my_dictionary = {"hair": "nutbrown",
                 "eyes": "brown",
                 "height:": 1.68,
                 "favorite color": "blue",
                 "favorite food": "spaghetti",
                 "favorite game": "Outer Wilds",
                 "favorite author": "F. Dostoevsky"}

question = input("What would you like to know about me?")
if question in my_dictionary:
    q = my_dictionary[question]
    print(q)
else:
    print("Unfortunately, I cannot answer your question...")

