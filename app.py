import os
import openai
import tkinter as tk
# askgpt class
import askgpt as asklegpt

# read the apikey from local dir
with open(r"D:\aAPIkeys\openaiprivate.txt", 'r') as f:
    openai.api_key = f.readline()
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
        self.master.title("ChatGPT GUI")

        # add label
        tk.Label(master, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome to ChatGPT", font=FONT_BOLD, pady=10,
                 width=20, height=1).grid(row=0, columnspan=2)

        # define the main textbox:
        self.master.txt = tk.Text(master, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=130, height=32)
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

        # bind a shortcut quit key:
        def quit(event):
            print("you pressed control-q")
            self.master.quit()

        # bind the quit function with control + q:
        self.master.bind('<Control-q>', quit)

    def clicked(self, event):
        """
        This function defines the cliked event, the api request is included

        Returns: no return for this function
        """
        send = "Q -> " + self.master.entry.get()
        self.master.txt.insert(tk.END, "\n" + send)
        user = self.master.entry.get().lower()
        ### check if null input ###
        print(user)
        self.master.txt.insert(tk.END, "\n" + "A -> " + asklegpt.askGPT(user)[2:] + "\n")
        self.master.entry.delete(0, tk.END)

        self.master.txt.see(tk.END)
        # end chat
        self.master.entry.delete(0, tk.END)

# start running the home window
root = tk.Tk()
app = ChatBotHomePage(root)
root.mainloop()