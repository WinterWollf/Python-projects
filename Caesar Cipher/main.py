import cipher
import art

print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or 'end' to terminate the program:\n").lower()
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

while not direction == "end":
    if direction == "encode":
        text = cipher.encrypt(text, shift)
        print(text)
        direction = input("Type 'encode' to encrypt, "
                          "type 'decode' to decrypt or 'end' to terminate the program:\n").lower()
    elif direction == "decode":
        text = cipher.decrypt(text, shift)
        print(text)
        direction = input("Type 'encode' to encrypt, "
                          "type 'decode' to decrypt or 'end' to terminate the program:\n").lower()
    elif direction == "end":
        break
    else:
        print("Wrong input! Please try again")
        direction = input("Type 'encode' to encrypt, "
                          "type 'decode' to decrypt or 'end' to terminate the program:\n").lower()
