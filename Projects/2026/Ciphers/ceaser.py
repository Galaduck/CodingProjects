lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Encrypts a message
def Encrypt(message, shift):
    EncryptedMessage = ''
    for x in message:
        if x in lowercase:
            EncryptedMessage += lowercase[(lowercase.index(x) + shift) % 26]

        elif x in uppercase:
            EncryptedMessage += uppercase[(uppercase.index(x) + shift) % 26]

        else:
            EncryptedMessage += x

    return EncryptedMessage
        
def Decrypt(message, shift):
    DecryptedMessage = ''
    for x in message:
        if x in lowercase:
            DecryptedMessage += lowercase[(lowercase.index(x) - shift) % 26]

        elif x in uppercase:
            DecryptedMessage += uppercase[(uppercase.index(x) - shift) % 26]

        else:
            DecryptedMessage += x

    return DecryptedMessage