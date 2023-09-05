# © 2023 summer https://fastcampus.co.kr/data_online_llama

from fastapi import FastAPI
import torch
from transformers import LlamaForCausalLM, AutoTokenizer

# FastAPI 인스턴스 설치
app = FastAPI()

# Tokenizer 로드
tokenizer = AutoTokenizer.from_pretrained("news_gpt2")

# 모델 로드
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = LlamaForCausalLM.from_pretrained("news_llama")
model.to(device)

def get_answer(prompt):

    inputs = tokenizer(prompt, return_tensors="pt")
    inputs.to(device)

    # 생성
    generate_ids = model.generate(inputs.input_ids, max_length=inputs.input_ids.shape[1]+5)
    output = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    output = output[len(prompt):]

    return(output)

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.post('/chat_test')
async def test(user_message):
    return {'message': get_answer(user_message)}

@app.post('/chat')
async def chat(param: dict={}):
    user_message = param.get('user_message', ' ')
    return {'message': get_answer(user_message)}