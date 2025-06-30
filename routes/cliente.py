from flask import Blueprint, render_template,request
from database.cliente import CLIENTES
from database.models.cliente import Cliente


cliente_routes = Blueprint('cliente', __name__)

    

@cliente_routes.route('/')
def lista_clientes():
    "Lista todos os clientes"
    
    clientes = Cliente.select()  # Usando o modelo Cliente para buscar todos os clientes
    return render_template('lista_clientes.html',clientes=clientes)

@cliente_routes.route('/<int:cliente_id>') #url passando parametro 
def detalhe_clientes(cliente_id):
    "Detalhes de um cliente específico"
    cliente = list(filter(lambda c: c['id'] == cliente_id, CLIENTES))[0]

    return render_template('detalhe_clientes.html', cliente=cliente)

@cliente_routes.route('/inserir',methods=['POST'])
def inserir_clientes():
    "Inserir os dados do cliente no BD"

    data=request.json

    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email'],
    )

    CLIENTES.append(novo_usuario)

    return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_routes.route('/new', methods=['GET'])
def form_clientes():
    "formulario para criar cliente"
    return render_template('form_clientes.html')

@cliente_routes.route('/<int:cliente_id>/edit') 
def edit_clientes(cliente_id):
    "editar um cliente existente usando um formulario"
    cliente= None
    
    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c
            

    return render_template('form_clientes.html',cliente=cliente)

@cliente_routes.route('/<int:cliente_id>/update', methods=['PUT']) 
def atualiza_clientes(cliente_id):
    cliente_editado = None
    data = request.json
    "atualiza um cliente existente informações"

    for c in CLIENTES:
        if c['id'] == cliente_id:
            c['nome'] = data['nome']
            c['email'] = data['email']
            # Atualiza o cliente editado
            cliente_editado = c
            
            return render_template('item_cliente.html', cliente=cliente_editado)

@cliente_routes.route('/<int:cliente_id>/delete', methods=['DELETE']) 
def delete_clientes(cliente_id):
    " Exclui um cliente"
    global CLIENTES 
    CLIENTES = [ c for c in CLIENTES if c['id'] != cliente_id]

    return {'deleted': 'ok'}