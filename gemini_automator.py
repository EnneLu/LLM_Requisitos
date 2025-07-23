import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class GeminiAutomator:
    def __init__(self):
        # Configura a API com sua chave
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("A variável de ambiente 'GEMINI_API_KEY' não está definida. Por favor, adicione sua chave no arquivo .env")
        genai.configure(api_key=api_key)
        
        # Inicializa o modelo Gemini que você quer usar
        # 'gemini-1.5-flash-latest' é um bom ponto de partida por ser rápido e custo-benefício
        self.model = genai.GenerativeModel('gemini-1.5-flash-latest')

    def _gerar_conteudo(self, prompt: str) -> str:
        """
        Método interno para enviar o prompt à API do Gemini e retornar a resposta.
        """
        try:
            response = self.model.generate_content(prompt)
            # Retorna apenas o texto gerado. Pode ser necessário tratamento de erro mais robusto
            # se a LLM não conseguir gerar uma resposta (por exemplo, bloqueio de conteúdo).
            return response.text
        except Exception as e:
            print(f"Erro ao gerar conteúdo com a API Gemini: {e}")
            return "Não foi possível gerar a resposta no momento. Tente novamente mais tarde."

    def gerar_introducao_documento(self, assunto: str) -> str:
        """
        Funcionalidade: Gera a seção de Introdução do documento de requisitos.
        """
        prompt = (
            f"Gere a seção de Introdução do documento de requisitos de um sistema de {assunto}. "
            f"Inclua os objetivos do sistema, o escopo geral e a motivação para seu desenvolvimento. "
            f"Seja claro e objetivo."
        )
        return self._gerar_conteudo(prompt)
    
    def listar_stakeholders(self, assunto: str) -> str:
        """
        Funcionalidade: Lista possíveis stakeholders para o documento de requisitos.
        """
        prompt = (
            f"Liste e descreva os principais stakeholders envolvidos no desenvolvimento e uso de um sistema de {assunto}. "
            f"Inclua suas funções, interesses e nível de influência no projeto."
        )
        return self._gerar_conteudo(prompt)
    
    def gerar_visao_geral_sistema(self, assunto: str) -> str:
        """
        Funcionalidade: Gera a visão geral do sistema.
        """
        prompt = (
            f"Descreva a visão geral de um sistema de {assunto}. "
            f"Inclua uma visão de alto nível das funcionalidades principais, integrações esperadas com outros sistemas e o público-alvo."
        )
        return self._gerar_conteudo(prompt)
    
    def listar_requisitos_funcionais(self, assunto: str) -> str:
        """
        Funcionalidade: Lista 15 requisitos funcionais para o sistema desejado.
        """
        prompt = (
            f"Liste 15 requisitos funcionais para um sistema de {assunto}. "
            f"Cada requisito deve descrever claramente uma funcionalidade esperada do sistema."
        )
        return self._gerar_conteudo(prompt)
    
    def listar_requisitos_qualidade(self, assunto: str) -> str:
        """
        Funcionalidade: Lista 10 requisitos de qualidade (não funcionais) para o sistema desejado.
        """
        prompt = (
            f"Liste 10 requisitos de qualidade (não funcionais) para um sistema de {assunto}. "
            f"Considere aspectos como desempenho, segurança, usabilidade, disponibilidade e escalabilidade."
        )
        return self._gerar_conteudo(prompt)
    
    def listar_restricoes_projeto(self, assunto: str) -> str:
        """
        Funcionalidade: Lista 5 restrições de projeto para o sistema desejado.
        """
        prompt = (
            f"Liste 5 restrições de projeto aplicáveis ao desenvolvimento de um sistema de {assunto}. "
            f"Considere limitações técnicas, de plataforma, prazos, padrões obrigatórios ou requisitos legais."
        )
        return self._gerar_conteudo(prompt)
    
    def listar_regras_negocio(self, assunto: str) -> str:
        """
        Funcionalidade: Lista 5 regras de negócio para o sistema desejado.
        """
        prompt = (
            f"Liste 5 regras de negócio para um sistema de {assunto}. "
            f"Inclua políticas, restrições operacionais, cálculos ou condições específicas de negócio."
        )
        return self._gerar_conteudo(prompt)
    
    def listar_requisitos_informacionais(self, assunto: str) -> str:
        """
        Funcionalidade: Lista 5 requisitos informacionais para o sistema desejado.
        """
        prompt = (
            f"Liste 5 requisitos informacionais para um sistema de {assunto}. "
            f"Eles devem descrever quais dados ou informações o sistema deve armazenar, processar ou disponibilizar."
        )
        return self._gerar_conteudo(prompt)