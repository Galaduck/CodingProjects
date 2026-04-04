import ceaser
lowercase = 'abcdefghijklmnopqrstuvwxyz'

# This is an attempt to create the Vigenere cypher in python.

# Turns the key into its individual ceaser cyphers.
def KeyAnalysis(key):
    FormattedKey = key.lower()
    CeaserList = []

    for x in FormattedKey:
        CeaserList.append(lowercase.index(x))


    return CeaserList

def Encrypt(message, key):
    EncryptedMessage = ''
    CeaserList = KeyAnalysis(key)
    KeyIndex = 0
    KeyLength = len(CeaserList)

    for char in message:
        if char.isalpha() == True:
            EncryptedMessage += ceaser.Encrypt(char, CeaserList[KeyIndex])

            KeyIndex = (KeyIndex + 1) % KeyLength
        
        
        else:
            EncryptedMessage += char
            KeyIndex = KeyIndex

    return EncryptedMessage

def Decrypt(message, key):
    DecryptedMessage = ''
    CeaserList = KeyAnalysis(key)
    KeyIndex = 0
    KeyLength = len(CeaserList)

    for char in message:
        if char.isalpha() == True:
            DecryptedMessage += ceaser.Decrypt(char, CeaserList[KeyIndex])

            KeyIndex = (KeyIndex + 1) % KeyLength
        
        
        else:
            DecryptedMessage += char
            KeyIndex = KeyIndex

    return DecryptedMessage