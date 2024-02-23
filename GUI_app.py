import cv2
import tkinter as tk
from tkinter import messagebox
import PIL.Image, PIL.ImageTk


# Function to start the webcam feed
def start_webcam():
    global cap
    cap = cv2.VideoCapture(0)
    update_webcam()


# Function to update the webcam feed
def update_webcam():
    ret, frame = cap.read()
    if ret:
        # Convert the frame to RGB format
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert the RGB frame to a PIL Image
        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(rgb_frame))
        # Update the canvas with the new frame
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo  # Keep reference to prevent garbage collection
    # Schedule the next update after 10 milliseconds
    root.after(10, update_webcam)


# Function to stop the webcam feed
def stop_webcam():
    if 'cap' in globals():
        cap.release()


# Function to handle quitting the program
def confirm_quit():
    stop_webcam()
    result = messagebox.askquestion("Confirmation", "Are you sure you want to quit?")
    if result == 'yes':
        root.quit()


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


# Create the root window
root = tk.Tk()
root.title('TenseBot Control')

# Create font with a larger size
titleFont = ('Calibre Light', 20, "bold")

# Create label with larger font
titleLabel = tk.Label(root, text="User GUI", font=titleFont, bg='white')
# Insert title label
titleLabel.grid(row=0, column=0, columnspan=6, sticky='ew')

# Create LabelFrame for buttons
buttonsFrame = tk.LabelFrame(root, text="  Buttons  ", font=titleFont)
buttonsFrame.grid(row=1, column=0, ipadx=0, columnspan=3, sticky='we')


# Button functions
def button_click():
    pass


# Buttons
button_x1 = tk.Button(buttonsFrame, text="Move in 'X+' direction", padx=15, pady=10, command=button_click)
button_x2 = tk.Button(buttonsFrame, text="Move in 'X-' direction", padx=15, pady=10, command=button_click)
button_y1 = tk.Button(buttonsFrame, text="Move in 'Y+' direction", padx=15, pady=10, command=button_click)
button_y2 = tk.Button(buttonsFrame, text="Move in 'Y-' direction", padx=15, pady=10, command=button_click)
button_z1 = tk.Button(buttonsFrame, text="Move in 'Z+' direction", padx=15, pady=10, command=button_click)
button_z2 = tk.Button(buttonsFrame, text="Move in 'Z-' direction", padx=15, pady=10, command=button_click)
button_reset = tk.Button(buttonsFrame, text="Back to origin", padx=37, pady=10, command=button_click)
button_kill = tk.Button(buttonsFrame, text="Stop", padx=61, pady=10, command=button_click)
button_quit = tk.Button(buttonsFrame, text="Exit program", padx=61, pady=10, command=confirm_quit)

# Displaying buttons to screen
button_x1.grid(row=0, column=0)
button_x2.grid(row=0, column=1)
button_y1.grid(row=1, column=0)
button_y2.grid(row=1, column=1)
button_z1.grid(row=2, column=0)
button_z2.grid(row=2, column=1)
button_reset.grid(row=3, column=0, columnspan=2, sticky='we')
button_kill.grid(row=4, column=0, columnspan=2, sticky='we')
button_quit.grid(row=5, column=0, columnspan=2, sticky='we')

# Create LabelFrame for webcam
webcamFrame = tk.LabelFrame(root, text="  Webcam  ", font=titleFont)
webcamFrame.grid(row=1, column=3, ipadx=0, columnspan=2, sticky='we')

# Create canvas for webcam feed
canvas = tk.Canvas(webcamFrame, width=640, height=480)
canvas.pack()

# Start the webcam feed
start_webcam()

root.mainloop()
