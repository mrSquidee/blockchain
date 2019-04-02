from merkleTree import merk
from hashlib import sha256
from createTransations import writeTransactions

transactions = 'transactions.txt'
difficulty = 3

def mine(nblock):
    tree = merk(nblock['transations'])
    nblock['transations'] = tree
    nblock['root'] = tree[-1][0]
    nblock['nonce'] = -1
    mined = False
    while not mined:
        nblock['nonce'] += 1
        tomine = nblock['root'] + nblock['ph'] + str(nblock['nonce'])
        nblock['id'] = sha256(tomine.encode('UTF-8')).hexdigest()
        mined = (nblock['id'][:difficulty] == '0'*difficulty)
    return nblock['id']

ph = ''
for i in range(10):
    writeTransactions(transactions)
    with open('chain.txt', 'r') as chain:
        ph = eval(chain.readlines()[-1])['id']
    block = {'id': '', 'nonce': 0, 'root': '', 'ph': ph, 'transations': transactions}
    mine(block)
    with open('chain.txt', 'a') as chain:
        chain.write(str(block) + '\n')