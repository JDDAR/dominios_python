from flask import Flask 

#--> crear el objeto principal 

app = Flask(__name__)

#Importar las rutas definidas 
from app import routers

if __name__ == '__main__':
    app.run()