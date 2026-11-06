import wpilib
import phoenix5
from wpilib import drive


class MyRobot(wpilib.TimedRobot):
    # def __init__(self):

    def robotInit(self):
        self.controller = wpilib.XboxController(0)

        self.myMotor = phoenix5.TalonSRX(28)

        self.myMotor1 = phoenix5.TalonSRX(24)

        self.myMotor2 = phoenix5.TalonSRX(6)

        self.myMotor3 = phoenix5.VictorSPX(26)

    def teleopPeriodic(self):
        input_x = self.controller.getLeftY()

        #Moves robot fwd and back
        self.myMotor.set(phoenix5.ControlMode.PercentOutput, input_x)
        self.myMotor1.set(phoenix5.ControlMode.PercentOutput, -input_x)
        self.myMotor2.set(phoenix5.ControlMode.PercentOutput, input_x)
        self.myMotor3.set(phoenix5.ControlMode.PercentOutput, -input_x)

        #input1 = self.controller.getLeftY()
        #self.myMotor.set(phoenix5.ControlMode.PercentOutput, input1)
        #self.myMotor1.set(phoenix5.ControlMode.PercentOutput, input1)
        #self.myMotor2.set(phoenix5.ControlMode.PercentOutput, input1)
        #self.myMotor3.set(phoenix5.ControlMode.PercentOutput, input1)

        #if self.controller.getRightX() > -1 and self.controller.getRightX() < 0:
        input_y = self.controller.getRightX()
        self.myMotor1.set(phoenix5.ControlMode.PercentOutput, input_y)
        self.myMotor3.set(phoenix5.ControlMode.PercentOutput, input_y)
        self.myMotor.set(phoenix5.ControlMode.PercentOutput, input_y)
        self.myMotor2.set(phoenix5.ControlMode.PercentOutput, input_y)
        #elif self.controller.getRightX() < 1 and self.controller.getRightX() > 0:
            #self.myMotor.set(phoenix5.ControlMode.PercentOutput, -input_x)
            #self.myMotor2.set(phoenix5.ControlMode.PercentOutput, -input_x)
        #else:
            #return