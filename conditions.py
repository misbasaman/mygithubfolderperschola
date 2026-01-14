userreply=input("Do you need to ship a package? (Enter yes / no) ")
if userreply == "yes":
    print("We can help you ship!")
    
else:
    print("Please come bach when you need : Thank You!")
    
userreply1=input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy)")
if userreply1 == "stamps":
    print("We have many stamp designs to choose from.")
elif userreply1 == "envelope":
    print("We have many envelope sizes to choose from.")
elif userreply1=="copy":
    copies=input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")

    