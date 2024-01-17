import this
from turtle import onclick
import streamlit as st;
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente
def Create():
    idAlteracao = st.query_params.get("id")
    clienteRecuperado = None
    if idAlteracao != None:
        idAlteracao = st.query_params.get("id")
        clienteRecuperado = ClienteController.SelecionarById(idAlteracao)
        st.query_params["id"]= clienteRecuperado.id
        st.title("Alterar cliente")
    else:
        st.title("Incluir cliente")

    with st.form(key="include_cliente"):
        listOccupation = ["Desenvolvedor", "Músico", "Designer", "Professor"]
        if clienteRecuperado == None:
            input_name = st.text_input(label="Insira o seu nome")
            input_age = st.number_input(label="Insira sua idade", format="%d", step=1)
            input_occupation = st.selectbox(label="Selecione sua profissão", options=listOccupation)
        else:
            input_name = st.text_input(label="Insira o seu nome", value=clienteRecuperado.nome)
            input_age = st.number_input(label="Insira sua idade", format="%d", step=1, value=clienteRecuperado.idade)
            input_occupation = st.selectbox(label="Selecione sua profissão", options=listOccupation, index=listOccupation.index(clienteRecuperado.profissao))
        input_button_submit = st.form_submit_button("Enviar")


    if input_button_submit:
        if clienteRecuperado == None:
            ClienteController.Incluir(cliente.Cliente(0, input_name, input_age, input_occupation))
            st.success("Cliente incluido com sucesso!")
        else:
            st.query_params.clear()
            ClienteController.Alterar(cliente.Cliente(clienteRecuperado.id, input_name, input_age, input_occupation))
            st.success("Cliente alterado com sucesso!")
        
        
