#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    count = 0
    try:
        for i in my_list:
            print(i, end="")
            count += 1
            if count == x:
                break
    except IndexError:
        pass
    print()
    return count
