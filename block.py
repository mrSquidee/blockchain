from hashlib import sha256

class Block():
    
    def __init__(self, i, ph, t, d):
        self.index = i
        self.id = '0'*64
        self.nonce = -1
        self.root = '0'*64
        self.prevHash = ph
        self.transactions: t
        self.tree = [t]
        self.difficulty = d
        self.mined = False

    def makeMerkle(self):
        self.tree.append(list(map(lambda x: sha256(x).hexdigest(), self.tree[0])))
        i = 1
        while len(self.tree[i]) != 1:
            nextLayer = []
            for j in range(int(round(len(self.tree[i])/2))):
                try:
                    nextLayer.append(sha256((self.tree[i][j] + self.tree[i][j-1]).encode('UTF-8')).hexdigest())
                except:
                    nextLayer.append(sha256((self.tree[i][j] + self.tree[i][j]).encode('UTF-8')).hexdigest())
            self.tree.append(nextLayer)
            i += 1

    def mine(self):
        self.makeMerkle()
        self.root = self.tree[-1][0]
        while not self.mined:
            self.nonce += 1
            tomine = self.root + self.prevHash + str(self.nonce)
            self.id = sha256(tomine.encode('UTF-8')).hexdigest()
            self.mined = (self.id[:self.difficulty] == '0'*self.difficulty)