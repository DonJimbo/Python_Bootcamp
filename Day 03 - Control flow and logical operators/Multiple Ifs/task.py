print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets $7.")
    else:
        bill = 12
        print("Adult tickets $12.")

    wants_photo= input("If you want a photo? y for Yes, n for No")
    if wants_photo == "y":
        #Add 3 USD to their bill
        bill += 3
        print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
