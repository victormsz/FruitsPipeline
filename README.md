# 🍌 FruitsPipeline

Projeto Python com CI/CD utilizando **GitHub Actions**, que avalia se uma fruta é uma boa fonte de proteína usando a [API Fruityvice](https://www.fruityvice.com/), executa testes automatizados com `pytest`, e envia notificações por e-mail ao final da pipeline.

---

## 📦 Funcionalidade

- Acessa dados nutricionais de frutas via API.
- Avalia a proporção de proteína por caloria.
- Retorna mensagens como:
  - `"Banana não é uma boa fonte de proteína."`
  - `"Soja é uma boa fonte de proteína."`
- Realiza testes automatizados com `pytest`.
- Envia notificação por e-mail após a execução da pipeline.

---

## 🧪 Como rodar os testes

1. Instale as dependências:

```bash
pip install -r requirements.txt
