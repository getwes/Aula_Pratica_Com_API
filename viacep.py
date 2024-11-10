import requests

viacep = "https://viacep.com.br/ws/{cep}/json/"


def pega_endereco(cep: str) -> dict:
    """busca o endereço atraves do cep"""
    response = requests.get(viacep.replace("{cep}", cep))
    if not response.status_code == 200:
        return {}
    return response.json()

print(pega_endereco("01001000"))