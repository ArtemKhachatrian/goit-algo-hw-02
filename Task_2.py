from collections import deque

def is_palindrome(text: str) -> bool:
    chars = deque(text.lower().replace(" ", ""))

    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False

    return True

# I'm willing to bet that this is the best solution to this problem
if __name__ == "__main__":
    text = input("Your input: ")

    if is_palindrome(text):
        print("It`s palindrome")
    else:
        print("It`s not palindrome")
