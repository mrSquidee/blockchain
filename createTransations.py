from hashlib import sha256
from random import randint

def writeTransactions(file):
    with open(file, 'w') as transations:
        transationsStr = ''
        for i in range(randint(0,100)):
            transationsStr += sha256(str(randint(0,10000)).encode("UTF-8")).hexdigest() + ' -{' + str(randint(0,10)) + '}> ' + sha256(str(randint(0,10000)).encode("UTF-8")).hexdigest() + '\n'
        transations.write(transationsStr)