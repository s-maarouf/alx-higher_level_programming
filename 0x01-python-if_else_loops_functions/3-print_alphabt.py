#!/usr/bin/python3
for ascii_val in range(97, 123):
    alpha = chr(ascii_val)
    if chr(ascii_val) not in ['q', 'e']:
        print("{}".format(alpha), end='')
