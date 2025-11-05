#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

bool check_digit_luhn(unsigned long long number) {
    int digits[16];
    int total = 0;

    // Extract digits from the number
    for (int i = 15; i >= 0; i--) {
        digits[i] = number % 10;
        number /= 10;
    }

    // Apply Luhn algorithm
    for (int i = 15; i >= 0; i--) {
        int digit = digits[i];
        if ((15 - i) % 2 == 1) { // Double every second digit from the right
            digit *= 2;
            if (digit > 9)
                digit -= 9;
        }
        total += digit;
    }

    return total % 10 == 0;
}

int main() {
    srand(time(NULL));
    while (1) {
        unsigned long long card_number = 0;

        // Generate a random 16-digit number
        for (int i = 0; i < 16; i++) {
            card_number = card_number * 10 + (rand() % 10);
        }

        if (check_digit_luhn(card_number)) {
            printf("Valid number: %llu\n", card_number);
            //break; // Remove this line if you want it to keep generating
        }
    }

    return 0;
}