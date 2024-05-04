import os

import numpy as np
import math
from sympy import Matrix
from egcd import egcd

bcc = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'

# Chuyển chữ thành số
CharToNum = dict(zip(bcc, range(len(bcc))))

# Chuyển số thành chữ
NumToChar = dict(zip(range(len(bcc)), bcc))


# Tìm ma trận phụ hợp
def adj_matrix(matrix_k):
    n = matrix_k.shape[0]
    pb = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            mt_con = np.delete(np.delete(matrix_k, i, axis=0), j, axis=1)
            pb[i][j] = np.linalg.det(mt_con) * pow(-1, i + j)

    adj = pb.T
    return adj


# Ma trận nghịch đảo theo modulo
def inverse(matrix_k, modulo):
    det = int(np.round(np.linalg.det(matrix_k)))
    inverse_det = egcd(det, modulo)[1] % modulo
    inverse_K = inverse_det * adj_matrix(matrix_k)

    return inverse_K


# Giải mã
def decrypt(matrix_k, enciphered):
    deciphered = ''
    enciphered_number = []

    for letter in enciphered:
        enciphered_number.append(CharToNum[letter])

    enciphered_number_s = [enciphered_number[i:i + int(matrix_k.shape[0])] for i in
                           range(0, len(enciphered_number), int(matrix_k.shape[0]))]

    for i in enciphered_number_s:
        i = np.transpose(np.asarray(i))[:, np.newaxis]
        numbers = np.dot(matrix_k, i) % len(bcc)
        n = numbers.shape[0]

        for j in range(n):
            num = np.round(numbers[j, 0])
            if num > 25:
                num = 0
            deciphered += NumToChar[num]

    return deciphered


K = np.matrix([[1, 2, -1],
               [2, 5, -3],
               [3, 7, -5]])

# Open the text.txt file and read the code from the file (2)
with open("text.txt") as file:
    code = file.read()

K = inverse(K, len(bcc))

message = decrypt(K, code)

# Open the text.txt file and write the msg to the file (3)
with open("text.txt", "w") as file:
    file.write(message)

print("The message is:",message)