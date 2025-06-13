def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)
choice = input("Type 'e' to encrypt or 'd' to decrypt: ").strip().lower()
text = input("Enter the text: ")
shift = int(input("Enter the shift value (e.g., 3): "))

if choice == 'e':
    print("Encrypted text:", encrypt(text, shift))
elif choice == 'd':
    print("Decrypted text:", decrypt(text, shift))
else:
    print("Invalid choice. Please enter 'e' or 'd'.")