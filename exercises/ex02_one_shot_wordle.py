"""One shot wordle."""

__author__ = "730325952" 


secret_word: str = "python"
chosen_word: str = input(f"What is your {len(secret_word)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji: str = ""
idx: int = 0
alt_idx: int = 0 

while len(chosen_word) != len(secret_word):
    chosen_word = input(f"That was not {len(secret_word)} letters! Try again: ")
while idx < len(secret_word): 
    # establishing a while loop to check if the chosen word and secret word are the same/similar.   
    if chosen_word[idx] == secret_word[idx]:
        emoji += GREEN_BOX 
    # ^if-else statement used to see if the letters and their placement are the exact same,
    # eventually leads to all green boxes if guess is correct.
    else:
        while alt_idx < len(secret_word):
            if chosen_word[idx] == secret_word[alt_idx]:
                emoji += YELLOW_BOX 
            alt_idx += 1
        # ^ while loop used to go through each of the secret's letters to see if any match up
        # with the chosen's letters, placement in secret does not matter. Goes through each 
        # idx value because it is a nested while loop.
        if idx == len(emoji):
            emoji += WHITE_BOX
        # if statement used to see if a yellow box was added, if not idx does == len(emoji) and 
        # a whitebox is added there 
    idx += 1
    # used to make sure the while loop that most everything is nested in is not an infinite loop
    alt_idx = 0
    # must be reset each time because each idx value of chosen_word needs to be evaluated 
    # starting at secret_word[0]. 
print(emoji)
# prints the entire emji string after exiting the while loop to see if the secret word and
# chosen word were the same, had some similar letters, or were completely different.   
if chosen_word != secret_word:
    print("Not quite. Play again soon! ")
if chosen_word == secret_word: 
    print("Woo! You got it!")
