

timeValue = input("Insert a time: ")
inttimeValue = int(timeValue)
hour = 0

while (inttimeValue < 0):
    print("Time Value must be positive")
while (inttimeValue > 0 & inttimeValue < 60):
    print("Calculated Time Value: 0:" + inttimeValue)
while (inttimeValue > 60):
        inttimeValue -= 60
        hour += 1
        print("Calculated Time Value: " + hour + ":" + inttimeValue)
print(type(inttimeValue))
print("Thanks for seeing this")
