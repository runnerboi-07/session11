d = {} # empty dictionary
eng_to_spa = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_to_spa)
eng_to_spa["I"] = "Yo"
eng_to_spa["am"] = "soy"
eng_to_spa["Spanish"] = "Español"
print(eng_to_spa)
sentence = "I am Spanish"
words = sentence.split()
for word in words:
    print(eng_to_spa[word])

# Can add two dictionaries together
eng_to_spa.update({"yes": "si", "no": "no"}) # update a dictionary with a new dictionary
print(eng_to_spa)
del eng_to_spa["no"] # to remove key/value from dict
print(eng_to_spa)

# print(eng_to_spa.popitem()) # removes last item from dictionary; not very useful since you do not really know what is the last item in the dictionary
print(eng_to_spa.pop("two")) # removes specific item using key; much better to pop value by specifying the key

if "tree" in eng_to_spa: # checks just the keys
    print(eng_to_spa["tree"])
else:
    print("I don't know that word")

print(eng_to_spa.get("tree", "unknown word")) # checks keys; returns value if not found

for key in eng_to_spa: # iterates over the keys
    print(f"{eng_to_spa[key]} means {key}")

for key, value in eng_to_spa.items(): # items gives both keys and the values
    print(f"{value} means {key}")


