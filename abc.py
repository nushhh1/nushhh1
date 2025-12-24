import streamlit as st
st.title("🎶简易音乐播放器")
st.text("使用Streamlit制作的简易音乐播放器，支持切歌和基本播放控制")
music_arr = [
    {
        'url': 'https://music.163.com/song/media/outer/url?id=437802725.mp3',
        'text': '四季'
    },
    {
        'url': 'https://music.163.com/song/media/outer/url?id=287744.mp3',
        'text': '富士山下'
    },
    
]

# 将当前的索引存到内存中，如果内存中没有ind，我才要0，如果有就不设置ind
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0
st.title(music_arr[st.session_state['ind']]['text'])
st.audio(music_arr[st.session_state['ind']]['url'])

# 技术2：分列容器
c1, c2 = st.columns(2)

def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(music_arr)

with c1:
    # 技术12：按钮
    st.button("上一首", use_container_width=True)
with c2:
    st.button("下一首", use_container_width=True, on_click=nextImg)
