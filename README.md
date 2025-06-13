# PRODIGY_CS_01
# 🔐 Caesar Cipher in Python

This is a simple implementation of the **Caesar Cipher**, one of the oldest and easiest encryption techniques. It includes both **encryption** and **decryption** functionalities using a basic shift value.

## 📌 What is Caesar Cipher?

The **Caesar Cipher** is a type of substitution cipher in which each letter in the plaintext is shifted a fixed number of positions in the alphabet. For example, with a shift of 3:

- `A` becomes `D`
- `B` becomes `E`
- `X` becomes `A` (wraps around the alphabet)

This technique is named after **Julius Caesar**, who used it in his private correspondence.

---

## 🔧 How It Works

The script uses two main functions:
- `encrypt(text, shift)` – Encrypts the input text by shifting letters forward in the alphabet.
- `decrypt(text, shift)` – Decrypts by reversing the shift.

✅ Features:
- Supports **both uppercase and lowercase** letters.
- **Non-alphabet characters** (spaces, punctuation, numbers) are preserved as-is.
- Easy to modify for different shift values or variations of the cipher.

📂 How to Run
- Save the code to a file named caesar_cipher.py.

Run using Python 3:
`python caesar_cipher.py `

🔒 Use Cases
- Educational tool for learning about classical cryptography.
- Teaching modular arithmetic and ASCII manipulation in Python.
- Light obfuscation of text (not suitable for real security).



---

## ▶️ Example Usage

```python
plain_text = "Hello, World!"
shift = 3

encrypted = encrypt(plain_text, shift)
decrypted = decrypt(encrypted, shift)

print("Plain Text :", plain_text)
print("Encrypted  :", encrypted)
print("Decrypted  :", decrypted)
