import streamlit as st

st.set_page_config(page_title='个人简历生成器',layout='wide')

st.title("个人简历生成器")
st.text('使用Seamline创建您的个性化简历')

c1,c2=st.columns([1,2])
def my_format_func(option):
    return option

with c1:
    st.markdown('<h2 style="border-bottom: 1px solid #ccc; padding-bottom: 5px;">个人信息表单</h2>', unsafe_allow_html=True)
    user_name=st.text_input('姓名')
    user_position=st.text_input('职位')
    user_phone=st.text_input('手机号')
    user_email=st.text_input('邮箱')
    user_birth=st.date_input('出生年月',value=None)
    user_gender=st.radio('选择性别',['男','女'],)
    user_enucational=st.selectbox(
        f'选择学历',
        ['小学','初中','高中','专科','本科','博士'],
        )
    user_language=st.selectbox(
        f'选择语言能力',
        ['中文','英语','俄语','西班牙语','印地语','日语'],
        )

    user_skill = st.multiselect(
    '选择你的技能（多选）',
    ['python', 'c语言', 'ps', 'word', 'ppt', 'excel'],
    format_func=my_format_func,
    )
    
    user_experience = st.slider('工作经验（年）', 0, 30, 0)
    
    user_salary = st.slider('期望薪资范围（万）', 0, 100, (10, 20))
    
    user_intro = st.text_area('个人简介', placeholder='请简要介绍您的专业背景、职业目标和个人特点...')
    
    user_contact_time = st.selectbox('每日最佳联系时间', ['8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00'])
    
    st.subheader('上传个人照片')
    user_photo = st.file_uploader('Drag and drop file here', type=['jpg', 'jpeg', 'png'])

with c2:
    st.markdown('<h2 style="border-bottom: 1px solid #ccc; padding-bottom: 5px;">简历实时预览</h2>', unsafe_allow_html=True)
    
    # 显示上传的照片
    if user_photo is not None:
        st.image(user_photo, width=150)
    
    # 使用两列布局显示基本信息
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.write(f'姓名: {user_name}')
        st.write(f'职位: {user_position}')
        st.write(f'手机: {user_phone}')
        st.write(f'邮箱: {user_email}')
        st.write(f'出生日期: {user_birth}')
    
    with col_right:
        st.write(f'性别: {user_gender}')
        st.write(f'学历: {user_enucational}')
        st.write(f'工作经验: {user_experience}年')
        st.write(f'期望薪资: {user_salary[0]} - {user_salary[1]}万')
        st.write(f'最佳联系时间: {user_contact_time}')
        st.write(f'语言能力: {user_language}')
    
    st.markdown('<h3 style="border-top: 1px solid #ccc; padding-top: 5px;">个人简介</h3>', unsafe_allow_html=True)
    if user_intro:
        st.write(user_intro)
    else:
        st.text('这个人很神秘，没有留下任何介绍...')
    
    st.markdown('<h3 style="border-bottom: 1px solid #ccc; padding-bottom: 5px;">专业技能</h3>', unsafe_allow_html=True)
    st.text(f'*只显示前5项技能，请控制数量*')
    st.write('技能:', ', '.join(user_skill[:5]) if user_skill else '暂无')
