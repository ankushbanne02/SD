def rail_fence_encrypt(plaintext, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    for char in plaintext:
        fence[rail].append(char)
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
    return ''.join([''.join(rail) for rail in fence])


def rail_fence_decrypt(ciphertext, rails):
    # Create an empty matrix with placeholders
    pattern = [['' for _ in range(len(ciphertext))] for _ in range(rails)]

    # Mark the zigzag pattern
    rail = 0
    direction = 1
    for i in range(len(ciphertext)):
        pattern[rail][i] = '*'
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1

    # Fill the matrix with ciphertext
    index = 0
    for r in range(rails):
        for c in range(len(ciphertext)):
            if pattern[r][c] == '*' and index < len(ciphertext):
                pattern[r][c] = ciphertext[index]
                index += 1

    # Read the matrix in zigzag to get the plaintext
    rail = 0
    direction = 1
    result = ''
    for i in range(len(ciphertext)):
        result += pattern[rail][i]
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1

    return result


# Input
plaintext = input("Enter plaintext: ")
rails = int(input("Enter number of rails: "))

# Encryption
ciphertext = rail_fence_encrypt(plaintext, rails)
print("Encrypted:", ciphertext)

# Decryption
decrypted = rail_fence_decrypt(ciphertext, rails)
print("Decrypted:", decrypted)



ROW Columpnar 

import math

def encrypt(text, key):
    """Encrypts the text using row-columnar transposition cipher."""
    text = text.replace(" ", "").upper()  
    col = len(key)  
    row = math.ceil(len(text) / col)  

    
    matrix = [['' for _ in range(col)] for _ in range(row)]
    idx = 0
    for r in range(row):
        for c in range(col):
            if idx < len(text):
                matrix[r][c] = text[idx]
                idx += 1

   
    cipher_text = ""
    for num in sorted(key): 
        col_idx = key.index(num)  
        cipher_text += "".join(matrix[r][col_idx] for r in range(row))

    return cipher_text

def decrypt(cipher, key):
    
    col = len(key)
    row = math.ceil(len(cipher) / col)

    
    matrix = [['' for _ in range(col)] for _ in range(row)]
    idx = 0
    for num in sorted(key):  
        col_idx = key.index(num)
        for r in range(row):
            if idx < len(cipher):
                matrix[r][col_idx] = cipher[idx]
                idx += 1

    
    plain_text = "".join("".join(row) for row in matrix)
    return plain_text


key = "3142" 
text = input("Enter text: ")
cipher = encrypt(text, key)
print("Cipher Text:", cipher)

decrypted_text = decrypt(cipher, key)
print("Decrypted Text:", decrypted_text)
