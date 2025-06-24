from flask import Flask
from routes.home import home_routes
from routes.cliente import cliente_routes


app = Flask(__name__)

app.register_blueprint(home_routes)
app.register_blueprint(cliente_routes, url_prefix='/clientes')

app.run(debug=True)