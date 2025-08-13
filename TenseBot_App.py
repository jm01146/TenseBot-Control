# Importing Libraries
from commsArduino import Ports
from ColorSetting import Color
import customtkinter
from CTkMenuBar import *
from tkinter import *
from PIL import Image, ImageTk  
import numpy as np
import cv2


# Setting the appearance for the GUI
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


# Setting the buttons, process, and features of the GUI
class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Creating the frames for the GUI to place the buttons and features
        self.menu_bar = None
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

        # Processes for the color detection
        self.camera_label = customtkinter.CTkLabel(self.feed_canvas, text='')
        self.camera_label.pack()
        self.color_list = ['Red', 'Blue', 'Green', 'Yellow']
        self.cap = cv2.VideoCapture(0)
        self.green_lower = np.array([50, 100, 50], dtype=np.uint8)  # Lower limit for red hue  WORKS
        self.green_upper = np.array([100, 255, 255], dtype=np.uint8)
        self.setColor = None
        self.kernel = np.ones((25, 25), np.uint8)
        self.show_color_detection = False
        self.color = Color()
        self.update_frame()

        self.status = Label(self.statusFrame, text="FIU - School of Engineering and Computing",
                            bd=1, relief='sunken', anchor=W, font=('Tahoma', 15))
        self.status.pack(side='bottom', expand=True, anchor='s', fill='x')

        # Processes for the ports connection
        self.port_selector = Ports()
        self.printing_port = self.port_selector.list_port()
        self.baudrate = ['9600', '57600', '115200']
        self.setBaudrate = None
        self.setPort = None

        # Creating the menu and options
        self.menu = CTkTitleMenu(self, padx=10, x_offset=325, y_offset=12)
        self.button_1 = self.menu.add_cascade("Comports")
        self.button_2 = self.menu.add_cascade('Baudrate')
        self.button_3 = self.menu.add_cascade("Colors Detecting")
        self.button_4 = self.menu.add_cascade("Connect!")

        # Listing the possible port options on start up and readies for connection
        self.dropdown1 = CustomDropdownMenu(widget=self.button_1, padx=2, pady=5, corner_radius=5, width=100)
        for x in self.printing_port:
            self.dropdown1.add_option(option=x, command=lambda r=x: self.set_port(r))

        # Listing the possible baudrate options and readies for connection
        self.dropdown2 = CustomDropdownMenu(widget=self.button_2, padx=2, pady=5, corner_radius=5, width=50)
        for x in self.baudrate:
            self.dropdown2.add_option(option=x, command=lambda r=x: self.set_baudrate(r))

        # Listing the possible color detection options and readies for usage
        self.dropdown3 = CustomDropdownMenu(widget=self.button_3, padx=2, pady=5, corner_radius=5, width=100)
        for x in self.color_list:
            self.dropdown3.add_option(option=x, command=lambda r=x: self.set_color(r))

        # Give the option to connect or disconnect from COM device
        self.dropdown4 = CustomDropdownMenu(widget=self.button_4, padx=2, pady=5, corner_radius=5, width=100)
        self.dropdown4.add_option(option="Connect to Device", command=self.select_device)
        self.dropdown4.add_option(option="Disconnect Device", command=self.disconnect_device)

        # Set up buttons with their respective images
        self.iconbitmap('robot.ico')
        self.rightButton = Image.open('right.png').resize((40, 40), Image.BOX)
        self.leftButton = Image.open('left.png').resize((40, 40), Image.BOX)
        self.forwardButton = Image.open('y_up.png').resize((40, 40), Image.BOX)
        self.backwardButton = Image.open('y_down.png').resize((40, 40), Image.BOX)
        self.homeButton = Image.open('home.png').resize((40, 40), Image.BOX)
        self.startAuto = Image.open('record.png').resize((40, 40), Image.BOX)
        self.stopAuto = Image.open('stop.png').resize((40, 40), Image.BOX)

        # Link button as clickable image
        self.rightButton_ctk = customtkinter.CTkImage(self.rightButton)
        self.leftButton_ctk = customtkinter.CTkImage(self.leftButton)
        self.forwardButton_ctk = customtkinter.CTkImage(self.forwardButton)
        self.backwardButton_ctk = customtkinter.CTkImage(self.backwardButton)
        self.homeButton_ctk = customtkinter.CTkImage(self.homeButton)
        self.startAuto_ctk = customtkinter.CTkImage(self.startAuto)
        self.stopAuto_ctk = customtkinter.CTkImage(self.stopAuto)

        # Creating margins for stylizing
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
                                                   corner_radius=25, command=self.right_click)

        self.leftButton = customtkinter.CTkButton(self.buttonsFrame, image=self.leftButton_ctk, text="Left",
                                                  font=("New Frank Bold", 15),
                                                  hover_color=self.hoverB, width=50, height=40, compound="top",
                                                  text_color="black",
                                                  border_color="black", border_width=2, border_spacing=1,
                                                  corner_radius=25, command=self.left_click)

        self.forwardButton = customtkinter.CTkButton(self.buttonsFrame, image=self.forwardButton_ctk, text="Forward",
                                                     font=("New Frank Bold", 15),
                                                     hover_color=self.hoverB, width=50, height=40, compound="top",
                                                     text_color="black",
                                                     border_color="black", border_width=2, border_spacing=1,
                                                     corner_radius=30,
                                                     command=self.forward_click)

        self.backwardButton = customtkinter.CTkButton(self.buttonsFrame, image=self.backwardButton_ctk, text="Backward",
                                                      font=("New Frank Bold", 15),
                                                      hover_color=self.hoverB, width=50, height=40, compound="top",
                                                      text_color="black",
                                                      border_color="black", border_width=2, border_spacing=1,
                                                      corner_radius=25,
                                                      command=self.backward_click)

        self.homeButton = customtkinter.CTkButton(self.buttonsFrame, image=self.homeButton_ctk,
                                                  text="Home",
                                                  font=("New Frank Bold", 15),
                                                  hover_color=self.hoverB, width=50, height=40, compound="top",
                                                  text_color="black",
                                                  border_color="black", border_width=2, border_spacing=1,
                                                  corner_radius=25,
                                                  command=self.home)

        self.startAuto = customtkinter.CTkButton(self.buttonsFrame, image=self.startAuto_ctk, text="Start Auto Control",
                                                 font=("New Frank Bold", 15),
                                                 hover_color=self.hoverB, width=50, height=40, compound="top",
                                                 text_color="black",
                                                 border_color="black", border_width=2, border_spacing=1,
                                                 corner_radius=25,
                                                 command=self.startauto_click)

        self.stopAuto = customtkinter.CTkButton(self.buttonsFrame, image=self.stopAuto_ctk, text="Start Manual Control",
                                                font=("New Frank Bold", 15),
                                                hover_color=self.hoverB, width=50, height=40, compound="top",
                                                text_color="black",
                                                border_color="black", border_width=2, border_spacing=1,
                                                corner_radius=25,
                                                command=self.stopauto_click)

        self.leftMargin.grid(column=0, padx=5, pady=5)
        self.rightMargin.grid(column=4, padx=5, pady=5)
        self.topMargin.grid(row=0, pady=5)
        self.bottomMargin.grid(row=7, padx=5, pady=5)

        self.rightButton.grid(row=2, column=3)
        self.leftButton.grid(row=2, column=1)
        self.forwardButton.grid(row=1, column=2)
        self.backwardButton.grid(row=3, column=2)
        self.homeButton.grid(row=2, column=2, pady=25)
        self.startAuto.grid(row=5, column=1)
        self.stopAuto.grid(row=5, column=3)

    # Creating right button click function
    def right_click(self):
        self.port_selector.send('R\n')

    # Creating left button click function
    def left_click(self):
        self.port_selector.send('L\n')

    # Creating forward button click function
    def forward_click(self):
        self.port_selector.send('F\n')

    # Creating backward button click function
    def backward_click(self):
        self.port_selector.send('D\n')

    # Creating auto button click function
    def startauto_click(self):
        self.show_color_detection = True

    # Creating manual button click function
    def stopauto_click(self):
        self.show_color_detection = False

    # Creating home button click function
    def home(self):
        self.port_selector.send('H\n')

    # Processing the color option from menu
    def set_color(self, color):
        self.setColor = color
        return

    # Processing the port option from menu
    def set_port(self, port):
        self.setPort = port
        self.port_selector.comm_selection(port)
        return

    # Processing the baudrate option from menu
    def set_baudrate(self, rate):
        self.setBaudrate = int(rate)
        self.port_selector.baudrate_selection(rate)
        return

    # Function to connect to device
    def select_device(self):
        self.port_selector.connect()

    # Function to disconnect to device
    def disconnect_device(self):
        self.port_selector.disconnect()

    # Creating the color detection function
    def update_frame(self):
        ret, frame = self.cap.read()
        if self.show_color_detection:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = self.color.color_detect(self.setColor, hsv)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, self.kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, self.kernel)
            mask_contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if len(mask_contours) != 0:
                for mask_contours in mask_contours:
                    if cv2.contourArea(mask_contours) > 500:
                        x, y, w, h = cv2.boundingRect(mask_contours)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        coordinates = f"{x},{y}\n"
                        self.port_selector.send(coordinates)
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
