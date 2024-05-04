# source: https://github.com/sympy/sympy/blob/d2be7bacd2604e98a642f74028e8f0d7d6084f78/sympy/crypto/crypto.py#L788-L880

# import everything from sympy module
from sympy import Matrix
from sympy import shape
from sympy import Array
import os

# create a conventional table
# conventional_table = {'Z': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
#                       'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
#                       'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
#                       'X': 24, 'Y': 25}

conventional_table = {'Z': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
                      'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
                      'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                      'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25}


Key = Matrix([[1, 2, -1],   # create a key matrix that will be used to encipher and decipher the message
              [2, 5, -3],
              [3, 7, -5]])

# input the sender's message, delete the blanks and put it to msg, then capitalize
# Open the text.txt file and read the msg from the file (2)
with open("text.txt") as file:
    sender_msg = file.read()

temp_msg = ""
for i in sender_msg :
    temp_msg += i
msg = temp_msg.upper()
# print("msg: ", msg)

# create a list that stores all the convert char in the msg string
msg_list = []
for i in msg :
    if i in conventional_table :
        msg_list.append(conventional_table.get(i))
# print("msg_list: ", msg_list)

# create a matrix 3xn where n = (len(msg_list) + (3 - (len(msg_list) % 3))) / 3
n = int((len(msg_list) + (3 - (len(msg_list) % 3))) / 3)
converted_msg_matrix = Matrix.zeros(3, n)
for col in range(n):    # fill the matrix from column to column
    for row in range(3):
        if col * 3 + row < len(msg_list):
            converted_msg_matrix[row, col] = msg_list[col * 3 + row]
        else:
            break
# print("converted_msg_matrix: ", converted_msg_matrix)

# multiply the Key matrix with the converted_msg_matrix to get the encrypted_matrix
# then check if the value exceed [0; 26]
encrypted_matrix = Key * converted_msg_matrix
# print("encrypted_matrix: ", encrypted_matrix)

for col in range(n):
    for row in range(3):
        if encrypted_matrix[row, col] > 25:
            encrypted_matrix[row, col] = encrypted_matrix[row, col] % 26
        elif encrypted_matrix[row, col] < 0:
            encrypted_matrix[row, col] = (encrypted_matrix[row, col] + 26) % 26
        else:
            continue
# print("encrypted_matrix: ", encrypted_matrix)


# put the encrypted_matrix into the encrypted_msg and print the encrypted message
encrypted_msg = ""
for col in range(n):
    for row in range(3):
        for key, value in conventional_table.items():
            if encrypted_matrix[row, col] == value:
                encrypted_msg += key

print("encrypted message:", encrypted_msg)

# Open the text.txt file and write the code to the file (3)
with open("text.txt", "w") as file:
    file.write(encrypted_msg)