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
    st.info("""1Q 明らかに詐欺だと思われるおかしい件名のメールが届いたが、
    おもしろそうなので、友達に共有したくて転送した。この際の問題点はあるか、
    ある場合はどのようなことが起こりうるか選択せよ。""")
    correct = "友達がさぎだと気付かずにリンクをクリックしてしまう恐れがある"
    incorrect1 = "友達も詐欺だと気付いてくれるので何も問題はない"
    incorrect2 = "詐欺師に自分のメールアドレスが使用されていることがバレてしまう"
    incorrect3 = "自宅がバレる"
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
    st.info("""2Q 以下の画像のメッセージが来ました。メッセージに従った場合
    どのようなことが起こるでしょうか？""")
    img = Image.open("./img/gg_warning.jpg")
    correct1 = "逆にウイルスに感染する"
    correct2 = "クレジットカード・ネットバンキングで不正利用される"
    incorrect = "ウイルスを取り除ける"
    correct3 = "個人情報が流出してしまう"
    st.image(img,caption="")
    option = st.multiselect(
     '全て選べ',
     [incorrect,correct1,correct2,correct3],
     [])
    if st.button("送信"):
        if correct1 in option and correct2 in option and correct3 in option and incorrect not in option:
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

    st.info("""3Q 観光地での写真を撮ってすぐSNSに投稿した。
    この時起こりうる問題は何か。複数ある場合はすべて選べ。""")
    
    incorrect = "特に問題ない"
    correct1 = "居場所が露呈し、個人を特定される"
    correct2 = "旅行中であることがバレ、空き巣被害に遭う可能性が高まる"
    correct3 = "写真に他者が写り込んでプライバシーを侵害してしまう"
    option = st.multiselect(
     '全て選べ',
     [incorrect,correct1,correct2,correct3],
     [])
    if st.button("送信"):
        if correct1 in option and correct2 in option and correct3 in option and incorrect not in option:
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
    st.info("""4Q PlayStation5が1万円でネット上で売られていたのでクレジットカードで購入した。
    この時起こり得ることは何か全て答えよ。""")
    correct1 = "何も届かずクレジット情報とお金を取られる"
    incorrect = "PS5が1万円で手に入る"
    correct2 = "箱だけ届く"
    correct3 = "故障しているPS5が届く"
    option = st.multiselect(
     '全て選べ',
     [incorrect,correct1,correct2,correct3],
     [])
    
    if st.button("送信"):
        if correct1 in option and correct2 in option and correct3 in option and incorrect not in option:
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
    st.info("""5Q 会員登録でパスワードを設定する必要があるが、覚えられないので
    他のサイトでも使用しているものを使い回した。この際の問題点はあるか、ある場合はどのような
    ことが起こりうるか選択せよ。""")
    correct = "自身が使用している他のサイトでもログインされ、悪用される恐れがある"
    incorrect1 = "パスワードが自分以外に知られることはないので問題ない"
    incorrect2 = "パスワードを管理する手間が省けるのでむしろ良い"
    incorrect3 = "使い回すことは悪いので単純なパスワードを設定する"
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