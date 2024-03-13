from collections import deque

DIGITS_TO_LETTERS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convert_string_to_digit(string: str) -> int:
    if len(string) > 1:
        raise ValueError("Expected a string with length 1.")

    index = DIGITS_TO_LETTERS.find(string)
    if index == -1:
        raise IndexError("Expected a number 0-9 or letter A-Z.")

    return index

def convert_digit_to_string(digit: int) -> str:
    if digit < 0:
        raise ValueError("Expected a digit greater than zero.")
    if digit > 35:
        raise ValueError("Digit too large to convert to string representation.")
    return DIGITS_TO_LETTERS[digit]

def convert_digits_to_string(digits: deque) -> str:
    string = ""
    for digit in digits:
        string += convert_digit_to_string(digit)
    return string

def convert_base_n_to_base_10(base: int, number: str) -> int:
    base_10_number = 0
    for i, string in enumerate(reversed(number.upper())):
        digit = convert_string_to_digit(string)
        if digit >= base:
            raise IndexError("One of the digits was greater than the base.")
        base_10_number += digit * base ** i

    return base_10_number

def convert_base_10_to_base_n(base: int, number: int) -> str:
    base_n_number = deque()
    remainder = 0
    quotient = number
    while quotient != 0:
        remainder = quotient % base
        quotient = quotient // base
        base_n_number.appendleft(remainder)

    string = convert_digits_to_string(base_n_number)
    return string

def convert_base_m_to_base_n(base_m: int, base_n, number: str) -> str:
    base_10_number = convert_base_n_to_base_10(base=base_m, number=number)
    base_n_number = convert_base_10_to_base_n(base=base_n, number=base_10_number)
    return base_n_number

base_10_number = convert_base_n_to_base_10(base=16, number="AE14F2")
print(base_10_number)
base_10_number = convert_base_n_to_base_10(base=8, number="267102")
print(base_10_number)

base_16_number = convert_base_10_to_base_n(base=16, number=11408626)
print(base_16_number)
base_8_number = convert_base_m_to_base_n(base_m=16, base_n=8, number="AE14F2")
print(base_8_number)
