
def caesar_cipher(message, shift, encrypting = True):
    eMessage = ""
    offset = shift if encrypting else -shift

    for char in message:
        if char.isalpha():
            if char.isupper():
                eMessage += chr((ord(char) - ord('A') + offset) % 26 + ord('A'))
                # ord(char) - ord('A') calculates the position of the char within the uppercase alphabet
                # then, position is shifted with offset to encipher and we modulo 26 to ensure its within the 26 letters in the alphabet
                # we read ord('A) to get back to the ASCII value of the uppercase letter
            else:
                eMessage += chr((ord(char) - ord('a') + offset) % 26 + ord('a'))
        else:
            eMessage += char

    return eMessage


def vigenere_cipher(message, keyword, encrypting = True):
    eMessage = ""
    keyword = str(keyword).upper()

    for i, char in enumerate(message):
            shift = ord(keyword[i % len(keyword)]) - ord('A')
            eMessage += caesar_cipher(char, shift, encrypting)
    return eMessage


##### TESTS #######

message = "Hello, World!"
shift = 3
keyword = "KEY"

# # CAESAR CIPHER 
# encrypted_message = caesar_cipher(message, shift, encrypting = True)
# decrypted_message = caesar_cipher(encrypted_message, shift, encrypting = False)

## VIGENERE CIPHER
encrypted_message = vigenere_cipher(message, keyword, encrypting = True)
decrypted_message = vigenere_cipher(encrypted_message, keyword, encrypting = False)


print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)

