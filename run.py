import os
import env_variables
from flask import render_template, request, url_for, redirect, session
from salary_simulation_API.models.addapters.inss.adaptador_csv_inss import Adaptador_CSV_INSS
from salary_simulation_API.models.addapters.ir.adaptador_csv_ir import Adaptador_CSV_IR
from salary_simulation_API.models.impostos.imposto_de_renda import Imposto_de_Renda
from salary_simulation_API.models.impostos.inss import INSS
from salary_simulation_API.models.modelos.clt import CLT
from salary_simulation_API.models.pessoas.pessoa_fisica import Pessoa_Fisica

app = env_variables.app

adaptador_inss = Adaptador_CSV_INSS()
adaptador_inss.set_informacoes(os.path.join(env_variables.DATA_PATH, 'tabela_INSS.csv'))
inss = INSS(adaptador_inss)

adaptador_ir = Adaptador_CSV_IR()
adaptador_ir.set_informacoes(os.path.join(env_variables.DATA_PATH, 'tabela_IR.csv'))
ir = Imposto_de_Renda(adaptador_ir)

dict_impostos = {
    'inss': inss,
    'ir': ir
}

pf = None

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_usuario():
    global pf

    if request.method == 'GET':
        return render_template('forms/cadastro_form.html')
    else:
        nome = request.form['inputNome']
        cpf = request.form['inputCPF']
        qtd_dependentes = int(request.form['inputDependentes'])

        pf = Pessoa_Fisica(nome, cpf, qtd_dependentes)
        if request.form['inputModalidadeContrato'] == 'CLT':
            print('CLT')
            return redirect(url_for('simular_clt'))
        else:
            print('PJ')
            return redirect(url_for(simular_pj))


@app.route('/cadastro/CLT', methods=['GET', 'POST'])
def simular_clt():
    global pf
    global dict_impostos

    if request.method == 'GET':
        if isinstance(pf, Pessoa_Fisica):
            return render_template('forms/clt_form.html', pf=pf)
        else:
            return '<h1>PROBLEMA</h1>'
    else:
        try:
            beneficios = request.form['hasBeneficios']
        except KeyError:
            beneficios = None
        salario_bruto = request.form['inputSalario']

        clt = CLT(pf, salario_bruto, dict_impostos)
        clt.calcular_imposto_total()
        return render_template('forms/clt_form.html', pf=pf, clt=clt)


@app.route('/cadastro/PJ', methods=['GET', 'POST'])
def simular_pj():
    pass


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
