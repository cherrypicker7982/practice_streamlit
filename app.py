import streamlit as st

# cd 240515_streamlit_연습
# streamlit run app.py


st.set_page_config(
    page_title='포켓몬도감',
    # page_icon='./images/monsterball.png',
    layout='wide',  # 이 줄을 수정했습니다.
    # initial_sidebar_state='expanded'
)

st.title('hello stream 포켓몬도감')
# st.markdown('**포켓몬** 텍스트입력')