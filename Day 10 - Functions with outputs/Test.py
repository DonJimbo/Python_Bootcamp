def is_leap_year(year):

    f_test = year / 4
    s_test = year / 100
    t_test = year / 400

    if f_test is not float:
        print(f_test)
        if s_test is not float:
            print(s_test)
            if t_test is not float:
                print(t_test)
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap_year(int(input("What is your year"))))