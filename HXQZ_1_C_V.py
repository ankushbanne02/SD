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