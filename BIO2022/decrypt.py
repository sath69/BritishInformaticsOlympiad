#Rating of Difficulty: 2/10
#Q1 2022 BIO - Decrypt

from itertools import product

alphaMap = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
    "E" : 5,
    "F" : 6,
    "G" : 7,
    "H" : 8,
    "I" : 9,
    "J" : 10,
    "K" : 11,
    "L" : 12,
    "M" : 13,
    "N" : 14,
    "O" : 15,
    "P" : 16,
    "Q" : 17,
    "R" : 18,
    "S" : 19,
    "T" : 20,
    "U" : 21,
    "V" : 22,
    "W" : 23,
    "X" : 24,
    "Y" : 25,
    "Z" : 26
}

def decrypt(code):
 encrypted_string = code
 encrypted = ""
 for x in range(1, len(encrypted_string)):
       decrypt = alphaMap[encrypted_string[x]] - alphaMap[encrypted_string[x-1]]
       if decrypt <= 0:
            decrypt += 26
       value = [i for i in alphaMap if alphaMap[i] == decrypt]
       encrypted += value[0]
 x = encrypted_string[0]
 x += encrypted
 return x 

#1 (b) ZZZZZ
#1 (c) for OLYMPIAD
#1 (d) 4394
def count(code):
 encrypted_string = code
 encrypted = ""
 counter = 0
 while encrypted != code:
    encrypted = ""
    for x in range(1, len(encrypted_string)):
       decrypt = alphaMap[encrypted_string[x]] - alphaMap[encrypted_string[x-1]]
       if decrypt <= 0:
            decrypt += 26
       value = [i for i in alphaMap if alphaMap[i] == decrypt]
       encrypted += value[0]
    encrypted_string = f"{encrypted_string[0]}{encrypted}"
    encrypted = encrypted_string
    counter += 1
 return counter 


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
maxCounter = 999999999999
unique = 0
p = product(alpha, repeat=3)
for x in p:
   perm = ''.join(x)
   n = count(perm)
   if maxCounter % n == 0:
      unique += 1


code = input()
print(decrypt(code))
