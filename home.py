import msvcrt
from idlelib import window
from tkinter import *
# class Join:
#     def __init__(self, id):
#         # 아이디
#         self.id = id
#         # 비밀번호
#         self.password = ''
#         # 이메일
#         self.email = ''
#
#     def set_password(self):
#         password = input('>> PASSWORD : ')
#         self.species = '필수 항목입니다.' if password == '' else password
#
#     def set_email(self):
#         email = input('>> E-mail : ')
#         self.email = '필수 항목입니다.' if email == '' else email
#
#     def set_joininfo(self):
#         self.set_password()
#         self.set_email()
#
#     def __str__(self):
#         return f'ID: {self.id}\nPASSWORD: {self.password}\nE-mail: {self.email}'
# class Login:
#     def __init__(self):
#         self.main_chang()
#     def main_chang(self):
class All():
    def __init__(self):
        self.start()

    def start(self):
        self.start = Tk()
        self.start.title("나혼자 분리수거")
        self.start.geometry("1000x700+250+35")   # 창 크기와 창이 뜨는 위치
        self.start.resizable(False, False)   #창 크기 고정
        self.start.configure(bg='#708467')
    #
    #     img = PhotoImage(file='title.png')
    #     img_title = Label(image=img, bg="#708467")
    #     img_title.image = img
    #     img_title.place(x=450, y=130)
    #
    #     title1 = Label(self.start, text="나혼자", bg="#708467")
    #     title1.configure(font=('Corbel', 23))
    #     title1.pack()
    #     title1.place(x=450, y=233)
    #     title2 = Label(self.start, text="분리수거", bg="#708467")
    #     title2.configure(font=('Corbel', 23))
    #     title2.pack()
    #     title2.place(x=434, y=270)
    #
    #     id_txt = Entry(self.start, width=18, font=("궁서체", 20))
    #     id_txt.pack()
    #     id_txt.place(x=370, y=345, height=40)
    #     pwd_txt = Entry(self.start, width=18, font=("궁서체", 20))
    #     pwd_txt.pack()
    #     pwd_txt.place(x=370, y=415, height=40)
    #
    #
    #     login_btn = Button(self.start, bg="#F9F3D5", text="Login", pady=10, padx=90)
    #     login_btn.pack()
    #     login_btn.configure(font=("Courier", 15, "italic", "bold"))
    #     login_btn.place(x=372, y=490)
    #     self.start.mainloop()


    def menu(self):
        self.menu_in = Tk()
        self.menu_in.title("나혼자 분리수거")
        self.menu_in.geometry("1000x700+250+35")   # 창 크기와 창이 뜨는 위치
        self.menu_in.resizable(False, False)   #창 크기 고정
        self.menu_in.configure(bg='#708467')
        self.menu_in.mainloop()

        img1 = PhotoImage(file='trash1.png')
        trash1 = Label(image=img1)
        trash1.image = img1
        trash1.place(x=450, y=130)




# lab1 = Label(Tk, text="ID")
# lab1.grid(row=0, column=0)
# txt = Entry(Tk)
# txt.grid(row=0, column=1)
# btn = Button(Tk, text="Login", width=200)
# btn.grid(row=1, column=1)


if __name__ == '__main__':
    all = All()























