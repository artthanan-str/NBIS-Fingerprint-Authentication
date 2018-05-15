import os
import subprocess, sys
import re

def getMinutiae(fileName, output):
    callMindtct = "./library/mindtct ./input/demo/" + fileName + " " + output
    extensionFiles = [".dm", ".hcm", ".lcm", ".lfm", ".mdt", ".min", ".qm"]
    deleteFiles = "rm -r " + output
    
    result = os.popen(callMindtct).read()  # returns the exit code in unix
    os.system('clear')

    for x in extensionFiles:
        cmd = deleteFiles + x
        os.system(cmd)

    return

def identify(fileName):
    cmd = "./library/bozorth3 -g ./" + fileName + " ./database/*.xyt"
    result = os.popen(cmd).read()

    for temp in result.splitlines():
        if(int(temp)>40):
            return True

    return False

def verify(fileName):
    cmd = "./library/bozorth3 -g ./" + fileName + " ./database/*.xyt"
    result = os.popen(cmd).read()
    fingerMatched = False
    fileNameMatched = False

    for temp in result.splitlines():
        if(int(temp)>40):
            fingerMatched = True

    for name in os.listdir('./database'):
        if name == fileName:
            fileNameMatched = True

    return fingerMatched, fileNameMatched

def checkVerifyOrNot(fingerMatched, fileNameMatched):
    print('==============================================================')
    print('                           Results                            ')
    print('==============================================================')
    if fingerMatched == True and fileNameMatched == True:
        print('The fingerprint is correctly verified.')
    elif fingerMatched == True and fileNameMatched == False:
        print('The fingerprint is partially matched with a fingerprint in the database.')
        print('The fingerprint is matched but one of the properties are not matched.\n')
    elif fingerMatched == False and fileNameMatched == True:
        print('The fingerprint is partially matched with a fingerprint in the database.')
        print('The properties are matched but the fingerprint is not matched.\n')
    else:
        print('The fingerprint is incorrectly verified.\n')


# Main code starts here

print('==============================================================')
print('                 Authentication by Fingerprint                ')
print('==============================================================')
print('The program can perform authentication and verification.')
print('Type "V" for Verification')
print('Type "I" for Identification')
print('==============================================================\n')
inputKeyboard = input('Input the letter: ')
os.system('clear')

if inputKeyboard.lower() == 'v':
    print('==============================================================')
    print('                      Verification Mode                       ')
    print('==============================================================')
    fileName = input('Input file name: ')
    getMinutiae(fileName+'.eft', fileName)
    fingerMatched, fileNameMatched = verify(fileName+'.xyt')
    checkVerifyOrNot(fingerMatched, fileNameMatched)
    os.system('rm -r ' + fileName + '.xyt')

elif inputKeyboard.lower() == 'i':
    print('==============================================================')
    print('                     Identification Mode                      ')
    print('==============================================================')
    fileName = input('Input file name: ')
    getMinutiae(fileName+'.eft', fileName)
    identifyStatus = identify(fileName+'.xyt')

    os.system('rm -r ' + fileName + '.xyt')

    print('==============================================================')
    print('                           Results                            ')
    print('==============================================================')
    if(identifyStatus):
        print('The fingerprint is identified.')
    else:
        print('NThe fingerprint is not identified.')

else:
    print('The input does not follow the instruction. The program will exit immediately.')