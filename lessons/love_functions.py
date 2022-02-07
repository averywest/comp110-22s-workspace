"""Function Definition Practice."""


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    x: int = 0
    while x < n:
        love_note += love(to) + "\n"
        x += 1
    return love_note
