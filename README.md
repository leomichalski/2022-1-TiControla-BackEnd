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
curl  -H "Content-Type: application/json" -X POST --data '{"username":"myusername", "password":"pass"}' "https://24.199.64.220.nip.io/register/"

# fazer login (é necessário salvar o valor do sessionid e o do csrftoken para usar depois)
curl -H "Content-Type: application/json" -X POST --data '{"username":"myusername", "password":"pass"}' "https://24.199.64.220.nip.io/login/"

# mostrar dados do usuario logado (email, primeiro nome, ultimo nome, data de criação do usuário)
curl -H "Cookie: sessionid=[sessionid];" -X GET 'https://24.199.64.220.nip.io/profile/'

# criar dados do usuário logado relacionados a finanças
curl -H "referer: https://24.199.64.220.nip.io/" -H "Cookie: csrftoken=[csrftoken];sessionid=[sessionid];" -H "X-CSRFToken: [csrftoken]" -X POST --data 'username=myusername&saldo=1000&limite_maximo=3000&limite_disponivel=2500' 'https://24.199.64.220.nip.io/profile/data/'

# mostrar dados do usuário logado relacionados a finanças (username, saldo, limite_maximo, limite_disponivel)
curl -H "Cookie: sessionid=[sessionid];" -X GET --data 'username=myusername' 'https://24.199.64.220.nip.io/profile/data/'

# atualizar dados do usuário logado relacionados a finanças
curl -H "referer: https://24.199.64.220.nip.io/" -H "Cookie: csrftoken=[csrftoken];sessionid=[sessionid];" -H "X-CSRFToken: [csrftoken]" -X PUT --data 'username=myusername&saldo=999&limite_disponivel=1500' 'https://24.199.64.220.nip.io/profile/data/'

curl -H "referer: https://24.199.64.220.nip.io/" -H "Cookie: csrftoken=[csrftoken];sessionid=[sessionid];" -H "X-CSRFToken: [csrftoken]" -X PATCH --data 'username=myusername&limite_maximo=7000&limite_disponivel=1500' 'https://24.199.64.220.nip.io/profile/data/'
