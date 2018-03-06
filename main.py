import random
from datetime import datetime

password = input("Password: ")
mult = int(input("Mult: "))
msgFile = input("Message File (.txt): ")
f = open(msgFile, 'r')
message = f.read()
message = "".join(message.split())
message.lower()
endFile = input("End File (.txt): ")
ef = open(endFile, 'w')
eord = input("E or D: ")

seed = []
endMsg = []
cryptCode = [None] * 26

if eord.lower() == 'e':
    print(str(datetime.now()))
    for characters in password:
        seed.append((ord(characters) - 96) * mult)
    print("Seed: ", seed)
    print("Length of array: ", len(seed))

    temp = 0
    for numbers in seed:
        temp += int(numbers)
    print("Temp Value pre %: ", temp)
    temp %= 26
    print("Temp Value post %: ", temp)
    print("Length of CryptCode: ", len(cryptCode))
    sequencer = (26 - temp - len(seed))
    while(sequencer > len(seed)):
        sequencer -= len(seed)
    for x in range(len(cryptCode)):
        if x == temp:
            sequencer = 0
        cryptCode[x] = seed[sequencer - 1]
        if sequencer < len(seed) - 1:
            sequencer += 1
        else:
            sequencer = 0
    print("CryptCode: ", cryptCode)

    for y in message:
        ef.write(y)
        #endMsg.append(y)
        for x in range(cryptCode[(ord(y) - ord('a'))]):
            #endMsg.append(chr(random.randint(97, 122)))
            ef.write(chr(random.randint(97, 122)))
    #print(''.join(endMsg))
    #ef.write(''.join(endMsg))
    print(str(datetime.now()))
elif eord.lower() == 'd':
    print(str(datetime.now()))
    msg = []
    decryptMsg = []
    for letters in message:
        msg.append(letters)
    for characters in password:
        seed.append((ord(characters) - 96) * mult)
    print("Seed: ", seed)
    print("Length of array: ", len(seed))

    temp = 0
    for numbers in seed:
        temp += int(numbers)
    print("Temp Value pre %: ", temp)
    temp %= 26
    print("Temp Value post %: ", temp)
    print("Length of CryptCode: ", len(cryptCode))
    sequencer = (26 - temp - len(seed))
    while(sequencer > len(seed)):
        sequencer -= len(seed)
    for x in range(len(cryptCode)):
        if x == temp:
            sequencer = 0
        cryptCode[x] = seed[sequencer - 1]
        if sequencer < len(seed) - 1:
            sequencer += 1
        else:
            sequencer = 0
    print("CryptCode: ", cryptCode)

    tmpStart = 0
    while True:
        decryptMsg.append(msg[tmpStart])
        tmpStart += (cryptCode[(ord(msg[tmpStart]) - ord('a'))]) + 1
        if tmpStart >= len(msg):
            break
    print(''.join(decryptMsg))
    ef.write(''.join(decryptMsg))
    print(str(datetime.now()))
