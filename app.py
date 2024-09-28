from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = []
clients = []


@app.route('/')
def index():
    return render_template('index.html', products=products)


@app.route('/clients')
def indexClients():
    return render_template('indexClients.html', clients=clients)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        product = {'id': len(products) + 1, 'name': name, 'description': description, 'price': price}
        products.append(product)
        return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/createClient', methods=['GET', 'POST'])
def createClient():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        born = request.form['born']
        bought = request.form['bought']
        client = {'id': len(clients) + 1, 'name': name, 'email': email, 'born': born, 'bought': bought}
        clients.append(client)
        return redirect(url_for('indexClients'))
    return render_template('createClients.html')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    product = next((p for p in products if p['id'] == id), None)
    if request.method == 'POST':
        product['name'] = request.form['name']
        product['description'] = request.form['description']
        product['price'] = request.form['price']
        return redirect(url_for('index'))
    return render_template('update.html', product=product)


@app.route('/updateClient/<int:id>', methods=['GET', 'POST'])
def updateClient(id):
    client = next((c for c in clients if c['id'] == id), None)
    if request.method == 'POST':
        client['name'] = request.form['name']
        client['email'] = request.form['email']
        client['born'] = request.form['born']
        client['bought'] = request.form['bought']
        return redirect(url_for('indexClients'))
    return render_template('updateClients.html', client=client)


@app.route('/delete/<int:id>')
def delete(id):
    global products
    products = [p for p in products if p['id'] != id]
    return redirect(url_for('index'))


@app.route('/deleteClient/<int:id>')
def deleteClient(id):
    global clients
    clients = [c for c in clients if c['id'] != id]
    return redirect(url_for('indexClients'))


if __name__ == '__main__':
    app.run(debug=True)
