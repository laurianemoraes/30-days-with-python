print ("how old are you?")
age = input()
age = int(age)

monthsold = age * 12
daysold = age * 365
hoursold = age * 60
minutesold = hoursold * 60
secondsold = minutesold * 60

secondsold = str(secondsold)
print("you are: "  + secondsold  + " seconds old!")
