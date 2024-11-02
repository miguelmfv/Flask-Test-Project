from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from sqlalchemy.testing.pickleable import Order

from extensions import db
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbweb2:dbweb2@localhost:5432/BancoDevWeb2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

from models import Product, Orders, Clients

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def indexProducts():
    products = Product.query.all()
    return render_template('indexProducts.html', products=products)


@app.route('/clients')
def indexClients():
    clients = Clients.query.all()
    return render_template('indexClients.html', clients=clients)


@app.route('/orders')
def indexOrders():
    orders = Orders.query.all()
    return render_template('indexOrders.html', orders=orders)


@app.route('/createProducts', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        product = Product(name=name, descricao=description, preco=price)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('indexProducts'))
    return render_template('createProducts.html')


@app.route('/createClient', methods=['GET', 'POST'])
def createClient():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        born = request.form['born']
        bought = request.form.get('bought') == 'true'
        client = Clients(name=name, email=email, bougth=bought, dataNasc=born)
        db.session.add(client)
        db.session.commit()
        return redirect(url_for('indexClients'))
    return render_template('createClients.html')


@app.route('/createOrders', methods=['GET', 'POST'])
def createOrders():
    if request.method == 'POST':
        nameClient = request.form['nameClient']
        nameProduct = request.form['nameProduct']
        numItems = request.form['numItems']
        order = Orders(nameClient = nameClient, nameProduct = nameProduct, numItems = numItems)
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('indexOrders'))
    return render_template('createOrders.html')

@app.route('/updateProducts/<int:id>', methods=['GET', 'POST'])
def updateProducts(id):
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.descricao = request.form['description']
        product.preco = request.form['price']
        db.session.commit()
        return redirect(url_for('indexProducts'))
    return render_template('updateProducts.html', product=product)


@app.route('/updateClient/<int:id>', methods=['GET', 'POST'])
def updateClient(id):
    client = Clients.query.get_or_404(id)
    if request.method == 'POST':
        client.name = request.form['name']
        client.email = request.form['email']
        client.dataNasc = request.form['born']
        client.bougth = request.form.get('bougth') == 'true'
        db.session.commit()
        return redirect(url_for('indexClients'))
    return render_template('updateClients.html', client=client)

@app.route('/updateOrder/<int:id>', methods=['GET', 'POST'])
def updateOrder(id):
    order = Orders.query.get_or_404(id)
    if request.method == 'POST':
        order.nameClient = request.form['nameClient']
        order.nameProduct = request.form['nameProduct']
        order.numItems = request.form['numItems']
        db.session.commit()
        return redirect(url_for('indexOrders'))
    return render_template('updateOrders.html', order=order)


@app.route('/delete/<int:id>')
def delete(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()

    return redirect(url_for('indexProducts'))


@app.route('/deleteClient/<int:id>')
def deleteClient(id):
    client = Clients.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()

    return redirect(url_for('indexClients'))

@app.route('/deleteOrder/<int:id>')
def deleteOrder(id):
    order = Orders.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()

    return redirect(url_for('indexOrders'))


if __name__ == '__main__':
    app.run(debug=True)
