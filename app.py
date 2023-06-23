import streamlit as st
import generate 

# Configs
st.set_page_config(page_title="Cronograma")
cronograma = False

tab1, tab2 = st.tabs(["Cadastro", "Roteiro"])

with tab1:
    nome = st.text_input("Nome do Estudante: ", key="nomeEstudante")
    cursos = st.multiselect("Curso Pretendido: ", [], )
    area = st.selectbox("Área de Estudo: ", ["Exatas e Tecnologia", "Artes e Humanidades", "Biológicas e Saúde"])
    disciplinas = st.multiselect("Disciplinas", ["Matemática", "Física", "Química", "Biologia",
                                                 "História", "Geografia", "Gramática", "Literatura",
                                                 "Sociologia"], default="Física")
    vestibulares = st.multiselect("Vestibulares: ", ["Unicamp", "Enem", "Unesp", "USP"])

    btn = st.button("Criar Cronograma")

    if btn:
        cronograma = True

with tab2:
    if cronograma:
        st.empty()  # Limpa o conteúdo anterior
        st.title("Roteiro de Estudos")
        st.text("Esse roteiro é uma parte experimental do projeto LUNA! Esperamos que goste.")

        #generate.generate(area, disciplinas, vestibulares)

tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 =  st.tabs(["Matemática", "Física", "Química", "Biologia",
                                                 "História", "Geografia", "Gramática", "Literatura",
                                                 "Sociologia"])
    
with tab3:
    generate.header(area)
    st.divider()
    generate.generate(["Matemática"])
with tab4:
    generate.header(area)
    st.divider()
    generate.generate(["Física"])
with tab5:
    generate.header(area)
    st.divider()
    generate.generate(["Química"])
with tab6:
    generate.header(area)
    st.divider()
    generate.generate(["Biologia"])
with tab7:
    generate.header(area)
    st.divider()
    generate.generate(["História"])
with tab8:
    generate.header(area)
    st.divider()
    generate.generate(["Geografia"])
with tab9:
    generate.header(area)
    st.divider()
    generate.generate(["Gramática"])
with tab10:
    generate.header(area)
    st.divider()
    generate.generate(["Literatura"])
with tab11:
    generate.header(area)
    st.divider()
    generate.generate(["Sociologia"])