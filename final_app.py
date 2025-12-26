import streamlit as st
import pandas as pd
import plotly.express as px

# 修复缩进+语法错误：函数定义要顶格，且修正所有笔误
def get_dataframe_from_excel():
    # pd.read_excel()函数用于读取Excel文件的数据
    # 'supermarket_sales.xlsx'表示Excel 文件的路径及名称
    # sheet_name='销售数据'表示读取名为"销售数据"的工作表的数据
    # skiprows=1表示跳过 Excel中的第1行，因为第1行是标题
    # index_col='订单号'表示将"订单号"这一列作为返回的数据框的索引
    # 最后将读取到的数据框赋值给变量df
    df = pd.read_excel(
        'supermarket_sales.xlsx',
        sheet_name='销售数据',  # 修复：sheet name -> sheet_name（下划线）
        skiprows=1,  # 修复：l -> 1（数字1）
        index_col='订单号'  # 修复：缺少闭合引号，多余中文逗号
    )
    df['小时数'] = pd.to_datetime(df["时间"], format="%H:%M:%S").dt.hour  # 修复：format后缺少等号
    return df

def add_sidebar_func(df):
    # 创建侧边栏
    with st.sidebar:
        # 添加侧边栏标题
        st.header("请筛选数据:")
        # 求数据框"城市"列去重复后的值，赋值给city_unique
        city_unique = df["城市"].unique()
        city = st.multiselect(
            "请选择城市:",
            options=city_unique,  # 将所有选项设置为city_unique
            default=city_unique,
        )  # 第1次的默认选项为city_unique
        customer_type_unique = df["顾客类型"].unique()
        customer_type = st.multiselect(
            "请选择顾客类型：",
            options=customer_type_unique,
            default=customer_type_unique,  # 修复：default-customer_type_unique -> default=...
        )
        # 求数据框"性别"列去重复后的值，赋值给 gender_unique
        gender_unique = df["性别"].unique()
        gender = st.multiselect(
            "请选择性别",
            options=gender_unique,  # 将所有选项设置为gender_unique
            default=gender_unique,
        )
        df_selection = df.query(
            "城市==@city & 顾客类型==@customer_type & 性别==@gender"  # 修复：@city前缺少==，空格规范
        )
        return df_selection

def product_line_chart(df):
    # 将df按'产品类型'列分组，并计算'总价'列的和，然后按总价排序
    sales_by_product_line = (
        df.groupby(by=["产品类型"])[["总价"]].sum().sort_values(by="总价")
    )
    fig_product_sales = px.bar(
        sales_by_product_line,
        x="总价",
        y=sales_by_product_line.index,
        orientation="h",
        title="<b>按产品类型划分的销售额</b>",
    )
    return fig_product_sales

def hour_chart(df):
    sales_by_hour = (
        df.groupby(by=["小时数"])[["总价"]].sum()  # 修复：(小时数] -> ["小时数"]，多余注释删除
    )
    fig_hour_sales = px.bar(
        sales_by_hour,
        x=sales_by_hour.index,
        y="总价",
        title="<b>按小时数划分的销售额</b>",
    )
    # 将生成的条形图返回
    return fig_hour_sales

def main_page_demo(df):
    """主界面函数"""
    # 设置标题
    st.title(':bar_chart：销售仪表板')
    # 创建关键指标信息区，生成3个列容器
    left_key_col, middle_key_col, right_key_col = st.columns(3)
    total_sales = int(df["总价"].sum())
    average_rating = round(df["评分"].mean(), 1)
    # 对刚刚的结果再次四舍五入，只保留整数，并使用int()函数，表示就要整数，增加代码的可读性
    star_rating_string = ":star:" * int(round(average_rating, 0))
    # 选中的数据框中的"总价"列，使用mean()计算"总价"列的平均值，使用round()四舍五入保留两位小数
    average_sale_by_transaction = round(df["总价"].mean(), 2)

    with left_key_col:
        st.subheader("总销售额：")
        st.subheader(f"RMB ¥{total_sales:,}")  # 修复：(total_sales:,) -> {total_sales:,}
    with middle_key_col:
        st.subheader("顾客评分的平均值：")
        st.subheader(f"{average_rating} {star_rating_string}")  # 修复：(average_rating) -> {average_rating}
    with right_key_col:
        st.subheader("每单的平均销售额：")
        st.subheader(f"RMB ¥{average_sale_by_transaction}")  # 修复：多余括号

    st.divider()  # 生成一个水平分割线
    # 创建图表信息区，生成两个列容器
    left_chart_col, right_chart_col = st.columns(2)
    with left_chart_col:
        # 生成纵向条形图
        hour_fig = hour_chart(df)
        # 展示生成的Plotly图形，并设置使用父容器的宽度
        st.plotly_chart(hour_fig, use_container_width=True)

    with right_chart_col:
        # 生成横向条形图
        product_fig = product_line_chart(df)
        # 展示生成的Plotly图形，并设置使用父容器的宽度
        st.plotly_chart(product_fig, use_container_width=True)

def run_app():
    """启动应用"""
    # 设置页面
    st.set_page_config(
        page_title="销售仪表板",  # 标题
        page_icon=":bar_chart:",  # 图标
        layout="wide"  # 宽布局
    )
    # 将Excel中的销售数据读取到数据框中
    sale_df = get_dataframe_from_excel()
    # 添加不同的多选下拉按钮，并形成筛选后的数据框，构建筛选区
    df_selection = add_sidebar_func(sale_df)
    # 构建主界面
    main_page_demo(df_selection)

if __name__ == "__main__":  # 修复：if__name__ -> if __name__（缺少空格）
    run_app()
