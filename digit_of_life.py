#digit of life

user_date = input("Enter your birthday date in this format: YYYYMMDD or YYYYDDMM: ")
if len(user_date) != 8 and not user_date.isdigit():
    print("invalid character inputted")

else:
    while len(user_date) > 1:
        total = 0
        for i in user_date:
            total += int(i)
        print(user_date)
        user_date = str(total)
    print("your digit of life is: " + user_date)

