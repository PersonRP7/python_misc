def five():
    return 5

def seven(multiplication):
    return 7 * multiplication

def multiplication(number):
    return number

seven(multiplication(five())) #35
