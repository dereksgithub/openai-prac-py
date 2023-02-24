import os
import openai
from flask import Flask, redirect, render_template, request, url_for, app

import tkinter as tk
import askgpt as asklegpt
with open(r"D:\aAPIkeys\openaiprivate.txt", 'r') as f:
    openai.api_key = f.readline()
    f.close()
# print(openai.api_key)
# openai.api_key = ""
openai.Model.list()
# Set theme for the GUI
BG_GRAY = "#ABB2B9"
BG_COLOR = "#0c0c0d"
TEXT_COLOR = "#28fa19"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# create the window
window = tk.Tk()

# set the window size
#window.geometry('900x500')

# set the window title
window.title("ChatGPT GUI")

# add a label
lable1 = tk.Label(window, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome to ChatGPT", font=FONT_BOLD, pady=10, width=20,
                  height=1).grid(row=0, columnspan=2)

# add the main interfacing text box
txt = tk.Text(window, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=130, height= 32)
txt.grid(row=1, column=0, columnspan=2)
txt.insert('1.0', 'Aks me anything:')

# for scrolling (auto)
scrollbar = tk.Scrollbar(txt)
scrollbar.place(relheight=1, relx=1.01)

# entry text-box
entry = tk.Entry(window, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=100)
entry.configure(bg=BG_COLOR, insertbackground=TEXT_COLOR, insertwidth=5)
# this function to adjust cursor location is not effective,entry.icursor(entry.index(tk.END)+555)
# height=215, width=200)
entry.grid(row=2, columnspan=2, padx=10, pady=20, ipady=3)

# add event:
def clicked(event):
    # At the start of each conversation

    send = "Q -> " + entry.get()
    txt.insert(tk.END, "\n" + send)
    user = entry.get().lower()
    print(user)
    txt.insert(tk.END, "\n" + "A -> " + asklegpt.askGPT(user)[2:] + "\n")
    entry.delete(0, tk.END)

    txt.see(tk.END)
    # end chat
    entry.delete(0, tk.END)

# Create the button
sendbtn = tk.Button(window, text="Send", font=FONT_BOLD, bg=BG_GRAY)
sendbtn.bind("<Button-1>", clicked)

# place the send button
sendbtn.grid(row=3, column=0)

# bind the send button with ctrl + enter:
window.bind('<Control-Return>', clicked)

# bind a shortcut quit key:
def quit(event):
    print("you pressed control-q")
    window.quit()

# bind the send button with with ctrl + enter:
window.bind('<Control-q>', quit)

# add another button, clear screen:


# run the window
window.mainloop()
