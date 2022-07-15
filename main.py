import math

import dictionary


def main():
    word_length = 5

    words_response = dictionary.word_list[:]

    for _ in range(6):
        min_chars = {i: 0 for i in "abcdefghijklmnopqrstuvwxyz"}
        max_chars = {i: math.inf for i in "abcdefghijklmnopqrstuvwxyz"}

        probability = 100 / len(words_response)
        guess = words_response.pop(0)

        print(f"Guess: {guess} (P = {probability}%)")
        output = input("Enter colors (G for green, Y for yellow, X for gray): ").lower()

        while output == "-":
            guess = words_response.pop(0)
            print(f"Guess: {guess} (P = {probability}%)")
            output = input("Enter colors (G for green, Y for yellow, X for gray): ").lower()

        if output == "ggggg":
            print("You win!!!!!")
            exit(0)

        for i in range(word_length):
            the_c = guess[i]
            if output[i] == "g":
                words_response = [word_guess for word_guess in words_response if word_guess[i] == the_c]
                min_chars[the_c] += 1
        for i in range(word_length):
            the_c = guess[i]
            if output[i] == "y":
                words_response = [word_guess for word_guess in words_response if word_guess[i] != the_c]
                min_chars[the_c] += 1
        for i in range(word_length):
            the_c = guess[i]
            if output[i] == "x":
                words_response = [word_guess for word_guess in words_response if word_guess[i] != the_c]
                max_chars[the_c] = min_chars[the_c]
        for i in range(word_length):
            the_c = guess[i]
            words_response = [
                word_guess for word_guess in words_response
                if min_chars[the_c] <= word_guess.count(the_c) <= max_chars[the_c]
            ]
    print("You lose... how do you lose if you have a bot that can solve this game??!?!?!")
    exit(0)


if __name__ == "__main__":
    main()
