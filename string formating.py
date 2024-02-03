def print_formatted(number):
    # "": decimal
    # x: hexadecimal
    # o: octal
    # b: binary
    bases = ["", "x", "o", "b"]
    numbers_formatted = [format(number, x).upper() for x in bases]

    return " ".join(numbers_formatted)
print(print_formatted(11))