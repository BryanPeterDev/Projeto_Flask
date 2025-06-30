from flask import Blueprint, render_template,request
from database.models.cliente import Cliente


cliente_routes = Blueprint('cliente', __name__)


@cliente_routes.route('/')
def lista_clientes():
    "Lista todos os clientes"
    clientes = Cliente.select()  # Obtém todos os clientes do banco de dados
    return render_template('lista_clientes.html',clientes=clientes)


@cliente_routes.route('/new', methods=['GET'])
def form_clientes():
    "formulario para criar cliente"
    
    return render_template('form_clientes.html')

@cliente_routes.route('/<int:cliente_id>') #url passando parametro 
def detalhe_clientes(cliente_id):
    "Detalhes de um cliente específico"
    
    cliente = Cliente.get_by_id(cliente_id)  # Obtém o cliente pelo ID do banco de dados
    return render_template('detalhe_clientes.html',cliente=cliente)

@cliente_routes.route('/inserir',methods=['POST'])
def inserir_clientes():
    "Inserir os dados do cliente no BD"

    data=request.json

    novo_usuario = Cliente.create( 
        nome = data['nome'],
        email = data['email'],
    )

   
    return render_template('item_cliente.html', cliente=novo_usuario)

@cliente_routes.route('/<int:cliente_id>/edit') 
def edit_clientes(cliente_id):
    "editar um cliente existente usando um formulario"
    
    cliente = Cliente.get_by_id(cliente_id)
    
    return render_template('form_clientes.html',cliente=cliente)

@cliente_routes.route('/<int:cliente_id>/update', methods=['PUT']) 
def atualiza_clientes(cliente_id):
    "atualiza um cliente existente informações"
    data = request.json
    
    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()
    
    return render_template('item_cliente.html', cliente=cliente_editado)
  

@cliente_routes.route('/<int:cliente_id>/delete', methods=['DELETE']) 
def delete_clientes(cliente_id):
    " Exclui um cliente"
    
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()  # Exclui o cliente do banco de dados
    
    # Retorna uma resposta indicando que a exclusão foi bem-sucedida

    return {'deleted': 'ok'}