from tkinter import*
from PIL import Image,ImageTk
from random import randint


#main window
root=Tk()
root.title("Rock Paper Scissor")
root.configure(background="lightgreen")


#picture
rock_img= ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_img= ImageTk.PhotoImage(Image.open("paper_user.png"))
scissor_img= ImageTk.PhotoImage(Image.open("scissor_user.png"))

rock_img_comp= ImageTk.PhotoImage(Image.open("rock_comp.png"))
paper_img_comp= ImageTk.PhotoImage(Image.open("paper_comp.png"))
scissor_img_comp= ImageTk.PhotoImage(Image.open("scissor_comp.png"))

# insert image

user_label= Label(root, image=scissor_img)
comp_label=Label(root,image=scissor_img_comp)

user_label.grid(row=1,column=0)
comp_label.grid(row=1,column=4)
#scores
player_score=Label(root,text=0,font=100,bg="lightgreen",fg="black")
comp_score=Label(root,text=0,font=100,bg="lightgreen",fg="black")
player_score.grid(row=1,column=1)
comp_score.grid(row=1,column=3)


#indicators

user_ind=Label(root,font=50,text="COMPUTER",bg="lightgreen").grid(row=0,column=3)
comp_ind=Label(root,font=50,text="USER",bg="lightgreen").grid(row=0,column=1)



#messages
msg=Label(root,font=50,bg="lightgreen",fg="black")
msg.grid(row=3,column=2)


#update message
def updatemassage(x):
    msg['text']=x

#update user score
def update_user():
    score= int(player_score['text'])
    score+=1
    player_score['text']=str(score)

#update comp score
def update_comp():
    score= int(comp_score['text'])
    score+=1
    comp_score['text']=str(score)



#check winner

def checkWin(player,computer):
    if player==computer:
        updatemassage("Its a tie!!")
    elif player=="rock":
        if computer=="paper":
            updatemassage("You loose!")
            update_comp()
        else:
            updatemassage("You win!!")
            update_user()
    elif player=="paper":
        if computer=="scissor":
            updatemassage("You loose!")
            update_comp()
        else:
            updatemassage("You win!!")
            update_user()
    elif player=="scissor":
        if computer=="paper":
            updatemassage("You Win!!")
            update_user()
        else:
            updatemassage("You loose!")
            update_comp()
    else:
        pass


#update choices

choices=["rock","paper","scissor"]

def updatechoice(x):
    
    #for computer
    comp_choice= choices[randint(0,2)]
    if comp_choice=="rock":
        comp_label.configure(image=rock_img_comp)
    elif comp_choice=="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


#for user

    if x=='rock':
        user_label.configure(image=rock_img)
    elif x=='paper':
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    
    checkWin(x,comp_choice)

#buttons
rock=Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command=lambda:updatechoice("rock")).grid(row=2,column=1)

paper=Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command=lambda:updatechoice("paper")).grid(row=2,column=2)

scissor=Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="white",command=lambda:updatechoice("scissor")).grid(row=2,column=3)


root.mainloop()