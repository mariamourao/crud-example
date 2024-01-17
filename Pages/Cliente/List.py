from unittest import main
import streamlit as st
import Controllers.ClienteController as ClienteController
#from streamlit import caching
import Pages.Cliente.Create as PageCreateCliente
import services.database as db


def List():
    paramId = st.experimental_get_query_params()

    if paramId.get("id") == None:
        st.experimental_set_query_params()
        colms = st.columns((1, 2, 1, 2, 1, 1))
        campos = ['Nº', 'Nome', 'Idade', 'Profissão', 'Excluir', 'Alterar']

        for col, campo_nome in zip(colms,campos):
            col.write(campo_nome)

        for x,item in enumerate(ClienteController.SelecionarTodos()):
            col1, col2, col3, col4, col5, col6 = st.columns((1, 2, 1, 2, 1, 1))
            col1.write(item.id)
            col2.write(item.nome)
            col3.write(item.idade)
            col4.write(item.profissao)
            button_space_delete = col5.empty()
            on_click_delete = button_space_delete.button('Delete','btnDelete' + str(item.id))
            button_space_edit = col6.empty()
            on_click_edit = button_space_edit.button('Edit','btnEdit' + str(item.id))

            if on_click_delete:
                ClienteController.Excluir(item.id)
                button_space_delete.button(
                    'Excluido','btnExcluir' + str(item.id)
                )
            if on_click_edit:
                st.experimental_set_query_params(
                    id=[item.id]
                )
                st.experimental_rerun()
    else:
        on_click_return = st.button("Return")
        if on_click_return:
            st.experimental_set_query_params()
            st.experimental_rerun()
        PageCreateCliente.Create()  