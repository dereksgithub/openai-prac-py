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

#image_resp = openai.Image.create(prompt="two dogs playing chess, oil painting", n=4, size="512x512")
#gpt_prompt = "Say this is a test"



# create the window
window = tk.Tk()

# set the window size
#window.geometry('900x500')

# set the window title
window.title("ChatGPT GUI")

# add a label
#label = tk.Label(window, text="Hi there! What can I do for you?")
#label.pack()
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

#entry.pack()

"""
end-1c is divided in 2 parts:

 1) end: Read until the end of the text.
 2) 1c: Remove 1 character starting from the end.
It deletes the last character to remove that last \n so your e-mail doesn't end with an extra line.
"""
# add a submit button
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
#sendbtn = tk.Button(window, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=clicked).grid(row=3, column=0)
#sendbtn = tk.Button(window, text="Send", font=FONT_BOLD, bg=BG_GRAY)
sendbtn = tk.Button(window, text="Send", font=FONT_BOLD, bg=BG_GRAY)
sendbtn.bind("<Button-1>", clicked)

# place the send button
sendbtn.grid(row=3, column=0)

# bind a shortcut quit key:
def quit(event):
    print("you pressed control-q")
    window.quit()

# bind the send button with with ctrl + enter:
window.bind('<Control-q>', quit)

# bind the send button with with ctrl + enter:
window.bind('<Control-Return>', clicked)
# add another button, clear screen:

#btn.pack()

# run the window
window.mainloop()

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="If",
#   max_tokens=100,
#   top_p=1,
#   frequency_penalty= 0.0,
#   presence_penalty= 0.0,
#   stop=["\n"]
# )
# print(response.choices[0].text)
#


# @app.route("/", methods=("GET", "POST"))
# def index():
#     if request.method == "POST":
#         animal = request.form["animal"]
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=generate_prompt(animal),
#             temperature=0.6,
#         )
#         return redirect(url_for("index", result=response.choices[0].text))
#
#     result = request.args.get("result")
#     return render_template("index.html", result=result)


# Create an OpenAI API client
# openai_client = openai.Client(openai.api_key)
#
# # Create a GPT-3 engine
# engine = openai_client.engine("davinci")
#
# # Ask GPT-3 a question
# prompt = "hello, how are you doing today?"
# response = engine.engine.completions(prompt, max_tokens=2000)
#
# # Print the response
# print(response["choices"][0]["text"])

"""Suggest three names for an animal that is a superhero.
def generate_prompt(animal):
    return.format(
        animal.capitaliz
e()
    )
Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:
"""

# # list engines
# engines = openai.Engine.list()
#
# # print the first engine's id
# print(engines.data[0].id)
#app = Flask(__name__)
#openai.api_key = os.getenv("OPENAI_API_KEY")
#print(openaiapikey)