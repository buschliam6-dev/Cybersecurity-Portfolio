Caesar Cipher Encryption

Project Overview

This project implements a Caesar Cipher encryption program using Python. The program encrypts user-provided messages by shifting alphabetical characters 15 positions forward in the alphabet.

The Caesar Cipher is a classical encryption technique that demonstrates the basic principles of substitution ciphers and introductory cryptography.

Features

- Encrypts messages using a fixed shift of 15 positions.
- Preserves uppercase and lowercase letters.
- Handles alphabet wrapping from Z back to A.
- Preserves spaces, punctuation, and other non-alphabetical characters.
- Accepts user input through the terminal.
- Displays the resulting encrypted message.

Technologies Used

- Python 3
- Visual Studio Code

How It Works

The program uses Python's built-in "ord()" and "chr()" functions to convert alphabetical characters into numerical values and back again.

A modulo operation ("% 26") ensures that letters wrap around the alphabet when the shift exceeds the final letter.

Non-alphabetical characters are added to the result without modification.

How to Run

1. Make sure Python 3 is installed.
2. Open the project in Visual Studio Code.
3. Open the terminal.
4. Run the following command:

python cipher.py

5. Enter a message when prompted.
6. The program displays the encrypted message.

Learning Outcomes

Through this project, I gained practical experience with:

- Basic cryptography concepts.
- Classical substitution encryption.
- Python string manipulation.
- Conditional statements and loops.
- Character encoding using "ord()" and "chr()".
- Modular arithmetic and alphabet wrapping.
- User input and output.

Security Considerations

The Caesar Cipher is a basic historical encryption technique and is not suitable for protecting sensitive information. Its fixed substitution pattern makes it vulnerable to brute-force attacks and frequency analysis.

This project is intended for educational purposes to demonstrate introductory encryption concepts.

Project Scope

This implementation focuses on message encryption using a fixed Caesar Cipher shift of 15 positions. Decryption functionality is not included in the current implementation.
