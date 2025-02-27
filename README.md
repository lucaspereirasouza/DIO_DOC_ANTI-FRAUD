
# Validador de Imagem de Cartão de Crédito

Este é um projeto Python para validar imagens de cartões de crédito. Ele utiliza uma API externa (por exemplo, Azure Computer Vision) para processar as imagens e verificar sua validade.

---

## Pré-requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes Python)
- Acesso a uma API de processamento de imagem (exemplo: Azure Computer Vision)

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/lucaspereirasouza/DIO_DOC_ANTI-FRAUD
cd DIO_DOC_ANTI-FRAUD
```

### 2. Crie e ative um ambiente virtual (venv)

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> **Nota:** Certifique-se de que o arquivo `requirements.txt` contém todas as bibliotecas necessárias para o projeto. Exemplo de conteúdo do arquivo:
>
> ```txt
> azure-storage-blob==12.14.1
> requests==2.28.1
> python-dotenv==1.0.0
> ```

---

## Configuração de Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e preencha as seguintes variáveis de ambiente:

```env
ENDPOINT="" #URL do endpoint da API de processamento de imagem (ex.: Azure Computer Vision).
SUBSCRIPTION_KEY="" #Chave de assinatura para acessar a API.
AZURE_STORAGE_CONNECTION_STRING="" #String de conexão para o armazenamento de blobs do Azure.
CONTAINER_NAME="defaultCardName" #Nome do contêiner no armazenamento de blobs onde as imagens serão salvas (valor padrão: `defaultCardName`).
``` 


---

## Como Usar

### Executar o script principal

Com o ambiente virtual ativado, execute o script principal:

```bash
python main.py
```

O script irá:
1. Ler a imagem do cartão de crédito.
2. Enviar a imagem para a API de processamento.
3. Validar os dados retornados pela API.

---

## Estrutura do Projeto

```
nome-do-repositorio/
├── .env                # Arquivo de configuração de variáveis de ambiente
├── main.py             # Script principal
├── requirements.txt    # Lista de dependências
├── README.md           # Documentação do projeto
└── venv/               # Ambiente virtual (não deve ser versionado)
```


---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
