from tkinter import *
import datetime
import time as tm
import threading
import pygame
from uncleengineer import thaistock


pygame.mixer.init()
def play():
	# playsound('sound1.mp3')
	pygame.mixer.music.load("search.mp3")
	pygame.mixer.music.play(loops=0)


def playThread():
	task = threading.Thread(target=play)
	task.start()


GUI = Tk()
GUI.title('4Q-UI INTER')
GUI.geometry('1080x700+300+20')
GUI.state('zoomed')

bg = '#303030' # back
bg1 = '#fc0505'
bg2 = '#fc9505'
bg3 ='#56d606' # green

fg = '#303030'
fg1 = '#fc0505'
fg2 = '#fc9505'
GUI.configure(background=bg)

FONT1 = 'kanit',30
FONT2 = 'Fira Code', 25
FONT3 = 'MesloLGS NF', 16
FONT4 = 'Radio Space',20
FONT5 = 'Welluxx Demo', 18

WW = 1920
WH = 1080

show = StringVar()
show.set('0100101000101010HEX')


#---------- stock ------
v_stockname = StringVar() #StringVar ตัวแปรสำหรับใช้กับ GUI
v_stockname2 = StringVar() #StringVar ตัวแปรสำหรับใช้กับ GUI


# def Fullscreen(event):
# 	GUI.attributes('-fullscreen',True)


# def ExitFullscreen(event):
# 	GUI.attributes('-fullscreen',False)

# GUI.bind('<F11>',Fullscreen)
# GUI.bind('<F2>',ExitFullscreen)

GUI.bind('<F10>', lambda event: GUI.attributes('-fullscreen', not GUI.attributes('-fullscreen')))

# CANVAS
canvas = Canvas(GUI,width=WW,height=WH, background=bg, bd=0, relief='ridge', highlightthickness=0)
canvas.place(x=0, y=0)

def MyfFram0(x,y,width=1410,height=865):
	frame1 = canvas.create_rectangle(0,0,width,height,fill=bg, outline=fg2, width=2)
	canvas.move(frame1,x,y)

def MyfFram1(x,y,width=300,height=100):
	frame1 = canvas.create_rectangle(0,0,width,height,fill=bg, outline=fg2, width=2)
	canvas.move(frame1,x,y)

def MyfFram2(x,y,width=300,height=460):
	frame1 = canvas.create_rectangle(0,0,width,height,fill=bg, outline=fg2, width=2)
	canvas.move(frame1,x,y)

def MyfFram3(x,y,width=220,height=460):
	frame1 = canvas.create_rectangle(0,0,width,height,fill=bg, outline=fg2, width=2)
	canvas.move(frame1,x,y)

def MyfFram4(x,y,width=900,height=350):
	frame1 = canvas.create_rectangle(0,0,width,height,fill=bg, outline=fg2, width=2)
	canvas.move(frame1,x,y)

def MyfFram5(x,y,width=450,height=845):
	frame1 = canvas.create_rectangle(0,0,width,height,fill=bg, outline=fg2, width=2)
	canvas.move(frame1,x,y)

 
def FixedLabel(text='THIS IS TEXT', x=50,y=50, font=FONT4, color=fg2):
	L1 = Label(GUI,text=text, font=font, bg=bg, fg=fg2)
	L1.place(x=x,y=y)

def ENTRY(x=50,y=50,font=FONT1):
	E1 = Entry(GUI,bg=bg2 ,font=font)
	E1.place(x=x,y=y)


######   TIME  ##########################

def NOW_TIME():

	now = tm.strftime("%H:%M:%S")  # เวลาปัจจุบัน
	CLOCK_DISTPLAY["text"] = now
	print('เวลา:', now)

	date = tm.strftime("%d/%m/%Y") 
	print("วันที่:",date)
	DATE_DISTPLAY["text"] = date
	GUI.after(1000, NOW_TIME)     # กำหนดให้ฟังก์ชั่นทำงานซ้ำ 1 วิ
			
CLOCK_DISTPLAY = Label(GUI, fg=fg, font=("Arial", 35, 'bold'),bg=bg2)
CLOCK_DISTPLAY.place(x=50, y=40)

DATE_DISTPLAY = Label(GUI, fg=fg, font=("Arial", 18, 'bold'),bg='gray')
DATE_DISTPLAY.place(x=202, y=47)



# ------ BTN ---------
# --- *** function POWER ***---
def ON():
	show.set('POWER ON')
	print('POWER ON')

