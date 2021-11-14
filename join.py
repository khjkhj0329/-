class Join:
    def __init__(self, id):
        # 아이디
        self.id = id
        # 비밀번호
        self.password = ''
        # 이메일
        self.email = ''



    def set_password(self):
        password = input('>> PASSWORD : ')
        self.species = '필수 항목입니다.' if password == '' else password
    def set_email(self):
        email = input('>> E-mail : ')
        self.email = '필수 항목입니다.' if email == '' else email

    def set_joininfo(self):
        self.set_password()
        self.set_email()

    def __str__(self):
        return f'ID: {self.id}\nPASSWORD: {self.password}\nE-mail: {self.email}'



