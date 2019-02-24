def print_elem(elem_code):
    print("{:6d} {}".format(elem_code, chr(elem_code)), end="")
    return


first_elem = 32
last_elem = 127

elem_code = first_elem

while elem_code <= last_elem:
    print_elem(elem_code)
    elem_code += 1
    if (elem_code-first_elem) % 10 == 0:
        print()
