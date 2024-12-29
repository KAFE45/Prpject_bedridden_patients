import serial
import time
from pygame import mixer
import pandas as pd  # Import pandas library
ser = serial.Serial('COM8', 115200, timeout=1)
time.sleep(2)

# def play(path): # สร้างฟังก์ชันชื่อ play โดยมี paremeter ชื่อ path
#     mixer.init() # เริ่มใช้งาน mixer
#     mixer.music.load(path) # โหลดไฟล์เสียง
#     mixer.music.play() # เล่นไฟล์เสียง
#     if (path == 'D:\Code\HeatMapSerialRead\heart-stop.mp3'): #
#         time.sleep(0.3)
#         mixer.music.stop()


# # path sound
# say = 'C:\\read_thermal\song\hello-thai.mp3'
# read = 'C:\\read_thermal\song\\read.mp3'

# play(say)



# def countdown(seconds):
#     for i in range(seconds, 0, -1):
#         print(f"นับถอยหลัง: {i} วินาที", end='\r')  # เคลียร์บรรทัดก่อนหน้าแล้วแสดงข้อความใหม่
#         time.sleep(1)

#     print("นับถอยหลังเสร็จสิ้น")

# try:
#     seconds = int(input("ป้อนจำนวนวินาทีที่ต้องการนับถอยหลัง: "))
#     countdown(seconds)
# except ValueError:
#     print("กรุณาป้อนจำนวนวินาทีให้ถูกต้อง")




class ReadLine: # สร้าง class ชื่อ ReadLine
    def __init__(self, s): # สร้าง constructor โดยมี paremeter ชื่อ s
        self.buf = bytearray() # สร้างตัวเเปรชื่อ buf เป็น bytearray
        self.s = s  # กำหนดค่าให้กับตัวเเปร s

    def readline(self): # สร้าง method ชื่อ readline โดยมี paremeter self 
        i = self.buf.find(b"\n") # กำหนดค่าให้กับตัวเเปร i โดยให้ค้นหาตัวขึ้นบรรทัดใหม่
        if i >= 0: # ถ้า i มีค่ามากกว่าหรือเท่ากับ 0
            r = self.buf[:i+1] # กำหนดค่าให้กับตัวเเปร r โดยให้เป็นตัวอักษรตั้งเเต่ตัวเเรกจนถึงตัวขึ้นบรรทัดใหม่
            self.buf = self.buf[i+1:] # กำหนดค่าให้กับตัวเเปร buff โดยให้เป็นตัวอักษรตั้งเเต่ตัวเเรกจนถึงตัวขึ้นบรรทัดใหม่
            return r # ส่งค่า r กลับไป
        while True: # วนลูป
            i = max(1, min(2048, self.s.in_waiting)) # กำหนดค่าให้กับตัวเเปร i โดยให้เป็นค่าที่มากที่สุดระหว่าง 1 กับ 2048 
            data = self.s.read(i) # กำหนดค่าให้กับตัวเเปร data โดยให้เป็นค่าที่อ่านมาจาก serial port
            i = data.find(b"\n") # กำหนดค่าให้กับตัวเเปร i โดยให้ค้นหาตัวขึ้นบรรทัดใหม่
            if i >= 0: # ถ้า i มีค่ามากกว่าหรือเท่ากับ 0
                r = self.buf + data[:i+1] # กำหนดค่าให้กับตัวเเปร r โดยให้เป็นตัวอักษรตั้งเเต่ตัวเเรกจนถึงตัวขึ้นบรรทัดใหม่
                self.buf[0:] = data[i+1:] # กำหนดค่าให้กับตัวเเปร buff โดยให้เป็นตัวอักษรตั้งเเต่ตัวเเรกจนถึงตัวขึ้นบรรทัดใหม่
                return r # ส่งค่า r กลับไป
            else:
                self.buf.extend(data) # กำหนดค่าให้กับตัวเเปร buff โดยให้เป็นค่าที่เก็บไว้ในตัวเเปร data


try:
    time.sleep(5)
    readline = ReadLine(ser)
    while True:
        line = readline.readline().decode('utf-8') # อ่านข้อมูลจาก Serial และแปลงเป็นข้อความ
        print(line.strip()) 
        
except KeyboardInterrupt:
    pass


# class scraping:
#     def process(self):

#         # Read Serial
#         serialRead = ReadLine(serial.Serial(self.port8, 115200))

#         # Informatiom
#         rounds = Prompt.ask("[bold cyan]Enter rounds[/bold cyan]")
#         case = Prompt.ask("[bold cyan]Enter case[/bold cyan]")
#         subject = Prompt.ask("[bold cyan]Enter name subject[/bold cyan]")
#         bmi = Prompt.ask("[bold cyan]Enter shape of subject[/bold cyan]")
#         pause = Prompt.ask(
#             "[bold cyan]Enter pause time (SEC.)[/bold cyan]")
#         label = int(Prompt.ask("[bold cyan]Enter label[/bold cyan] "))
#         number = int(Prompt.ask(
#             f"[bold cyan]Enter number of frames[/bold cyan] [bold green][DEFAULT[/bold green] [bold red]60[/bold red] [bold green]FRAME][/bold green] ", default=60))