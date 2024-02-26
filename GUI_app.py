from tkinter import *
from tkinter import messagebox
import GUI_Functions as myGUI
import customtkinter as ctk
from PIL import Image, ImageTk
import cv2
import numpy as np

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
GUI = ctk.CTk()
GUI.title('TenseBot Control')
GUI.geometry('800x500')
GUI.minsize(825, 475)
GUI.maxsize(900, 475)

# Add an icon
GUI.iconbitmap('C:/Users/Nari/PycharmProjects/GUI_Functions/icons/robot.ico')

# Button Images
rightButton = Image.open('C:/Users/Nari/PycharmProjects/GUI_Functions/icons/right.png').resize((40, 40), Image.BOX)
leftButton = Image.open('C:/Users/Nari/PycharmProjects/GUI_Functions/icons/left.png').resize((40, 40), Image.BOX)
yUpButton = Image.open('C:/Users/Nari/PycharmProjects/GUI_Functions/icons/y_up.png').resize((40, 40), Image.BOX)
yDownButton = Image.open('C:/Users/Nari/PycharmProjects/GUI_Functions/icons/y_down.png').resize((40, 40), Image.BOX)
zUpButton = Image.open('C:/Users/Nari/PycharmProjects/GUI_Functions/icons/z_up.png').resize((40, 40), Image.BOX)
zDownButton = Image.open('C:/Users/Nari/PycharmProjects/GUI_Functions/icons/z_down.png').resize((40, 40), Image.BOX)
homeButton = Image.open('C:/Users/Nari/PycharmProjects/GUI_Functions/icons/home.png').resize((40, 40), Image.BOX)
stopButton = Image.open('C:/Users/Nari/PycharmProjects/GUI_Functions/icons/stop.png').resize((40, 40), Image.BOX)
pauseButton = Image.open('C:/Users/Nari/PycharmProjects/GUI_Functions/icons/pause.png').resize((40, 40), Image.BOX)
recordButton = Image.open('C:/Users/Nari/PycharmProjects/GUI_Functions/icons/record.png').resize((500, 500), Image.BOX)
stopRecButton = Image.open('C:/Users/Nari/PycharmProjects/GUI_Functions/icons/stop_rec.png').resize((500, 500),
                                                                                                    Image.BOX)

# Convert images to CTkImage objects
rightButton_ctk = ctk.CTkImage(rightButton)
leftButton_ctk = ctk.CTkImage(leftButton)
yUpButton_ctk = ctk.CTkImage(yUpButton)
yDownButton_ctk = ctk.CTkImage(yDownButton)
zUpButton_ctk = ctk.CTkImage(zUpButton)
zDownButton_ctk = ctk.CTkImage(zDownButton)
homeButton_ctk = ctk.CTkImage(homeButton)
stopButton_ctk = ctk.CTkImage(stopButton)
pauseButton_ctk = ctk.CTkImage(pauseButton)
recordButton_ctk = ctk.CTkImage(recordButton)
stopRecButton_ctk = ctk.CTkImage(stopRecButton)


# Main frame
mainFrame = ctk.CTkFrame(master=GUI)
mainFrame.pack(side='top', expand=True, fill='x')
statusFrame = ctk.CTkFrame(master=GUI)
statusFrame.pack(side='bottom', expand=True, fill='x')


# Buttons frame
buttonsFrame = ctk.CTkFrame(master=mainFrame,
                            fg_color="#E3F4FF",
                            border_width=5,
                            border_color="#C2C5D6")
buttonsFrame.grid_columnconfigure((0, 1, 2, 3, 4), weight=0)
buttonsFrame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=0)

# buttonsFrame.grid(row=0, column=0, sticky="nsew")
buttonsFrame.pack(side='left', expand=True, fill='both')

leftMargin = ctk.CTkLabel(buttonsFrame, text="", width=10)
rightMargin = ctk.CTkLabel(buttonsFrame, text="", width=10)
topMargin = ctk.CTkLabel(buttonsFrame, text="", height=1)
bottomMargin = ctk.CTkLabel(buttonsFrame, text="", width=1)

