import streamlit as st
import yaml
import streamlit_authenticator as stauth
import streamlit as st
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import CharacterTextSplitter



with open('config.yaml') as file:
    config = yaml.load(file, Loader=stauth.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)





# 로그인 창
name, authentication_status, username = authenticator.login("main")

# authentication_status : 인증 상태 (실패=>False, 값없음=>None, 성공=>True)
if authentication_status == False:
    st.error("Username/password is incorrect")

# if authentication_status == None:
#     st.warning("Please enter your username and password")

if authentication_status:
    authenticator.logout("Logout","sidebar")
    st.sidebar.title(f"Welcome {name}님")

        ## 로그인 이후

    st.title('💬 KB Chatbot')
    st.caption("더 나은 금융생활을 위한 맞춤형 서비스를 지원해드립니다.")
    st.header('')
        # st.write('이 앱의 `.streamlit/config.toml` 파일 내용')

        # 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
    tab1, tab2= st.tabs(['카드 추천' , '가계부'])

    with tab1:
        #tab A 를 누르면 표시될 내용
        st.write('TAB1')
        st.header('1. st.button test')
        
        if st.button('Say hello'):
            st.write('Why hello there')
        else:
            st.write('Goodbye')  

    with tab2:
        #tab B를 누르면 표시될 내용 
            st.write('TAB2')
            st.header('2. st.slider test')
            st.write('아 이걸로 연회비해도 좋겠다')
            st.subheader('연회비')

            year = st.slider('연회비 선택', 0, 100000, 20000)
            st.write("연회비 ", year, '원 선택')


    number = st.sidebar.slider('KB', 0, 10, 5)