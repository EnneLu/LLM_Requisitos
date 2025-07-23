# Gerador de Documentos de Requisitos com Gemini

![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-red?logo=streamlit)
![Google Gemini](https://img.shields.io/badge/LLM-Gemini-blue?logo=google)
![License](https://img.shields.io/github/license/SEU_USUARIO/NOME_DO_REPOSITORIO)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Este é um sistema web desenvolvido com **Streamlit** que utiliza o modelo **Google Gemini** (via API) para gerar automaticamente **documentos de requisitos de software (ERS)** de forma assistida e estruturada.

## Funcionalidades

- Entrada de tema/sistema do projeto
- Geração passo-a-passo das seções do documento:
  - Introdução e Contexto
  - Requisitos Funcionais
  - Requisitos Não Funcionais
  - Matriz de Rastreabilidade
- Exibição e validação manual de cada seção antes de continuar
- Exportação do documento final em formato **Markdown (.md)**
- Regeneração de seções quando necessário
