print("Python has 3 numeric datatypes: int, float, and complex")
myvalue=1
print(myvalue)
print(type(myvalue))
print(str(myvalue) + "is of the data type" + str(type(myvalue)))
myval=3.12
print(myval)
print(type(myval))
print(str(myval) + "is of the data type " + str(type(myval)))
print(str(myval) + "is of datatype" + str(type(myval)))
mycomplex=5j
print(mycomplex)
print(type(mycomplex))
print(str(mycomplex) + "is of the data type" + str(type(mycomplex)))
mybool=True
print(mybool)
print(type(mybool))
print(str(mybool) + " is of the datatype" + str(type(mybool)))
myboolean=False
print(myboolean)
print(type(myboolean))
print(str(myboolean) + " is of the typr" + str(type(myboolean)))
mystring="this is a string."
print(mystring)
print(type(mystring))
print(str(mystring) + "is of the datatype" + str(type(mystring)))
firststring="water"
secondstring="fall"
thirdstring=firststring+secondstring
print(thirdstring)
name=input("what is your name")
print(name)
color=input("what is your fav color?")
animal=input("what is your fav animal?")
print("{}, you like a {} {}!".format(name,color,animal))
myfruitlist=["apple","grapes","banana"]
print(myfruitlist)
print(type(myfruitlist))
print(myfruitlist[1])
myfruitlist[2]="orange"
print(myfruitlist)
myfinaltuple=("apple","cherry","strawberry")
print(myfinaltuple)
print(type(myfinaltuple))
print(myfinaltuple[0])
print(myfinaltuple[1])
print(myfinaltuple[2])
myfavfruitdic={
    "misba" : "apple",
    "sana" : "cherry",
    "paulo" : "pineapple"
}
print(myfavfruitdic)
print(type(myfavfruitdic))
print(myfavfruitdic["misba"])


