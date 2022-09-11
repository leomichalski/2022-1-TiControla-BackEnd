## Como levantar a API

```
# esteja na pasta "2022-1-TiControla/django-api"
cd 2022-1-TiControla-BackEnd/api

# rode o container
sudo docker-compose up --build
```

## Como fazer requisições HTTP para a API usando cURL
A biblioteca cURL não é necessária. Para converter um comando cURL para uma linguagem de programação (como javascript), use o site <https://curlconverter.com/#javascript>. Para fins de debugging, além do cURL, por exemplo, existem as ferramentas httpie e postman.

```
# criar usuário (não superusuário)
curl -H "Content-Type: application/json" -X POST --data '{"username":"myusername", "password":"pass"}' "localhost:8000/register/"

# fazer login (é necessário salvar o valor do sessionid e o do csrftoken para usar depois)
curl -v -H "Content-Type: application/json" -X POST --data '{"username":"myusername", "password":"pass"}' "localhost:8000/login/"

# mostrar dados do usuario logado (email, primeiro nome, ultimo nome, data de criação do usuário)
curl -H "Cookie: sessionid=[sessionid];" -X GET 'localhost:8000/profile/'

# criar dados do usuário logado relacionados a finanças
curl -H "Cookie: csrftoken=[csrftoken];sessionid=[sessionid];" -H "X-CSRFToken: [csrftoken]" -X POST --data 'username=myusername&saldo=1000&limite_maximo=3000&limite_disponivel=2500' 'localhost:8000/profile/data/'

# mostrar dados do usuário logado relacionados a finanças (username, saldo, limite_maximo, limite_disponivel)
curl -H "Cookie: sessionid=[sessionid];" -X GET --data 'username=myusername' 'localhost:8000/profile/data/'

# atualizar dados do usuário logado relacionados a finanças
curl -H "Cookie: csrftoken=[csrftoken];sessionid=[sessionid];" -H "X-CSRFToken: [csrftoken]" -X PUT --data 'username=myusername&saldo=999&limite_disponivel=1500' 'localhost:8000/profile/data/'

curl -H "Cookie: csrftoken=[csrftoken];sessionid=[sessionid];" -H "X-CSRFToken: [csrftoken]" -X PATCH --data 'username=myusername&limite_maximo=7000&limite_disponivel=1500' 'localhost:8000/profile/data/'
```


## Como gerar migrations

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
