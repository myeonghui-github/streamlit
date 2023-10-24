# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd

# header, subheader, text, caption 연습하기
st.title('Text elements')
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')
st.header('Header : 데이터 분석 표현')
st.subheader('Subheader : 스트림릿')
st.text('Text : this is the Streamlit')
st.caption('Caption : Streamlit 은 2019년 하반기에 등정한 파이썬 웹 어플리케이션 툴입니다.')

# markdown 연습하기
st.markdown('# Markdown #')
st.markdown('## Markdown ##')
st.markdown('### Markdown ###')
st.markdown('this is markdown')
st.markdown('this is **markdown**')
st.markdown('this is **_markdown_**')
st.markdown('this is _markdown_')
st.markdown('this is *markdown*')

st.markdown('- items \n'
            '  - item \n'
            '  - item \n'
            '    - other \n'
            ' - item')
st.markdown(" 1. item 1\n"
            "    1. item 1\n"
            "    1. item 1\n"
            "       1. item1\n"
            " 1. item 2")

# Latex & Code 연습하기
st.markdown('## Code & Latex ##')

st.code('x=1234')
st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1}ar^k = a \left(\frac{1-r^{n}}{1-r}\right) ''')

# write 연습하기
st.title('write')
st.caption('참고사이트: https://docs.streamlit.io/library/api-reference/write-magic/st.write')
st.text('아래 딕셔너리를 판다스 데이터프레임으로 변경')
st.caption("{'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']}")
df = pd.DataFrame({'이름': ['홍길동', '김사랑', '일지매', '이루리'],'등급': ['1', '3', '2', '2']})
st.write('딕셔너리를 판다스의 데이터프레임으로 바꿔서 :', df, '스트림릿의 write 함수로 표현')


# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\1.text.py