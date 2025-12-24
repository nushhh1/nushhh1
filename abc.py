import streamlit as st

# 页面配置
st.set_page_config(page_title="简易音乐播放器", layout="centered")

# 初始化会话状态
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 音乐数据（补充专辑封面、歌手、时长信息）
music_arr = [
    {
        'url': 'https://music.163.com/song/media/outer/url?id=437802725.mp3',
        'title': '四季',
        'singer': '张国荣',
        'duration': '4:12',
        'cover': 'https://p2.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg'  # 专辑封面
    },
    {
        'url': 'https://music.163.com/song/media/outer/url?id=1303464858.mp3',
        'title': '于是',
        'singer': '郑润泽',
        'duration': '3:52',
        'cover': 'https://p1.music.126.net/PEGvmO3OqgGOkx4m9qxAJA==/109951163478499713.jpg?param=130y130'
    },
    {
        'url': 'https://music.163.com/song/media/outer/url?id=1360512113.mp3',
        'title': '记得',
        'singer': '张惠妹',
        'duration': '4:46',
        'cover': 'https://p1.music.126.net/Qq_aPcN5Ny64uHaQzq2nnQ==/109951172084712681.jpg?param=130y130'
    }
]

# 切换歌曲函数
def prev_song():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(music_arr)

def next_song():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(music_arr)

# 主标题与说明
st.title("🎶简易音乐播放器")
st.markdown("使用Streamlit制作的简单音乐播放器，支持切歌和基本播放控制")

# 当前歌曲信息展示（封面+详情）
current = music_arr[st.session_state['ind']]
col_cover, col_info = st.columns([1, 2])
with col_cover:
    st.image(current['cover'], caption="专辑封面", width=150)
with col_info:
    st.subheader(current['title'])
    st.write(f"歌手: {current['singer']}")
    st.write(f"时长: {current['duration']}")

# 切歌按钮
col_prev, col_next = st.columns(2)
with col_prev:
    st.button("◀️ 上一首", use_container_width=True, on_click=prev_song)
with col_next:
    st.button("▶️ 下一首", use_container_width=True, on_click=next_song)

# 音频播放组件
st.audio(current['url'], format="audio/mp3")

# 使用说明与任务
with st.expander("使用说明", expanded=True):
    st.subheader("音乐播放器功能说明:")
    st.write("1. 播放/暂停: 点击音频组件的播放/暂停按钮控制音乐播放")
    st.write("2. 切换功能: 使用左右箭头按钮切换上一首/下一首")
    st.write("3. 歌曲列表: 可通过切换按钮选择任意歌曲播放")
    
    st.subheader("课堂练习任务:")
    st.write("1. 实现基本的播放控制功能")
    st.write("2. 添加专辑封面显示")
    st.write("3. 实现切歌功能（上一首/下一首）")
    st.write("4. 显示歌曲基本信息（标题、歌手、时长）")
    
    st.subheader("扩展练习（可选）:")
    st.write("• 添加随机播放功能")
    st.write("• 实现音量控制")
    st.write("• 添加播放进度显示")

st.caption("Streamlit音乐播放器 | 课堂练习示例 | 使用python和Streamlit构建")
