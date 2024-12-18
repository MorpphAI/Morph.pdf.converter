# Conversor de PDF para JSONLines usando Flask

Este projeto é uma aplicação Flask que converte arquivos PDF enviados em formato **JSONLines**. Cada página do PDF é extraída e salva como um objeto JSON contendo o número da página e o conteúdo de texto correspondente.

---

## Como funciona?

A aplicação possui uma única rota `/convert`, que aceita requisições `POST` com um arquivo PDF. O PDF enviado é processado para extrair o texto de suas páginas, e o resultado é retornado no formato **JSONLines**.

---

## Tecnologias utilizadas

- **Flask**: Framework web para criar a API.
- **PyPDF2**: Biblioteca para leitura e manipulação de arquivos PDF.
- **jsonlines**: Biblioteca para trabalhar com o formato JSONLines.
- **io**: Para manipular fluxos de entrada e saída em memória.
- **os**: Para gerenciar diretórios e arquivos no sistema.

---

## Como executar o projeto

### Pré-requisitos

1. **Python 3.8 ou superior** instalado.

2. Instalar as dependências do projeto:

   ```bash
   pip install flask PyPDF2 jsonlines
