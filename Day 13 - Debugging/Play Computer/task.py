year = int(input("What's your year of birth?"))
if (year > 1980) is True:
    print("1")
elif (year < 1994) is True:
    print("2")
if (year > 1994) is True:
    print("3")

if year > 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
elif year < 1980:
    print("You are OLD!")