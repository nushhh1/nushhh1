import streamlit as st
import pandas as pd
import numpy as np
import random

# 设置页面配置
st.set_page_config(
    page_title="南宁美食地图",
    page_icon="🍜",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------- 数据准备 ----------------------
# 1. 店铺基础信息
stores_data = {
    "店铺名称": ["肯德基", "瑶长府", "查理王子", "DEMO蛋糕", "皇氏新鲜屋"],
    "美食类型": ["快餐", "桂北菜", "茶饮", "甜品", "乳制品/烘焙"],
    "评分": [4.0, 4.5, 4.2, 4.3, 4.4],
    "人均消费(元)": [35, 89, 18, 45, 22],
    "纬度": [22.827478, 22.827112, 22.828724, 22.827572, 22.827567],
    "经度": [108.396606, 108.395839, 108.399637, 108.400045, 108.402658]
}
df_stores = pd.DataFrame(stores_data)

# 2. 12个月价格走势（5家店）
months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
price_trend_data = {
    "月份": months,
    "快餐": [32 + i*0.5 for i in range(12)],
    "桂北菜": [85 + i*0.8 for i in range(12)],
    "茶饮": [16 + i*0.3 for i in range(12)],
    "甜品": [42 + i*0.6 for i in range(12)],
    "乳制品/烘焙": [20 + i*0.4 for i in range(12)]
}
df_price = pd.DataFrame(price_trend_data)

# 3. 用餐高峰时段数据
peak_hours = ["10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]
peak_data = {
    "时段": peak_hours,
    "客流量": [80, 100, 60, 70, 95, 85]
}
df_peak = pd.DataFrame(peak_data)

# ---------------------- 界面设计 ----------------------
st.markdown("### 探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。")
st.markdown("---")

# 1. 南宁美食地图
st.markdown("#### 📍 南宁美食地图")
st.map(
    df_stores[["纬度", "经度"]].rename(columns={"纬度": "lat", "经度": "lon"}),
    zoom=14,
    use_container_width=True
)
st.markdown("---")

# 2. 餐厅评分
st.markdown("#### ⭐ 餐厅评分")
st.bar_chart(
    df_stores.set_index("店铺名称")["评分"],
    use_container_width=True,
    color="#1E88E5"
)
st.markdown("---")

# 3. 不同类型餐厅价格（修复color参数问题）
st.markdown("#### 💰 不同类型餐厅价格")
# 这里不指定color，或传入和列数一致的颜色列表
st.line_chart(
    df_price.set_index("月份"),
    use_container_width=True,
    # 可选：传入5个颜色（对应5列）
    # color=["#1E88E5", "#FFA000", "#4CAF50", "#9C27B0", "#F44336"]
)
st.markdown("---")

# 4. 用餐高峰时段
st.markdown("#### ⏰ 用餐高峰时段")
st.area_chart(
    df_peak.set_index("时段"),
    use_container_width=True,
    color="#FFA000"
)

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>© 2025 南宁美食地图 | 数据为模拟数据</div>",
    unsafe_allow_html=True
)
