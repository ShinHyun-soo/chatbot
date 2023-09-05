![image](https://github.com/ShinHyun-soo/chatbot/assets/69250097/3b67030d-95de-4aa4-a288-f0bc173ffd38)
# Chatbot using LLaMA pre-trained by cnn_dailymail

[cnn_dailymail](https://huggingface.co/datasets/ccdv/cnn_dailymail)

## Download

    Move 'pytorch_model.bin' to news_llama folder. (224Mb)

[pytorch_model.bin](http://naver.me/GnvrjQZp)

## Runs (Using 2 Anaconda Prompts on Windows 11)

    cd chatbot\src
    python -m uvicorn main_fastapi:app --reload
    cd chatbot\src
    streamlit run main_streamlit.py

## Citation

    © 2023 summer https://fastcampus.co.kr/data_online_llama



