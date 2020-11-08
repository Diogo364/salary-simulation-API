import os
import env_variables
from flask import render_template, request, url_for, redirect, session
from salary_simulation_API.models.addapters.inss.adaptador_csv_inss import Adaptador_CSV_INSS
from salary_simulation_API.models.addapters.ir.adaptador_csv_ir import Adaptador_CSV_IR
from salary_simulation_API.models.impostos.imposto_de_renda import Imposto_de_Renda
from salary_simulation_API.models.impostos.inss import INSS
from salary_simulation_API.models.modelos.clt.beneficio import Beneficio
from salary_simulation_API.models.modelos.clt.clt import CLT
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
clt = None
beneficios = []


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


@app.route('/cadastro/CLT', methods=['GET', 'POST', 'PUT'])
def simular_clt():
    global pf
    global clt
    global beneficios
    global dict_impostos

    if request.method == 'GET':
        if len(request.args) > 0:
            if all(value != '' for value in request.args.values()):
                nome = request.args['inputBeneficioNome']
                valor = request.args['inputBeneficioValor']
                frequencia = request.args['inputBeneficioFrequencia']
                try:
                    descontar = bool(request.args['inputBeneficioDescontar'])
                except KeyError:
                    descontar = False

                print('apended')
                beneficios.append(Beneficio(nome, valor, frequencia, descontar))

        if isinstance(pf, Pessoa_Fisica):
            print(len(beneficios))
            return render_template('forms/clt_form.html', pf=pf, clt=clt, beneficios=beneficios)
        else:
            return '<h1>PROBLEMA</h1>'
    else:
        salario_bruto = request.form['inputSalario']

        clt = CLT(pf, salario_bruto, dict_impostos, lista_beneficios=beneficios)
        clt.calcular_imposto_total()
        return render_template('forms/clt_form.html', pf=pf, clt=clt, beneficios=beneficios)


@app.route('/cadastro/PJ', methods=['GET', 'POST'])
def simular_pj():
    pass


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
