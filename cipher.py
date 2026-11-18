"""
Caesar cipher program with a shift of 15
Encodes a message by shifting letters 15 places forward.
Spaces and punctuation remain unchanged.
"""


def encode(text):
    """
    Encodes a message using a Caesar cipher with a shift of 15.
    letters wrap around the alphabet.Spaces and punctuation stay the same
    """
    result = ""
    shift = 15

    for char in text:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')

            # Convert to 0 - 25, shift , wrap with 26 % , convert back
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char  # keep spaces , punctuation , etc.

    return result


user_message = input("enter the message to encode: ")
encoded = encode(user_message)
print("Encoded message:", encoded)
