import streamlit as st
from controller import ItemController

controller = ItemController()
st.title("Cadastro de Itens")
st.subheader("Cadastrar novo item")
descricao = st.text_input("Descrição do item")
quantidade = st.number_input("Quantidade", min_value=0)

if st.button("Adicionar item"):
    controller.criarItem(descricao, quantidade)
    st.success("Item adicionado com sucesso!")

st.subheader("Lista de itens")
itens = controller.obterTodosOsItens()

if itens:
    for item in itens:
        st.write(f"{item.get_id()} - **Descrição:** {item.get_descricao()} | **Quantidade:** {item.get_quantidade()}")
else:
    st.info("Nenhum item cadastrado ainda.")
