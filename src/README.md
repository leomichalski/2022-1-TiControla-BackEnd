
## Setup do ambiente de debug/desenvolvimento

#### Usando Docker

Mude o diretório atual para "2022-1-TiControla-BackEnd/src"
```
cd 2022-1-TiControla-BackEnd/src
```

Crie um arquivo .env na pasta "src"
```
touch .env
```

Bote o seguinte conteúdo no arquivo .env. Lembre de substituir o valor das variáveis de ambiente por valores adequados.
```
EMAIL_HOST_USER=SUBSTITUIR.PELO.SEU.EMAIL@gmail.com
DEFAULT_FROM_EMAIL=SUBSTITUIR.PELO.SEU.EMAIL@gmail.com
EMAIL_HOST_PASSWORD=SUBSTITUIR.PELA.SUA.APP.SPECIFIC.PASSWORD@gmail.com
```


Rode o container da API usando o docker-compose
```
sudo docker-compose up --build
```

## Como gerar migrations. 
Este processo não é automático e nem deve ser automatizado: "Once the migration is applied, commit the migration and the models change to your version control system as a single commit - that way, when other developers (or your production servers) check out the code, they’ll get both the changes to your models and the accompanying migration at the same time." [fonte](https://docs.djangoproject.com/en/4.1/topics/migrations/#workflow)

#### Usando Docker

```
# baixe a imagem docker a partir do Docker Hub
docker pull leommiranda/ti-controla-django-api

# navegue até o diretório "src"
cd src

# rode um terminal dentro da imagem docker usando o seguinte comando
docker run --rm -it -v $(pwd):/current_dir -w /current_dir --user "$(id -u):$(id -g)" leommiranda/ti-controla-django-api bash

# crie as migrations
python3 manage.py makemigrations
python3 manage.py makemigrations user
python3 manage.py makemigrations user_data
```
