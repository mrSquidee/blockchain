from hashlib import sha256
from random import randint
from transaction import Transaction

def writeTransactions():
    transations = []
    for _ in range(randint(5,10)):
        amount = randint(0,10)
        sender = sha256(str(randint(0,10000)).encode("UTF-8")).hexdigest()
        reciever = sha256(str(randint(0,10000)).encode("UTF-8")).hexdigest()
        transations.append(Transaction(amount, sender, reciever))
    return transations