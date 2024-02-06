from app import app 

@app.route('/')
def hola():
    return 'Esto funciona' 