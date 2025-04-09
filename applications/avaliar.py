import requests

def avaliar_proteina(fruta: str) -> str:
    url = f"https://fruityvice.com/api/fruit/{fruta.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Erro ao buscar a fruta."

    dados = response.json()
    calorias = dados['nutritions']['calories']
    proteina = dados['nutritions']['protein']

    if calorias == 0:
        return "Não é possível calcular. Calorias igual a 0."

    relacao = proteina / calorias

    if relacao > 0.001:
        return f"{fruta.capitalize()} é uma boa fonte de proteína."
    else:
        return f"{fruta.capitalize()} não é uma boa fonte de proteína."