def shift(letter, shift_amount):
    unicode_value = ord(letter) + shift_amount

    if unicode_value > 126:
        unicode_value = unicode_value - 95
    elif unicode_value < 32:
        unicode_value = unicode_value + 95
    

    new_letter = chr(unicode_value)

    return new_letter

def encrypt(message, shift_amount):
    result = ''

    for letter in message:
        result += shift(letter, shift_amount)

    return result


def decrypt(message, shift_amount):
    return encrypt(message, -1 * shift_amount)



with open('C:/Users/cbrown6134/APCSP/Snel@Mann/text_files/file_001597.txt', 'r') as f:
    contents = f.read()

print(decrypt(contents, 34))
