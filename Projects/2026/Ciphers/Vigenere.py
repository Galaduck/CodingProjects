import ceaser
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# This is an attempt to create the Vigenere cypher in python.

# Turns the key into its individual ceaser cypher.
def KeyAnalysis(key):
    FormattedKey = key.lower()
    CeaserList = []

    for x in FormattedKey:
        CeaserList.append(lowercase.index(x))


    return CeaserList

def Encrypt(message, key):
    EncryptedMessage = ''
    CeaserList = KeyAnalysis(key)
    Remover = int(len(CeaserList))



    for x in message:
        for y in CeaserList:
            EncryptedMessage += ceaser.Encrypt(x, y)

    

    return EncryptedMessage



message = 'The lazy brown fox jumps quickly over the bear.'
key = 'Prime'
print(Encrypt(message, key))