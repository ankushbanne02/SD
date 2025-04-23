def encrypt(text, s):
    result = ""
    decrypt = ""
    
    # Encryption logic
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + s) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + s) % 26 + 97)
        else:
            result += char  # Keep spaces and special characters unchanged

    # Decryption logic
    for char in result:  # Decrypt from the encrypted text
        if char.isupper():
            decrypt += chr((ord(char) - 65 - s) % 26 + 65)
        elif char.islower():
            decrypt += chr((ord(char) - 97 - s) % 26 + 97)
        else:
            decrypt += char  # Keep spaces and special characters unchanged

    return result, decrypt

text = input("Enter text: ")
s = 4
cipher, dec = encrypt(text, s)

print("Text     : " + text)
print("Shift    : " + str(s))
print("Cipher   : " + cipher)
print("Decrypted: " + dec)



def vigenere_encrypt(text, key):
    
    key = key.lower()
    encrypted = []
    key_index = 0
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('a') if char.islower() else ord('A')
            encrypted.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            encrypted.append(char)
    
    return ''.join(encrypted)


text = input("Enter text: ")
key = input("Enter key: ")

encrypted_text = vigenere_encrypt(text, key)
print("Encrypted Text:", encrypted_text)




import numpy as np

def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")
    n = int(len(key) ** 0.5)  # Determine the size of the key matrix
    if len(text) % n != 0:
        text += 'X' * (n - len(text) % n)  # Padding with 'X'

    key_matrix = np.array(key).reshape(n, n)
    encrypted = ""
    
    for i in range(0, len(text), n):
        block = np.array([ord(char) - 65 for char in text[i:i + n]])
        result = np.dot(key_matrix, block) % 26
        encrypted += ''.join(chr(num + 65) for num in result)
    
    return encrypted

# Take key as space-separated input from user
key_input = input("Enter the key (as space-separated integers, e.g., '9 4 5 7'): ")
key = list(map(int, key_input.strip().split()))

plaintext = input("Enter Plain text: ")
ciphertext = hill_encrypt(plaintext, key)
print("Encrypted Text:", ciphertext)



def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")
    n = int(len(key) ** 0.5)  # Assuming square matrix for the key
    if len(text) % n != 0:
        text += 'X' * (n - len(text) % n)  # Padding with 'X' if needed

    # Reshaping the key into a matrix
    key_matrix = [key[i:i + n] for i in range(0, len(key), n)]
    
    encrypted = ""
    
    for i in range(0, len(text), n):
        block = [ord(char) - 65 for char in text[i:i + n]]
        result = []
        
        # Matrix multiplication of key_matrix and the block
        for row in key_matrix:
            sum_val = sum(row[j] * block[j] for j in range(n)) % 26
            result.append(sum_val)
        
        encrypted += ''.join(chr(num + 65) for num in result)
    
    return encrypted

# Taking input from the user
key_input = input("Enter the key (as a space-separated list of integers): ")
key = list(map(int, key_input.split()))

plaintext = input("Enter Plain text: ")
ciphertext = hill_encrypt(plaintext, key)
print("Encrypted Text:", ciphertext)



///Playfair Cipher 

def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix, seen = [], set()
    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    return [matrix[i*5:(i+1)*5] for i in range(5)]

def find_pos(matrix, letter):
    for r, row in enumerate(matrix):
        if letter in row:
            return r, row.index(letter)

def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(filter(str.isalpha, text))
    result, i = "", 0
    while i < len(text):
        result += text[i] + ("X" if i+1 < len(text) and text[i] == text[i+1] else "")
        i += 2 if i+1 < len(text) and text[i] != text[i+1] else 1
    return result + "X" if len(result) % 2 else result

def encrypt(text, key):
    matrix, text, cipher = generate_matrix(key), prepare_text(text), ""
    for a, b in zip(text[0::2], text[1::2]):
        r1, c1, r2, c2 = *find_pos(matrix, a), *find_pos(matrix, b)
        if r1 == r2:
            cipher += matrix[r1][(c1+1) % 5] + matrix[r2][(c2+1) % 5]
        elif c1 == c2:
            cipher += matrix[(r1+1) % 5][c1] + matrix[(r2+1) % 5][c2]
        else:
            cipher += matrix[r1][c2] + matrix[r2][c1]
    return cipher

def decrypt(cipher, key):
    matrix, text, plain = generate_matrix(key), cipher.upper(), ""
    for a, b in zip(text[0::2], text[1::2]):
        r1, c1, r2, c2 = *find_pos(matrix, a), *find_pos(matrix, b)
        if r1 == r2:
            plain += matrix[r1][(c1-1) % 5] + matrix[r2][(c2-1) % 5]
        elif c1 == c2:
            plain += matrix[(r1-1) % 5][c1] + matrix[(r2-1) % 5][c2]
        else:
            plain += matrix[r1][c2] + matrix[r2][c1]
    return plain

# Example Usage
key = "SECRET"
text = input("Enter text: ")
cipher_text = encrypt(text, key)
print("Cipher Text:", cipher_text)

# Decryption
plain_text = decrypt(cipher_text, key)
print("Decrypted Text:", plain_text)
