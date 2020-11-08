# Salary-Simulation-API

## Descrição:
Aplicação que realiza simulações de rendimentos e tributos baseadas
 na modalidade de contratação e salário mensal.

## Motivação:
Hoje, principalmente na área de tecnologia, vivemos em um momento onde
a contratação de profissionais não seguem um padrão definido, podendo
ser feita nos moldes da legislação trabalhista - CLT - ou como autônomos
prestadores de serviço - PJ, MEI etc.

Com isso surge a necessidade de se entender melhor as vantagens,
desvantagens e obrigações tributárias de cada modalidade, de forma a 
facilitar a tomada de decisão.   
 
## Autor:
- Diogo Telheiro do Nascimento
    - [Github](https://github.com/Diogo364)
    - [Linkedin](https://www.linkedin.com/in/diogo-telheiro-do-nascimento-95384a104/)


## Contexto:
Esse projeto foi desenvolvido como trabalho prático para a disciplina 
de Programação Orientada a Objeto - POO do IESB, ofertado em 2º/2020 
pelo professor [Kenniston](https://github.com/kenniston).

## Objetivo
Esse trabalho tem como objetivo a aplicação dos pilares de POO, Design
Patterns e dos princípios SOLID na criação de um API.

## Quickstart:
Existem duas formas de se executar essa aplicação:

### 1. Container Docker
Para executar a aplicação utilizando um container Docker você precisa
ter o Docker instalado e configurado em sua máquina. 
Para isso, dê uma olhada no site oficial por este [link](https://www.docker.com/).

Caso já o tenha instalado em sua máquina execute os passos seguintes:
#### 1.1 Execute o shellscript `docker-build.sh`
Esse shellscript irá executar o comando para a construção da imagem 
Docker a ser utilizada.

#### 1.2 Execute o shellscript `docker-run.sh`
Esse shellscript ira executar o comando para o executar o container.


### 2. Python
Você pode executar o projeto em sua máquina local.
Basta seguir os passos abaixo.

#### 2.1 Instalar o Python
Para esse projeto iremos utilizar o `Python==3.8`. Caso não o tenha
em sua máquina, basta entrar neste 
[link](https://www.python.org/downloads/release/python-380/)
para o site oficial e fazer o download.

#### 2.2 Criar um Ambiente Virtual
O ambiente virtual é utilizado para isolar as dependências entre
diferentes projetos. Além de melhorar a exportabilidade de um projeto. 

Minha sugestão para esse projeto é utilizar o `venv`, que já vem 
instalado por padrão no python.

Para criarmos um ambiente virtual chamado `venv` basta executarmos 
o comando abaixo:

```
$ python -m venv venv
```

> **NOTA:**  Sinta-se livre para utilizar qualquer gerenciador de 
>ambientes virtuais, porém seguirei utilizando o `venv` neste 
>documento.

#### 2.3 Ativar o ambiente virtual
Esse passo depende de qual SO você está utilizando, para detalhes de como
realizar esse passo em Windows, por favor, confira a [Documentação
Oficial](https://docs.python.org/3/library/venv.html)

Já para os SO baseados em Unix, basta executar o comando abaixo:
```
$ source venv/bin/activate
```
Você deverá notar o aparecimento do nome dado ao venv em seu prompt.
Algo similar ao que está abaixo:
```
(venv) $ 
```

#### 2.4 Instalar dependências:
Uma vez que você ativou o ambiente virtual, basta utilizar o pip, que
é o principal gerenciador de dependências do python, para fazer o 
download das depenências que estão no arquivo `requirements.txt`.
```
(venv) $ pip install -r requirements.txt
```

#### 2.5 Executar o código
Para essa parte basta executar o comando abaixo:
```
(venv) $ python run.py
```

Após a execução você deverá ver uma mensagem semelhante à abaixo:
```
(venv) $ python run.py
 * Serving Flask app "env_variables" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Isso significa que a aplicação já está de pé e pode ser acessada pela
url [http://localhost:5000/](http://localhost:5000/).