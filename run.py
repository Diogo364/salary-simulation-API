from env_variables import app, pf, clt, beneficios, dict_impostos
from flask import render_template, request, url_for, redirect, session
from salary_simulation_API.models.modelos.clt.beneficio import Beneficio
from salary_simulation_API.models.modelos.clt.clt import CLT
from salary_simulation_API.models.pessoas.pessoa_fisica import Pessoa_Fisica


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
                desconto = request.args['inputBeneficioDesconto']
                frequencia = request.args['inputBeneficioFrequencia']
                try:
                    descontar = bool(request.args['inputBeneficioDescontar'])
                except KeyError:
                    descontar = False

                print('apended')
                beneficios.append(Beneficio(nome, valor, desconto, frequencia, descontar))

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


@app.route('/API/pessoa_fisica', methods=['GET', 'POST'])
def pessoa_fisica():
    global pf

    if request.method == 'GET':
        try:
            return pf.to_json()
        except AttributeError:
            return 'Inicialize uma pessoa antes de recupera-la'
    else:
        nome = request.json['nome']
        cpf = request.json['cpf']
        qtd_dependentes = 0 if 'qtd_dependentes' not in request.json else request.json['qtd_dependentes']
    pf = Pessoa_Fisica(nome, cpf, qtd_dependentes)
    return 'Pessoa Cadastrada com Sucesso'


@app.route('/API/beneficios', methods=['GET', 'POST'])
def cadastro_beneficios():
    global beneficios

    if request.method == 'GET':
        return {'beneficios': [beneficio.to_json() for beneficio in beneficios]}
    else:
        inclusoes = 0
        for beneficio in request.json:
            nome = beneficio['nome']
            valor = beneficio['valor']
            desconto = beneficio['desconto']
            frequencia = beneficio['frequencia']
            is_incluido = beneficio['incluido_salario']
            beneficios.append(Beneficio(nome, valor, desconto, frequencia, is_incluido))
            inclusoes += 1
        return f'Foram incluídos {inclusoes} beneficios'


@app.route('/API/CLT', methods=['GET', 'POST'])
def clt():
    global clt
    global pf
    global beneficios

    if request.method == 'GET':
        return clt.to_json()
    else:
        salario_bruto = request.json['salario_bruto']
        clt = CLT(pf, salario_bruto, dict_impostos, beneficios)
        return 'CLT cadastrada com sucesso'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
