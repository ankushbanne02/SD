pip install pycryptodome


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()

    key = key.ljust(16)[:16].encode()  # Ensure key is exactly 16 bytes
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))

    # Save the encrypted data along with IV in a .txt file
    encrypted_file_path = file_path + ".enc.txt"
    with open(encrypted_file_path, 'wb') as f:
        f.write(iv + encrypted_data)

    print(f"File encrypted and saved as: {encrypted_file_path}")

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    key = key.ljust(16)[:16].encode()  # Ensure key is exactly 16 bytes
    iv, encrypted_data = encrypted_data[:16], encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    # Save the decrypted data to a .txt file
    original_file_path = file_path.replace(".enc.txt", "_decrypted.txt")
    with open(original_file_path, 'wb') as f:
        f.write(decrypted_data)

    print(f"File decrypted successfully and saved as: {original_file_path}")

def main():
    print("AES File Encryption/Decryption")
    choice = input("Choose an option (encrypt/decrypt): ").strip().lower()
    file_path = input("Enter the full path to the file: ").strip()
    key = input("Enter the key (max 16 characters): ").strip()

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
