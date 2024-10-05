from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from extensions import db

app = Flask(__name__)
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

from models import Product
from models import Clients


@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)


@app.route('/clients')
def indexClients():
    clients = Clients.query.all()
    return render_template('indexClients.html', clients=clients)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        product = Product(name=name, descricao=description, preco=price)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/createClient', methods=['GET', 'POST'])
def createClient():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        born = request.form['born']
        bought = request.form['bought']
        client = Clients(name=name, email=email, dataNasc=born, bought=bought)
        db.session.add(client)
        db.session.commit()
        return redirect(url_for('indexClients'))
    return render_template('createClients.html')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):

    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.descricao = request.form['description']
        product.preco = request.form['price']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', product=product)


@app.route('/updateClient/<int:id>', methods=['GET', 'POST'])
def updateClient(id):
    client = Clients.query.get_or_404(id)
    if request.method == 'POST':
        client.name = request.form['name']
        client.email = request.form['email']
        client.dataNasc = request.form['born']
        client.bought = request.form['bought']
        db.session.commit()
        return redirect(url_for('indexClients'))
    return render_template('updateClients.html', client=client)


@app.route('/delete/<int:id>')
def delete(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/deleteClient/<int:id>')
def deleteClient(id):
    client = Clients.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()

    return redirect(url_for('indexClients'))


if __name__ == '__main__':
    app.run(debug=True)
