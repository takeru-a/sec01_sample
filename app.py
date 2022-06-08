import streamlit as st
from PIL import Image 

def increment():
    if 'count' not in st.session_state:
        st.session_state.count = 0
    st.session_state.count += 1

def next():
    if 'quizCount' not in st.session_state:
        st.session_state.quizCount = 0
    st.session_state.quizCount += 1

def first():
    st.info('1Q 問題はドコにあるでしょうか？')
    correct = "正解"
    incorrect1 = "不正解"
    incorrect2 = "不正解"
    incorrect3 = "不正解"
    option = st.selectbox("",(incorrect1,correct, incorrect2,incorrect3))

    if st.button("送信"):
        if option == correct:
            st.button("next")
            st.success('正解！')
            st.balloons()
            increment()
            next()
        
        else:
            st.button("next")
            st.error('不正解')
            st.snow()
            next()
     
def second():
    st.info('2Q 以下の画像のメッセージが来ました\nどう対応しますか？')
    img = Image.open("./img/gg_warning.jpg")
    correct = "無視する"
    incorrect1 = "メッセージの指示に従う"
    incorrect2 = "不正解"
    incorrect3 = "不正解"
    option = st.selectbox("",(correct, incorrect1,incorrect2,incorrect3))
    st.image(img,caption="")
    if st.button("送信"):
        if option==correct:
            st.button("next")
            st.success('正解！')
            st.balloons() 
            increment()
            next()
        else:
            st.button("next")
            st.error('不正解')
            st.snow()
            next()

def third():

    st.info("""3Q よく使う図書館の蔵書検索システムが使いづらく不満であったため、1秒に1アクセス程度のリクエストを送るようなクローラを自作し、
    蔵書検索システムから図書の情報をスクレイピングした""")
    st.text("この行動に問題はあるかまたある場合はどのようなことが問題か")
    correct = "問題ない"
    incorrect1 = "スクレイピングしている点"
    incorrect2 = "不正解"
    incorrect3 = "不正解"
    option = st.selectbox("",(correct, incorrect1,incorrect2,incorrect3))

    if st.button("送信"):
        if option == correct:
            st.button("next")
            st.success('正解！')
            st.balloons()
            increment()
            next()
        
        else:
            st.button("next")
            st.error('不正解')
            st.snow()
            next()   

def forth():
    st.info('4Q 問題はドコにあるでしょうか？')
    correct = "正解"
    incorrect1 = "不正解"
    incorrect2 = "不正解"
    incorrect3 = "不正解"
    option = st.selectbox("",(incorrect1,incorrect2,incorrect3,correct))

    if st.button("送信"):
        if option == correct:
            st.button("next")
            st.success('正解！')
            st.balloons()
            increment()
            next()
        
        else:
            st.button("next")
            st.error('不正解')
            st.snow()
            next()

def fifth():
    st.info('5Q 問題はドコにあるでしょうか？')
    correct = "正解"
    incorrect1 = "不正解"
    incorrect2 = "不正解"
    incorrect3 = "不正解"
    option = st.selectbox("",(incorrect1,incorrect2,correct,incorrect3))

    if st.button("送信"):
        if option == correct:
            st.button("next")
            st.success('正解！')
            st.balloons()
            increment()
            next()
        
        else:
            st.button("next")
            st.error('不正解')
            st.snow()
            next()

def finish():
    st.write("これで終了です！お疲れさまでした")


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
    elif st.session_state.quizCount == 2:
        third()
    elif st.session_state.quizCount == 3:
        forth()
    elif st.session_state.quizCount == 4:
        fifth()
    else:
        finish()
        if st.button("もう一度"):
            st.session_state.count=0
            st.session_state.quizCount = 0
    
    # st.write(f"{st.session_state.quizCount+1}問目")    
    st.write(f"正解数：{st.session_state.count}")

if __name__ == '__main__':
    main()