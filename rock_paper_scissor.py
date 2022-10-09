import tkinter as tk
import random

root = tk.Tk()
root.geometry("500x600")
root.title("Rock Paper Scissor")
user_sc = 0
computer_sc = 0

 
# creating a message box

def random_computer_choice():
    return random.choice(['stone', 'paper', 'scissor'])


def choice_to_number(choice):
    rps = {'stone': 0, 'paper': 1, 'scissor': 2}
    return rps[choice]


def stone():
    usr_choice = "stone"
    cmp_choice = random_computer_choice()
    result(usr_choice, cmp_choice)


def paper():
    usr_choice = "paper"
    cmp_choice = random_computer_choice()
    result(usr_choice, cmp_choice)


def scissor():
    usr_choice = "scissor"
    cmp_choice = random_computer_choice()
    result(usr_choice, cmp_choice)


def result(usr_ch, cmp_ch):
    t = tk.Text(root, width=100, height=100, padx=10, pady=10, fg="green", font=("cursive", 16, 'bold'))
    global user_sc
    global computer_sc
    usr_v = choice_to_number(usr_ch)
    cmp_v = choice_to_number(cmp_ch)
    if usr_v == cmp_v:
        tie = f"Result: Tie \n"
        t.insert(tk.END, tie)
    elif (usr_v-cmp_v) % 3 == 1:
        win = f"Result: Congrats! You win \n"
        user_sc += 1
        t.insert(tk.END, win)
    else:
        lose = f"Result: Computer win \n"
        computer_sc += 1
        t.insert(tk.END, lose)
    
    answer = f"You choose : {usr_ch} \ncomputer choose : {cmp_ch} \nYou score is : {user_sc} \nComputer score is : {computer_sc}"
    t.insert(tk.END, answer)
    t.place(x=0, y=200)


b1 = tk.Button(root, text="STONE", fg="white", bg="red", command=stone)
b1.place(x=180, y=30, width=80, height=20)
b2 = tk.Button(root, text="PAPER", fg="blue", bg="white", command=paper)
b2.place(x=180, y=80, width=80, height=20)
b3 = tk.Button(root, text="SCISSOR", fg="white", bg="magenta", command=scissor)
b3.place(x=180, y=130, width=80, height=20)
b4 = tk.Button(root, text="Exit", fg="red", bg="white", command=root.destroy)
b4.place(x=400, y=160, width=80, height=20)

root.mainloop()