# Buttons
hoverB = "#f9b613"
rightButton = ctk.CTkButton(buttonsFrame, image=rightButton_ctk, text="Right", font=("New Frank Bold Italic", 15),
                            hover_color=hoverB, width=50, height=40, compound="top", text_color="black",
                            border_color="black", border_width=2, border_spacing=1, corner_radius=25,
                            command=myGUI.right_click)

leftButton = ctk.CTkButton(buttonsFrame, image=leftButton_ctk, text="Left", font=("New Frank Bold", 15),
                           hover_color=hoverB, width=50, height=40, compound="top", text_color="black",
                           border_color="black", border_width=2, border_spacing=1, corner_radius=25,
                           command=myGUI.left_click)

yUpButton = ctk.CTkButton(buttonsFrame, image=yUpButton_ctk, text="Up", font=("New Frank Bold", 15),
                          hover_color=hoverB, width=50, height=40, compound="top", text_color="black",
                          border_color="black", border_width=2, border_spacing=1, corner_radius=30,
                          command=myGUI.right_click)

yDownButton = ctk.CTkButton(buttonsFrame, image=yDownButton_ctk, text="Down", font=("New Frank Bold", 15),
                            hover_color=hoverB, width=50, height=40, compound="top", text_color="black",
                            border_color="black", border_width=2, border_spacing=1, corner_radius=25,
                            command=myGUI.right_click)

zUpButton = ctk.CTkButton(buttonsFrame, image=zUpButton_ctk, text="Zoom In", font=("New Frank Bold", 15),
                          hover_color=hoverB, width=50, height=40, compound="top", text_color="black",
                          border_color="black", border_width=2, border_spacing=1, corner_radius=25,
                          command=myGUI.right_click)

zDownButton = ctk.CTkButton(buttonsFrame, image=zDownButton_ctk, text="Zoom Out", font=("New Frank Bold", 15),
                            hover_color=hoverB, width=50, height=40, compound="top", text_color="black",
                            border_color="black", border_width=2, border_spacing=1, corner_radius=25,
                            command=myGUI.right_click)

homeButton = ctk.CTkButton(buttonsFrame, image=homeButton_ctk, text="Home\n(Back to Origin)",
                           font=("New Frank Bold", 15),
                           hover_color=hoverB, width=50, height=40, compound="top", text_color="black",
                           border_color="black", border_width=2, border_spacing=1, corner_radius=25,
                           command=myGUI.right_click)

stopButton = ctk.CTkButton(buttonsFrame, image=stopButton_ctk, text="Stop", font=("Consolas", 15),
                           hover_color=hoverB, width=50, height=40, compound="top", text_color="black",
                           border_color="black", border_width=2, border_spacing=1, corner_radius=25,
                           command=myGUI.right_click)

pauseButton = ctk.CTkButton(buttonsFrame, image=pauseButton_ctk, text="Pause", font=("Consolas", 15),
                            hover_color=hoverB, width=50, height=40, compound="top", text_color="black",
                            border_color="black", border_width=2, border_spacing=1, corner_radius=25,
                            command=myGUI.right_click)

# Adding buttons to the frame
leftMargin.grid(column=0, padx=5, pady=5)
rightMargin.grid(column=4, padx=5, pady=5)
topMargin.grid(row=0, pady=5)
bottomMargin.grid(row=7, padx=5, pady=5)

rightButton.grid(row=2, column=3)
leftButton.grid(row=2, column=1)
yUpButton.grid(row=1, column=2)
yDownButton.grid(row=3, column=2)
zUpButton.grid(row=5, column=1)
zDownButton.grid(row=5, column=3)
homeButton.grid(row=6, column=2, pady=50)
# stopButton.grid(row=6, column=0, pady=50, ipady=5)
# pauseButton.grid(row=6, column=2, pady=50, ipady=5)

