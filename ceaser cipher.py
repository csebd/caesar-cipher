def caesar_encrypt(plaintext, key):
    '''Encrypts plaintext using a Caesar Cipher with a given key.'''
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shifted = (ord(char) - 65 + key) % 26
            ciphertext += chr(shifted + 65)
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, key):
    '''Decrypts ciphertext using a Caesar Cipher with a given key.'''
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = (ord(char) - 65 - key) % 26
            plaintext += chr(shifted + 65)
        else:
            plaintext += char
    return plaintext
plaintext = "A SOFTWARE DEVELOPER"
key = 3

ciphertext = caesar_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted = caesar_decrypt(ciphertext, key)
print("Decrypted plaintext:", decrypted)
