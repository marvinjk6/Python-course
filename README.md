# Python-course
This is a Python course


## Instalando Django
* Instalar Django no computador: pip install django <br>
Quando precisar de uma determinada versão do Django para algum projeto, é possível criar um ambiente virtual (é como se fosse uma caixa que o projeto é armazenado), para isso é preciso instalar um ambiente virtual, Tomi recomenda Anaconda (ver algum tutorial).

* Virtual Environment Wrapper <br>
Instalar: pip install virtualenvwrapper-win

* criar um ambiente virtual: mkvirtualenv (nome do amb. virtual) <br>
(nome do amb. virt) aparece no lado esquerdo

* <strong>Agora instalar o Django no ambiente virtual</strong>: pip install django

* Criar um projeto com o Django: django-admin startproject (nome do projeto)

* Depois de criar o projeto na pasta desejada, verificar os arquivos e pasta criados: <br>
settings.py = Esse arquivo é muito importante, todas as configurações e apps e banco de dados
vão ficar dentro desse arquivo. <br>
urls.py = Especifica as URLs que queremos no projeto

* comando para desativar o amb. virtual: deactivate

* para ativar novamente: workon myapp -> (nome do ambiente)