import streamlit as st
from services.blobservice import upload_blob
from services.credit_card_service import analize_credit_card

def configure_interface():
    st.title("Upload de Arquivos DIO - desafio 1 - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png","jpg","jpeg"])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        
        blob_url = upload_blob(uploaded_file, fileName)
        
        if blob_url is not None:
            st.write(f"Arquvio {fileName} enviado com sucesso para o Azure Blob storage.")
            credit_card_info = analize_credit_card(card_url=blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f("Erro ao enviar o arquivo."))


def show_image_and_validation(blob_url,credit_card_info):
    st.image(blob_url, caption="imagem enviada")
    st.write("Resultado da verificação:")
    st.write("Inforamções de cartão de crédito encontradas:")
    st.write(credit_card_info)
    
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Cartão valido</h1>")
        st.write(f"Nome do titular: {credit_card_info['card_name']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de validade: {credit_card_info['expire_date']}")
    else:
        st.markdown("<h1 style='color: red'> cartão invalido.</h1>")
        st.write("este não é um cartão valido.")
        
        
        
if __name__ == "__main__":
    configure_interface()    
    