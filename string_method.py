#to capitalise the first letter of a group of words
print("abcd".capitalize())

#to center a string
print("[" + "Stephen".center(10)  + "]")
#to add a kind of style to it
print("[" + "Chisom".center(10, "*") + "]")

#to check if a string end with a word or a letter we use the .endswith() method
if "Stephen".endswith("en"):
    print("yeah it is so")
else:
    print("nah nah nah")
#or
me = "ugota chisom stephen is my name"
print(me.endswith("name"))

#to check if a character is found in a string we can use the find() method
if "name".find("me"):
    print("letter m,e is find in this string")
else:
    print("letter m,e is not find")
#to perform the find, not from the string's beginning, but from any position
print("Stephen".find("e", 3))

# isalnum() checks if the string contains only digits or alphabetical characters (letters)
if "Ugota".isalnum():
    print("is an alphabet or a numeric")
else:
    print("is not an alpha nor numeric")

#The isalpha() method is more specialized – it's interested in letters only.
if "steven".isalpha():
    print("is an alphabet")
else:
    print("is not an alphabet")

#the isdigit() method looks at digits only
if "1234".isdigit():
    print("is a digit")
else:
    print("is not a digit")

#The islower() method is a fussy variant of isalpha() – it accepts lower-case letters only.
if "stephen".islower():
    print("is a lowercase string")
else:
    print("is not a lowercase string")

#The isspace() method identifies whitespaces only – it disregards any other character (the result is False then).
if " ".isspace():
    print("is a whitespace")
else:
    print("is not a whitespace")

#The isupper() method is the upper-case version of islower() – it concentrates on upper-case letters only.
if "STEPHEN".isupper():
    print("is an uppercase string")
else:
    print("is not an uppercase string")

#the join() method performs a join especially among list
print(",".join(["Ugota", "Chisom", "Stephen"]))

#The lower() method makes a copy of a source string, replaces all upper-case letters with their lower-case counterparts
if "STEPHEN".lower():
    print("i converted this to lowercase all through")
else:
    print("i couldn't do conversion to lowercase")

#The rstrip() method in Python is used to remove any trailing (or right-side) whitespace characters from a string.
if "    steve    ".rstrip():
    print("i removed all right sided trailing whitespace")
else:
    print("i couldn't removed all right sided trailing whitespace")

#the startswith() method checks if a given string starts with the specified substring.
if "STEPHEN".startswith("ST"):
    print("the startswith method is wosrking")
else:
    print("the startswith method is not working")

#strip() method it makes a new string lacking all the leading and trailing whitespaces.
print("[" + "   ugota   ".strip() + "]")

#swapcase() method makes a new string by swapping the cases of all letters within the source string: lower-case characters become upper-case, and vice versa.
print("hello my name IS Stephen CHISOM ugota".swapcase())

#title() method it changes every word's first letter to upper-case, turning all other ones to lower-case.
print("my name is ugota chisom stephen".title())

#upper() method makes a copy of the source string, replaces all lower-case letters with their upper-case counterparts, and returns the string as the result.
print("stephen you are a great guy and a legend in the making and a champion".upper())

