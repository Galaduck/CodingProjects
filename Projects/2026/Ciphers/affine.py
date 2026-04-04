lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(message, slope, yIntercept):
    EncryptedMessage = ''

    for x in message:
        if x in lowercase:
            EncryptedMessage += lowercase[((slope * lowercase.index(x)) + yIntercept) % 26]

        elif x in uppercase:
            EncryptedMessage += uppercase[((slope * uppercase.index(x)) + yIntercept) % 26]

        else:
            EncryptedMessage += x


    return EncryptedMessage


        