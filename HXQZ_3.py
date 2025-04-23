pip install pycryptodome

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt_file(file_path, key):
    key = key.ljust(8)[:8].encode()  # Ensure the key is exactly 8 bytes (DES uses 56-bit key)
    
    with open(file_path, 'rb') as f:
        data = f.read()

    cipher = DES.new(key, DES.MODE_CBC)  # DES in CBC mode
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(data, DES.block_size))

    # Save the encrypted data along with IV in a .txt file
    encrypted_file_path = file_path + ".enc.txt"
    with open(encrypted_file_path, 'wb') as f:
        f.write(iv + encrypted_data)

    print(f"File encrypted and saved as: {encrypted_file_path}")

def decrypt_file(file_path, key):
    key = key.ljust(8)[:8].encode()  # Ensure the key is exactly 8 bytes (DES uses 56-bit key)
    
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    iv, encrypted_data = encrypted_data[:8], encrypted_data[8:]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), DES.block_size)

    # Save the decrypted data to a .txt file
    original_file_path = file_path.replace(".enc.txt", "_decrypted.txt")
    with open(original_file_path, 'wb') as f:
        f.write(decrypted_data)

    print(f"File decrypted successfully and saved as: {original_file_path}")

def main():
    print("DES File Encryption/Decryption")
    choice = input("Choose an option (encrypt/decrypt): ").strip().lower()
    file_path = input("Enter the full path to the file: ").strip()
    key = input("Enter the key (max 8 characters): ").strip()

    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        return

    if choice == 'encrypt':
        encrypt_file(file_path, key)
    elif choice == 'decrypt':
        if not file_path.endswith(".enc.txt"):
            print("Error: The provided file is not a valid encrypted .txt file.")
            return
        decrypt_file(file_path, key)
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
