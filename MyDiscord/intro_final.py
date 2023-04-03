from tkinter import *
from tkinter import ttk
from customtkinter import *
from PIL import Image, ImageTk
from math import pi
import time


set_appearance_mode('dark')
set_default_color_theme("green")

bob= CTk()
bob.title('DISCARD')
bob.geometry('1600x900')
bob.resizable(False,False)
bob.configure(fg_color='#1e1c1c')
bob.iconbitmap("ImageResources/discard.ico")

def main():

    def skip(frame,color):
        def skip_clicked():
            bob.destroy()
           
        skip_button = CTkButton(frame,
                                text = 'Skip',
                                text_font = ('Segoe UI Black', 40),
                                width = 50,
                                height = 15,
                                fg_color = color,
                                hover_color = color,
                                command= skip_clicked)
        skip_button.place(x=1450, y = 20)

    def close():
        bob.destroy()

    def intro1():
        global intro_1
        
        intro_1 = CTkFrame(bob,
                           fg_color = 'white',
                           width = 1600,
                           height = 900)
        intro_1.pack()


        skip(intro_1,'white')

        pic1 = Image.open('ImageResources/intro1.png')
        pic1_resize = pic1.resize((700,700))
        pic1_1 = ImageTk.PhotoImage(pic1_resize)
        pic1label = CTkButton(intro_1,
                             image = pic1_1,
                             fg_color = 'white',
                             height = 400,
                             width = 400,
                             text = '',
                             state='disabled')
        pic1label.place(x=75,y=30)

        msg1 = CTkLabel(intro_1,
                        width = 100,
                        height = 200,
                        text = 'Connect.\nCommunicate.\nCelebrate.',
                        text_font = ('Segoe UI Black', 45),
                        text_color = 'gray',
                        fg_color = 'white',
                        justify = LEFT)
        msg1.place(x=1000, y = 300)


    def intro2():
        global intro_2
        
        bob.after(4145,intro_1.destroy)          
        intro_2 = CTkFrame(bob,
                           fg_color = '#C8BFE7',
                           width = 1600,
                           height = 900)
        intro_2.pack()


        pic2 = Image.open('ImageResources/intro2.png')
        pic2_resize = pic2.resize((700,700))
        pic2_1 = ImageTk.PhotoImage(pic2_resize)
        pic2label = CTkButton(intro_2,
                             image = pic2_1,
                             fg_color = '#C8BFE7',
                             height = 400,
                             width = 400,
                             text = '',
                             state='disabled')
        pic2label.place(x=800,y=50)

        skip(intro_2,'#C8BFE7')

        msg2 = CTkLabel(intro_2,
                        width = 100,
                        height = 200,
                        text = 'Personalize your profile\nand share other\nsocial media handles.',
                        text_font = ('Segoe UI Black', 45),
                        text_color = 'white',
                        fg_color = '#C8BFE7',
                        justify = LEFT)
        msg2.place(x=75, y = 300)


    def intro3():
        bob.after(8290,intro_2.destroy)          
        intro_3 = CTkFrame(bob,
                           fg_color = 'black',
                           width = 1600,
                           height = 900)
        intro_3.pack()
        skip(intro_3, 'black')
        pic3 = Image.open('ImageResources/intro3.png')
        pic3_resize = pic3.resize((700,700))
        pic3_1 = ImageTk.PhotoImage(pic3_resize)
        pic3label = CTkButton(intro_3,
                             image = pic3_1,
                             fg_color = 'black',
                             height = 400,
                             width = 400,
                             text = '',
                             state='disabled')
        pic3label.place(x=75,y=10)

        msg3 = CTkLabel(intro_3,
                        width = 100,
                        height = 200,
                        text = 'Start your journey\non DISCARD\ntoday.',
                        text_font = ('Segoe UI Black', 45),
                        text_color = 'white',
                        fg_color = 'black',
                        justify = LEFT)
        msg3.place(x=950, y = 300)

                

    intro1()
    intro2()
    intro3()
    
    progress1 = CTkProgressBar(bob,
                               width = 200,
                               height = 5,
                               progress_color = 'sky blue',
                               determinate_speed= 0.4)
    progress1.place(x=500,y=800)
    progress1.set(0,100)

    progress2 = CTkProgressBar(bob,
                               width =200,
                               height = 5,
                               progress_color='sky blue',
                               determinate_speed= 0.4)
    progress2.place(x=710,y=800)
    progress2.set(0,100)
    progress3 = CTkProgressBar(bob,
                               width = 200,
                               height = 5,
                               progress_color = 'sky blue',
                               determinate_speed= 0.4)
    progress3.place(x=920,y=800)
    progress3.set(0,100)

    def pr1():
        progress1.stop()
        progress2.start()
        
    def pr2():
        progress2.stop()
        progress3.start()
    def pr3():
        progress3.stop()
    progress1.start()
    bob.after(4140,pr1)
    
    bob.after(8290,pr2)
    
    bob.after(12425,pr3)

    bob.protocol("WM_DELETE_WINDOW", close)

main()

bob.mainloop()
