import customtkinter
from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("TenseBot Control")
        self.geometry('800x500')
        self.minsize(825, 475)
        self.maxsize(900, 475)
        self.mainFrame = customtkinter.CTkFrame(self)
        self.mainFrame.pack(side='top', expand=True, fill='x')
        self.statusFrame = customtkinter.CTkFrame(self)
        self.statusFrame.pack(side='bottom', expand=True, fill='x')
        self.buttonsFrame = customtkinter.CTkFrame(master=self.mainFrame,
                                                   fg_color="#E3F4FF",
                                                   border_width=5,
                                                   border_color="#C2C5D6")
        self.buttonsFrame.grid_columnconfigure((0, 1, 2, 3, 4), weight=0)
        self.buttonsFrame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=0)
        self.buttonsFrame.pack(side='left', expand=True, fill='both')
        self.secFrame = customtkinter.CTkFrame(master=self.mainFrame,
                                               fg_color="white",
                                               border_width=5,
                                               border_color="#C2C5D6")
        self.secFrame.pack(side='right', expand=True, fill='both')
        self.feed_canvas = Canvas(self.secFrame, width=640, height=480)
        self.feed_canvas.grid(row=0, column=0, padx=10, pady=10)

        self.camera_label = customtkinter.CTkLabel(self.feed_canvas, text='')
        self.camera_label.pack()
        self.show_color_detection = False
        self.cap = cv2.VideoCapture(0)
        self.green_lower = np.array([50, 100, 50], dtype=np.uint8)  # Lower limit for red hue  WORKS
        self.green_upper = np.array([100, 255, 255], dtype=np.uint8)
        self.kernel = np.ones((25, 25), np.uint8)
        self.update_frame()

        self.status = Label(self.statusFrame, text="FIU - School of Engineering and Computing",
                            bd=1, relief='sunken', anchor=W, font=('Tahoma', 15))
        self.status.pack(side='bottom', expand=True, anchor='s', fill='x')

        self.iconbitmap('robot.ico')
        self.rightButton = Image.open('right.png').resize((40, 40), Image.BOX)
        self.leftButton = Image.open('left.png').resize((40, 40), Image.BOX)
        self.yUpButton = Image.open('y_up.png').resize((40, 40), Image.BOX)
        self.yDownButton = Image.open('y_down.png').resize((40, 40), Image.BOX)
        self.startAuto = Image.open('record.png').resize((40, 40), Image.BOX)
        self.stopAuto = Image.open('stop.png').resize((40, 40), Image.BOX)
        self.homeButton = Image.open('home.png').resize((40, 40), Image.BOX)

        self.rightButton_ctk = customtkinter.CTkImage(self.rightButton)
        self.leftButton_ctk = customtkinter.CTkImage(self.leftButton)
        self.yUpButton_ctk = customtkinter.CTkImage(self.yUpButton)
        self.yDownButton_ctk = customtkinter.CTkImage(self.yDownButton)
        self.startAuto_ctk = customtkinter.CTkImage(self.StartAuto)
        self.stopAuto_ctk = customtkinter.CTkImage(self.StopAuto)
        self.homeButton_ctk = customtkinter.CTkImage(self.homeButton)

        self.leftMargin = customtkinter.CTkLabel(self.buttonsFrame, text="", width=10)
        self.rightMargin = customtkinter.CTkLabel(self.buttonsFrame, text="", width=10)
        self.topMargin = customtkinter.CTkLabel(self.buttonsFrame, text="", height=1)
        self.bottomMargin = customtkinter.CTkLabel(self.buttonsFrame, text="", width=1)

        self.hoverB = "#f9b613"
        self.rightButton = customtkinter.CTkButton(self.buttonsFrame, image=self.rightButton_ctk, text="Right",
                                                   font=("New Frank Bold Italic", 15),
                                                   hover_color=self.hoverB, width=50, height=40, compound="top",
                                                   text_color="black",
                                                   border_color="black", border_width=2, border_spacing=1,
                                                   corner_radius=25,
                                                   command=self.right_click)

        self.leftButton = customtkinter.CTkButton(self.buttonsFrame, image=self.leftButton_ctk, text="Left",
                                                  font=("New Frank Bold", 15),
                                                  hover_color=self.hoverB, width=50, height=40, compound="top",
                                                  text_color="black",
                                                  border_color="black", border_width=2, border_spacing=1,
                                                  corner_radius=25,
                                                  command=self.left_click)

        self.yUpButton = customtkinter.CTkButton(self.buttonsFrame, image=self.yUpButton_ctk, text="Up",
                                                 font=("New Frank Bold", 15),
                                                 hover_color=self.hoverB, width=50, height=40, compound="top",
                                                 text_color="black",
                                                 border_color="black", border_width=2, border_spacing=1,
                                                 corner_radius=30,
                                                 command=self.up_click)

        self.yDownButton = customtkinter.CTkButton(self.buttonsFrame, image=self.yDownButton_ctk, text="Down",
                                                   font=("New Frank Bold", 15),
                                                   hover_color=self.hoverB, width=50, height=40, compound="top",
                                                   text_color="black",
                                                   border_color="black", border_width=2, border_spacing=1,
                                                   corner_radius=25,
                                                   command=self.down_click)

        self.startAuto = customtkinter.CTkButton(self.buttonsFrame, image=self.StartAuto_ctk, text="Start Auto Control",
                                                 font=("New Frank Bold", 15),
                                                 hover_color=self.hoverB, width=50, height=40, compound="top",
                                                 text_color="black",
                                                 border_color="black", border_width=2, border_spacing=1,
                                                 corner_radius=25,
                                                 command=self.startauto_click)

        self.stopAuto = customtkinter.CTkButton(self.buttonsFrame, image=self.StopAuto_ctk, text="Start Manual Control",
                                                font=("New Frank Bold", 15),
                                                hover_color=self.hoverB, width=50, height=40, compound="top",
                                                text_color="black",
                                                border_color="black", border_width=2, border_spacing=1,
                                                corner_radius=25,
                                                command=self.stopauto_click)

        self.homeButton = customtkinter.CTkButton(self.buttonsFrame, image=self.homeButton_ctk,
                                                  text="Home\n(Back to Origin)",
                                                  font=("New Frank Bold", 15),
                                                  hover_color=self.hoverB, width=50, height=40, compound="top",
                                                  text_color="black",
                                                  border_color="black", border_width=2, border_spacing=1,
                                                  corner_radius=25,
                                                  command=self.home_click)

        self.leftMargin.grid(column=0, padx=5, pady=5)
        self.rightMargin.grid(column=4, padx=5, pady=5)
        self.topMargin.grid(row=0, pady=5)
        self.bottomMargin.grid(row=7, padx=5, pady=5)

        self.rightButton.grid(row=2, column=3)
        self.leftButton.grid(row=2, column=1)
        self.yUpButton.grid(row=1, column=2)
        self.yDownButton.grid(row=3, column=2)
        self.startAuto.grid(row=5, column=1)
        self.stopAuto.grid(row=5, column=3)
        self.homeButton.grid(row=6, column=2, pady=50)

    def right_click(self):
        print('right')

    def left_click(self):
        print('left')

    def up_click(self):
        print('up')

    def down_click(self):
        print('down')

    def startauto_click(self):
        self.show_color_detection = True

    def stopauto_click(self):
        self.show_color_detection = False

    def home_click(self):
        print('homing')

    # def confirm_quit(self):
    #     result = self.messagebox.askquestion("Confirmation", "Are you sure you want to quit?")
    #     if result == 'yes':
    #         GUI.quit()

    def update_frame(self):
        ret, frame = self.cap.read()
        if self.show_color_detection:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self.green_lower, self.green_upper)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, self.kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, self.kernel)
            mask_contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            results = frame.copy()
            results = cv2.drawContours(results, mask_contours, -1, (0, 0, 255), 3)
            if ret:
                cv_image = cv2.cvtColor(results, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(cv_image)
                tk_image = ImageTk.PhotoImage(image=pil_image)

                # Update the label with the new image
                self.camera_label.configure(image=tk_image)
                self.camera_label.image = tk_image

                # Call this method again after 10ms
                self.after(10, self.update_frame)

        if ret and not self.show_color_detection:
            # Convert the image to RGB (OpenCV uses BGR)
            cv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(cv_image)
            tk_image = ImageTk.PhotoImage(image=pil_image)

            # Update the label with the new image
            self.camera_label.configure(image=tk_image)
            self.camera_label.image = tk_image

            # Call this method again after 10ms
            self.after(10, self.update_frame)
