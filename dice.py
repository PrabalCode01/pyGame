# import random

# again =True

# while again:
#     print(random.randint(1,6))
#     another_roll=input("Want to roll the dice again? (yes/no): ")
#     if another_roll.lower()=="yes":
#         continue
#     else:
#         break


import random
from tkinter import*   #means to import everything




class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)
 
    def style_text(code):
        return "\33[{code}m".format(code=code)
 
    def color_text(code):
        return "\33[{code}m".format(code=code)

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb  

root=Tk()    #means tkinter window
root.geometry("1000x1000")

text_1= Label(root,text='',font=("arial",450))


def roll_the_dice():
    num_code=['\u2680', '\u2681' ,'\u2682' ,'\u2683' ,'\u2684' ,'\u2685']
    text_1.config(text=f'{random.choice(num_code)}{random.choice(num_code)}')
    text_1.pack()

button_1= Button(root,text="Roll the Dice",font=("arial",50), padx=10, pady=10,bg='#4a7abc',    fg='yellow',command=roll_the_dice)
button_1.place(x=250,y=0)

root.config(bg=rgb_hack((255, 0, 122))) 


root.mainloop()
