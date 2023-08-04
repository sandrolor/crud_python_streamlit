import streamlit as st
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente

def Create():
    idAlteracao = st.experimental_get_query_params()
    #st.experimental_set_query_params()
    clienteRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        clienteRecuperado = ClienteController.selecionarById(idAlteracao)
        st.experimental_set_query_params(id=[clienteRecuperado.id])
        st.title('Alterar Cliente')
    else:
        st.title('Incluir Cliente')
    
    with st.form(key="include_cliente"):
        listOccupation = ["Desenvolvedor", "Músico", "Designer", "Professor"]
        if clienteRecuperado == None:
            input_id = 0
            input_name = st.text_input(label="Insira o seu Nome")
            input_age = st.number_input(label="Insira a sua idade",format="%d",step=1)
            input_occupation = st.selectbox("Selecione sua Ocupação", options=listOccupation)
        else:
            input_id = clienteRecuperado.id
            input_name = st.text_input(label="Insira o seu Nome", value=clienteRecuperado.nome)
            input_age = st.number_input(label="Insira a sua idade",format="%d",step=1, value=clienteRecuperado.idade)
            input_occupation = st.selectbox("Selecione sua Ocupação", options=listOccupation, index=listOccupation.index(clienteRecuperado.profissao))
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        cliente.id = input_id
        cliente.nome = input_name
        cliente.idade = input_age
        cliente.profissao = input_occupation

        if clienteRecuperado == None:
            ClienteController.incluir(cliente)
            st.success("Cliente cadastrado com sucesso!")    
        else:
            ClienteController.alterar(cliente)
            st.success("Cliente alterado com sucesso!")    