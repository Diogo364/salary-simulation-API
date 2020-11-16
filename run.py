import os
import env_variables
from flask import render_template, request, url_for, redirect
from salary_simulation_API.models.addapters.adaptador_csv_aliquotas_cumulativas import Adaptador_CSV_Aliquotas_Cumulativas
from salary_simulation_API.models.addapters.adaptador_csv_aliquotas_unicas import Adaptador_CSV_Aliquotas_Unicas
from salary_simulation_API.models.impostos.irpf_clt import IRPF_CLT
from salary_simulation_API.models.impostos.inss import INSS
from salary_simulation_API.models.impostos.irpf_mei import IRPF_MEI
from salary_simulation_API.models.impostos.simples_nacional import Simples_Nacional
from salary_simulation_API.models.modelos.clt.beneficio import Beneficio
from salary_simulation_API.models.modelos.clt.clt import CLT
from salary_simulation_API.models.modelos.pj.mei import MEI
from salary_simulation_API.models.pessoas.pessoa_fisica import Pessoa_Fisica
from salary_simulation_API.models.pessoas.pessoa_juridica import Pessoa_Juridica

app = env_variables.app

adaptador_inss = Adaptador_CSV_Aliquotas_Cumulativas()
adaptador_inss.set_informacoes(os.path.join(env_variables.DATA_PATH, 'tabela_INSS.csv'))
inss = INSS(adaptador_inss)

adaptador_ir = Adaptador_CSV_Aliquotas_Unicas()
adaptador_ir.set_informacoes(os.path.join(env_variables.DATA_PATH, 'tabela_IR.csv'))
irpf_clt = IRPF_CLT(adaptador_ir)


adaptador_ir_mei = Adaptador_CSV_Aliquotas_Unicas()
adaptador_ir_mei.set_informacoes(os.path.join(env_variables.DATA_PATH, 'tabela_IR.csv'))
irpf_mei = IRPF_MEI(adaptador_ir)

adaptador_sn = Adaptador_CSV_Aliquotas_Unicas()
adaptador_sn.set_informacoes(os.path.join(env_variables.DATA_PATH, 'tabela_SimplesNacional.csv'))
sn = Simples_Nacional(adaptador_sn, is_mei=True)

dict_impostos_pf = {
    'inss': inss,
    'ir': irpf_clt
}

dict_impostos_pj = {
    'simple_nacional': sn,
    'ir': irpf_mei
}

pf = None
pj = None
mei = None
clt = None
beneficios = []


@app.route('/')
@app.route('/home')
def home():
    global pf
    global pj
    global mei
    global clt
    global beneficios

    pf = None
    pj = None
    mei = None
    clt = None
    beneficios = []

    return render_template('home.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_usuario():
    global pf
    global pj

    if request.method == 'GET':
        return render_template('forms/cadastro_form.html')
    else:
        nome = request.form['inputNome']
        id_number = request.form['inputId']
        qtd_dependentes = int(request.form['inputDependentes'])

        if request.form['inputModalidadeContrato'] == 'CLT':
            print('CLT')
            pf = Pessoa_Fisica(nome, id_number, qtd_dependentes)
            return redirect(url_for('simular_clt'))
        else:
            print('PJ')
            pj = Pessoa_Juridica(nome, id_number, qtd_dependentes)
            return redirect(url_for('simular_pj'))


@app.route('/cadastro/CLT', methods=['GET', 'POST'])
def simular_clt():
    global pf
    global clt
    global beneficios
    global dict_impostos_pf

    if request.method == 'GET':
        if len(request.args) > 0:
            if all(value != '' for value in request.args.values()):
                nome = request.args['inputBeneficioNome']
                valor = request.args['inputBeneficioValor']
                valor_descontar = request.args['inputBeneficioDesconto']
                frequencia = request.args['inputBeneficioFrequencia']

                beneficios.append(Beneficio(nome, valor, valor_descontar, frequencia))

        return render_template('forms/clt_form.html', pessoa=pf, contrato=clt, beneficios=beneficios)
    else:
        salario_bruto = request.form['inputSalario']

        clt = CLT(pf, salario_bruto, dict_impostos_pf, lista_beneficios=beneficios)
        clt.calcular_imposto_total()
        return render_template('forms/clt_form.html', pessoa=pf, contrato=clt, beneficios=beneficios)


@app.route('/cadastro/PJ', methods=['GET', 'POST'])
def simular_pj():
    global pj
    global mei
    global dict_impostos_pj

    if request.method == 'GET':
        return render_template('forms/pj_form.html', pessoa=pj, contrato=mei)
    else:
        salario_bruto = request.form['inputSalario']

        mei = MEI(pj, salario_bruto, dict_impostos_pj, pj.qtd_dependentes)
        mei.calcular_imposto_total()
        return render_template('forms/pj_form.html', pessoa=pj, contrato=mei)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
