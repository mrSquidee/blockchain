from block import Block
from hashlib import sha256

class Blockchain():
    def __init__(self):
        self.chain = [Block(0, '0'*64, [], 0)]

    def addBlock(self, block):
        if(self.verifyBlock(block)):
            self.chain.append(block)
        else:
            print('no')

    def verifyBlock(self, block):
        toVerify = block.root + block.prevHash + str(block.nonce)
        if(sha256(toVerify.encode('UTF-8')).hexdigest() == block.id): return True

