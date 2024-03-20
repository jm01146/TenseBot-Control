/* This is just for testing GUI buttons wireless
communication with stepper motors. It will need
to be updated once robot computational model is 
completed */

// Include the AccelStepper Library
#include <AccelStepper.h>
#include <MultiStepper.h>
#include <SoftwareSerial.h>

//Starting the serial wireless communication
SoftwareSerial HC06(10, 11);

// Define pin connections
AccelStepper stepper1(1, 4, 5); // (Typeof driver: with 2 pins, STEP, DIR)
AccelStepper stepper2(1, 6, 7);
AccelStepper stepper3(1, 8, 9);

MultiStepper steppersControl;  // Create instance of MultiStepper

long gotoposition[3]; // An array to store the target positions for each stepper motor

/* #define conversion for steps to string length in mm here? */

void setup() {

  //Opening the communication channle
  HC06.begin(9600);

	// initial speed and the target position
	stepper1.setMaxSpeed(500); // Set maximum speed value for the stepper
  stepper2.setMaxSpeed(500);
  stepper3.setMaxSpeed(500);

  // Adding the 3 steppers to the steppersControl instance for multi stepper control
  steppersControl.addStepper(stepper1);
  steppersControl.addStepper(stepper2);
  steppersControl.addStepper(stepper3);
}

void loop() {
  if(HC06.available() > 0){
    char receive = HC06.read();
    if(receive == 'U'){ //Up
      gotoposition[0] = 300;
      gotoposition[1] = 300;
      gotoposition[2] = 0;
    }
    else if(receive == 'D'){ //Down
      gotoposition[0] = -300;
      gotoposition[1] = -300;
      gotoposition[2] = 0;
    }
    else if(receive == 'L'){ //Left
      gotoposition[0] = -300;
      gotoposition[1] = 300;
      gotoposition[2] = -300;
    }
    else if(receive == 'R'){ //Right
      gotoposition[0] = 300;
      gotoposition[1] = -300;
      gotoposition[2] = 300;
    }
    else if(receive == 'H'){
      gotoposition[0] = 0;
      gotoposition[1] = 0;
      gotoposition[2] = 0;
    }
    steppersControl.moveTo(gotoposition);
  }
  steppersControl.runSpeedToPosition();
}
