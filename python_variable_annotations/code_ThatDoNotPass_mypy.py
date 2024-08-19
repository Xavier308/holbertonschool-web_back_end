def add_numbers(a: int, b: int) -> int:
    # The function is supposed to return an int, but it returns a string instead
    return "The sum is: " + str(a + b)

# This function call expects integer arguments, but strings are provided
result = add_numbers("three", "five")
