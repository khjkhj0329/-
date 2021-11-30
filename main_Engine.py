import tkinter as tk
from tkinter import LEFT, N, RIGHT, Y


class Rice():
    def __init__(self):
        self.start()

    # 시작 화면
    def start(self):
        self.start = tk.Tk()
        self.start.title("나혼자 분리수거")
        self.start.geometry("1000x700+250+35")
        self.start.resizable(False, False)
        self.start.config(bg="#708467")

        title_img = tk.PhotoImage(file="image/title_img.png")
        title_img1 = tk.Label(self.start, image=title_img, bg="#708467")
        title_img1.place(x=435, y=180)

        startBtn = tk.Button(self.start, width=256, height=70, borderwidth=0, bg="#708467", command=self.login_in)
        startBtn.place(x=375, y=450)
        btnStart1 = tk.PhotoImage(file="image/start_btn.png")
        startBtn.config(image=btnStart1)

        make_in = tk.Label(self.start, text="made.빛이 나는 솔로", bg="#708467")
        make_in.configure(font=('Corbel', 15))
        make_in.place(x=795, y=650)

        self.start.mainloop()

    def save_name(self, text):
        name_f = open("name.txt", "a")
        name_f.write(text+"\n")

    def login_in(self):
        self.login = tk.Toplevel()
        self.login.title("나혼자 분리수거")
        self.login.geometry("700x500+250+35")
        self.login.resizable(False, False)
        self.login.config(bg="#708467")

        title_img = tk.PhotoImage(file="image/title_img.png")
        title_img1 = tk.Label(self.login, image=title_img, bg="#708467")
        title_img1.place(x=275, y=30)

        str = tk.StringVar()
        name_txt = tk.Entry(self.login, width=16, font=("Courier", 20), textvariable=str)
        name_txt.place(x=210, y=300, height=50)

        loginBtn = tk.Button(self.login, width=256, height=70, borderwidth=0, bg="#708467", command=lambda:self.save_name(str.get()))
        loginBtn.place(x=212, y=370)
        btnLogin = tk.PhotoImage(file="image/login_btn.png")
        loginBtn.config(image=btnLogin)

        really_Btn = tk.Button(self.login, text="시작하기", width=20, height=2, borderwidth=0, bg="#F9F3D5" ,fg="black", command=self.move)
        really_Btn.configure(font=('Corbel', 10))
        really_Btn.place(x=530, y=20)

        self.login.mainloop()

    # 마이페이지
    def mypage_in(self):
        self.mypage_in = tk.Toplevel()
        self.mypage_in.geometry("300x300")
        self.mypage_in.config(bg="#708467")
        mypage_f = open("name.txt", "r")
        mypage_text = mypage_f.read()
        mypage_label = tk.Label(self.mypage_in, text=mypage_text)
        mypage_label.pack()

    # 메인 창
    def move(self):
        self.move = tk.Toplevel()
        self.move.title("나혼자 분리수거")
        self.move.geometry("1000x700+200+40")
        self.move.resizable(False, False)
        self.move.config(bg="#708467")

        title_bar = tk.PhotoImage(file="image/title_bar.png")
        bar_title = tk.Label(self.move, image=title_bar, bg="#708467")
        bar_title.place(x=360, y=30)

        # 검색
        searchBtn = tk.Button(self.move, width=150, height=180, borderwidth=0, bg="#708467", command=self.search_in)
        searchBtn.place(x=170, y=280)
        btnImage = tk.PhotoImage(file="image/btn_search.png")
        searchBtn.config(image=btnImage)

        #일반 쓰레기
        trashBtn = tk.Button(self.move, width=150, height=180, borderwidth=0, bg="#708467", command=self.trash_in)
        trashBtn.place(x=425, y=280)
        btnImage1 = tk.PhotoImage(file="image/general_trash.png")
        trashBtn.config(image=btnImage1)

        # 재활용
        trashBtn_2 = tk.Button(self.move, width=150, height=180, borderwidth=0, bg="#708467", command=self.recycling_menu)
        trashBtn_2.place(x=674, y=280)
        btnImage_2 = tk.PhotoImage(file="image/recycling.png")
        trashBtn_2.config(image=btnImage_2)

        # 기타 등등
        etcBtn = tk.Button(self.move, width=175, height=80, borderwidth=0, bg="#708467", command=self.etc_in)
        etcBtn.place(x=780, y=35)
        btnImage_3 = tk.PhotoImage(file="image/etc.png")
        etcBtn.config(image=btnImage_3)

        # 마이페이지
        mypageBtn = tk.Button(self.move, width=40, height=45, borderwidth=0, bg="#708467",command=self.mypage_in)
        mypageBtn.place(x=910, y=620)
        mypageImage = tk.PhotoImage(file="image/mypage_in.png")
        mypageBtn.config(image=mypageImage)

        self.move.mainloop()


    # 검색창
    def search_in(self):
        self.search_in = tk.Toplevel()
        self.search_in.title("나혼자 분리수거")
        self.search_in.geometry("1000x700")
        self.search_in.resizable(False, False)
        self.search_in.config(bg="#708467")

        title_bar1 = tk.PhotoImage(file="image/title_bar.png")
        bar_title2 = tk.Label(self.search_in, image=title_bar1, bg="#708467")
        bar_title2.place(x=360, y=30)

        #검색 창
        entry_search = tk.Entry(self.search_in, width=25, font=("Courier", 20))
        entry_search.place(x=297, y=160)

        # 검색 버튼
        trashBtn = tk.Button(self.search_in, width=50, height=50, borderwidth=0, bg="#708467")
        trashBtn.place(x=710, y=152)
        btnImage1 = tk.PhotoImage(file="image/search_btn.png")
        trashBtn.config(image=btnImage1)

        backBtn = tk.Button(self.search_in, width=66, height=59, borderwidth=0, bg="#708467", command=self.move)
        backBtn.place(x=900, y=30)
        backImage = tk.PhotoImage(file="image/mypage_in.png")
        backBtn.config(image=backImage)

        make_in = tk.Label(self.search_in, text="made.빛이 나는 솔로", bg="#708467")
        make_in.configure(font=('Corbel', 15))
        make_in.place(x=795, y=650)

        self.search_in.mainloop()

    # 일반 쓰레기
    def trash_in(self):
        self.trash_in = tk.Toplevel()
        self.trash_in.title("나혼자 분리수거")
        self.trash_in.geometry("1000x700+200+40")
        self.trash_in.resizable(False, False)
        self.trash_in.config(bg="#708467")

        title_bar = tk.PhotoImage(file="image/title_bar.png")
        bar_title = tk.Label(self.trash_in, image=title_bar, bg="#708467")
        bar_title.place(x=360, y=30)

        f = open("trash_menu.txt", "r", encoding="utf-8")
        text = f.read()
        label = tk.Label(self.trash_in, text=text, bg="#708467", height=100, fg="white", justify=LEFT)
        label.configure(font=('Corbel', 13))
        label.pack(pady=180)

        self.trash_in.mainloop()

    # 재활용 세부 메뉴
    def recycling_menu(self):
        self.recycling_menu = tk.Toplevel()
        self.recycling_menu.title("나혼자 분리수거")
        self.recycling_menu.geometry("1000x700")
        self.recycling_menu.resizable(False, False)
        self.recycling_menu.config(bg="#708467")

        title_bar1 = tk.PhotoImage(file="image/title_bar.png")
        bar_title2 = tk.Label(self.recycling_menu, image=title_bar1, bg="#708467")
        bar_title2.place(x=360, y=30)

        # 유리
        GlassBtn = tk.Button(self.recycling_menu, width=150, height=180, borderwidth=0, bg="#708467", command=self.glass_way)
        GlassBtn.place(x=270, y=200)
        btnImage1 = tk.PhotoImage(file="image/trash1.png")
        GlassBtn.config(image=btnImage1)

        # 종이
        PaperBtn = tk.Button(self.recycling_menu, width=150, height=180, borderwidth=0, bg="#708467", command=self.paper_way)
        PaperBtn.place(x=270, y=440)
        btnImage2 = tk.PhotoImage(file="image/trash2.png")
        PaperBtn.config(image=btnImage2)

        # 플라스틱
        PlasticBtn = tk.Button(self.recycling_menu, width=150, height=180, borderwidth=0, bg="#708467", command=self.plastic_way)
        PlasticBtn.place(x=550, y=200)
        btnImage3 = tk.PhotoImage(file="image/trash3.png")
        PlasticBtn.config(image=btnImage3)

        # 캔류
        CanBtn = tk.Button(self.recycling_menu, width=150, height=180, borderwidth=0, bg="#708467", command=self.can_way)
        CanBtn.place(x=550, y=440)
        btnImage4 = tk.PhotoImage(file="image/trash4.png")
        CanBtn.config(image=btnImage4)

        self.recycling_menu.mainloop()

    # 유리 버리는 법
    def glass_way(self):
        self.glass_way = tk.Toplevel()
        self.glass_way.title("나혼자 분리수거")
        self.glass_way.geometry("1000x700")
        self.glass_way.resizable(False, False)
        self.glass_way.config(bg="#708467")

        title_bar1 = tk.PhotoImage(file="image/title_bar.png")
        bar_title2 = tk.Label(self.glass_way, image=title_bar1, bg="#708467")
        bar_title2.place(x=360, y=30)

        title_glass = tk.Label(self.glass_way, text="유리 버리는 방법", bg="#F7F4E3")
        title_glass.configure(font=('Corbel', 15))
        title_glass.place(x=795, y=46)

        f = open("glass_info.txt", "r", encoding="utf-8")
        text=f.read()
        label = tk.Label(self.glass_way, text=text, bg="#708467", height=100, fg="white", justify=LEFT)
        label.configure(font=('Corbel', 13))
        label.pack(pady = 180)

        self.glass_way.mainloop()

    # 종이 버리는 법
    def paper_way(self):
        self.paper_way = tk.Toplevel()
        self.paper_way.title("나혼자 분리수거")
        self.paper_way.geometry("1000x700")
        self.paper_way.resizable(False, False)
        self.paper_way.config(bg="#708467")

        title_bar1 = tk.PhotoImage(file="image/title_bar.png")
        bar_title2 = tk.Label(self.paper_way, image=title_bar1, bg="#708467")
        bar_title2.place(x=360, y=30)

        title_paper = tk.Label(self.paper_way, text="종이 버리는 방법", bg="#F7F4E3")
        title_paper.configure(font=('Corbel', 15))
        title_paper.place(x=795, y=46)


        f = open("paper_info.txt", "r", encoding="utf-8")
        text = f.read()
        label = tk.Label(self.paper_way, text=text, bg="#708467", height=100, fg="white", justify=LEFT)
        label.configure(font=('Corbel', 13))
        label.pack(pady=110)

        self.paper_way.mainloop()
    # 플라스틱 버리는 법
    def plastic_way(self):
        self.plastic_way = tk.Toplevel()
        self.plastic_way.title("나혼자 분리수거")
        self.plastic_way.geometry("1000x700")
        self.plastic_way.resizable(False, False)
        self.plastic_way.config(bg="#708467")

        title_bar1 = tk.PhotoImage(file="image/title_bar.png")
        bar_title2 = tk.Label(self.plastic_way, image=title_bar1, bg="#708467")
        bar_title2.place(x=360, y=30)

        title_plastic = tk.Label(self.plastic_way, text="플라스틱 버리는 방법", bg="#F7F4E3")
        title_plastic.configure(font=('Corbel', 15))
        title_plastic.place(x=750, y=46)

        f = open("plastic_info.txt", "r", encoding="utf-8")
        text = f.read()
        label = tk.Label(self.plastic_way, text=text, bg="#708467", height=50, fg="white", justify=LEFT)
        label.configure(font=('Corbel', 13))
        label.pack(pady=130)

        self.plastic_way.mainloop()

    # 캔 버리는 법
    def can_way(self):
        self.can_way = tk.Toplevel()
        self.can_way.title("나혼자 분리수거")
        self.can_way.geometry("1000x700")
        self.can_way.resizable(False, False)
        self.can_way.config(bg="#708467")

        title_bar1 = tk.PhotoImage(file="image/title_bar.png")
        bar_title2 = tk.Label(self.can_way, image=title_bar1, bg="#708467")
        bar_title2.place(x=360, y=30)

        title_can = tk.Label(self.can_way, text="캔 버리는 방법", bg="#F7F4E3")
        title_can.configure(font=('Corbel', 15))
        title_can.place(x=810, y=46)

        f = open("can_info.txt", "r", encoding="utf-8")
        text = f.read()
        label = tk.Label(self.can_way, text=text, bg="#708467", height=100, fg="white", justify=LEFT)
        label.configure(font=('Corbel', 14))
        label.pack(pady=180)

        self.can_way.mainloop()

    # 기타 등등 버리는 법
    def etc_way(self):
        self.etc_way = tk.Toplevel()
        self.etc_way.title("나혼자 분리수거")
        self.etc_way.geometry("1000x700")
        self.etc_way.resizable(False, False)
        self.etc_way.config(bg="#708467")

        title_bar1 = tk.PhotoImage(file="image/title_bar.png")
        bar_title2 = tk.Label(self.etc_way, image=title_bar1, bg="#708467")
        bar_title2.place(x=360, y=30)

        title_etc = tk.Label(self.etc_way, text="기타 등등 버리는 방법", bg="#F7F4E3", fg="white", justify=LEFT)
        title_etc.configure(font=('Corbel', 13))
        title_etc.place(x=760, y=46)

        self.etc_way.mainloop()

    def etc_in(self):
        self.etc_in = tk.Toplevel()
        self.etc_in.title("나혼자 분리수거")
        self.etc_in.geometry("1000x700")
        self.etc_in.resizable(False, False)
        self.etc_in.config(bg="#708467")

        title_bar1 = tk.PhotoImage(file="image/title_bar.png")
        bar_title2 = tk.Label(self.etc_in, image=title_bar1, bg="#708467")
        bar_title2.place(x=360, y=30)

        # 음식물 쓰레기
        foodBtn = tk.Button(self.etc_in, width=150, height=180, borderwidth=0, bg="#708467", command=self.food_etc)
        foodBtn.place(x=270, y=200)
        foodmage = tk.PhotoImage(file="image/etc_food.png")
        foodBtn.config(image=foodmage)


        # 헌 옷
        dressBtn = tk.Button(self.etc_in, width=150, height=180, borderwidth=0, bg="#708467", command=self.dress_etc)
        dressBtn.place(x=270, y=440)
        dressImage = tk.PhotoImage(file="image/etc_dress.png")
        dressBtn.config(image=dressImage)

        # 스티로폼
        styrofoamBtn = tk.Button(self.etc_in, width=150, height=180, borderwidth=0, bg="#708467", command=self.styrofoam_etc)
        styrofoamBtn.place(x=550, y=200)
        styrofoamImage = tk.PhotoImage(file="image/etc_Styrofoam.png")
        styrofoamBtn.config(image=styrofoamImage)

        # 비닐
        plasticBtn = tk.Button(self.etc_in, width=150, height=180, borderwidth=0, bg="#708467", command=self.plastic_etc)
        plasticBtn.place(x=550, y=440)
        plasticImage = tk.PhotoImage(file="image/etc_plastic.png")
        plasticBtn.config(image=plasticImage)

        self.etc_in.mainloop()

    # 음식물 쓰레기 버리는 방법
    def food_etc(self):
        self.food_etc = tk.Toplevel()
        self.food_etc.title("나혼자 분리수거")
        self.food_etc.geometry("1000x700")
        self.food_etc.resizable(False, False)
        self.food_etc.config(bg="#708467")

        title_bar1 = tk.PhotoImage(file="image/title_bar.png")
        bar_title2 = tk.Label(self.food_etc, image=title_bar1, bg="#708467")
        bar_title2.place(x=360, y=30)

        title_food = tk.Label(self.food_etc, text="음식물 쓰레기 버리는 방법", bg="#F7F4E3")
        title_food.configure(font=('Corbel', 15))
        title_food.place(x=750, y=46)

        f = open("etc_food.txt", "r", encoding="utf-8")
        text = f.read()
        label = tk.Label(self.food_etc, text=text, bg="#708467", height=100, fg="white", justify=LEFT)
        label.configure(font=('Corbel', 13))
        label.pack(pady=180)

        self.food_etc.mainloop()

    # 헌 옷 버리는 방법
    def dress_etc(self):
        self.dress_etc = tk.Toplevel()
        self.dress_etc.title("나혼자 분리수거")
        self.dress_etc.geometry("1000x700")
        self.dress_etc.resizable(False, False)
        self.dress_etc.config(bg="#708467")

        title_bar1 = tk.PhotoImage(file="image/title_bar.png")
        bar_title2 = tk.Label(self.dress_etc, image=title_bar1, bg="#708467")
        bar_title2.place(x=360, y=30)

        title_dress = tk.Label(self.dress_etc, text="헌 옷 버리느 방법", bg="#F7F4E3")
        title_dress.configure(font=('Corbel', 15))
        title_dress.place(x=750, y=46)

        f = open("etc_dress.txt", "r", encoding="utf-8")
        text = f.read()
        label = tk.Label(self.dress_etc, text=text, bg="#708467", height=100, fg="white", justify=LEFT)
        label.configure(font=('Corbel', 13))
        label.pack(pady=180)

        self.dress_etc.mainloop()

    # 스티로폼 버리는 방법
    def styrofoam_etc(self):
        self.styrofoam_etc = tk.Toplevel()
        self.styrofoam_etc.title("나혼자 분리수거")
        self.styrofoam_etc.geometry("1000x700")
        self.styrofoam_etc.resizable(False, False)
        self.styrofoam_etc.config(bg="#708467")

        title_bar1 = tk.PhotoImage(file="image/title_bar.png")
        bar_title2 = tk.Label(self.styrofoam_etc, image=title_bar1, bg="#708467")
        bar_title2.place(x=360, y=30)

        title_styrofoam = tk.Label(self.styrofoam_etc, text="스티로폼 버리는 방법", bg="#F7F4E3")
        title_styrofoam.configure(font=('Corbel', 15))
        title_styrofoam.place(x=750, y=46)

        f = open("etc_styrofoam.txt", "r", encoding="utf-8")
        text = f.read()
        label = tk.Label(self.styrofoam_etc, text=text, bg="#708467", height=100, fg="white", justify=LEFT)
        label.configure(font=('Corbel', 13))
        label.pack(pady=180)

        self.styrofoam_etc.mainloop()

    # 비닐 만드는 방법
    def plastic_etc(self):
        self.plastic_etc = tk.Toplevel()
        self.plastic_etc.title("나혼자 분리수거")
        self.plastic_etc.geometry("1000x700")
        self.plastic_etc.resizable(False, False)
        self.plastic_etc.config(bg="#708467")

        title_bar1 = tk.PhotoImage(file="image/title_bar.png")
        bar_title2 = tk.Label(self.plastic_etc, image=title_bar1, bg="#708467")
        bar_title2.place(x=360, y=30)

        title_plastic = tk.Label(self.plastic_etc, text="비닐 버리는 방법", bg="#F7F4E3")
        title_plastic.configure(font=('Corbel', 15))
        title_plastic.place(x=750, y=46)

        f = open("etc_plastic.txt", "r", encoding="utf-8")
        text = f.read()
        label = tk.Label(self.plastic_etc, text=text, bg="#708467", height=300, fg="white", justify=LEFT)
        label.configure(font=('Corbel', 13))
        label.pack(pady=180)

        self.plastic_etc.mainloop()


if __name__ == '__main__':
    rice = Rice()
