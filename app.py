from flask import Flask, render_template, request, redirect, session;

app = Flask(__name__)
app.config["SECRET_KEY"] = 'chave_secreta'

@app.route("/")
def login():
    return render_template ("login.html")

@app.route("/painel")
def painel():
    if 'usuario_name' in session:
        return render_template("painel.html", usuario_nome = session['usuario_nome'], usuario_cpf = session['usuario_cpf'])
    return redirect('/')

@app.route("/verificar", methods = ['POST'])
def verificar():
    CPF = request.form.get('CPF')
    senha = request.form.get('senha')

    print('Tentando login com:', CPF, '/SENHA', senha)

    if CPF == '12345678900' and senha =='123456':
        session['usuario_nome'] = "Eloah"
        session['usuario_cpf'] = CPF
        return redirect('/painel')

    if CPF == '98765432100' and senha == '654321':
        session['usuario_nome'] = "Kiara"
        sessiom['usuario_cpf'] = CPF
        return redirect('/painel')

    return redirect('/')
@app.route("/sair")
def sair():
    session.pop('usuario_nome', none)
    session.pop('usuario_cpf', none)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
    