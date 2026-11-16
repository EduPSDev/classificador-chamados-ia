from dotenv import load_dotenv
from google import genai

# Carrega a chave GEMINI_API_KEY do arquivo .env
load_dotenv()

# Inicializa o cliente que se comunica com a API
client = genai.Client()

# Envia uma requisição simples para o modelo
resposta = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explique em duas frases por que classificar chamados de suporte por urgência ajuda uma operação."
)

print("Resposta da IA:")
print(resposta.text)