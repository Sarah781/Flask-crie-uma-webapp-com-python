from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route("/inicio")
def ola():
    jogo1= Jogo('God of War', 'Ação', 'PS4')
    jogo2= Jogo('GTA V', 'Ação', 'PS4')
    jogo3= Jogo('Minecraft', 'Aventura', 'PC')
    jogo4= Jogo('FIFA 19', 'Esporte', 'XBOX')
    jogo5= Jogo('Lethal Company', 'FPS', 'PC')
    
    lista = [jogo1, jogo2, jogo3, jogo4, jogo5]
    return render_template('lista.html', titulo='Jogos', jogos = lista)

app.run()