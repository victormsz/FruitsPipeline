from applications.avaliar import avaliar_proteina as avaliar
from unittest.mock import patch
import pytest

@pytest.mark.parametrize("nome, calorias, proteina, esperado", [
    ("soja", 100, 36, "é uma boa fonte de proteína"),
    ("amendoim", 567, 25.8, "é uma boa fonte de proteína"),
    ("banana", 96, 1, "não é uma boa fonte de proteína"),
    ("melancia", 30, 0.6, "não é uma boa fonte de proteína"),
    ("abacate", 160, 2, "não é uma boa fonte de proteína"),
    ("espinafre", 23, 2.9, "é uma boa fonte de proteína"),
    ("brocolis", 34, 2.8, "é uma boa fonte de proteína"),
    ("alface", 15, 1.4, "é uma boa fonte de proteína"),
    ("morango", 32, 0.7, "não é uma boa fonte de proteína"),
    ("cenoura", 41, 0.9, "não é uma boa fonte de proteína"),
])
@patch("applications.avaliar.requests.get")
def test_fontes_de_proteina(mock_get, nome, calorias, proteina, esperado):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "name": nome,
        "nutritions": {
            "calories": calorias,
            "protein": proteina,
        }
    }

def test_banana_nao_tem_muita_proteina_sem_mock():
    resultado = avaliar("banana")
    assert "não é uma boa fonte de proteína" in resultado

def test_proteina_fruta_nao_existe():
    resultado = avaliar("fruta_imaginaria")
    assert "Erro ao buscar a fruta." == resultado

@patch("applications.avaliar.requests.get")
def test_banana_nao_tem_muita_proteina(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "name": "Banana",
        "nutritions": {
            "calories": 996,
            "protein": 1,
        }
    }

    resultado = avaliar("banana")
    assert "não é uma boa fonte de proteína" in resultado

@patch("applications.avaliar.requests.get")
def test_fruta_com_erro(mock_get):
    mock_get.return_value.status_code = 404

    resultado = avaliar("abacate")
    assert resultado == "Erro ao buscar a fruta."


@patch("applications.avaliar.requests.get")
def test_fruta_muito_proteica(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "name": "Soja",
        "nutritions": {
            "calories": 100,
            "protein": 20,
        }
    }

    resultado = avaliar("soja")
    assert "é uma boa fonte de proteína" in resultado


@patch("applications.avaliar.requests.get")
def test_fruta_com_calorias_zero(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "name": "Fantasia",
        "nutritions": {
            "calories": 0,
            "protein": 10,
        }
    }

    resultado = avaliar("fantasia")
    assert resultado == "Não é possível calcular. Calorias igual a 0."

@patch("applications.avaliar.requests.get")
def test_fruta_com_dados_incompletos(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "name": "FrutaBugada",
        "nutritions": {
            "calories": 50
            # protein ausente
        }
    }

    try:
        resultado = avaliar("frutabugada")
        assert False, "Deveria lançar KeyError"
    except KeyError:
        pass  # esperado,


@patch("applications.avaliar.requests.get")
def test_capitalizacao_do_nome(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "name": "banana",
        "nutritions": {
            "calories": 100,
            "protein": 1,
        }
    }

    resultado = avaliar("BaNaNa")
    assert resultado.startswith("Banana")


@patch("applications.avaliar.requests.get")
def test_fruta_sem_proteina(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "name": "Melancia",
        "nutritions": {
            "calories": 30,
            "protein": 0,
        }
    }

    resultado = avaliar("melancia")
    assert "não é uma boa fonte de proteína" in resultado


@patch("applications.avaliar.requests.get")
def test_fruta_com_minimos_valores(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "name": "MiniFruta",
        "nutritions": {
            "calories": 1,
            "protein": 1,
        }
    }

    resultado = avaliar("minifruta")
    assert "é uma boa fonte de proteína" in resultado