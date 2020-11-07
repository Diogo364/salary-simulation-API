from flask import Flask, render_template, url_for, request
from salary_simulation_API.models.modelos.clt import CLT
import os


app = Flask(__name__, template_folder='./salary_simulation_API/templates')


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/quick_start', methods=['GET', 'POST'])
def quick_start():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        nome = request.form['inputNome']
        cpf = request.form['inputCPF']
        salario = float(request.form['inputSalario'])
        qtd_dependentes = int(request.form['inputDependentes'])
        try:
            beneficios = request.form['hasBeneficios']
        except KeyError:
            beneficios = None

        clt = CLT(nome, cpf, qtd_dependentes, salario, beneficios)
        return "<h1>SUCESSO</h1>"


if __name__ == '__main__':
    print(app.root_path)
    app.run()
