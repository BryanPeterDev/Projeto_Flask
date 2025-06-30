from database.database import db
from database.models.cliente import Cliente
from routes.home import home_routes
from routes.cliente import cliente_routes


def configure_all(app):
    configure_routes(app)
    configure_db()
    
    
def configure_routes(app):
    app.register_blueprint(home_routes)
    app.register_blueprint(cliente_routes, url_prefix='/clientes')
    

def configure_db():
    # Initialize the database connection
    db.connect()
    db.create_tables([Cliente])  
  

    
    print("Configuration complete. All components are set up.")
    
    
    