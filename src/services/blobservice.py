import os
import azure.storage.blbo import BlobServiceClient
import streamlit as st
from utils.config import config

def upload_blob(file, filename):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(config.AZURE_STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=config.CONTAINER_NAME, blob=file_name)
        blob_client.upload.blob(file)
        return blob_client.url
    
    except Exception as ex:
        st.error(f"Erro ao enviar o arquivo para a Azure Blbo Storage.")
        return None