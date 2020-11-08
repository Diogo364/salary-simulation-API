import os

from flask import Flask

app = Flask(__name__, template_folder='./salary_simulation_API/templates', static_folder='./salary_simulation_API/static')
DATA_PATH = os.path.join(app.root_path, 'data')
