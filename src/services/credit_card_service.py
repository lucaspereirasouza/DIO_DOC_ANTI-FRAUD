from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.config import config

def analize_credit_card(card_url):
    try:
        credential = AzureKeyCredential(config.SUBSCRIPTION_KEY)
        document_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)
        card_info = document_Client.being_analyze_document(
            "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url)
        )
    
        result = card_info.result()
    
        for document in result.documents:
            fields = document.get('fields', {})
            
            return {
                "card_name": fields.get('CardHolderName',{}).get('content'),
                "card_number": fields.get('CardNumber',{}).get('content'),
                "expire_date": fields.get('ExpirationDate',{}).get('content'),
                "bank_name": fields.get('issuingBank',{}).get('content')     
            }

    except Exception as ex:
        return None

