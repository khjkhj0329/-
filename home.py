import tkinter

import main_in


class Login:
    def __init__(self, start):
        self.start = start

        self.img = tkinter.PhotoImage(file='image/title.png')
        self.img_title = tkinter.Label(image=self.img, bg="#708467")
        self.img_title.place(x=450, y=130)

        self.title1 = tkinter.Label(self.start, text="나혼자", bg="#708467")
        self.title1.configure(font=('Corbel', 23))
        self.title1.place(x=450, y=233)
        self.title2 = tkinter.Label(self.start, text="분리수거", bg="#708467")
        self.title2.configure(font=('Corbel', 23))
        self.title2.place(x=434, y=270)

        self.id_txt = tkinter.Entry(self.start, width=18, font=("궁서체", 20))
        self.id_txt.place(x=370, y=345, height=40)
        self.pwd_txt = tkinter.Entry(self.start, width=18, font=("궁서체", 20))
        self.pwd_txt.place(x=370, y=415, height=40)

        self.login_btn = tkinter.Button(self.start, bg="#F9F3D5", text="Login", command=self.move, pady=10, padx=90)
        self.login_btn.configure(font=("Courier", 15, "italic", "bold"))
        self.login_btn.place(x=372, y=490)

    def move(self):
        moveBtn_main = main_in.Main_in(self.start)

    def play(self):
        self.start.mainloop()


if __name__ == '__main__':
    start = tkinter.Tk()
    start.title("나혼자 분리수거")
    start.geometry("1000x700+250+35")  # 창 크기와 창이 뜨는 위치
    start.resizable(False, False)  # 창 크기 고정
    start.configure(bg='#708467')

    kang = Login(start)
    kang.play()
