from dotenv import load_dotenv
import openai
import os

load_dotenv()
# 環境変数からAPIキーを取得
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY が設定されていません。環境変数にAPIキーを設定してください。")

openai.api_key = api_key


def ask_ai(message):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": message}],
    )
    return response["choices"][0]["message"]["content"]
