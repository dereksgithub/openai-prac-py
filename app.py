import os
import openai
import tkinter as tk
# askgpt class
import askgpt as asklegpt

# read the apikey from local dir
with open(r"D:\aAPIkeys\openaiprivate.txt", 'r') as f:
    openai.api_key = f.readline()
    f.close()

# read the test line:
with open(r"D:\aAPIkeys\madgpt.txt", 'r') as f:
    madmode = f.readline()
    f.close()

# Set theme for the GUI
BG_GRAY = "#ABB2B9"
BG_COLOR = "#0c0c0d"
TEXT_COLOR = "#28fa19"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


# OOP Style:
class ChatBotHomePage:

    def __init__(self, master):
        """
        The home window
        """
        self.master = master
        # add window title:
        self.master.title("ChatGPT and DALL.E GUI")

        # add label
        tk.Label(master, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome to ChatGPT and DALL.E", font=FONT_BOLD, pady=10,
                 width=30, height=1).grid(row=0, columnspan=2)

        # define the main textbox:
        self.master.txt = tk.Text(master, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=130, height=20)
        self.master.txt.grid(row=1, column=0, columnspan=2)
        self.master.txt.insert('1.0', 'Aks me anything:')

        # add scrollbars
        self.master.scrollbar = tk.Scrollbar(self.master.txt)
        self.master.scrollbar.place(relheight=1, relx=1.01)

        # add a standard entry box, configure its appearance and location
        self.master.entry = tk.Entry(master, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=100)
        self.master.entry.configure(bg=BG_COLOR, insertbackground=TEXT_COLOR, insertwidth=5)
        self.master.entry.grid(row=2, columnspan=2, padx=10, pady=20, ipady=3)

        # Create the button, configure its appearance and location
        self.master.sendbtn = tk.Button(master, text="Send", font=FONT_BOLD, bg=BG_GRAY)
        self.master.sendbtn.bind("<Button-1>", self.clicked)
        self.master.sendbtn.grid(row=3, column=0)

        # bind the send button with ctrl + enter:
        self.master.bind('<Control-Return>', self.clicked)

        # mad mode, Create the button, configure its appearance and location
        self.master.sendmadbtn = tk.Button(master, text="MadSend", font=FONT_BOLD, bg=BG_GRAY)
        # bind left mouse click
        self.master.sendmadbtn.bind("<Button-1>", self.madclicked)
        self.master.sendmadbtn.grid(row=3, column=1)
        # bind the send button with ctrl + m:
        self.master.bind('<Control-m>', self.madclicked)

        # Create the button, configure its appearance and location
        self.master.sendbtn = tk.Button(master, text="Send to DALL.E", font=FONT_BOLD, bg=BG_GRAY)
        self.master.sendbtn.bind("<Button-1>", self.dalleclicked)
        self.master.sendbtn.grid(row=5, column=0)

        # bind the send button with ctrl + enter: dalleclicked
        self.master.bind('<Control-d>', self.dalleclicked)

        # bind a shortcut quit key:
        def quitchat(event):
            print("you pressed control-q")
            # tkinter method quit()
            self.master.quit()

        # bind the quit function with control + q:
        self.master.bind('<Control-q>', quitchat)

    def clicked(self, event):
        """
        This function defines the cliked event, the api request is included

        Returns: no return for this function
        """
        send = "Q -> " + self.master.entry.get()
        self.master.txt.insert(tk.END, "\n" + send)
        user = self.master.entry.get().lower()

        # store asked question in another dir:
        gptanswertext = asklegpt.askGPT(user)[2:]

        # insert the reply to the textbox
        self.master.txt.insert(tk.END, "\n" + "A -> " + gptanswertext + "\n")

        # store our q and a locally
        with open(r"D:\gptQandA.txt", 'a', encoding="utf-8") as f1:
            # write the question and answer into our txt file
            f1.write("\n" + "Q: " + user + "\n")
            f1.write("A: " + gptanswertext + "\n")
            f1.close()

        # clear entry:
        self.master.entry.delete(0, tk.END)
        self.master.txt.see(tk.END)
        # end chat
        self.master.entry.delete(0, tk.END)

    def madclicked(self, event):
        """
        This function defines the madliked event, the secret string for api request is included

        Returns: no return for this function
        """
        send = "Q-mad -> " + self.master.entry.get()
        self.master.txt.insert(tk.END, "\n" + send)
        user = self.master.entry.get().lower()

        # store asked question in another dir:
        madgptanswertext = asklegpt.askGPT(madmode + user)[2:]

        # insert the reply to the textbox
        self.master.txt.insert(tk.END, "\n" + "A-mad -> " + madgptanswertext + "\n")

        # store our q and a locally
        with open(r"D:\gptQandA.txt", 'a', encoding="utf-8") as f1:
            # write the question and answer into our txt file
            f1.write("\n" + "Q-mad: " + user + "\n")
            f1.write("A-mad: " + madgptanswertext + "\n")
            f1.close()

        # clear entry:
        self.master.entry.delete(0, tk.END)
        self.master.txt.see(tk.END)
        # end chat
        self.master.entry.delete(0, tk.END)

    def dalleclicked(self, event):
        """
        This function defines the is for asking dall.e to generate an image, default is 256 x 256

        Returns: no return for this function
        """
        send = "Q-image -> " + self.master.entry.get()
        self.master.txt.insert(tk.END, "\n" + send)
        user = self.master.entry.get().lower()

        # store asked question in another dir:
        urltoimagegen = asklegpt.askdalle(user)

        # insert the reply to the textbox
        self.master.txt.insert(tk.END, "\n" + "A-image -> " + urltoimagegen + "\n")

        # store our q and a locally
        with open(r"D:\gptQandA.txt", 'a', encoding="utf-8") as f1:
            # write the question and answer into our txt file
            f1.write("\n" + "Q-image: " + user + "\n")
            f1.write("A-image: (link only valid for an hour) " + urltoimagegen + "\n")
            f1.close()

        # clear entry:
        self.master.entry.delete(0, tk.END)
        self.master.txt.see(tk.END)
        # end chat
        self.master.entry.delete(0, tk.END)


# start running the home window
root = tk.Tk()
app = ChatBotHomePage(root)
root.mainloop()
