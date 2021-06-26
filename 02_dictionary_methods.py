myDict = { 
    "fast": "In a Quick Manner",
    "Harry": "A Coder",
    "Marks": [1,3,3],
    "anotherdict": {'harry': 'player'},
    1: 2
}
# Dictionary Methods
print(myDict.keys()) # Prints the keys of the dictionary
print(list(myDict.keys())) # Prints the keys of dictionary
print(myDict.items())
print(myDict.values()) # Prints the (key, value) for all contents of Dictionary
print(myDict)
updateDict = {

    "Lovish": "Friend",
    "Raka": "Classmate",
    "Rajveer": "Friend",
    "Harry": "A Rapper" # this will update ("Harry": "A Coder") to ("Harry": "A Rapper")
}
myDict.update(updateDict) # Updates the dictionary by aadding key-value pairs from updateDict
# print(myDict)

print(myDict.get("Harry2")) # Prints value associated with key "harry"
print(myDict["Harry2"]) # Prints value associated with key "harry"

# The diffrence between .get and [] syntax in Dictionaries?
print(myDict.get("harry2")) # returns None as harry2 is not present in the dictionary
print(myDict["harry2"]) # throws an error as harry2 is not present in the dictionary


updateDict = {
    "Harry": "A Programmer" # update ("A Rapper") to ("A Programmmer")
}

myDict.update(updateDict)
print(myDict)

