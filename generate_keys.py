import streamlit_authenticator as stauth

import yaml

names = ["오구의모험","로그인테스트"]
usernames = ["오구", "로그인"]
# passwords = ["1234","5678"] # yaml 파일 생성하고 비밀번호 지우기!

hashed_passwords = stauth.Hasher(passwords).generate() # 비밀번호 해싱

data = {
    "credentials" : {
        "usernames":{
            usernames[0]:{
                "name":names[0],
                "password":hashed_passwords[0]
                },
            usernames[1]:{
                "name":names[1],
                "password":hashed_passwords[1]
                }            
            }
    },
    "cookie": {
        "expiry_days" : 0, # 만료일, 재인증 기능 필요없으면 0으로 세팅
        "key": "some_signature_key",
        "name" : "some_cookie_name"
    },
    "preauthorized" : {
        "emails" : [
            "melsby@gmail.com"
        ]
    }
}

with open('config.yaml','w') as file:
    yaml.dump(data, file, default_flow_style=False)