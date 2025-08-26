'''
def calculate_love_score(name1,name2):
    first= ['t','r','u','e']
    second=['l','o','v','e']
    total1 = 0
    total2 = 0
    total3 = 0

    for letter in name1.lower():
        if letter in first:
            total1 += 1
        else:
            total1 += 0

    for letter in name2.lower():
        if letter in first:
            total1 += 1
        else:
            total1 += 0

        print(total1)

    print('----------------------------------')

    for letter in name1.lower():
        if letter in second:
            total2 += 1
        else:
            total2 += 0

    for letter in name2.lower():
        if letter in second:
            total2 += 1
        else:
            total2 += 0

        print(total2)

    print('----------------------------------')

    love_score = f"{total1}{total2}"
    print(love_score)

calculate_love_score("Kanye West", "Kim Kardashian")
'''




