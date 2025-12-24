import streamlit as st


st.set_page_config(page_title='视频网站')
    


video_arr=[
    {
        'url':'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
        'title':'大白兔第一集'
        },{
        'url':'https://www.w3schools.com/html/movie.mp4',
        'title':'大白兔第二集'
        },{
        'url':'https://media.w3.org/2010/05/sintel/trailer.mp4',
        'title':'大白兔第三集'
        },{
        'url':'https://media.w3.org/2010/05/sintel/trailer.mp4',
        'title':'大白兔第四集'
        }

    ]

if 'ind' not in st.session_state:
    st.session_state['ind']=0

st.title(video_arr[st.session_state['ind']]['title'])

st.video(video_arr[st.session_state['ind']]['url'])

def playVideo(e):
    st.session_state['ind']=int(e)

cols=st.columns(len(video_arr))
for i in range(len(video_arr)):
    with cols[i]:
        st.button('第'+str(i+1)+'集',on_click=playVideo,args=([i]),use_container_width=True)
    


