from symtable import Class

from extensions import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'
    

class Clients(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    bougth = db.Column(db.Boolean, nullable=False)
    dataNasc = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Clients {self.name}>'


class Orders(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    nameClient = db.Column(db.String(100), nullable=False)
    nameProduct = db.Column(db.String(100), nullable=False)
    numItems = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Orders {self.id}>'