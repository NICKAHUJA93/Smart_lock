#Important Links
#//  //Autor Nipun Ahuja a free Lancer from Delhi
# https://tutorials-raspberrypi.com/connecz-raspberry-pi-kecpad-code-lock/
import socket
import time
import datetime
#import pandas as pd

import RPi.GPIO as GPIO
import requests
from keypad import keypad
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
# selection of pin 3 as GPIO2
#Motor should be connected to GPIO PIN 2 or physical pin 3
GPIO_MOTOR_PIN = 3
GPIO.setup(GPIO_MOTOR_PIN,GPIO.OUT)
def motor_on():
    GPIO.output(GPIO_MOTOR_PIN,GPIO.HIGH)
    time.sleep(1)

def motor_off():
    GPIO.output(GPIO_MOTOR_PIN,GPIO.LOW)
    time.sleep(1)

def convert(list):
        # Converting integer list to string list
        s = [str(i) for i in list]
        # Join list items using join()
        res = int("".join(s))
        print(res)
        return (res)
def KEY_PAD_INPUT():
        print("Please enter keypad input data")
        kp = keypad(columnCount=3)
        # waiting for a keypress
        digit = None
        while digit == None:
            digit = kp.getKey()
        # Print result
        print(digit)
        time.sleep(0.5)
        ###### 6 Digit wait ######
        seq = []
        for i in range(6):
            digit = None
            while digit == None:
                digit = kp.getKey()
                #print(digit)
                #This will append the digit in the list
            seq.append(digit)
            #Time interval between consecutive key press
            time.sleep(0.4)
        # Check digit code
        # The sequence will be stored in form of list ,now it's time to convert into integer
        data1=convert(seq)
        print(data1)
        return data1
old_otp = 777777

while True:
    print("top");
    token_data= requests.get("https://oauth.livwize.com/lockDevice/lockGet.php");
    otp_data=int(token_data.text)
    new_otp=otp_data;
    print(otp_data);
    if(old_otp != new_otp):
        
        # Create a socket object
        # S socket object is to listen  a string which will be send by lock
        # 5 minute is maximum expiration OTP
        # This function will convert list into integer value
        
        MAXIMUM_KEYPAD_INPUT_RETRY =  3
        MAXIMUM_OTP_EXPIRATION_TIME = 5
        #socket_cloud = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        start_time = datetime.datetime.now()
        #pd.datetime.now().minute
        #print(pd.datetime.now().second)
        print(start_time.minute)
        error_code = 000000
        #OTP_DATABASE = [101010,708090,102030,101112]
        #Adifico_cloud_server_IP = '192.168.1.10'
        #Adifico_cloud_server_port = 9000
        #socket_cloud.connect((Adifico_cloud_server_IP, Adifico_cloud_server_port))
        #print("The socket has successfully connected to Adifico server having socket information",Adifico_cloud_server_IP,Adifico_cloud_server_port)
        # Receive the OTP now through socket listening
        # 1024 represent size of the string
        #OTP_data = socket_cloud.recv(1024)
        #Retry input will be done when wrong keys are press
        while MAXIMUM_KEYPAD_INPUT_RETRY >0:
            KEY_PAD_DATA =KEY_PAD_INPUT()
            # Now check the OTP data is equal to keypad data
            if KEY_PAD_DATA == otp_data:
                print("Given OTP matches with KEYPAD DATA",KEY_PAD_DATA)
                if otp_data != error_code:
                    print("Thanks GOD we are at safe zone ......!!!!!")
                    end_time = datetime.datetime.now();
                    Difference_time =end_time.minute - start_time.minute
                    if Difference_time <= MAXIMUM_OTP_EXPIRATION_TIME:
                        print("Trigger the lock to open the door and see the magic inside the door")
                        motor_on()
                        time.sleep(5)
                        motor_off()
                        MAXIMUM_KEYPAD_INPUT_RETRY = 0
                    else:
                        print("Do not trigger the lock OTP expire ,Please Note our expiry time is %d",MAXIMUM_OTP_EXPIRATION_TIME)
                else:
                    print("We have error code OTP receive ,Danger Alert Someone is Tampering the data,Please add some encryptions")
            else:
                print("Given OTP does not match with input keypad data")
                MAXIMUM_KEYPAD_INPUT_RETRY =MAXIMUM_KEYPAD_INPUT_RETRY -1
                print("Retry value is equal to",MAXIMUM_KEYPAD_INPUT_RETRY) 
    old_otp = new_otp;
    print("hello");
    time.sleep(5);
        #This function will take input from keypad and return integer keypad data with 6 digit
        
