import random
def check_digit_luhn(number):
    digits = [int(d) for d in str(number)]
    total = 0
    reverse_digits = digits[::-1]
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:  # Double every second digit
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total % 10 == 0  # Valid if total divisible by 10

# Example use:
while True:
    card_number = random.randint(0, 9999999999999999)
    if check_digit_luhn(card_number):
        print(f"Valid number {card_number}")