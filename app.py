from flask import Flask, request, render_template, redirect, url_for
from block import Block
from chain import Blockchain
from createTransations import writeTransactions
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

c = Blockchain()
making = False

@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == 'POST'):
        i = request.form['blockReq']
        return redirect(url_for('blocks', index=i)) 
    return render_template('index.html', chainString=c.toRender)

@socketio.on('newBlock')
def newBlock():
    global making
    if(not making):
        making = True
        emit('makingBlock')
        pBlock = c.chain[-1]
        i = pBlock.index + 1
        ph = pBlock.id
        t = writeTransactions()
        d = 5
        c.addBlock(Block(i, ph, t, d))
        making = False
    emit('createdBlock', {'data': c.toRender[0]})

@app.route('/blocks/<index>', methods=['GET', 'POST'])
def blocks(index):
    if(request.method == 'POST'):
        return redirect(url_for('index'))

    return render_template('blocks.html', fullBlock=vars(c.chain[int(index)]), i=index)