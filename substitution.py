alphabet = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]\\^_`abcdefghijklmnopqrstuvwxyz{|}~"
key = "~}|{zyxwvutsrqponmlkjihgfedcba`_^\\][ZYXWVUTSRQPONMLKJIHGFEDCBA@?>=<;:9876543210/.-,+*)('&%$#\"! "

def encrypt(message):
    result = ""

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]

    return result

def decrypt(message):
    result = ""

    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]

    return result


unencrypted_message = "Everyone was $^@%#&*? busy, so I went to the movie alone! Rock music (never) approaches at high velocity. The river stole all 473 gods."
encrypted_message = encrypt(unencrypted_message)
decrypted_message = decrypt(encrypted_message)

'''
print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)
'''

with open('C:/Users/cbrown6134/APCSP/Snel@Mann/text_files/file_007271.txt', 'r') as f:
    contents = f.read()

print(decrypt(contents))
