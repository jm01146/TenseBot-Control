//Importing Libraries
#include <AccelStepper.h>
#include <MultiStepper.h>
#include <SoftwareSerial.h>

//Conenction to the Bluetooth Module HC-06
SoftwareSerial HC06(10, 11);

// (Type of driver: with 2 pins, STEP, DIR)
AccelStepper stepper1(1, 4, 5);
AccelStepper stepper2(1, 6, 7);
AccelStepper stepper3(1, 8, 9);

MultiStepper steppersControl;

// Setting 3 motor posistions to modify
long gotoposition[3];

// Creating limits for the robot to operate
const int MIN = 0;
const int MAX_LIMIT = 650;

void setup() {
  // Set communications for possible HC06 or Serial
  HC06.begin(9600);
  Serial.begin(9600);

  // Setting the max speed for the motors
  stepper1.setMaxSpeed(200);
  stepper2.setMaxSpeed(200);
  stepper3.setMaxSpeed(200);

  // Creating the family to move unianimously
  steppersControl.addStepper(stepper1);
  steppersControl.addStepper(stepper2);
  steppersControl.addStepper(stepper3);
}

void loop() {
  if (HC06.available()) {
    String data = HC06.readStringUntil('\n');
    
    // If the received data length is 1, it's a command
    if (data.length() == 1) {
      char command = data[0];
      adjustPosition(command);
    } 
    else {
      int x = 0, y = 0;
      sscanf(data.c_str(), "%d,%d", &x, &y);
      adjustPosition(x, y);
    }
    steppersControl.moveTo(gotoposition);
  }
  steppersControl.runSpeedToPosition();
}

// Creating function to move via character command
void adjustPosition(char command) {
  switch(command) {
    // Foward command
    case 'F':
      gotoposition[0] = 0;
      gotoposition[1] = 250;
      gotoposition[2] = 150;
      break;
    // Backward command
    case 'B':
      gotoposition[0] = 200;
      gotoposition[1] = 0;
      gotoposition[2] = 0;
      break;
    // Left command
    case 'L':
      gotoposition[0] = 100;
      gotoposition[1] = 200;
      gotoposition[2] = 0;
      break;
    // Right command
    case 'R':
      gotoposition[0] = 100;
      gotoposition[1] = 0;
      gotoposition[2] = 250;
      break;
    // Home command
    case 'H':
      gotoposition[0] = 0;
      gotoposition[1] = 0;
      gotoposition[2] = 0;
      break;
    default:
      break;
  }
}

// Fucntion to move via XY coordinates with color detection code
void adjustPosition(int x, int y) {
  if (x > 320 && y > 240) {
    gotoposition[0] = 0;
    gotoposition[1] = constrain(gotoposition[1] + (y - 240), MIN, MAX_LIMIT);
    gotoposition[2] = constrain(gotoposition[2] + (x - 320), MIN, MAX_LIMIT);
  } else if (x > 320 && y < 240) {
    gotoposition[0] = constrain(gotoposition[0] + (240 - y), MIN, MAX_LIMIT);
    gotoposition[1] = 0;
    gotoposition[2] = constrain(gotoposition[2] + (x - 320), MIN, MAX_LIMIT);
  } else if (x < 320 && y > 240) {
    gotoposition[0] = 0;
    gotoposition[1] = constrain(gotoposition[1] + (320 - x), MIN, MAX_LIMIT);
    gotoposition[2] = constrain(gotoposition[2] + (y - 240), MIN, MAX_LIMIT);
  } else if (x < 320 && y < 240) {
    gotoposition[0] = constrain(gotoposition[0] + (240 - y), MIN, MAX_LIMIT);
    gotoposition[1] = constrain(gotoposition[1] + (320 - x), MIN, MAX_LIMIT);
    gotoposition[2] = 0;
  } else {
    gotoposition[0] = 0;
    gotoposition[1] = 0;
    gotoposition[2] = 0;
  }
}
