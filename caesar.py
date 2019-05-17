#This is a tutorial from the book Invent Your
#Own Computer Games with Python

#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' #calls alphabet as "symbols"
MAX_KEY_SIZE = len(SYMBOLS) #constant of length of SYMBOLS'

def getMode(): #defines function
    while True: #while loop
        print('Do you wish to encrypt or decrypt a message?')#print statements
        mode = input().lower() #assigns mode as input but in lowercase
        if mode in ['encrypt', 'e', 'decrypt', 'd']: #testing for word or letter
            return mode #return
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".') #else statement with check

def getMessage(): #define function
    print('Enter your message: ') #print statement
    return input() #return input

def getKey(): #define function Key
    key = 0 #key is 0
    while True: #while loop that always runs
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE)) #print 1- the number of values in symbols
        key = int(input()) #key is the integer value of input
        if (key >= 1 and key <= MAX_KEY_SIZE): #if key is between 1 and 52 return value
            return key

def getTranslatedMessage(mode, message, key): #define function with variables mode, message, and key
    if mode[0] == 'd': #if decrypting then key is going to move backward instead of forwards
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol
        else:
            #Encrypt or decrypt
            symbolIndex += key
        if symbolIndex >= len(SYMBOLS): #this is where the shift starts happening depending on nthe
            symbolIndex -= len(SYMBOLS)# the symbol or character becomes the encrypted or decrypted letter using the length of the SYMBOLS and key provided
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode() # calling all functions
message = getMessage()
key = getKey()
print('Your translated text is: ') #print statements
print(getTranslatedMessage(mode, message, key)) #print statements