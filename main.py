import collections

key = int(input("What is the key? (integers only)"))
command = input("Do you want to encode or decode a message?")


alphabet = collections.deque(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])

shifted_alphabet = alphabet.copy()

for x in range(key):
    temp = shifted_alphabet[0]
    shifted_alphabet.popleft()
    shifted_alphabet.append(temp)

def decode():
    encrypted_message = input("What is the encrypted message?").lower()
    decrypted_message = ""
    for char in encrypted_message:
        if char in alphabet:
            idx = shifted_alphabet.index(char)
            decrypted_message += alphabet[idx]
        else:
            decrypted_message += char
    print(f"Decrypted message: {decrypted_message}")

def encode():
    message = input("Please input the message.").lower()
    encrypted_message = ""
    for char in message:
        if char in alphabet:
            idx = alphabet.index(char)
            encrypted_message += shifted_alphabet[idx]
        else:
            encrypted_message += char
    print(f"Encoded message: {encrypted_message}")

if command == "decode":
    decode() 
elif command == "encode":
    encode()
else:
    print("That was not a valid command.")

