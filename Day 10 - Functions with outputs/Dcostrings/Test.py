
def is_leap_year(year):
    f_test = year / 4
    s_test = year / 100
    t_test = year / 400
    if f_test % 1 == 0:
        print(year / 4)
        if s_test % 1 == 0:
            print(year / 100)
            if t_test % 1 == 0:
                print(year / 400)
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap_year(int(2000)))
