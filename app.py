from flask import Flask
from routes.routes import contactosEnrutador

from flask_sqlalchemy import SQLAlchemy
from config import SQL_DATABASE_URI


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQL_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key="clave super secreta"
#sqlite:///tmp/contactos.db => https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#what-to-remember => 
# configure extension, explica como conectar a SQLITE

SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)
    
app.register_blueprint(contactosEnrutador)