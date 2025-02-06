# 필요한 라이브러리 설치 (VS Code 터미널에서 실행)
# 터미널에서 수동으로 실행: pip install langchain langchain-openai python-dotenv

import os
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()  
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    api_key = input("Enter your OpenAI API key: ")
    os.environ["OPENAI_API_KEY"] = api_key

from langchain_openai import ChatOpenAI

# GPT 모델 불러오기
chat_model = ChatOpenAI(model_name="gpt-3.5-turbo")

# 번역 함수 정의
def translate_text(text, target_language):
    prompt = f"Translate the following text to {target_language}:\n\n'{text}'"
    response = chat_model.invoke(prompt)
    return response

# 사용자 입력 받기
text_to_translate = input("번역할 문장을 입력하세요: ")
target_language = input("번역할 언어를 입력하세요 (예: English, Korean, French): ")

# 번역 실행 및 출력
translated_text = translate_text(text_to_translate, target_language)
print(f"번역된 문장: {translated_text}")
