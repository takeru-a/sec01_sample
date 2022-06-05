import streamlit as st
from PIL import Image 

def increment():
    if 'quizCount' not in st.session_state:
        st.session_state.quizCount = 0
    st.session_state.count += 1

def next():
    if 'quizCount' not in st.session_state:
        st.session_state.quizCount = 0
    st.session_state.quizCount += 1

def first():
    st.text('1Q パスワードを使い回してよい')
    correct = "良くない"
    incorrect = "良い"
    option = st.selectbox("",(correct, incorrect))

    if st.button("送信"):
        if option == correct:
            st.button("next")
            st.success('正解！')
            st.balloons()
            increment()
            next()
        
        elif option == incorrect:
            st.button("next")
            st.error('不正解')
            st.snow()
            next()
     
def second():
    st.text('2Q 以下の画像のメッセージが来ました\nどう対応しますか？')
    img = Image.open("./img/gg_warning.jpg")
    correct = "無視する"
    incorrect = "メッセージの指示に従う"
    st.image(img,caption="")
    if st.button(correct):
        st.button("next")
        st.success('正解！')
        st.balloons() 
        increment()
        next()
        

    elif st.button(incorrect):
        st.error('不正解')
        st.snow()
    
def main():
    st.title('情報リテラシークイズ！')
    if 'count' not in st.session_state:
        st.session_state.count = 0
        
    if 'quizCount' not in st.session_state:
        st.session_state.quizCount = 0
    
    if st.session_state.quizCount == 0:
        first()
        
    elif st.session_state.quizCount == 1:
        second()
    
    st.write(f"{st.session_state.quizCount+1}問目")    
    st.write(f"正解数：{st.session_state.count}")

if __name__ == '__main__':
    main()