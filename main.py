import streamlit as st
import Pages.Cliente.Create as PageCreateCliente
import Pages.Cliente.List as PageListCliente

st.sidebar.title('Menu')
pagina_cliente = st.sidebar.selectbox('Cliente', ['Incluir', 'Consultar'])

if pagina_cliente == 'Incluir':
    PageCreateCliente.Create()

if pagina_cliente == 'Consultar':
    PageListCliente.List()
    