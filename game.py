import tkinter as tk
from tkinter import font

class GameScreen():
    def __init__(self, master, image, roi, inventory_item=None, help_text=None):
        self.master = master
        self.roi = roi
        self.image = tk.PhotoImage(file=image)
        self.inventory_item = inventory_item
        self.help_text = help_text

    def on_clock(self, event):
        if (self.roi[0] <= event.x <= self.roi[2]
            and self.roi[1] <= event.y <= self.roi[3]):

            if self.inventory_item:
                self.master.add_inventory_item(self.inventory_item)
            self.master.show_next_screen()

class Game(tk.Tk):
    def __init__(self):
        super().__init__()

        self.inventory_slots = []
        self.inventory_slots_in_use = []
        self.current_screen_number = 0
        self.success_font = font.Font(family="ubuntu", size=50, weight=font.BOLD)

        self.title("Point and Click")
        self.geometry("800x640")
        self.resizeable(False, False)

        self.key_image = tk.PhotoImage(file="assets/key.png")
        self.questions_mark_image = tk.PhotoImage(file="assets/questionmark.png")

        self.screen = tk.Canvas(self, bg="white", width=500, height=800)
        self.right_frame = tk.Frame(self, width=300, height=800)
        self.right_frame.pack_propagate(0)

        self.help_var = tk.StringVar(self.right_frame)
        self.help_var.set("Try Clicking Something")

        self.help_box = tk.Label(self.right_frame, textvar=self.help_var, background="black", foreground="white", padx=10, pady=20)
        self.help_box.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        inventory_title = tk.Label(self.right_frame, text="Inventory:", background="grey", foreground="white")

        inventory_space = tk.Frame(self.right_frame, background="lightgrey", width=300, height=320)
        inventory_space.pack_propagate(0)

        inventory_space.pack(side=tk.BOTTOM)
        inventory_title.pack(side=tk.BOTTOM, fill=tk.X)

        inventory_slot_1 = tk.Button(inventory_space, image=self.questions_mark_image)
