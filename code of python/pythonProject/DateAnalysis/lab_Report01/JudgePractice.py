# 正确的用户名和密码
USERNAME = "admin"
PASSWORD = "password123"

def authenticate(input_username, input_password):
    if input_username == USERNAME and input_password == PASSWORD:
        return "登录成功！"
    else:
        return "用户名或密码错误。"
