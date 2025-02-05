import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list).upper()
print(chosen_word)
placeholder = ""
display = ""
count = 0
for position in range(len(chosen_word)):
    placeholder += "＿ "
print('\033[1m', placeholder, '\033[0m')

while count != len(chosen_word):
    # TODO-1: - Use a while loop to let the user guess again.
    guess = input("Guess a letter: ").upper()

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.
    for letter in chosen_word:
        if letter == guess:
            display += letter
            count = count + 1
        else:
            display += " ＿ "
    print('\033[1m', count, '\033[0m')
    print('\033[1m', display, '\033[0m')