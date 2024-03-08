from tkinter import *
from tkinter import messagebox
import customtkinter as ctk


# button click function
def button_click():
    return


def right_click():
    GUI = ctk.CTk()
    my_label = Label(GUI, text='Right click')
    my_label.grid(row=1, column=2, padx=20, pady=10)
    print('right')


def left_click():
    GUI = ctk.CTk()
    my_label = Label(GUI, text='left click')
    my_label.grid(row=1, column=0)
    print('left')


def up_click():
    GUI = ctk.CTk()
    my_label = Label(GUI, text='up click')
    my_label.grid(row=0, column=1)
    print('up')


def down_click():
    GUI = ctk.CTk()
    my_label = Label(GUI, text='down click')
    my_label.grid(row=2, column=1)
    print('down')


def confirm_quit():
    GUI = ctk.CTk()
    result = messagebox.askquestion("Confirmation", "Are you sure you want to quit?")
    if result == 'yes':
        GUI.quit()
