import streamlit as st
from gemini_automator import GeminiAutomator

st.set_page_config(page_title="Gerador de Documentos de Requisitos com Gemini", layout="wide")
st.title("👩‍💻 Engenharia de Requisitos com Gemini")

# --- Inicialização de estado ---
for key in ['automator', 'assunto', 'conteudo_gerado', 'secao_atual_index', 'documento_completo']:
    if key not in st.session_state:
        st.session_state[key] = None if key == 'automator' else "" if key == 'assunto' else 0 if key == 'secao_atual_index' else ""

# --- Fluxo de Geração ---
opcoes_fluxo = [
    ("Introdução e Contexto", "contexto_documento"),
    ("Requisitos Funcionais", "requisitos_funcionais"),
    ("Requisitos Não Funcionais", "requisitos_nao_funcionais"),
    ("Matriz de Rastreabilidade", "matriz_rastreabilidade"),
]

# --- Etapa 1: Tema do sistema ---
if st.session_state.automator is None:
    st.header("1. Qual o tema do seu sistema?")
    tema_input = st.text_input(
        "Ex: Sistema de Gestão de Eventos, Plataforma de E-commerce, Aplicativo de Saúde",
        placeholder="Digite o assunto aqui...",
        help="Esse tema será usado para guiar a IA na criação das seções do documento."
    )

    if st.button("Iniciar Geração do Documento", type="primary"):
        if tema_input and len(tema_input.strip()) >= 10:
            st.session_state.assunto = tema_input.strip()
            with st.spinner("Inicializando IA para o seu projeto..."):
                try:
                    st.session_state.automator = GeminiAutomator(st.session_state.assunto)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao inicializar a IA: {e}")
        else:
            st.warning("Descreva melhor o tema. Mínimo 10 caracteres.")
else:
    st.header(f"Documento de Requisitos: **{st.session_state.assunto}**")
    st.markdown("---")

    if st.session_state.secao_atual_index < len(opcoes_fluxo):
        secao_nome, metodo_nome = opcoes_fluxo[st.session_state.secao_atual_index]

        # Verifica se o conteúdo já foi gerado e está aguardando confirmação
        if st.session_state.conteudo_gerado:
            st.subheader(f"✅ Conteúdo Gerado: {secao_nome}")
            st.markdown(st.session_state.conteudo_gerado)

            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Confirmar e Continuar", key="confirmar_secao"):
                    st.session_state.documento_completo += f"\n\n## {secao_nome}\n{st.session_state.conteudo_gerado}"
                    st.session_state.conteudo_gerado = ""
                    st.session_state.secao_atual_index += 1
                    st.rerun()

            with col2:
                if st.button("🔄 Regenerar Seção", key="regenerar_secao"):
                    st.session_state.conteudo_gerado = ""
                    st.rerun()
        else:
            st.info(f"Próxima seção: **{secao_nome}**")

            if st.button(f"Gerar '{secao_nome}'", key=f"btn_{secao_nome}"):
                with st.spinner(f"Gerando '{secao_nome}'..."):
                    func = getattr(st.session_state.automator, metodo_nome)
                    resposta = func()

                    if not resposta.strip():
                        st.warning("A IA não gerou conteúdo. Tente novamente.")
                    elif "bloqueado" in resposta.lower():
                        st.warning("Conteúdo bloqueado por política da API.")
                    elif "Erro ao gerar" in resposta:
                        st.error(resposta)
                    else:
                        st.session_state.conteudo_gerado = resposta
                        st.rerun()
    else:
        st.success("✅ Todas as seções foram geradas!")
        st.subheader("📄 Documento Completo:")
        st.markdown(st.session_state.documento_completo)

        st.download_button(
            label="📥 Baixar Documento (.md)",
            data=st.session_state.documento_completo,
            file_name=f"documento_requisitos_{st.session_state.assunto.lower().replace(' ', '_')}.md",
            mime="text/markdown"
        )

        if st.button("🔄 Reiniciar"):
            st.session_state.clear()
            st.rerun()