def Mute():
	show.set('MUTE')
	print('MUTE')

#---*** function source ***--
def YT():
	show.set('open YouTube\nHS4QWC')
	print('open YouTube HS4QWC')

def SOURCE():
	show.set("open SOURCE")
	print('open source')

def NF():
	show.set('open NETFLIX')
	print('open NETFLIX')

def FB():
	show.set('open Facebook')
	print('open Facebook')




#---*** function ***---
def LISTS():
	show.set('Button List')
	print("Button List")
def ADD():
	show.set("Button ADD")
	print('Button ADD')




#---*** function button 0-9 ***---
def Number1():
	print('BUTTON-1')
	show.set('BUTTON-1')

def Number2():
	print('BUTTON-2')	
	show.set('BUTTON-2')

def Number3():
	print('BUTTON-3')
	show.set('BUTTON-3')

def Number4():
	print('BUTTON-4')
	show.set('BUTTON-4')

def Number5():
	print('BUTTON-5')
	show.set('BUTTON-5')

def Number6():
	print('BUTTON-6')
	show.set('BUTTON-6')	

def Number7():
	print('BUTTON-7')
	show.set('BUTTON-7')

def Number8():
	print('BUTTON-8')
	show.set('BUTTON-8')

def Number9():
	print('BUTTON-9')
	show.set('BUTTON-9')

def Number0():
	print('BUTTON-0')
	show.set('BUTTON-0')	



#------------------------
# ---***  ส่วนแสดงผล *** ---
LL1 = Label(GUI, textvariable=show,
				font=('YouTube Sans', 14, ),
				bg=bg2,
				fg='black',
			 	borderwidth=2,
		  		relief='groove',
			  	width=20, # width
			   	height=5) # height
LL1.place(x=720, y=35)


#--------------------------------#

# FRAME ***
F2 =Frame(GUI,bg=bg2)
F2.place(x=725, y=185)

F1 = Frame(GUI,bg='black')
F1.place(x=720, y=250)



#*********************
POWER = Button(GUI, text='ON', bg=bg3, command=ON)
POWER.place(x=720,y=430)

OFF = Button(GUI,text='OFF', command=Mute)
OFF.place(x=840,y=430)


#*********  ปุ่มตัวเลข FRAME-1 **********

b1 = Button(F1, text='1', bg=bg2, fg=fg2, command=Number1).grid(ipadx=10, ipady=5, padx=5,pady=5,row=0, column=0)
b2 = Button(F1, text='2', bg=bg2, fg=fg2, command=Number2).grid(ipadx=10, ipady=5, padx=5,pady=5,row=0, column=1)
b3 = Button(F1, text='3', bg=bg2, fg=fg2, command=Number3).grid(ipadx=10, ipady=5, padx=5,pady=5,row=0, column=2)

b4 = Button(F1, text='4', bg=bg2, fg=fg2, command=Number4).grid(ipadx=10, ipady=5, padx=5,pady=5,row=1, column=0)
b5 = Button(F1, text='5', bg=bg2, fg=fg2, command=Number5).grid(ipadx=10, ipady=5, padx=5,pady=5,row=1, column=1)
b6 = Button(F1, text='6', bg=bg2, fg=fg2, command=Number6).grid(ipadx=10, ipady=5, padx=5,pady=5,row=1, column=2)

b7 = Button(F1, text='7', bg=bg2,fg=fg2, command=Number7).grid(ipadx=10, ipady=5, padx=5,pady=5,row=2, column=0)
b8 = Button(F1, text='8', bg=bg2,fg=fg2, command=Number8).grid(ipadx=10, ipady=5, padx=5,pady=5,row=2, column=1)
b9 = Button(F1, text='9', bg=bg2, fg=fg2, command=Number9).grid(ipadx=10, ipady=5, padx=5,pady=5,row=2, column=2)
b0 = Button(F1, text='0', bg=bg2, fg=fg2, command=Number0).grid(ipadx=10, ipady=5, padx=5,pady=5,row=3, column=0)

b_list = Button(F1, text='LIS',bg='orange',fg=fg2, command=LISTS)
b_list.grid(ipadx=10, ipady=5, padx=5,pady=5,row=3, column=1)
b_AD = Button(F1, text='AD', bg=fg2, fg=fg2, command=ADD)
b_AD.grid(ipadx=10, ipady=5, padx=5,pady=5,row=3, column=2)

