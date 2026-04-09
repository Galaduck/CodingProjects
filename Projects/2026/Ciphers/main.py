from pathlib import Path
import affine
import ceaser
import Vigenere

ThisFile = Path(__file__).parent.resolve()
Input = ThisFile / 'TextFiles' / 'Input.txt'
Output = ThisFile / 'TextFiles' / 'Output.txt'

with open(Input, 'r') as file:
    Message = file.read()
    file.close()

# The table below shows what values of WhichCypher correspond to which cipher
# 1 = Affine
# 2 = Ceaser
# 3 = Vigenere
WhichCypher = int()

# This one is what it says
Encrypt = bool()

while True:
    print('1 = Affine Cipher')
    print('2 = Ceaser Cipher')
    print('3 = Vigenere Cipher')
    WhichCypher = input('Which cipher would you like to use: ')

    if WhichCypher in ['1']:
        WhichCypher = 1
        break

    elif WhichCypher in ['2']:
        WhichCypher = 2
        break

    elif WhichCypher in ['3']:
        WhichCypher = 3
        break

    else:
        print('Enter either 1, 2, or 3')

while True:
    TrueDecider = ''
    TrueDecider = input('Would you like to encrypt or decrypt (E\D): ')

    if TrueDecider in ['E', 'e']:
        Encrypt = True
        break

    elif TrueDecider in ['D', 'd']:
        Encrypt = False
        break
    
    else:
        print('Choose either\'E\' or \'D\'.')


# Affine
if WhichCypher == 1:
    while True:
        Slope = input('What slope do you want / did you use?: ')

        try:
            Slope = int(Slope)
            break

        except ValueError:
            print('Enter an integer.')

    Slope = int(Slope)

    while True:
        yIntercept = input('What  Y-Intercept du you want / did you use?: ')

        try:
            yIntercept = int(yIntercept)
            break

        except ValueError:
            print('Enter an integer.')

    if Encrypt == True:
        EncryptedMessage = affine.encrypt(Message, Slope, yIntercept)

        with open(Output, 'w') as o:
            o.write(EncryptedMessage)
            file.close()

        print('Check TextFIles/output.txt')

    if Encrypt == False:
        DecryptedMessage = affine.decrypt(Message, Slope, yIntercept)

        with open(Output, 'w') as o:
            o.write(DecryptedMessage)
            file.close()

        print('Check TextFIles/output.txt')

# Ceaser
elif WhichCypher == 2:
    while True:
        Shift = input('What shift would you like / did you use?: ')

        try:
            Shift = int(Shift)
            break
        except ValueError:
            print('Enter an integer.')

    if Encrypt == True:
        EncryptedMessage = ceaser.Encrypt(Message, Shift)

        with open(Output, 'w') as o:
            o.write(EncryptedMessage)
            file.close()

        print('Check TextFIles/output.txt')

    if Encrypt == False:
        DecryptedMessage = ceaser.Decrypt(Message, Shift)

        with open(Output, 'w') as o:
            o.write(DecryptedMessage)
            file.close()

        print('Check TextFIles/output.txt')



# Vigenere
elif WhichCypher == 3:
    a = 0

    while True:
        Key = input('What key do you want to use / did you use?: ')

        for x in Key:
            if x.isalpha() == False:
                a += 1

            else:
                a += 0

        if a == 0:
            break

        else:
            print('Only use letters in your key. ')

    if Encrypt == True:
        EncryptedMessage = Vigenere.Encrypt(Message, Key)

        with open(Output, 'w') as o:
            o.write(EncryptedMessage)
            file.close()

        print('Check TextFIles/output.txt')

    if Encrypt == False:
        DecryptedMessage = Vigenere.Decrypt(Message, Key)

        with open(Output, 'w') as o:
            o.write(DecryptedMessage)
            file.close()

        print('Check TextFIles/output.txt')

    

else:
    print('Idk how this happened, just do it again.')