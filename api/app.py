from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres://root:itnisanjr19@localhost/"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

vendas_adquirente = db.Table('vendas_adquirente', db.metadata, autoload=True, autoload_with=db.engine)
venda = (db.session.query(vendas_adquirente).all())


@app.route('/<empparameter>/<dataparameter>')
def index(empparameter,dataparameter):
    contador = 0
    valor_bruto = valor_liquido = taxa_adm = 0
    vendas = (db.session.query(vendas_adquirente).filter_by(empresa=empparameter, data_transacao=dataparameter))
    for r in vendas:
        contador += 1
        valor_bruto += r.valor_bruto
        valor_liquido += r.valor_liquido
        taxa_adm += r.taxa_adm


    #return ("Total de vendas: {}, Valor Total bruto R$: {}, Valor Total liquido R$: {}, Taxa adm R$: {}'".format(contador,valor_bruto,valor_liquido,taxa_adm))
    return {"Total de vendas": contador, "Total bruto": f'R$: {valor_bruto}', "Total liquido": f'R$: {valor_liquido}', "Taxa adm": f'R$: {taxa_adm}'}
