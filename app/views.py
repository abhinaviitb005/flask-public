from app import app

@app.route('/')
def home():
    return 'Hello, Flask on Azure!'
