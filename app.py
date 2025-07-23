# import time
# import google.generativeai as genai
# import streamlit as st
# import os

# with st.sidebar:
#     st.title("Chave da API Gemini")
#     gemini_api_key = st.text_input("Gemini API Key", key="chatbot_api_key", type="password")

# st.title("💬 Chatbot com Gemini")
# st.caption("🚀 Um chatbot Streamlit alimentado pelo Google Gemini")

# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "model", "content": "Olá! Em que posso ajudar hoje?"}]

# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])

# if prompt := st.chat_input():
#     if not gemini_api_key:
#         st.info("Por favor, adicione sua chave da API do Gemini para continuar.")
#         st.stop()

#     genai.configure(api_key=gemini_api_key)

#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)

#     try:
#         model = genai.GenerativeModel('gemini-1.5-flash-latest')
#         chat = model.start_chat(history=[])
#         response = chat.send_message(prompt)
#         msg = response.text

#         st.session_state.messages.append({"role": "model", "content": msg})

#         # Efeito de digitação palavra por palavra
#         with st.chat_message("model"):
#             message_placeholder = st.empty()
#             typed_text = ""
#             for word in msg.split():
#                 typed_text += word + " "
#                 message_placeholder.markdown(typed_text + "▌")
#                 time.sleep(0.1)
#             message_placeholder.markdown(typed_text)

#     except Exception as e:
#         st.error(f"Ocorreu um erro ao chamar a API do Gemini: {e}")



from gemini_automator import GeminiAutomator
import streamlit as st
import google.generativeai as genai
import os


# --- Lógica do Frontend com Streamlit ---
st.set_page_config(page_title="Gerador de Documentos de Requisitos com Gemini", layout="wide")

st.title("✍️ Gerador de Documentos de Requisitos com Gemini")
st.markdown("Use a inteligência artificial para auxiliar na criação de seções de documentos de requisitos.")

# Inicializa o automator (cria uma instância uma vez para a sessão)
# @st.cache_resource garante que o objeto GeminiAutomator seja criado apenas uma vez
@st.cache_resource
def get_automator():
    return GeminiAutomator()

automator = get_automator()

# --- Entrada do Usuário: Assunto do Sistema ---
st.header("1. Assunto do Sistema")
st.markdown("Qual é o tema ou nome do sistema que você quer documentar?")
tema_do_sistema = st.text_input("Ex: Sistema de Gestão de Eventos, Plataforma de E-commerce, Aplicativo de Saúde", 
                                 key="tema_input", 
                                 placeholder="Digite o assunto aqui...",
                                 help="O assunto será usado para gerar todas as seções do documento.")

st.markdown("---")

# --- Seleção da Funcionalidade ---
st.header("2. Selecione a Seção para Gerar")

opcoes_geracao = {
    "Introdução": automator.gerar_introducao_documento,
    "Stakeholders": automator.listar_stakeholders,
    "Visão Geral do Sistema": automator.gerar_visao_geral_sistema,
    "Requisitos Funcionais (15 itens)": automator.listar_requisitos_funcionais,
    "Requisitos de Qualidade (10 itens)": automator.listar_requisitos_qualidade,
    "Restrições de Projeto (5 itens)": automator.listar_restricoes_projeto,
    "Regras de Negócio (5 itens)": automator.listar_regras_negocio,
    "Requisitos Informacionais (5 itens)": automator.listar_requisitos_informacionais,
}

# Criar um menu suspenso (select box) para o usuário escolher
secao_selecionada = st.selectbox(
    "Escolha qual seção do documento de requisitos você deseja gerar:",
    options=list(opcoes_geracao.keys()),
    key="secao_select"
)

# Botão para gerar o conteúdo
gerar_botao = st.button("Gerar Seção", type="primary")

st.markdown("---")

# --- Exibição do Resultado ---
st.header("3. Resultado Gerado")
if gerar_botao and tema_do_sistema:
    with st.spinner("Gerando conteúdo... Por favor, aguarde."):
        # Chama o método correspondente baseado na seleção do usuário
        funcao_selecionada = opcoes_geracao[secao_selecionada]
        conteudo_gerado = funcao_selecionada(tema_do_sistema)
    
    st.subheader(f"Conteúdo para '{secao_selecionada}' sobre '{tema_do_sistema}':")
    st.write(conteudo_gerado) # st.write renderiza Markdown automaticamente
    
    # Opção para copiar o texto
    st.download_button(
        label="Copiar Texto",
        data=conteudo_gerado,
        file_name=f"{secao_selecionada.lower().replace(' ', '_')}_{tema_do_sistema.lower().replace(' ', '_')}.txt",
        mime="text/plain"
    )

elif gerar_botao and not tema_do_sistema:
    st.warning("Por favor, insira o **Assunto do Sistema** antes de gerar a seção.")

else:
    st.info("Digite o assunto do sistema e selecione a seção desejada para começar.")