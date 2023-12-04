def encrypt(text, shift):
    encrypted_text = ""

    for letter in text:
        if ord(letter) + shift > 122:
            encrypted_text += chr(64 + ord(letter) + shift - 122)
        elif ord(letter) < 65:
            encrypted_text += letter
        else:
            encrypted_text += chr(ord(letter) + shift)
    return encrypted_text


def decrypt(text, shift):
    decrypt_text = ""

    for letter in text:
        if ord(letter) < 65:
            decrypt_text += letter
        elif ord(letter) - shift < 65:
            decrypt_text += chr(122 - (64 - (ord(letter) - shift)))
        else:
            decrypt_text += chr(ord(letter) - shift)
    return decrypt_text