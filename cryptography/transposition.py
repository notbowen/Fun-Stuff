# Transposition Cipher in Python

# Libraries
import math

# Get input from user
plaintext = input("Enter text to encrypt: ")
key = list(input("Enter key: "))

# Put plaintext into array
plaintext_array = []
for i in range(math.ceil(len(plaintext) / len(key))):
    plaintext_array.append(list(plaintext[i*len(key):i*len(key)+len(key)]))
    
# Fill in empty parts of array
while len(plaintext_array[-1]) != len(plaintext_array[0]):
    plaintext_array[-1].append("")

# Flip array across its axis
plaintext_array = list(zip(*plaintext_array))

dic = []
for letter, corresponding in zip(key, plaintext_array):
    dic.append([letter, corresponding])
dic.sort()

# Print out ciphertext
for letter, text in dic:
    print("".join(text), end=" ")
