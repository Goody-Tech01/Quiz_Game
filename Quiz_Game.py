import tkinter as tk
from tkinter import messagebox
import json

with open ("question.json","r") as file:
    questions=json.load(file)

current_question=0
score=0
selected_answers=[None] * len(questions)

def start_quiz():
    start_button.pack_forget()
    question_label.pack(pady=20)

    next_button.pack(pady=5)
    previous_button.pack(pady=5)
    Retry_button.pack(pady=5)
    show_question()

def show_question():
    global current_question

    q=questions[current_question]

    question_label.config(text=f"Q{current_question + 1}: {q["question"]}")

    for i in range (4):
        options_buttons[i].config(text=q["options"][i],
                        bg="SystemButtonFace")
        options_buttons[i].pack(pady=8,fill="x")

    if selected_answers[current_question] is not None:
        options_buttons[selected_answers[current_question]].config(bg="green")

    if current_question == len(questions) -1:
        next_button.config(text="Submit",command=show_result)
    else:
        next_button.config(text="Next",command=next_question)

def select_answer(index):
    global current_question
    for btn in options_buttons:
        btn.config(bg="SystemButtonFace",fg="black")

    selected_answers[current_question]=index

    options_buttons[index].config(bg="green")


def next_question():
    global current_question
    if current_question < len(questions) -1:
        current_question +=1
        show_question()
    else:
         show_result()

def previous_question():
    global current_question
    if current_question >0:
        current_question-=1
        show_question()


def show_result():
    global score
    score=0

    for i in range (len(questions)):
        if selected_answers[i] is not None:
            if questions[i]["options"][selected_answers[i]]==questions[i]["answer"]:
                score+=1
    percentage=int((score/len(questions))*100)

    messagebox.showinfo("Quiz Finished",f"Your score:{score}/{len(questions)}\n(percentage:{percentage}%")



def retry_quiz():
    global current_question,score,selected_answers
    current_question=0
    score=0
    selected_answers=[None]*len(questions)

    show_question()


root=tk.Tk()
root.geometry("400x350")
root.title("Python Quiz Game")

start_button=tk.Button(root,text="Start Quiz",font=("Arial",20,"bold"),command=start_quiz)
start_button.pack(pady=250)

question_label=tk.Label(root,
                        text="",font=("Verdana",14),wraplength=350)
question_label.pack(pady=20)

options_frame=tk.Frame(root)
options_frame.pack(pady=10)

options_buttons=[]
for i in range(4):
    btn=tk.Button(options_frame,
                  text="",width=25,height=2,command=lambda idx=i:select_answer(idx))
    options_buttons.append(btn)
    btn.pack(pady=5)


nav_frame=tk.Frame(root,bg="#F5F5F5")
nav_frame.pack(pady=10)
previous_button=tk.Button(nav_frame,text="Previous",command=previous_question)
previous_button.pack(side=tk.LEFT,padx=5)

Retry_button=tk.Button(nav_frame,text="Retry Quiz",command=retry_quiz,font=("Arial",8,"bold"))
Retry_button.pack(side=tk.LEFT,padx=5)

next_button=tk.Button(nav_frame,text="Next",command=next_question)
next_button.pack(side=tk.LEFT,padx=5)

root.mainloop()
