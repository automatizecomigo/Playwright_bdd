# 🚀 Configurando o Playwright em uma Máquina

## 📌 **Pré-requisitos**
Antes de instalar o Playwright, verifique se você tem os seguintes requisitos:


- **Python 3.7 ou superior** → Verifique com:
  ```bash
  python --version
  ```
- **Gerenciador de pacotes pip atualizado**:
  ```bash
  python -m pip install --upgrade pip
  ```
## 📥 **Instalação do Playwright**

1️⃣ **Criar um ambiente virtual (Recomendado)**
```bash
python -m venv venv
```
Ative o ambiente:
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```

2️⃣ **Instalar o Playwright e dependências**
```bash
pip install playwright pytest pytest-bdd
```

3️⃣ **Instalar os navegadores compatíveis**
```bash
playwright install
```

---

## ✅ **Testando a Instalação**
Para verificar se a instalação foi concluída com sucesso, execute:
```bash
python -m playwright --version
```
Se aparecer a versão do Playwright, está tudo certo!

---

## ⚡ **Executando um Teste Simples**
dentro da pasta tests executa o comando:
```python
pytest
```


## 🎯 **Dicas Extras**
- Para rodar testes no modo **headless** (sem interface gráfica), use `headless=True` ao iniciar o navegador.
- Se precisar instalar apenas um navegador específico, use:
  ```bash
  playwright install chromium  # Ou firefox/webkit
  ```
- Se houver erro ao rodar o Playwright, tente reinstalar:
  ```bash
  playwright install --force
  ```

---

Agora sua máquina está pronta para rodar testes com Playwright! 🚀🔥