# Secondary frame
secFrame = ctk.CTkFrame(master=mainFrame,
                        fg_color="white",
                        border_width=5,
                        border_color="#C2C5D6")
secFrame.pack(side='right', expand=True, fill='both')


# Function to handle webcam related stuff
def webcam_functions(root, canvas):
    global camera_paused
    camera_paused = True

    # Function to start webcam feed
    def start_webcam():
        global cap
        if camera_paused:  # Check if the camera is paused before starting
            cap = cv2.VideoCapture(0)
            update_webcam()

    # Function to update webcam feed
    def update_webcam():
        green_lower = np.array([50, 100, 50], dtype=np.uint8)  # Lower limit for red hue  WORKS
        green_upper = np.array([100, 255, 255], dtype=np.uint8)
        kernel = np.ones((25, 25), np.uint8)
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, green_lower, green_upper)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask_contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        results = frame.copy()  # Make a copy of the original frame
        results = cv2.drawContours(results, mask_contours, -1, (0, 0, 255),
                                   3)
        if ret:
            # Draw contours on the original frame

            # cv2.imshow('Results', results)

            # Convert the frame to RGB format
            rgb_frame = cv2.cvtColor(results, cv2.COLOR_BGR2RGB)
            # Convert the RGB frame to a PIL Image
            photo = ImageTk.PhotoImage(image=Image.fromarray(rgb_frame))
            # Update the canvas with the new frame
            canvas.create_image(0, 0, anchor=ctk.NW, image=photo)
            canvas.image = photo  # Keep reference to prevent garbage collection
        # Schedule the next update after 5 milliseconds
        GUI.after(5, update_webcam)

    # Function to stop the webcam feed
    def stop_webcam():
        if 'cap' in globals():
            cap.release()

    # Start the webcam feed
    start_webcam()

    # Function to handle stopping the webcam feed
    def stop_camera():
        global camera_paused
        if not camera_paused:
            stop_webcam()
            camera_paused = True

    # Function to handle resuming the webcam feed
    def continue_camera():
        global camera_paused
        if camera_paused:
            start_webcam()
            camera_paused = False

    # Function to handle quitting the program
    def confirm_quit():
        stop_webcam()
        result = messagebox.askquestion("Confirmation", "Are you sure you want to quit?")
        if result == 'yes':
            GUI.quit()

    # Return the functions to be used outside this module
    return start_webcam, stop_camera, confirm_quit


# Camera feed
feed_canvas = Canvas(secFrame, width=640, height=480)
feed_canvas.grid(row=0, column=0, padx=10, pady=10)
#feed_canvas.pack(pady=10, padx=5)

start_webcam, stop_camera, confirm_quit = webcam_functions(GUI, feed_canvas)

# recordButton = ctk.CTkButton(buttonsFrame, image=recordButton_ctk, text="Start camera", font=("Consolas", 15),
#                              hover_color="#9EF296", width=50, height=40, compound="top", text_color="black",
#                              border_color="black", border_width=2, border_spacing=1, corner_radius=25,
#                              command=start_webcam)
#
# stopRecButton = ctk.CTkButton(buttonsFrame, image=recordButton_ctk, text="Stop camera", font=("Consolas", 15),
#                               hover_color="#9EF296", width=50, height=40, compound="top", text_color="black",
#                               border_color="black", border_width=2, border_spacing=1, corner_radius=25,
#                               command=stop_camera)
# recordButton.grid(row=7, column=1, pady=50, ipady=5)
# stopRecButton.grid(row=7, column=2, pady=50, ipady=5)


# Add status bar
status = Label(statusFrame, text="FIU - School of Engineering and Computing",
               bd=1, relief='sunken', anchor=W, font=('Tahoma', 15))
# status.grid(row=3, columnspan=2,
#             sticky="ew")  # Place the status bar in row 2 and span it across both columns, fill it horizontally
status.pack(side='bottom', expand=True, anchor='s', fill='x')

# func.configure_grid()

GUI.mainloop()
