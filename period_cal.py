#this is a program that gives the time duration for an event

hours = int(input("Enter a starting hour: "))
Min = int(input("Enter a starting minutes: "))
dur = int(input("Enter event duration(minute): "))

# we are get the total number of minutes

Min = Min + dur

# we are gonna get the hours hidden in minutes and it will be updated

hours = hours + dur // 60

# we are gonna make sure minute fall in the range of 0 - 59

Min = Min % 60

#we are gonna make sure that hours fall in the range of 0 - 23

hours = hours % 24

print(hours, Min, sep=":")

