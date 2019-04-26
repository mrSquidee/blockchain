from block import Block
from hashlib import sha256

class Blockchain():
    def __init__(self):
        self.chain = [Block(0, '0'*64, [], 0)]
        self.toRender = [str([self.chain[0].index, self.chain[0].id, self.chain[0].nonce])]

    def addBlock(self, block):
        block.mine()
        if(self.verifyBlock(block)):
            self.chain.append(block)
            self.toRender = [str([block.index, block.id, block.nonce])] + self.toRender
        else:
            print('no')

    def verifyBlock(self, block):
        toVerify = block.root + block.prevHash + str(block.nonce)
        print(toVerify)
        print(sha256(toVerify.encode('UTF-8')).hexdigest())
        print(block.id)
        return sha256(toVerify.encode('UTF-8')).hexdigest() == block.id

