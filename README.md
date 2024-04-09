# TenseBot-Control
FIU EE Senior Design Project for Team 13 Spring 2024

Team Members:
* Dr.Pozdin (Mentor) email: vpozdin@fiu.edu
* John Marcial (Team Leader) email: jmarc114@fiu.edu
* Jorge Habib (Team Member) email: jhabi006@fiu.edu
* Daniel Rodriguez (Team Member) email: jrodr1405@fiu.edu
* Vivish Gieowar-Singh (Team Member) email: vgieo001@fiu.edu
* Carlos Sanabria (Team Member) email: csana011@fiu.edu

These are the components we used for the robot we created: HC-06 Bluetooth Module, Aa4988 motor driver, Pololu 12V, 2.2A Step-Down Voltage Regulator D24V22F12, and Stepper NEMA 17 motors
![circuit](https://github.com/jm01146/TenseBot-Control/assets/59844100/98bbffdd-5261-472a-81bf-2402b0952ccd)

The main python code need to activate the control software is TenseBotApp.py the other python files are utilzed as the backend processes of the control software.
The ino file is for the arduino you plan to use and you can modify the steps it takes but the logic is uses should remain untouched unless you modified the amount of motors in use.

For using the device this link shows the usage cases for this control software. https://www.youtube.com/watch?v=2kFFXKGkytE

However not in the video was how the color detection works. 
You can choose what color you want to detect and the robot will respond accordingly.
*We have not added this part as of yet but by the end of the semster we will have this done*
This is out figure to showcase the color option.
![image](https://github.com/jm01146/TenseBot-Control/assets/59844100/62d63483-08e5-4c6b-9273-7d36b83ae6b9)

Last but not least. We created a shield to reduce the amount of wiring needed for the project. This allows the entire series of components to be on one platform and easily replaceable if broken.
![image](https://github.com/jm01146/TenseBot-Control/assets/59844100/f1daa60e-cbbf-4800-a897-1da333bf714e)

In case there becomes a need to make more here is the entire Gerber file to make them and modify if you need.
We are also adding the mounting plate to hold the nema 17 motors and arduino.
