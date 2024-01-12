# 회원
# 번호, 아이디, 비밀번호, 이름


# private: 자신의 클래스에서만 접근 가능
# 1. 외부에서 접근하지 말자!
# 2. 외부에서 접근할 떄 꼭 메소드로 접근하자!
# __user_number = 0
class User:
    user_number = 0
    def __init__(self, user_name, user_id, user_pw):
        User.user_number += 1
        self.user_number = User.user_number
        self.user_name = user_name
        self.user_id = user_id
        self.user_pw = user_pw

# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다(class method).
    @classmethod
    def set_admin(cls, **kwargs):
        kwargs['admin'] = 'admin_' + kwargs['user_id']
        return cls(**kwargs)

lee = User('기영', 'rldud', 'rldud1')
kwon = User('가은', 'admin_rkdms', 'rkdms1')
print(lee.user_name, lee.user_id, lee.user_pw, lee.user_number)
print(kwon.user_name, kwon.user_id, kwon.user_pw, kwon.user_number)