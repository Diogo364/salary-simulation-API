import os
from flask import Flask
from salary_simulation_API.models.addapters.inss.adaptador_csv_inss import Adaptador_CSV_INSS
from salary_simulation_API.models.addapters.ir.adaptador_csv_ir import Adaptador_CSV_IR
from salary_simulation_API.models.impostos.imposto_de_renda import Imposto_de_Renda
from salary_simulation_API.models.impostos.inss import INSS

app = Flask(__name__, template_folder='./salary_simulation_API/templates', static_folder='./salary_simulation_API/static')

DATA_PATH = os.path.join(app.root_path, 'data')

pf = None
clt = None
beneficios = []


adaptador_inss = Adaptador_CSV_INSS()
adaptador_inss.set_informacoes(os.path.join(DATA_PATH, 'tabela_INSS.csv'))
inss = INSS(adaptador_inss)

adaptador_ir = Adaptador_CSV_IR()
adaptador_ir.set_informacoes(os.path.join(DATA_PATH, 'tabela_IR.csv'))
ir = Imposto_de_Renda(adaptador_ir)

dict_impostos = {
    'inss': inss,
    'ir': ir
}