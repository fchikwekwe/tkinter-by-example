import tkinter as tk


class Root (tk.Tk):
    def __init__(self):
        super().__init__()

        self.label = tk.Label(self, text ="Hello World", padx=20, pady=20)

        self.label.pack()

if __name__=="__main__":
    root = Root()
    root.mainloop()
