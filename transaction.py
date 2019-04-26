from hashlib import sha256

class Transaction():

    def __init__(self, amount, sender, reciever):
        self.amount = amount
        self.sender = sender
        self.reciever = reciever
        self.hash = self.hashMe()

    def hashMe(self):
        return sha256((str(self.amount) + self.sender + self.reciever).encode('UTF-8')).hexdigest()