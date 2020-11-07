import os
import env_variables
from flask import render_template, request
from salary_simulation_API.models.addapters.inss.adaptador_csv_inss import Adaptador_CSV_INSS
from salary_simulation_API.models.addapters.ir.adaptador_csv_ir import Adaptador_CSV_IR
from salary_simulation_API.models.modelos.clt import CLT
from salary_simulation_API.models.pessoas.pessoa_fisica import Pessoa_Fisica

app = env_variables.app


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

        adaptador_inss = Adaptador_CSV_INSS()
        adaptador_ir = Adaptador_CSV_IR()

        adaptador_inss.set_informacoes(os.path.join(env_variables.DATA_PATH, 'tabela_INSS.csv'))
        adaptador_ir.set_informacoes(os.path.join(env_variables.DATA_PATH, 'tabela_IR.csv'))
        pf = Pessoa_Fisica(nome, cpf, qtd_dependentes, salario, adaptador_imposto_ir=adaptador_ir)
        clt = CLT(pf, adaptador_inss)
        clt.calcular_imposto()
        print(clt)
        return "<h1>SUCESSO</h1>"


if __name__ == '__main__':
    print(app.root_path)
    app.run()
