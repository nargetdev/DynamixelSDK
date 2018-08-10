from dynamixel_sdk import *


BAUDRATE                = 1000000             # Dynamixel default baudrate : 57600
DEVICENAME              = '/dev/ttyACM1'    # Check which port is being used on your controller
# Protocol version
PROTOCOL_VERSION        = 1.0               # See which protocol version is used in the Dynamixel
PING_RANGE = 8

# Control table addresses
ADDR_MX_TORQUE_ENABLE      = 64               # Control table address is different in Dynamixel model
ADDR_MX_GOAL_POSITION      = 116
ADDR_MX_PRESENT_POSITION   = 132
TORQUE_ENABLE               = 1                 # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque

CCW_ANGlE_LIMIT_L  = [6, 0]  # setting both of these
CCW_ANGlE_LIMIT_H  = [7, 0]  # setting both of these
CC_ANGlE_LIMIT_L  = [8, 0]  # to zero enables wheel mode
CC_ANGlE_LIMIT_H  = [9, 0]  # to zero enables wheel mode
SET_WHEEL_INSTRUCTIONS = [CCW_ANGlE_LIMIT_L, CC_ANGlE_LIMIT_L, CCW_ANGlE_LIMIT_H, CC_ANGlE_LIMIT_H]

class LXMoCo ():

    motors = {}
    portHandler = None
    packetHandler = None

    def __init__(self):

        print("initialized LXMoCo")

        # Initialize PortHandler instance
        # Set the port path
        # Get methods and members of PortHandlerLinux or PortHandlerWindows
        self.portHandler = PortHandler(DEVICENAME)

        # Initialize PacketHandler instance
        # Set the protocol version
        # Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
        self.packetHandler = PacketHandler(PROTOCOL_VERSION)

        # Open port
        if self.portHandler.openPort():
            print("Succeeded to open the port")
        else:
            print("Failed to open the port")
            print("Press any key to terminate...")
            getch()
            quit()

        # Set port baudrate
        if self.portHandler.setBaudRate(BAUDRATE):
            print("Succeeded to change the baudrate")
        else:
            print("Failed to change the baudrate")
            print("Press any key to terminate...")
            getch()
            quit()

    def __del__(self):
        self.portHandler.closePort()
        print(120, 'LXMoco has died')


    def network_discovery(self):
        print("discover")
        for DXL_ID in range(1,PING_RANGE):
            dxl_model_number, dxl_comm_result, dxl_error = self.packetHandler.ping(self.portHandler, DXL_ID)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % self.packetHandler.getRxPacketError(dxl_error))
            else:
                print("[ID:%03d] ping Succeeded. Dynamixel model number : %d" % (DXL_ID, dxl_model_number))
                self.motors[DXL_ID] = dxl_model_number
        print(self.motors)

    def command_wheel_mode(self, DXL_ID):
        print("configuring our motor to wheel mode")
        dxl_model_number = self.motors[DXL_ID]
        dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(self.portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
        print(dxl_comm_result)

        for instruction in SET_WHEEL_INSTRUCTIONS:
            dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(self.portHandler, DXL_ID, instruction[0], instruction[0])
            print(dxl_comm_result)


    def control_motor(self):
        print("discover")
        for DXL_ID in range(1,PING_RANGE):
            dxl_model_number, dxl_comm_result, dxl_error = self.packetHandler.ping(self.portHandler, DXL_ID)
            if dxl_comm_result != COMM_SUCCESS:
                print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % self.packetHandler.getRxPacketError(dxl_error))
            else:
                print("[ID:%03d] ping Succeeded. Dynamixel model number : %d" % (DXL_ID, dxl_model_number))
                self.motors[DXL_ID] = dxl_model_number
        print(self.motors)

    def keyboard_interface(self, DXL_ID):
        ADDR_MOVING_SPEED_L = 32
        ADDR_MOVING_SPEED_H = 33
        dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(self.portHandler, DXL_ID, ADDR_MOVING_SPEED_L, 100)
        dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(self.portHandler, DXL_ID, ADDR_MOVING_SPEED_H, 0)
        time.sleep(0.4)
        dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(self.portHandler, DXL_ID, ADDR_MOVING_SPEED_L, 0)
        dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(self.portHandler, DXL_ID, ADDR_MOVING_SPEED_L, 0)

