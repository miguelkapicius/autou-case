import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
model = "gemini-2.5-flash"


async def classify_text(text: str) -> str:
    response = client.models.generate_content(
        model=model,
        contents=[
            {
                "text": """
                Você é um analisador de emails.
                Dado o texto do usuário, identifique a intenção e, se for retirada, extraia produto e quantidade.
                Dado o email, identifique a categoria do email conforme as categorias possíveis.
                
                Possíveis Categorias:
                - Produtivo: Emails que requerem uma ação ou resposta específica (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema).
                - Improdutivo: Emails que não necessitam de uma ação imediata (ex.: mensagens de felicitações, agradecimentos).

                Responda somente com o nome da categoria, sem usar um bloco de código.
            """
            },
            {
                "text": text
            }
        ],
    )
    print(response.text)
    return response.text


async def suggest_reply(text: str) -> str:
    response = client.models.generate_content(
        model=model,
        contents=[
            {
                "text": f"""
                Você é um assistente de email do setor financeiro.
                Dado o texto do usuário, sugira uma resposta profissional e amigável.
                Considere o contexto do email e responda de forma adequada.

                Email:
                {text}

                Responda somente com o texto da resposta sugerida, sem usar um bloco de código.
                """
            }
        ],
    )
    print(response.text)
    return response.text
