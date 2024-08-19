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

## Register a new User

### Example Request

`POST /register/`
```bash
curl --location 'http//127.0.0.1:8000/api/produtores-rurais/' \
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
