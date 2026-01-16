def getDoubleAlphabet(alphabet):
    return alphabet + alphabet


def getMessage():
    return input("Please enter a message to encrypt: ")


def getCipherKey():
    return int(input("Please enter a key (whole number from 1-25): "))


def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()

    for currentCharacter in uppercaseMessage:
        if currentCharacter in alphabet:
            position = alphabet.find(currentCharacter)
            newPosition = position + cipherKey
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += currentCharacter

    return encryptedMessage


def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -cipherKey
    return encryptMessage(message, decryptKey, alphabet)


def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')

    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')

    myMessage = getMessage()
    myCipherKey = getCipherKey()

    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')

    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')


# all the program ONCE
runCaesarCipherProgram()
