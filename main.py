from tkinter import *
import random

TITLE = ("chiller", 38, "bold")
CONTENT = ("book antiqua", 12, "bold")
FONT = ("arial", 12, "bold")

BLOOD = "#650000"
DARK = "#421212"
MID = "#9B3922"
GREY = "#222222"
LIGHT = "#F2613F"


class AddHunger:
    def __init__(self):
        self.dice_num = 0
        self.dice_positions = [[2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 2], [3, 3], [3, 4]]
        self.dice_list = []
        self.successes = 0
        self.failures = 0
        self.crit_success = 0
        self.crit_fail = 0
        self.rolled = []

    def new_dice(self):
        if self.dice_num < 7:
            column = self.dice_positions[self.dice_num][0]
            row = self.dice_positions[self.dice_num][1]
            img = PhotoImage("Reg.png").subsample(23, 23)
            dice = Label(
                image=img,
                bg=BLOOD,
                fg="white",
                height=4,
                width=8,
                highlightthickness=2,
                highlightbackground="black"
            )
            dice.grid(column=column, row=row, pady=5)
            self.dice_num += 1
            self.dice_list.append(dice)
        roll.grid(column=0, row=10, columnspan=4, pady=20,)

    def remove_dice(self):
        if self.dice_num >= 1:
            self.dice_list[self.dice_num-1].grid_forget()
            self.dice_list.pop()
            self.dice_num -= 1

        if self.dice_num == 0 and add.dice_num == 0:
            roll.grid_forget()

    def roll(self):
        for each in self.dice_list:
            num = random.randint(1, 10)
            self.rolled.append(num)

            if num >= 6:
                if num == 10:
                    self.crit_success += 1
                    self.successes += 1
                else:
                    self.successes += 1
            elif num < 6:
                if num == 1:
                    self.crit_fail += 1
                else:
                    self.failures += 1

        self.rolled = sorted(self.rolled, reverse=True)
        rolled_range = 0
        for dice in self.dice_list:
            dice.config(image="")
            dice.config(text=self.rolled[rolled_range], font=FONT, width=6, height=3)
            rolled_range += 1

        total_crits = add.crit + self.crit_success
        extra = 0
        if total_crits >= 2:
            extra = (2 * (total_crits//2))
        successes = add.successes + hunger.successes + extra

        stats.config(
            text=f"Successes:  {successes}       Crits: {total_crits}     "
                 f"Messy Crit:  {hunger.crit_success}\n\nFailures:  {add.failures + hunger.failures}      "
                 f"Bestial Failure:  {hunger.crit_fail}"
        )
        stats.grid(column=0, row=11, columnspan=4, pady=20)
        roll.grid_forget()


class AddDice:
    def __init__(self):
        self.dice_num = 0
        self.dice_positions = [[0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6]]
        self.dice_list = []
        self.successes = 0
        self.failures = 0
        self.crit = 0
        self.rolled = []

    def new_dice(self):
        if self.dice_num < 10:
            column = self.dice_positions[self.dice_num][0]
            row = self.dice_positions[self.dice_num][1]

            dice = Label(
                height=4,
                width=8,
                bg=GREY,
                fg="white",
                highlightthickness=2,
                highlightbackground="black"
            )
            dice.grid(column=column, row=row, pady=5)
            self.dice_num += 1
            self.dice_list.append(dice)
        roll.grid(column=0, row=10, columnspan=4, pady=20,)

    def remove_dice(self):
        if self.dice_num >= 1:
            self.dice_list[self.dice_num-1].grid_forget()
            self.dice_list.pop()
            self.dice_num -= 1

        if self.dice_num == 0 and hunger.dice_num == 0:
            roll.grid_forget()

    def roll(self):
        for each in self.dice_list:
            num = random.randint(1, 10)
            self.rolled.append(num)

            if num >= 6:
                if num == 10:
                    self.crit += 1
                    self.successes += 1

                else:
                    self.successes += 1

            elif num < 6:
                self.failures += 1
        self.rolled = sorted(self.rolled, reverse=True)

        rolled_range = 0
        for dice in self.dice_list:
            dice.config(image="")
            dice.config(compound="center", text=self.rolled[rolled_range], font=FONT, width=6, height=3)
            rolled_range += 1

        reset_button.grid(column=0, row=12)
        if self.dice_num != 0 and self.failures != 0:
            re_roll_button.grid(column=2, row=12)

        add_dice.grid_forget()
        add_hunger.grid_forget()
        remove_hunger.grid_forget()
        remove_dice.grid_forget()


    def re_roll(self):
        re_roll_button.grid_forget()
        re_rollable = []
        for each in self.rolled:
            if each < 6:
                re_rollable.append(each)
            re_rollable = re_rollable[-3:]

        print(re_rollable)
        for each in range(0, len(re_rollable)):
            self.failures -= 1
            self.dice_list[self.dice_num-1].grid_forget()
            self.dice_list.pop()
            self.dice_num -= 1

        for each in range(0, len(re_rollable)):
            num = random.randint(1, 10)
            self.rolled.append(num)
            self.rolled.pop()
            self.rolled.append(num)
            if num >= 6:
                if num == 10:
                    self.crit += 1
                    self.successes += 1

                else:
                    self.successes += 1

            elif num < 6:
                self.failures += 1
            column = self.dice_positions[self.dice_num][0]
            row = self.dice_positions[self.dice_num][1]
            dice = Label(
                text=num,
                height=3,
                width=6,
                bg=MID,
                fg="white",
                highlightthickness=2,
                highlightbackground="black",
                font=FONT
            )
            dice.grid(column=column, row=row, pady=5)
            self.dice_num += 1
            self.dice_list.append(dice)

        total_crits = add.crit + hunger.crit_success
        extra = 0
        if total_crits >= 2:
            extra = (2 * (total_crits//2))
        successes = add.successes + hunger.successes + extra

        stats.config(
            text=f"Successes:  {successes}       Crits: {total_crits}     "
                 f"Messy Crit:  {hunger.crit_success}\n\nFailures:  {add.failures + hunger.failures}      "
                 f"Bestial Failure:  {hunger.crit_fail}"
        )
        stats.grid(column=0, row=11, columnspan=4, pady=20)

def reset():
    while add.dice_num > 0:
        for _ in add.dice_list:
            add.remove_dice()
    while hunger.dice_num > 0:
        for _ in hunger.dice_list:
            hunger.remove_dice()

    hunger.successes = 0
    hunger.failures = 0
    hunger.crit_success = 0
    hunger.crit_fail = 0
    hunger.dice_num = 0
    add.successes = 0
    add.failures = 0
    add.crit = 0
    add.dice_num = 0
    hunger.rolled = []
    add.rolled = []
    add.dice_list = []
    reset_button.grid_forget()
    stats.grid_forget()
    re_roll_button.grid_forget()

    add_dice.grid(column=0, row=1, padx=3)
    remove_dice.grid(column=1, row=1, padx=3)
    add_hunger.grid(column=2, row=1, padx=3, pady=15)
    remove_hunger.grid(column=3, row=1, padx=3)

# Window and Canvas---------------------------------
window = Tk()
window.config(bg=DARK, padx=20, pady=20, highlightthickness=0,)
window.resizable(False, False)
window.minsize(400, 650)
hunger = AddHunger()
add = AddDice()
# Buttons-------------------------------------------
add_dice = Button(
    text="Add\nd10", height=2, width=10, bg=GREY, fg="white", font=CONTENT, highlightthickness=0, relief="solid", activebackground=LIGHT,
    command=add.new_dice)
add_dice.grid(column=0, row=1, padx=3)

remove_dice = Button(
    text="Remove\nd10", height=2, width=10, bg=GREY, fg="white", font=CONTENT, highlightthickness=0, relief="solid", activebackground=LIGHT,
    command=add.remove_dice)
remove_dice.grid(column=1, row=1, padx=3)

add_hunger = Button(
    text="Add\nHunger D10", height=2, width=10, bg=BLOOD, fg="white", font=CONTENT, highlightthickness=0, relief="solid", activebackground=LIGHT,
    command=hunger.new_dice)
add_hunger.grid(column=2, row=1, padx=3, pady=15)

remove_hunger = Button(
    text="Remove\nHunger D10", height=2, width=10, bg=BLOOD, fg="white", font=CONTENT, highlightthickness=0, relief="solid", activebackground=LIGHT,
    command=hunger.remove_dice)
remove_hunger.grid(column=3, row=1, padx=3)

roll = Button(
    text="Roll Dice", bg=BLOOD, fg="white", font=CONTENT, highlightthickness=0, relief="solid", activebackground=LIGHT,
    command=lambda: [add.roll(), hunger.roll()])

reset_button = Button(
    text="Reset", bg=BLOOD, fg="white", font=CONTENT, highlightthickness=0, relief="solid", activebackground=LIGHT,
    command=reset)

re_roll_button = Button(
    text="Reroll", bg=BLOOD, fg="white", font=CONTENT, highlightthickness=0, relief="solid", activebackground=LIGHT,
    command=add.re_roll)

# Labels--------------------------------------------
header = Label(
    text="Vampire Masquerade Dice Roller",
    justify="center",
    bg=DARK,
    fg=LIGHT,
    font=TITLE,
)
header.grid(column=0, row=0, columnspan=4)
stats = Label(
    text="",
    font=FONT,
    bg=DARK,
    fg="white",
)

window.mainloop()
