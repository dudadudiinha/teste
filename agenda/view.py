import streamlit as st
from agenda.controller import ItemController

st.set_page_config(page_title="Cadastro de Itens", layout="centered")

controller = ItemController()

st.title("📦 Cadastro de Itens")

# Formulário de cadastro
st.subheader("Cadastrar novo item")
descricao = st.text_input("Descrição do item")
quantidade = st.number_input("Quantidade", min_value=0, step=1)

if st.button("Adicionar Item"):
    try:
        controller.criarItem(descricao, quantidade)
        st.success("Item adicionado com sucesso!")
    except ValueError as e:
        st.error(str(e))

# Listagem de itens
st.subheader("Itens cadastrados")
itens = controller.obterTodosOsItens()

if itens:
    for item in itens:
        st.write(f"**ID:** {item.id} | **Descrição:** {item.descricao} | **Quantidade:** {item.quantidade}")
else:
    st.info("Nenhum item cadastrado ainda.")
