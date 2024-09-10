def vigenere_cipher(text, key, mode='encrypt'):
    """
    Encrypts or decrypts the given text using the Vigenère cipher with the specified key.
    
    :param text: The plaintext or ciphertext to be encrypted or decrypted.
    :param key: The keyword used for encryption or decryption.
    :param mode: 'encrypt' for encryption, 'decrypt' for decryption.
    :return: The encrypted or decrypted text.
    """
    def shift_letter(letter, shift):
        if letter.isalpha():
            shift = shift % 26
            start = ord('A') if letter.isupper() else ord('a')
            return chr(start + (ord(letter) - start + shift) % 26)
        return letter

    def get_shifts(key):
        return [ord(char.upper()) - ord('A') for char in key]

    key_shifts = get_shifts(key)
    key_length = len(key_shifts)
    result = []
    
    for i, char in enumerate(text):
        shift = key_shifts[i % key_length]
        if mode == 'decrypt':
            shift = -shift
        result.append(shift_letter(char, shift))
    
    return ''.join(result)

# Example usage
if __name__ == "__main__":
    plaintext = "HELLO WORLD"
    key = "CAT"
    
    # Encrypt
    encrypted = vigenere_cipher(plaintext, key, mode='encrypt')
    print(f"Encrypted: {encrypted}")
    
    # Decrypt
    decrypted = vigenere_cipher(encrypted, key, mode='decrypt')
    print(f"Decrypted: {decrypted}")
