import string
import random
import datetime


def encrypt_number(number):
    x = 0
    toreturn = ''
    while True:
        if not x + 4 > number:
            toreturn += '#'
            x += 4
        if not x + 3 > number:
            toreturn += '*'
            x += 3
        elif not x + 2 > number:
            toreturn += ':'
            x += 2
        elif not x + 1 > number:
            toreturn += '.'
            x += 1
        else:
            break
        
    return toreturn

def encrypt_string(strings:str):
    strings = strings
    values = {}
    toreturn = ''
    valuekeys = string.ascii_letters + string.punctuation
    for x,valuekey in enumerate(valuekeys):
        values[valuekey] = x + 1
    for letter in strings:
        if letter in values:
            toreturn += encrypt_number(values[letter])
        elif letter == ' ':
            toreturn += ' '

        toreturn += '/'
    return toreturn

def decrypt_string(encryptedstring:str):
    values = {}
    toreturn = ''
    valuekeys = string.ascii_letters + string.punctuation
    for x,valuekey in enumerate(valuekeys):
        values[x+1] = valuekey
    egg1 = encryptedstring.split(' ')
    for egg in egg1:
        egg2 = egg.split('/')
    for egg in egg1:
        egg2 = egg.split('/')
        for egg in egg2:
            x = 0
            for letter in egg:
                if letter == '#':
                    x += 4
                if letter == '*':
                    x += 3
                elif letter == ':':
                    x += 2
                elif letter == '.':
                    x += 1
            if not x == 0:
                toreturn += values[x]
        toreturn += ' '
    return toreturn
    




decrypted = decrypt_string('')
encrypted = encrypt_string('the simplicity of having to code python is amazing!')

print(decrypted)
print(encrypted)




