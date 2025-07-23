import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

class GeminiAutomator:
    def __init__(self, assunto: str):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("A variável de ambiente 'GEMINI_API_KEY' não está definida.")
        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel("gemini-1.5-flash-latest")
        self.chat = self.model.start_chat(history=[])
        self.chat.send_message(
            f"Você é um engenheiro de requisitos especialista em {assunto}. Gere conteúdos profissionais e objetivos para um documento ERS."
        )

    def _enviar_prompt_ao_chat(self, prompt: str) -> str:
        try:
            response = self.chat.send_message(prompt)
            return response.text or ""
        except Exception as e:
            return f"Erro ao gerar conteúdo com a API Gemini: {e}"

    def contexto_documento(self) -> str:
        prompt = (
            "Gere a seção 1. Introdução e Contexto para um Documento de Requisitos de Software (ERS) profissional e bem estruturado."
            "Siga estas instruções cuidadosamente:"
            "1. **Objetivo do Documento**:"
            "- Explique o propósito deste documento."
            "- Indique quais stakeholders o utilizarão (ex: analistas, desenvolvedores, clientes)."
            "2. **Descrição Geral do Sistema**:"
            "- Apresente o sistema de forma sucinta e clara."
            "- Inclua o tipo de sistema (ex: web, mobile, embarcado) e seu domínio (ex: saúde, educação, eventos)."
            "- Informe as principais funções do sistema."
        )
        return self._enviar_prompt_ao_chat(prompt)

    def requisitos_funcionais(self) -> str:
        prompt = (
            "Gere a seção de Requisitos Funcionais. Liste no mínimo 15 RFs detalhados usando este template:\n"
            "| ID | Título | Descrição | Critério de Aceitação | Prioridade (MoSCoW) |\n"
            "**Formato:** [**Como um** <stakeholder>, **eu quero** <ação> **para que** <objetivo>.]"
        )
        return self._enviar_prompt_ao_chat(prompt)

    def requisitos_nao_funcionais(self) -> str:
        prompt = (
            "Gere a seção de Requisitos Não Funcionais. Liste no mínimo 10 RNFs abordando usabilidade, desempenho, segurança e confiabilidade. "
            "Use o template:\n"
            "| ID | Título | Descrição | Critério de Aceitação | Prioridade (MoSCoW) | Conflita com o RNF |"
        )
        return self._enviar_prompt_ao_chat(prompt)

    def matriz_rastreabilidade(self) -> str:
        prompt = (
            "Crie uma tabela Markdown de matriz de rastreabilidade relacionando os IDs dos RFs com os RNFs. "
            "Formato da matriz:\n"
            "| RF \\ RNF | RNF01 | RNF02 | RNF03 |\n"
            "|----------|--------|--------|--------|\n"
            "| RF01     |   X    |        |   X    |"
        )
        return self._enviar_prompt_ao_chat(prompt)
