lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(message, slope, yIntercept):
    slope = slope % 26
    yIntercept = yIntercept % 26
    EncryptedMessage = ''

    for x in message:
        if x in lowercase:
            EncryptedMessage += lowercase[((slope * lowercase.index(x)) + yIntercept) % 26]

        elif x in uppercase:
            EncryptedMessage += uppercase[((slope * uppercase.index(x)) + yIntercept) % 26]

        else:
            EncryptedMessage += x


    return EncryptedMessage

def SolveMod(coefficent, congruency, base):
    # This is just a bashy way to solve ax = b (mod x)
    coefficent = coefficent % base
    congruency = congruency % base
    NumberToTest = 0
    Break = False

    while Break == False:
        ICantComeUpWithAGoodNameForThisVariable = (coefficent * NumberToTest) % base

        if ICantComeUpWithAGoodNameForThisVariable == congruency:
            Break = True

        else:
            NumberToTest = NumberToTest + 1
            Break = False


    #The line below is completely useless but i am doing it for peace of mind
    NumberToTest = NumberToTest % base

    return NumberToTest

def decrypt(message, slope, yIntercept):
    coefficent = slope % 26
    yIntercept = yIntercept % 26
    DecryptedMessage = ''

    for x in message:
        if x in lowercase:
            congruency = (lowercase.index(x) - yIntercept) % 26
            Letter = lowercase[SolveMod(coefficent, congruency, 26)]
            DecryptedMessage += Letter

        elif x in uppercase:
            congruency = (uppercase.index(x) - yIntercept) % 26
            Letter = uppercase[SolveMod(coefficent, congruency, 26)]
            DecryptedMessage += Letter

        else:
            DecryptedMessage += x

    return DecryptedMessage