#---***  BUTTON FRAME 2 *****---
b_youtube = Button(F2, text='YouTube',font=('YouTube Sans', 12), fg=fg2, bg=bg2, command=YT)#font=YouTube Sans
b_youtube.grid(row=0, column=0)

b_SOURCE = Button(F2, text='SOURCE', font=('YouTube Sans', 12), bg=bg2, fg=fg2, command=SOURCE)
b_SOURCE.grid(row=0, column=1,ipadx=15)

b_NETFLIX = Button(F2, text='NETFLIX', font=('Bebas Neue', 12) ,fg=fg2, bg=fg2, padx=10, command=NF)
b_NETFLIX.grid(row=1,column=0)

b_FB = Button(F2, text='Facebook', font=('Facebook Letter Faces', 11) ,fg=fg2, bg=fg2, padx=10, command=FB)
b_FB.grid(row=1,column=1, padx=3, )
#------------------------
 
#FRAME-0
MyfFram0(10,10)

# time
MyfFram1(20,20)

FixedLabel('TIME',NOW_TIME(), 50,50,)
FixedLabel('DATE TIME', 50,100)
FixedLabel('PROJECT 4Q-UI',50,400,font=FONT1)



# coin
MyfFram1(20,200)
FixedLabel('MY COIN', 50,290)
FixedLabel('BTC COIN', 50,220)
FixedLabel('TETAIL 109999 btc', 50,250)



#TEMP
MyfFram1(20,380)

# CHECK
MyfFram2(350,20)
ENTRY(390, 50,font=FONT3)
FixedLabel('"Syniverse has,', 380,100, font=FONT3)
FixedLabel('experienced,', 380,130, font=FONT3)
FixedLabel('and may in the,', 380,160, font=FONT3)
FixedLabel('future face, hackers,', 380,190, font=FONT3)
FixedLabel('cybercriminals or others,', 380,220, font=FONT3)
FixedLabel(' F1 or F2 ENTER', 380,260,font=FONT2)



# FRAME BUTTON
MyfFram3(700, 20)

# FRAME-4
MyfFram4(20,515)

# FRAMR-5
MyfFram5(960,20)


E11 = Entry(GUI, textvariable=v_stockname, font=FONT2,bg=bg,fg=fg2)
E11.configure(insertbackground=fg) # cursor color
E11.configure(highlightthickness=2,highlightbackground=fg2,highlightcolor=fg2)
E11.place(x=1030,y=440)

v_result = StringVar()
v_result.set('MY STOCK: 50,000 BAHT')

LResult = Label(GUI, textvariable=v_result, font=FONT2, bg=bg, fg=fg2, justify=LEFT)
LResult.place(x=1030,y=500)

E12 = Entry(GUI, textvariable=v_stockname2, font=FONT2,bg=bg,fg=fg2)
E12.configure(insertbackground=fg) # cursor color
E12.configure(highlightthickness=2,highlightbackground=fg2,highlightcolor=fg2)
E12.place(x=1030,y=900)

v_result2 = StringVar()
v_result2.set('MY STOCK: 50,000 BAHT')

LResult2 = Label(GUI, textvariable=v_result2, font=FONT2, bg=bg, fg=fg2, justify=LEFT)
LResult2.place(x=1030,y=500)



def CheckStockPrice(event):
	playThread()
	try:
		stockname = v_stockname.get()
		print(stockname)
		result = thaistock(stockname)
		text = 'STOCK: {}\nPRICE: {}\nCHANGE: {}\n%CHANGE: {}'.format(result[0],result[1],result[2],result[3])
		v_result.set(text)
	except:
		v_result.set('NOT FOUND')

E11.bind('<Return>',CheckStockPrice)



def CheckStockPrice2(event):
	playThread()
	try:
		stockname2 = v_stockname2.get()
		print(stockname)
		result2 = thaistock(stockname)
		text = 'STOCK: {}\nPRICE: {}\nCHANGE: {}\n%CHANGE: {}'.format(result[0],result[1],result[2],result[3])
		v_result2.set(text)
	except:
		v_result2.set('NOT FOUND')

E12.bind('<Return>',CheckStockPrice)

###-------------- clock  -----------

def clock():
    string = tm.strftime('%H:%M:%S')
    lbl.config(text = string)
    lbl.after(1000, clock)
 

lbl = Label(GUI, font = ('impact', 30),
            background = bg,
            foreground = 'white')

lbl.place(x=1280,y=800)
clock()
#-----------------------------
GUI.mainloop()