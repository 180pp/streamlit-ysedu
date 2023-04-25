# -*- coding:UTF-8 -*-
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from utils import p_lans
from PIL import Image

import plotly.express as px
import seaborn as sns

def main():
    # title
    st.title("Hello World")

    # text
    st.text('This is so {}'.format("good"))

    # Header
    st.header("This is Header")

    # Subheader
    st.subheader('This is subHeader')

    # Markdown
    st.markdown('## This is Markdown')

    # 색상이 들어간 텍스트 feature
    st.success('성공')
    st.warning('경고')
    st.info('정보와 관련된 탭')
    st.error('에러 메시지')
    st.exception('예외처리')

    # st.write()
    st.write('일반텍스트')
    st.write(1 + 2)
    st.write(dir(str))

    st.title(':sunglasses:')

    # Help
    st.help(range)
    st.help(st.title)

    # 데이터 불러오기
    iris = pd.read_csv('data/iris.csv')

    st.title("IRIS 테이블")
    st.dataframe(iris, 500, 100)  # Height, Width

    st.title('table()')
    st.table(iris)

    st.title('write()')
    st.write(iris)

    myCode = """
    def hello():
        print("hi")
    """
    st.code(myCode, language="Python")

    # 위젯, button 기능활용
    name = 'Evan'
    if st.button('Submit'):
        st.write(f'name: {name.upper()}')

    # RadioButton
    s_state = st.radio('Status', ('활성화', '비활성화'))
    if s_state == '활성화':
        st.success('활성화 상태')
    else:
        st.error('비활성화 상태')

    # Check Box
    if st.checkbox('show/hide'):
        st.text('무언가를 보여줘!!')

    # Select Box
    choice = st.selectbox('프로그래밍 언어', p_lans)
    st.write(f'{choice} 언어를 선택함')

    # multiple selection
    lans = ("영어", "일본어", "중국어", "독일어")
    myChoice = st.multiselect("언어 선택", lans, default="중국어")
    st.write("선택", myChoice)

    # Slider
    age = st.slider('나이', 1, 120)
    st.write(age)

    #이미지 가져오기
    img = Image.open('data/image_01.jpg')
    st.image(img)

    url='data:image/jpeg;base64,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'
    st.image(url)

    #비디오 출력
    with open('data/secret_of_success.mp4','rb') as rb:
        video_file = rb.read()
        st.video(video_file, start_time=1)

    #오디오 출력
    with open('data/song.mp3' ,'rb') as rb:
        audio_file =rb.read()
        st.audio(audio_file , format="audion/mp3")

    fig = px.scatter(data_frame=iris,
                     x='sepal_length',
                     y='sepal_width')
    st.plotly_chart(fig)

    choice = st.selectbox('프로그래밍 언어', iris['species'].unique())
    # st.title(choice)

    result = iris[iris['species'] == choice].reset_index(drop=True)
    # st.dataframe(result)

    col1, col2 = st.columns([0.5, 0.5], gap='large')
    with col1:
        fig2, ax = plt.subplots()
        # ax.scatter(x=iris['petal_length'], y=iris['sepal_width'])
        sns.scatterplot(result, x='petal_length',
                        y='sepal_width')
        st.pyplot(fig2)

    with col2:
        fig3, ax = plt.subplots()
        ax.scatter(x=result['sepal_length'], y=result['sepal_width'])
        st.pyplot(fig3)

if __name__ == "__main__":
    main()

