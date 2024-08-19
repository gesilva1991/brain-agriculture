# brain-agriculture
REST API

## Install
1 - First clone the repository and enter the project folder.
```bash
  $ git clone https://github.com/gesilva1991/brain-agri.git
  $ cd brain-agriculture
```
2 - Configure environment variables
```bash
 create .env based on .env-exemple
```
3 - Start docker compose
```bash
  $ docker compose up --build
```
4 - Start tests
```bash
  $ cd app/
  $ python manage.py test
```

## Register a new Producers

### Example Request

`POST /register/`
```bash
curl --location 'http://3.144.138.204:8000/api/produtores/' \
--data-raw '{
    "nome": "João da Silva",
    "cpf": "12345678901",
    "cidade": "São Paulo",
    "estado": "SP",
    "area_total": 100.0,
    "area_agricultavel": 60.0,
    "area_vegetacao": 30.0,
    "culturas_plantadas": "Soja"
}'
```
### Example Response
```bash
{
    "id": 1,
    "nome": "João da Silva",
    "cpf": "12345678901",
    "cnpj": null,
    "cidade": "São Paulo",
    "estado": "SP",
    "area_total": 100.0,
    "area_agricultavel": 60.0,
    "area_vegetacao": 30.0,
    "culturas_plantadas": "Soja"
}
```
### Example Request

`GET /register/`
```bash
curl --location 'http://3.144.138.204:8000/api/produtores/' \
```
### Example Response
```bash
[
{
    "id": 1,
    "nome": "João da Silva",
    "cpf": "12345678901",
    "cnpj": null,
    "cidade": "São Paulo",
    "estado": "SP",
    "area_total": 100.0,
    "area_agricultavel": 60.0,
    "area_vegetacao": 30.0,
    "culturas_plantadas": "Soja"
}
]
```
### Example Request

`DELETE /register/`
```bash
curl --location 'http://3.144.138.204:8000/api/produtores/{id}' \

### Example Response
```bash
No body returned for response
```

### Example Request

`PUT /register/`
```bash
curl --location 'http://3.144.138.204:8000/api/produtores/{1}' \
--data-raw '{
    "nome": "João da Silva Atualizado",    
    "cidade": "São Paulo Atualizado",
}'
```
### Example Response
```bash
{
    "id": 1,
    "nome": "João da Silva Atualizado",
    "cpf": "12345678901",
    "cnpj": null,
    "cidade": "São Paulo Atuaçizado",
    "estado": "SP",
    "area_total": 100.0,
    "area_agricultavel": 60.0,
    "area_vegetacao": 30.0,
    "culturas_plantadas": "Soja"
}
```


### Example Request

`GET /dashboard/`
```bash
curl --location ''http://3.144.138.204:8000/api/dashboard' \
```
### Example Response
```bash
{
	"total_fazendas": 1,
	"uso_do_solo": 1
}
```
