from app import app

@app.route('/')
def index():
    return "Bem-vindo ao AutoCataloger!"
