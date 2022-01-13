# python3

import sys

# Using classes to keep track of brackets and their positions
class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        """Class method to compare bracket type to input character and return True if they are a matching pair"""
        if self.bracket_type == ']' and c == '[':
            return True
        if self.bracket_type == '}' and c == '{':
            return True
        if self.bracket_type == ')' and c == '(':
            return True
        return False

# Main code:
if __name__ == "__main__":
    text = input()
    opening_brackets_stack = []
    open_bracket_key_stack = []

    # nested for loop; enumerate starts at 1 because assignment required 1-based index
    for key, char in enumerate(text, start=1):
        if char == '(' or char == '[' or char == '{':
            # Process opening bracket, push to stack
            opening_brackets_stack.append(char)
            open_bracket_key_stack.append(key)

        if char == ')' or char == ']' or char == '}':
            # Process closing bracket
            closeBracket = Bracket(char, key)

            # if the first character in the text is a closing bracket, we already know it's unbalanced
            if key == 1:
                print(f"Text is unbalanced! Look at position {1}.")

            # otherwise, compare the closing bracket to the top of the stack
            match = closeBracket.Match(opening_brackets_stack.pop())
            if match == True:
                open_bracket_key_stack.pop()
            elif match == False:
                print(f"Text is unbalanced! Look at position {key}.")

    # outside of loop, check if stack is empty:
    if len(opening_brackets_stack) == 0:
        print("Success! Text is balanced.")
    else:
        print(f"Text is unbalanced! Look at position {open_bracket_key_stack[-1]}.")

    # Printing answer, write your code here
