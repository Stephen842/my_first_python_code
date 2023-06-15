#in this program i will be working on a distance converter to convert a miles to a kilometer and vice versa

miles = float(input("Enter your distance in miles: "))
kilometer = float(input("Enter your distance in kilometer: "))

miles_to_kilometer = miles * 1.61
kilometer_to_miles = kilometer / 1.61

print(miles, "the number of miles is ", round(miles_to_kilometer, 2), "kilometers")
print(kilometer, "the number of kilometer is ", round(kilometer_to_miles, 2), "miles")
