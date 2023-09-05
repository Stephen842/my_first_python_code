#Anagram

user = input("Enter your message: ")
user2 = input("Enter your message: ")

users1 = "".join(sorted(list(user.upper().replace(" ",""))))
users2 = "".join(sorted(list(user2.upper().replace(" ",""))))

if len(users1) > 0 and users1 == users2:
    print("this is an anagram")
else:
    print("not an anagram")

