import streamlit as st

# cd 240515_streamlit_연습
# streamlit run app.py


st.set_page_config(
    page_title='포켓몬도감',
    page_icon='./images/monsterball.png',
    layout='wide',  # 이 줄을 수정했습니다.
    # initial_sidebar_state='expanded'
)

st.title('hello stream 포켓몬도감')
st.markdown('**포켓몬** 텍스트입력')

type_emoji_dict = {
    "노말": "⚪",
    "격투": "✊",
    "비행": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}



initial_pokemons = [
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/pikachu.webp"
    },
    {
        "name": "누오",
        "types": ["물", "땅"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp",
    },
    {
        "name": "갸라도스",
        "types": ["물", "비행"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/garados.webp",
    },
    {
        "name": "개굴닌자",
        "types": ["물", "악"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/frogninja.webp"
    },
    {
        "name": "루카리오",
        "types": ["격투", "강철"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/lukario.webp"
    },
    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/acebun.webp"
    },
]

if 'pokemons' not in st.session_state:
    st.session_state['pokemons'] = initial_pokemons



auto_complete = st.toggle(label='예시 자동완성')

auto_complete_pokemons =  {
        "name": "예시1",
        "types": ["물", "땅"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp",
    }


with st.form(key='pokemon_form'):
    col1, col2 = st.columns(2)
    
    with col1:
        user_input = st.text_input(
            label='포켓몬 이름을 입력하세요',
            value=auto_complete_pokemons['name'] if auto_complete else ''
            )
    
    with col2:
        types_input = st.multiselect(
            label='타입을 선택하세요', 
            options=list(type_emoji_dict.keys()), 
            default=auto_complete_pokemons['types'] if auto_complete else [],
            max_selections=3,
            
            )


        # types_input = st.multiselect(label='타입을 선택하세요', options=list(type_emoji_dict.keys()), default=type_emoji_dict.keys())
        
        
    image_url_input = st.text_input(
        label='이미지 URL을 입력하세요',
        value = auto_complete_pokemons['image_url'] if auto_complete else ''
        )    
    # image_url_input = auto_complete_pokemons['image_url'] if auto_complete else ''
    
    
    submit_button = st.form_submit_button(label='추가')

if submit_button:
    print(user_input)
    
    if not user_input:
        st.error('포켓몬 이름을 입력하세요')
    if not  types_input:
        st.error('타입을 선택하세요')

    else:    
        if not image_url_input:
            print('image url 없어서 기본 이미지 입력함')
            image_url_default = 'https://storage.googleapis.com/firstpenguine-coding-school/pokemons/acebun.webp'
            image_url_input = image_url_default

        st.session_state['pokemons'].append({
            "name": user_input,
            "types": types_input,
            "image_url": image_url_input
        })
        





# col1, col2, col3 = st.columns(3)
cols = st.columns(3)

for i in range(len(st.session_state['pokemons'])):
    # print(i)
    with cols[i%3]:
        pokemon = st.session_state['pokemons'][i]
        with st.expander(label=f"{i+1} {pokemon['name']}", expanded=True):
            st.image(pokemon['image_url'])
            eomiji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon['types']]
            st.subheader(' / '.join(eomiji_types))
            delete_buttn = st.button(label = '삭제', key=f'delete_button_{i}', use_container_width=True)

            if delete_buttn:
                del st.session_state['pokemons'][i]
                st.rerun()


