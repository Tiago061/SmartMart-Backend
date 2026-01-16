Documentation: SmartMart Solutions Project Este projeto é uma aplicação Full Stack para gerenciamento de vendas e produtos, composta por um Backend em Python (FastAPI) e um Frontend em React (Next.js) com suporte a importação de dados via CSV e visualização de dashboards.

🚀 Como Rodar o Projeto

Pré-requisitos Python 3.10+ instalado.

Configurando o Backend (Python/FastAPI)
Navegue até a pasta do backend:

Faça git clone do projeto

Bash: cd backend

Instale as dependências:

Bash: pip install fastapi uvicorn sqlalchemy pydantic python-multipart ou pip install -r requirements.txt

Inicie o servidor: uvicorn app.main:app --reload

O servidor estará rodando em: http://127.0.0.1:8000

Documentação interativa (Swagger): http://127.0.0.1:8000/docs