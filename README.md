# olympic_history

[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Este projeto foi feito com base no cookiecutter, que facilita o desenvolvimento e prapara o ambiente com a configurações de banco de dados e bibliotecas, e um padrão para organização dos modulos.

# Prerequisites

Optei por desenvolver o projeto dentro de um container. O que facilita o desenvolvimento.

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

Para iniciar o desenvolvimento local apenas execute o commando:
```bash
docker-compose up
```

Depois é necessário criar um superusuario:
```bash
docker-compose run --rm web ./manage.py createsuperuser
```

O desafio é criar uma API com os dados [120 years of Olympic history](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results#%20athlete_events.csv).

Para subir os dados para o banco de dados é necessário digitar o comando:
```bash
docker-compose run --rm web ./manage.py load_csv resources/athlete_events.csv
```

OBS: Para minimizar a repetição de dados, por isso pode demora quase 90 minutos para carregar os dados da planilhas. Então você pode tentar carregar os dados deste json.
```bash
docker-compose run --rm web ./manage.py loaddata olympic_data.json
```

A documentação das API, pode ser acessado pelos seguintes links (localmente):
- [Swagger](http://127.0.0.1:8000/swagger/)
- [Redoc](http://127.0.0.1:8000/redoc/)

