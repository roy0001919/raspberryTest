#! /usr/bin/env python3
# coding:utf-8

import tkinter as tk
import time
import RPi.GPIO as GPIO
import pymssql
import datetime
import requests
import threading
import os
import logging

mydb2 = pymssql.connect(host='192.168.0.43',
                       user='sa',
                       password='test123',
                       database='Raspberry_pi',)
                       #charset='utf8')
logging.basicConfig(
                    filename='log.txt',  filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
                    
window = tk.Tk()
window.title('my window')
window.geometry('2000x3000')
mycursor = mydb2.cursor()
mycursor4 = mydb2.cursor()
mycursor9 = mydb2.cursor()
mycursor3 = mydb2.cursor()
mycursor5 = mydb2.cursor()
mycursor6 = mydb2.cursor()

x = datetime.datetime.now()
y = x.strftime("%Y%m%d")
z = x.strftime("%X")
a = x.strftime("%Y-%m-%d %H:%M:%S")
#sql = "DELETE FROM distanceTest WHERE test = '1'"
#mycursor.execute(sql)
#sql2 = "DELETE FROM distanceAlarm WHERE test = '1'"
#mycursor.execute(sql2)
mydb2.commit()
cycle1=0
x1=0
x2=0
x3=0
x4=0
a1=0
a2=0
a3=0
g=0

def endTime():
    global a,endTime
    endTime=a
    return endTime

def startTime():
    global a,startTime
    startTime=a
    return startTime

def CallKeyboard():
    #global lock
    #lock.acquire()
    added_thread = threading.Thread(target=keyboard)
    added_thread.start()

def keyboard():
    os.system('florence')
    #lock.release()
    
def sensor():
   global distance 
#   GPIO.setmode(GPIO.BCM)
   MONITOR_PIN = 26
# Define GPIO to use on Pi
   GPIO_TRIGGER = 23
   GPIO_ECHO = 24
   GPIO.setup(MONITOR_PIN, GPIO.OUT)
   GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
   GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
   GPIO.output(GPIO_TRIGGER, False)

# Allow module to settle

   time.sleep(0.5)

# Send 10us pulse to trigger

   GPIO.output(GPIO_TRIGGER, True)
   time.sleep(0.00001)
   GPIO.output(GPIO_TRIGGER, False)
   start = time.time()
   while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

   while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()
   elapsed = stop-start
   distance = elapsed * 34000
# That was the distance there and back so halve the value
   distance = distance / 2/100
   logging.warning('sensor')

def returnCycle():
    
    global cycle1,var,var2,var3,a,g
    #print(var)
    #print(cycle1)
   # sql4 = "UPDATE distance SET total =(%s),lm_time=(%s) where wo_id=(%s) and lm_user=(%s) and op=(%s)"
   # val4=(cycle1,,var,var2,var3)
   # mycursor4.execute(sql4,val4)
    #sql5 = "update distanceAlarm set hourlyMove=(select MAX(cycle) from distanceAlarm where hourlyMove is NULL)-(select MIN(cycle) from distanceAlarm where hourlyMove is NULL)+2 where hourlyMove is NULL"
    g=1
    Var.set('finish')
    #sql5 ="INSERT INTO distance (count) values ('c')"
    #mycursor4.execute(sql5)
    #mydb2.commit()
    cycle1=0
    #print(cycle1)
    return cycle1,g
    

def InsertSQL():
      
    added_thread = threading.Thread(target=Distance)
    added_thread.start()
    
    global e1,e2,e3,e4,e5,Var,var,var2,var3,a,var4,var5,Var2,lb,value
    
    var5=e1.get()
    var=e2.get()
    var2=e3.get()
    var3=e4.get()
    var4=e5.get()
    #value = lb.get(lb.curselection())  
    #Var.set(value) 
    #int(var4)
    Var.set('start')
    startTime()
    logging.warning('InsertSQL')
    #mycursor = mydb2.cursor()
    #sql = "INSERT INTO distance (wo_id,op,count,lm_time,lm_user,eqp_status,ma_id,start_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    #val = (var,var3,var4,a,var2,value,var5,startTime)
    #mycursor.execute(sql,val)
    #mydb2.commit()
    return var,var2,var3,var4
    #distance()
    
def Distance():
 while True:
  global cycle1,Var,a,x1,x2,distance,var,var2,var3,var4,var5,a1,value,g,startTime
  x = datetime.datetime.now()
  y = x.strftime("%Y%m%d")
  z = x.strftime("%X")
  a = x.strftime("%Y-%m-%d %H:%M:%S")
  GPIO.setmode(GPIO.BCM)
  MONITOR_PIN = 26
# Define GPIO to use on Pi
  GPIO_TRIGGER = 23
  GPIO_ECHO = 24
  GPIO.setup(MONITOR_PIN, GPIO.OUT)
  GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
  GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
  GPIO.output(GPIO_TRIGGER, False)

# Allow module to settle

  time.sleep(0.5)

# Send 10us pulse to trigger

  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()
  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

# Calculate pulse length
  elapsed = stop-start
 
# Distance pulse travelled in that time is time
# multiplied by the speed of sound (cm/s)
  distance = elapsed * 34000

# That was the distance there and back so halve the value
  distance = distance / 2/100

  #print("Distance : %.1f" % distance+"m")
  int(distance)
  if g==1:
      g=0
      return g
  if distance<=0.3:
   x1=distance
   print('x1:'+str(x1))
   #GPIO.output(MONITOR_PIN, GPIO.HIGH)
  #lineNotify(token, msg, stickerPackageId, stickerId)
   mydb2.commit()
   #Var.set(cycle1)
   
   #time.sleep(0.001)
   time.sleep(0.2)
   sensor()
   x2=distance
   print('x2:'+str(x2))
   if x1-x2>0:
     a1=1
   else:
     a1=0
  #time.sleep(0.001)
   time.sleep(0.2)
   sensor()
   x3=distance
   print('x3:'+str(x3))
   if x2-x3>0:
     #GPIO.output(MONITOR_PIN, GPIO.HIGH)
      a2=1
   else:
      #GPIO.output(MONITOR_PIN, GPIO.LOW)
      a2=0
   #time.sleep(0.001)
   #sensor()
   #x4=distance
   #print('x4:'+str(x4))
   #if x3-x4>0:
      #GPIO.output(MONITOR_PIN, GPIO.HIGH)
       #a3=1
   #else:
      #GPIO.output(MONITOR_PIN, GPIO.LOW)
       #a3=0
   #if cycle1<=3:
            
       #sql= "update distance SET end_time=(%s) where start_time=(%s)"
       #val= (a,startTime)
       #mycursor3.execute(sql,val)
       
   if a1==1 and a2==1 and x1-x3>0.025:
       global var4,value,var5,startTime,endTime
       cycle1=cycle1+int(var4)
       sql3 = "INSERT INTO distanceAlarm (workOrder,process,count,time1,date1,xaxis,cycle,JobNumber) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
       val2 = (var,var3,var4,z,y,a,cycle1,var2)
       mycursor3.execute(sql3,val2)
       endTime=a
       sql6 = "INSERT INTO distance (start_time,wo_id,op,count,lm_time,lm_user,ma_id,end_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
       val6 = (startTime,var,var3,var4,a,var2,var5,endTime)
       mycursor3.execute(sql6,val6)
       print(cycle1)
       startTime=endTime
       logging.warning('insert')
       time.sleep(20)
   
  # if g==1:
     # g=0
      #return g
  #if int(x.strftime("%H"))==9 and int(x.strftime("%M"))==0:
      #sql5 ="update distanceAlarm set hourlyMove=(SELECT SUM (count) FROM distanceAlarm where  DATEPART(hh,time1)=8 and workOrder=(%s) and JobNumber=(%s) and Process=(%s))where DATEPART(hh,time1)=8 and workOrder=(%s) and JobNumber=(%s) and Process=(%s)"
      #val5 = (var,var2,var3,var,var2,var3)
      #mycursor9.execute(sql5,val5)
      #mydb2.commit()
  #if int(x.strftime("%H"))==10 and int(x.strftime("%M"))==0:
      #sql5 ="update distanceAlarm set hourlyMove=(SELECT SUM (count) FROM distanceAlarm where  DATEPART(hh,time1)=9 and workOrder=(%s) and JobNumber=(%s) and Process=(%s))where DATEPART(hh,time1)=9 and workOrder=(%s) and JobNumber=(%s) and Process=(%s)"
      #val5 = (var,var2,var3,var,var2,var3)
      #mycursor9.execute(sql5,val5)
      #mydb2.commit()
  #if int(x.strftime("%H"))==11 and int(x.strftime("%M"))==0:
      #sql5 ="update distanceAlarm set hourlyMove=(SELECT SUM (count) FROM distanceAlarm where  DATEPART(hh,time1)=10 and workOrder=(%s) and JobNumber=(%s) and Process=(%s))where DATEPART(hh,time1)=10 and workOrder=(%s) and JobNumber=(%s) and Process=(%s)"
      #val5 = (var,var2,var3,var,var2,var3)
      #mycursor9.execute(sql5,val5)
      #mydb2.commit()
  #if int(x.strftime("%H"))==12 and int(x.strftime("%M"))==0:
      #sql5 ="update distanceAlarm set hourlyMove=(SELECT SUM (count) FROM distanceAlarm where  DATEPART(hh,time1)=11 and workOrder=(%s) and JobNumber=(%s) and Process=(%s))where DATEPART(hh,time1)=11 and workOrder=(%s) and JobNumber=(%s) and Process=(%s)"
      #val5 = (var,var2,var3,var,var2,var3)
      #mycursor9.execute(sql5,val5)
      #mydb2.commit()
  #if int(x.strftime("%H"))==13 and int(x.strftime("%M"))==0:
      #sql5 ="update distanceAlarm set hourlyMove=(SELECT SUM (count) FROM distanceAlarm where  DATEPART(hh,time1)=12 and workOrder=(%s) and JobNumber=(%s) and Process=(%s))where DATEPART(hh,time1)=12 and workOrder=(%s) and JobNumber=(%s) and Process=(%s)"
      #val5 = (var,var2,var3,var,var2,var3)
      #mycursor9.execute(sql5,val5)
      #mydb2.commit()
  #if int(x.strftime("%H"))==14 and int(x.strftime("%M"))==0:
      #sql5 ="update distanceAlarm set hourlyMove=(SELECT SUM (count) FROM distanceAlarm where  DATEPART(hh,time1)=13 and workOrder=(%s) and JobNumber=(%s) and Process=(%s))where DATEPART(hh,time1)=13 and workOrder=(%s) and JobNumber=(%s) and Process=(%s)"
      #val5 = (var,var2,var3,var,var2,var3)
      #mycursor9.execute(sql5,val5)
      #mydb2.commit()
  #if int(x.strftime("%H"))==15 and int(x.strftime("%M"))==0:
      #sql5 ="update distanceAlarm set hourlyMove=(SELECT SUM (count) FROM distanceAlarm where  DATEPART(hh,time1)=14 and workOrder=(%s) and JobNumber=(%s) and Process=(%s))where DATEPART(hh,time1)=14 and workOrder=(%s) and JobNumber=(%s) and Process=(%s)"
      #val5 = (var,var2,var3,var,var2,var3)
      #mycursor9.execute(sql5,val5)
      #mydb2.commit()
  #if int(x.strftime("%H"))==16 and int(x.strftime("%M"))==0:
      #sql5 ="update distanceAlarm set hourlyMove=(SELECT SUM (count) FROM distanceAlarm where  DATEPART(hh,time1)=15 and workOrder=(%s) and JobNumber=(%s) and Process=(%s))where DATEPART(hh,time1)=15 and workOrder=(%s) and JobNumber=(%s) and Process=(%s)"
      #val5 = (var,var2,var3,var,var2,var3)
      #mycursor9.execute(sql5,val5)
      #mydb2.commit()
  #if int(x.strftime("%H"))==17 and int(x.strftime("%M"))==0:
      #sql5 ="update distanceAlarm set hourlyMove=(SELECT SUM (count) FROM distanceAlarm where  DATEPART(hh,time1)=16 and workOrder=(%s) and JobNumber=(%s) and Process=(%s))where DATEPART(hh,time1)=16 and workOrder=(%s) and JobNumber=(%s) and Process=(%s)"
      #val5 = (var,var2,var3,var,var2,var3)
      #mycursor9.execute(sql5,val5)
      #mydb2.commit()
  #if int(x.strftime("%H"))==18 and int(x.strftime("%M"))==0:
      #sql5 ="update distanceAlarm set hourlyMove=(SELECT SUM (count) FROM distanceAlarm where  DATEPART(hh,time1)=17 and workOrder=(%s) and JobNumber=(%s) and Process=(%s))where DATEPART(hh,time1)=17 and workOrder=(%s) and JobNumber=(%s) and Process=(%s)"
      #val5 = (var,var2,var3,var,var2,var3)
      #mycursor9.execute(sql5,val5)
      #mydb2.commit()    
  sql9 = "INSERT INTO distanceTest (distanceM,count,time1,date1,xaxis) VALUES (%s,%s,%s,%s,%s)"
  val9 = (distance,"1",z,y,a)

  mycursor9.execute(sql9,val9)

  mydb2.commit()
  logging.warning('distanceTest')
def main(): 
 
 global e1,e2,e3,e4,e5,Var,var,var2,var3,a,var4,Var2,lb,value
  
 lock = threading.Lock()
 #self.state = threading.Condition()

 l1=tk.Label(window,text="機台:",font=("Courier", 45)).grid(row=0)
 e1 = tk.Entry(window,font=("Courier", 24),width=12)
 e1.grid(row=0, column=1)

 l2=tk.Label(window,text="工單:",font=("Courier", 45)).grid(row=1)
 e2 = tk.Entry(window,font=("Courier", 24),width=12)
 e2.grid(row=1, column=1)

 l3=tk.Label(window,text="工號:",font=("Courier", 45)).grid(row=2)
 e3 = tk.Entry(window,font=("Courier", 24),width=12)
 e3.grid(row=2, column=1)

 #l0=tk.Label(window,text=" ",width=10,height=17).grid(row=4,colume=10)

 l4=tk.Label(window,text="製程:",font=("Courier", 45)).grid(row=0,column=20)
 e4 = tk.Entry(window,font=("Courier", 24),width=12)
 e4.grid(row=0,column=30)
 
 l5=tk.Label(window,text="穴數:",font=("Courier", 45)).grid(row=1,column=20)
 e5 = tk.Entry(window,font=("Courier", 24),width=12)
 e5.grid(row=1,column=30)

 #l100=tk.Label(window,text=" ",width=5,height=10).grid(column=40)

 Var2=tk.StringVar()
 Var2.set(("RUN","DOWN","IDLE","PM"))
 #lb = tk.Listbox(window, listvariable=Var2,height=4,width=4,bg='yellow',font=("Courier", 36))
 #lb.grid(column=50,row=3,rowspan=3)
 
 l200=tk.Label(window,text=" ",width=5,height=10).grid(column=60)

#l300=tk.Label(window,text=" ",width=10,height=10).grid(row=0,column=70)

 b1 = tk.Button(window,text="start",width=20,height=5,font=("Courier", 16),command=InsertSQL).grid(column=70,row=0)
 
 Var=tk.StringVar()
 l4=tk.Label(window,textvariable=Var,font=("Courier", 16)).grid(column=70,row=1)
 Var.set(a1)
  
 b2 = tk.Button(window,text="finish",width=20,height=5,font=("Courier", 16),command=returnCycle).grid(column=70,row=2)

 b3 = tk.Button(window,text="鍵盤",width=20,height=5,font=("Courier", 10),command=CallKeyboard).grid(column=30,row=3,rowspan=3,columnspan=3)

 window.mainloop()
main()


