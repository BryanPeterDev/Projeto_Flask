from flask import Blueprint, render_template
from db.cliente import CLIENTES


cliente_routes = Blueprint('cliente', __name__)



@cliente_routes.route('/')
def lista_clientes():
    "Lista todos os clientes"
    return render_template('lista_clientes.html',clientes=CLIENTES)

@cliente_routes.route('/<int:cliente_id>') #url passando parametro 
def detalhe_clientes(cliente_id):
    "Detalhes de um cliente específico"
    return render_template('detalhe_clientes.html')

@cliente_routes.route('/inserir',methods=['POST'])
def inserir_clientes():
    "Inserir os dados do cliente no BD"
    pass

@cliente_routes.route('/new', methods=['GET'])
def form_clientes():
    "formulario para criar cliente"
    return render_template('form_clientes.html')

@cliente_routes.route('/<int:cliente_id>/edit',methods=['PUT']) 
def edit_clientes(cliente_id):
    "editar um cliente existente usando um formulario"
    return render_template('form_edit_clientes.html')

@cliente_routes.route('/<int:cliente_id>/update', methods=['PUT']) 
def atualiza_clientes(cliente_id):
    "atualiza um cliente existente informações"
    pass
@cliente_routes.route('/<int:cliente_id>/delete', methods=['DELETE']) 
def delete_clientes(cliente_id):
    " Exclui um cliente"
    pass