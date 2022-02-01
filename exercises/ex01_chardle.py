"""EX01 - Chardle - A cute step toward wordle."""

__author__ = "730325952"

chosen_word: str = input("Enter a 5-character word:")
if len(chosen_word) != 5:
    print("Error: Word must contain 5 characters.")
    quit()
chosen_letter: str = input("Enter a single character:")
if len(chosen_letter) != 1:
    print("Error: Character must be a single character.")
    quit()
print("Searching for " + chosen_letter + " in " + chosen_word)
counter_for_matches: int = 0
if chosen_letter == chosen_word[0]:
    print(chosen_letter + str(" found at index 0"))
    counter_for_matches = counter_for_matches + 1
if chosen_letter == chosen_word[1]:
    print(chosen_letter + str(" found at index 1"))
    counter_for_matches = counter_for_matches + 1
if chosen_letter == chosen_word[2]:
    print(chosen_letter + str(" found at index 2"))
    counter_for_matches += 1
if chosen_letter == chosen_word[3]:
    print(chosen_letter + str(" found at index 3"))
    counter_for_matches += 1
if chosen_letter == chosen_word[4]:
    print(chosen_letter + str(" found at index 4"))
    counter_for_matches += 1
if counter_for_matches == 1:
    print(str(counter_for_matches) + " instance of " + chosen_letter + " found in " + chosen_word)
else:
    if counter_for_matches > 1:
        print(str(counter_for_matches) + " instances of " + chosen_letter + " found in " + chosen_word)
    else: 
        print("No instances of " + chosen_letter + " found in " + chosen_word)
