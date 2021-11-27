import tkinter

import details_menu
import home

class Main_in:
    def __init__(self, menu_in1):
        self.menu_in1 = menu_in1

        self.background = tkinter.PhotoImage(file="image/background.png")
        self.background_in = tkinter.Label(image=self.background)
        self.background_in.place(x=-2, y=-2)

        self.title3 = tkinter.Label(self.menu_in1, text="나혼자 분리수거", bg="#708467")
        self.title3.configure(font=('Corbel', 23))
        self.title3.place(x=360, y=50)

        self.title_img = tkinter.PhotoImage(file='image/title_img_mini.png')
        self.title_img_in = tkinter.Label(image=self.title_img, bg="#708467")
        self.title_img_in.place(x=600, y=40)

        self.my_page_btn = tkinter.PhotoImage(file='image/my_page.png')
        self.my_page_btn_in = tkinter.Button(self.menu_in1, image=self.my_page_btn, bg="#708467")
        self.my_page_btn_in.place(x=900, y=30)

        self.img1 = tkinter.PhotoImage(file='image/btn_search.png')
        self.search_img = tkinter.Button(image=self.img1, bg="#708467")
        self.search_img.place(x=200, y=280)

        self.img2 = tkinter.PhotoImage(file='image/general_trash.png')
        self.trash1 = tkinter.Button(image=self.img2, bg="#708467")
        self.trash1.place(x=400, y=280)

        self.img3 = tkinter.PhotoImage(file='image/recycling.png')
        self.trash2 = tkinter.Button(image=self.img3, bg="#708467", command=self.move_details_menu)
        self.trash2.place(x=600, y=280)

    def move_details_menu(self):
        moveDetails = details_menu.Details_menu(self.move_details_menu)