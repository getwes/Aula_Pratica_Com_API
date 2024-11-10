import requests

viacep = "https://viacep.com.br/ws/{cep}/json/"


def pega_endereco(cep: str) -> dict:
    """busca o endereço atraves do cep"""
    response = requests.get(viacep.replace("{cep}", cep))
