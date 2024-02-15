%pip install git+https://github.com/huggingface/transformers
#%pip install git+https://github.com/huggingface/peft.git
%pip install langchain
%pip install openai
%pip install streamlit
%pip install streamlit_lottie
%pip install streamlit-authenticator

!wget -q -O - ipv4.icanhazip.com
! streamlit run /content/interface.py & npx localtunnel --port 8501

