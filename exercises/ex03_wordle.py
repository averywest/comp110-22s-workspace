"""Structured Wordle."""

_author_ = "730325952"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(secret_string: str, guess_character: str) -> bool:
    """Detecting the character in the word."""
    assert len(guess_character) == 1
    x: int = 0
    i: int = 0
    while x < len(secret_string):
        if secret_string[x] == guess_character:
            i += 1
        x += 1
    if i >= 1:
        return True 
    return False


def emojified(guess: str, secret: str) -> str:
    """Generates emojis for corresponding characters of guess."""
    assert len(guess) == len(secret)
    idx: int = 0
    emoji: str = ""
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            emoji += GREEN_BOX
        else:
            c: bool = contains_char(secret, guess[idx])
            if c:
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        idx += 1
    return emoji


def input_guess(number_characters: int) -> str:
    """Ensures the guess is 5 characters."""
    guess: str = input(f"Enter a {number_characters} character word: ")
    while len(guess) != number_characters:
        guess = input(f"That wasn't {number_characters} chars! Try again: ")
    else:
        return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    guess: str = ""
    total_left: int = 1
    while total_left <= 6 and guess != secret:
        print(f"=== Turn {total_left}/6 ===")
        guess: str = input_guess(5)
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {total_left}/6 turns!")
        total_left += 1
    if total_left > 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
    