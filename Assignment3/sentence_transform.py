#!/usr/bin/env python3

# Function to convert text to all CAPITAL letters
def all_caps(text):
    return text.upper()

# Function to convert text to all SMALL letters
def all_small(text):
    return text.lower()

# Function to capitalize the first letter of each word
def first_letter_caps(text):
    words = text.split()
    result = " ".join(word.capitalize() for word in words)

    return result

# Function to make alternate letters of a word CAPITAL, starting of the word is always CAPITAL
def alternate_word_caps(text):
    words = text.split()
    result = ""

    for word in words:
        caps_word = ""
        for i in range(len(word)):
            if i % 2 == 0:
                caps_word += word[i].upper()
            else:
                caps_word += word[i]
        
        result += word[0].upper() + caps_word[1:] + " "

    return result.rstrip()

# Function to make alternate letters CAPITAL
def alternate_caps(text):
    result = ""

    for i in range(len(text)):
        if i % 2 == 0:
            result += text[i].upper()
        else:
            result += text[i]
    
    return result.rstrip()

# Get user input
text = input("Enter text:")

caps = all_caps(text)
small = all_small(text)
first_caps = first_letter_caps(text)
alt_word_caps = alternate_word_caps(text)
alt_letter_caps = alternate_caps(text)

print(f"\nALL CAPITAL: {caps}")
print(f"All small: {small}")
print(f"First letter of each word CAPITAL: {first_caps}")
print(f"Alternate letters of a word CAPITAL, starting of the word is always CAPITAL: {alt_word_caps}")
print(f"Alternate letters CAPITAL: {alt_letter_caps}")