pip install cryptography


from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(message, private_key):
    
    return private_key.sign(
        data=message,
        padding=padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        algorithm=hashes.SHA256(),
    )


def verify_signature(message, signature, public_key):
    try:
        public_key.verify(
            signature,
            data=message,
            padding=padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            algorithm=hashes.SHA256(),
        )
        return True
    except Exception:
        return False


if __name__ == "__main__":
    print("Welcome to the Digital Signature Program!")
    
    # Generate keys
    private_key, public_key = generate_keys()
    print("Keys generated successfully.")

    while True:
        print("\nOptions:")
        print("1. Sign a message")
        print("2. Verify a signature")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            message = input("Enter the message to sign: ").encode()
            signature = sign_message(message, private_key)
            print(f"Message signed successfully. Signature: {signature.hex()}")

        elif choice == "2":
            message = input("Enter the original message: ").encode()
            signature_hex = input("Enter the signature (in hex): ")
            try:
                signature = bytes.fromhex(signature_hex)
                is_valid = verify_signature(message, signature, public_key)
                print("Signature is valid!" if is_valid else "Invalid signature.")
            except ValueError:
                print("Invalid signature format. Please provide a valid hex string.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
