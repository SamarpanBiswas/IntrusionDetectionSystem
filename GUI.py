import sys
import os
import face_recognition
import cv2
import numpy as np
import pandas as pd
import time 
from datetime import datetime
from save_photo import go_snap
from Detection import intrusion_fn
if sys.version_info[0] < 3:
        from Tkinter import *
        import tkMessageBox
else:
        from tkinter import *
        from tkinter import messagebox


global PassLock
global PassChild
global expression 
global expression_1
global expression_2
global expression_3
global dirname
global numfiles
global x_signal 
global y_signal
global z_signal
global key_signal 
global lckdwn
global parlckdwn
numfiles = 0
x_signal = 0
y_signal = 0
z_signal = 0
key_signal = 0
lckdwn = 0
parlckdwn  = 0  
labels = []
file = open("Passwords.txt","r+")
p_signal = file.readlines()
for line in p_signal:
	words = line.split(" ")
PassLock = words[0]
PassChild = words[1]
print(PassLock)
print(PassChild)
file.close()

# creating basic window
window = Tk()
window.geometry("410x330") # size of the window width:- 500, height:- 375
window.resizable(0, 0) # this prevents from resizing the window
window.title("GUI")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def detect(detect1):
	intrusion_fn(detect1)

def btn_click_1(item_1):
    global expression_1
    expression_1 = expression_1 + str(item_1)
    input_text_1.set(expression_1)
def btn_clear_1():
    global expression_1
    expression_1 = ""
    input_text_1.set("")

def btn_click_2(item_2):
    global expression_2
    expression_2 = expression_2 + str(item_2)
    input_text_3.set(expression_2)
def btn_clear_2():
    global expression_2
    expression_2 = ""
    input_text_3.set("")    

def btn_click_3(item_3):
    global expression_3
    expression_3 = expression_3 + str(item_3)
    input_text_5.set(expression_3)
def btn_clear_3():
    global expression_3
    expression_3 = ""
    input_text_5.set("firstname_lastname")    

def btn_Lock(try1):
	global parlckdwn
	global lckdwn
	global expression
	global PassLock
	#if parlckdwn == 0:
	if lckdwn == 0: #to lock
		if try1 == PassLock:
			input_text.set("Lock down")
			messagebox.showinfo("Alert","Complete Lock down initiated.")
			input_text.set("")
			expression = ""
			lckdwn = 1
			detect(lckdwn)
		else:
			input_text.set("Error")
			expression = ""
	elif lckdwn == 1: #to unlock
		if try1 == PassLock:
			input_text.set("UnLocked")
			messagebox.showinfo("Alert","Unlocked.")
			input_text.set("")
			expression = ""
			lckdwn = 0
		else:
			input_text.set("Error")
			expression = ""
			messagebox.showinfo("Alert","Wrong Password Entered")
			detect(lckdwn)
#	elif parlckdwn == 1:
#		input_text.set("Error")
#		messagebox.showinfo("Alert","First Disable Parental Lock")
#		input_text.set("")
#		expression = ""

def btn_SystemLock(try2):
	global lckdwn
	global parlckdwn
	global expression
	global PassChild
	if lckdwn == 0: #to lock
		if parlckdwn == 0:
			if try2 == PassChild:
				input_text.set("System Lock")
				messagebox.showinfo("Alert","System Lock Enabled.")
				input_text.set("")
				expression = ""
				parlckdwn = 1
			else:
				input_text.set("Error") 
				expression=""
		elif parlckdwn == 1:
			if try2 == PassChild:
				input_text.set("UnLocked")
				messagebox.showinfo("Alert","System Lock Disabled.")
				input_text.set("")
				expression = ""
				parlckdwn = 0 
			else:
				input_text.set("Error")
				expression=""
	elif lckdwn == 1: 
		input_text.set("Error")
		messagebox.showinfo("Alert","Full Lockdown. Can't access System Control")
		input_text.set("")
		expression = ""


def submit_keyboard():
	global expression_3
	global key_signal
	global lckdwn
	global parlckdwn
	global dirname
	input_text_5.set("firstname_lastname")
	dirname = expression_3
	expression_3=""
	if lckdwn == 0 and parlckdwn == 0:
		if dirname != "":
			messagebox.showinfo("Alert", "Press 'p' to take the photo")
			go_snap(dirname)
		else:
			messagebox.showinfo("Alert", "No input given")
	else:
		if lckdwn == 1:
			messagebox.showinfo("Alert", "Cannot make update. System on Full Lockdown!")
		elif parlckdwn == 1:
			messagebox.showinfo("Alert", "Cannot make update. System Lock Enabled!")

def Change_it_1():
	global x_signal
	global z_signal
	global lckdwn
	global parlckdwn
	global expression_1
	global PassLock
	global PassChild
	if lckdwn == 0 and parlckdwn == 0: 
		if x_signal == 0:
			if expression_1 == PassLock:
				input_text_1.set("")
				input_text_2.set("Enter New Password")
				expression_1=""
				x_signal = 1
			else:
				input_text_1.set("Error")
				expression_1=""
		elif x_signal == 1:
			z_signal = str(expression_1) + str(" ") + str(PassChild)
			print(z_signal)
			PassLock = expression_1
			print(PassLock)
			file = open("Passwords.txt", "w")
			file.seek(0,0)
			file.write(z_signal)
			file.close()
			messagebox.showinfo("Alert","Password changed for Full Lockdown!")
			x_signal = 0
			input_text_2.set("Enter Password for Full Lock")
			input_text_1.set("")
			expression_1=""
	else:
		if lckdwn == 1:
			input_text_1.set("Error")
			messagebox.showinfo("Alert","Password cannot be changed. System on Full Lockdown!")
			input_text_1.set("")
			expression_1=""
		elif parlckdwn == 1:
			input_text_1.set("Error")
			messagebox.showinfo("Alert","Password cannot be changed. System Lock Enabled!")
			input_text_1.set("")
			expression_1=""


def Change_it_2():
	global y_signal
	global z_signal
	global lckdwn
	global parlckdwn
	global expression_2
	global PassChild
	global PassLock
	if lckdwn == 0 and parlckdwn == 0: 
		if y_signal == 0:
			if expression_2 == PassChild:
				input_text_3.set("")
				input_text_4.set("Enter New Password")
				expression_2=""
				y_signal = 1
			else:
				input_text_3.set("Error")
				expression_2=""
		elif y_signal == 1:
			z_signal = str(PassLock) + str(" ") + str(expression_2)
			print(z_signal)
			PassChild = expression_2
			print(PassChild)
			file = open("Passwords.txt", "w")
			file.seek(0, 0)
			file.write(z_signal)
			file.close()
			messagebox.showinfo("Alert","Password changed for system Lock!")
			y_signal = 0
			input_text_4.set("Enter Password for Full Lock")
			input_text_3.set("")
			expression_2=""
	else:
		if lckdwn == 1:
			input_text_3.set("Error")
			messagebox.showinfo("Alert","Password cannot be changed. System on Full Lockdown!")
			input_text_3.set("")
			expression_2=""
		elif parlckdwn == 1:
			input_text_3.set("Error")
			messagebox.showinfo("Alert","Password cannot be changed. System Lock Enabled!")
			input_text_1.set("")
			expression_2=""


def Pass_window():
    newwin1 = Toplevel(window)
    newwin1.geometry("290x110")
    newwin1.resizable(0,0)
    newwin1.title("Password Change")
    Op1 = Button(newwin1, text = "Full Lock", fg = "black", width = 40, height = 3, bd = 0, bg = "#fff",activebackground="green",cursor = "hand2", command = lambda: Pass_select_Op1()).grid(row = 0, column = 0, columnspan = 1, padx = 1, pady = 1) 
    Op2 = Button(newwin1, text = "System Lock", fg = "black", width = 40, height = 3, bd = 0, bg = "#fff",activebackground="green",cursor = "hand2", command = lambda: Pass_select_Op2()).grid(row = 1, column = 0, columnspan = 1, padx = 1, pady = 1)

def Pass_select_Op1():
	global expression_1
	global x_signal
	x_signal = 0
	expression_1=""
	input_text_1.set("")
	input_text_2.set("Enter Password for Full Lock")
	newwin2 = Toplevel(window)
	newwin2.geometry("260x350")
    #newwin2.resizable(1,1)
	input_frame_1 = Frame(newwin2, width = 30, height = 20, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
	input_frame_1.pack(side = TOP,ipady=2)

	input_field_1 = Entry(input_frame_1, font = ('arial', 30, 'bold'), textvariable = input_text_1, width = 30, bg = "#eee", bd = 0, justify = RIGHT)
	input_field_1.grid(row = 0, column = 0,columnspan=3)
	input_field_1.pack(ipady=2) # 'ipady' is internal padding to increase the height of input field

	Label1 = Label(newwin2,textvariable=input_text_2)
	Label1.pack()
	
	btns_frame_1 = Frame(newwin2, width = 50, height = 330, bg = "grey",bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
	btns_frame_1.pack(side=LEFT,ipadx=0)
	clear_1 = Button(btns_frame_1, text = "Clear", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_clear_1()).grid(row = 0, column = 0, columnspan = 1, padx = 3, pady = 1)
	submit_bt = Button(btns_frame_1, text = "Submit", fg = "black", width = 23, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: Change_it_1()).grid(row = 0, column = 1, columnspan = 2, padx = 0, pady = 1)

	seven_1 = Button(btns_frame_1, text = "7", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_1(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
	eight_1 = Button(btns_frame_1, text = "8", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_1(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
	nine_1 = Button(btns_frame_1, text = "9", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_1(9)).grid(row = 1, column = 2, padx = 1, pady = 1)

	four_1 = Button(btns_frame_1, text = "4", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_1(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
	five_1 = Button(btns_frame_1, text = "5", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_1(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
	six_1 = Button(btns_frame_1, text = "6", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_1(6)).grid(row = 2, column = 2, padx = 1, pady = 1)

	one_1 = Button(btns_frame_1, text = "1", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_1(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
	two_1 = Button(btns_frame_1, text = "2", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_1(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
	three_1 = Button(btns_frame_1, text = "3", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_1(3)).grid(row = 3, column = 2, padx = 1, pady = 1)

	astk_1 = Button(btns_frame_1, text = "*", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_1("*")).grid(row = 4, column = 0,padx = 1, pady = 0)
	zero_1 = Button(btns_frame_1, text = "0", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_1(0)).grid(row = 4, column = 1,padx = 1, pady = 0)
	hstg_1 = Button(btns_frame_1, text = "#", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_1("#")).grid(row = 4, column = 2, padx = 1, pady = 0)



def Pass_select_Op2():
	global expression_2
	global y_signal
	expression_2=""
	input_text_3.set("")
	y_signal = 0
	input_text_4.set("Enter Password for System Lock")
	newwin3 = Toplevel(window)
	newwin3.geometry("260x350")
    #newwin3.resizable(1,1)
	input_frame_2 = Frame(newwin3, width = 30, height = 20, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
	input_frame_2.pack(side = TOP,ipady=2)

	input_field_2 = Entry(input_frame_2, font = ('arial', 30, 'bold'), textvariable = input_text_3, width = 30, bg = "#eee", bd = 0, justify = RIGHT)
	input_field_2.grid(row = 0, column = 0,columnspan=3)
	input_field_2.pack(ipady=2) # 'ipady' is internal padding to increase the height of input field

	Label2 = Label(newwin3,textvariable=input_text_4)
	Label2.pack()

	btns_frame_2 = Frame(newwin3, width = 50, height = 330, bg = "grey",bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
	btns_frame_2.pack(side=LEFT,ipadx=0)

	clear_2 = Button(btns_frame_2, text = "Clear", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_clear_2()).grid(row = 0, column = 0, columnspan = 1, padx = 3, pady = 1)
	submit_bt_1 = Button(btns_frame_2, text = "Submit", fg = "black", width = 23, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: Change_it_2()).grid(row = 0, column = 1, columnspan = 2, padx = 0, pady = 1)

	seven_2 = Button(btns_frame_2, text = "7", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_2(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
	eight_2 = Button(btns_frame_2, text = "8", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_2(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
	nine_2 = Button(btns_frame_2, text = "9", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_2(9)).grid(row = 1, column = 2, padx = 1, pady = 1)

	four_2 = Button(btns_frame_2, text = "4", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_2(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
	five_2 = Button(btns_frame_2, text = "5", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_2(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
	six_2 = Button(btns_frame_2, text = "6", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_2(6)).grid(row = 2, column = 2, padx = 1, pady = 1)

	one_2 = Button(btns_frame_2, text = "1", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_2(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
	two_2 = Button(btns_frame_2, text = "2", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_2(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
	three_2 = Button(btns_frame_2, text = "3", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_2(3)).grid(row = 3, column = 2, padx = 1, pady = 1)

	astk_2 = Button(btns_frame_2, text = "*", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_2("*")).grid(row = 4, column = 0,padx = 1, pady = 0)
	zero_2 = Button(btns_frame_2, text = "0", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_2(0)).grid(row = 4, column = 1,padx = 1, pady = 0)
	hstg_2 = Button(btns_frame_2, text = "#", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_2("#")).grid(row = 4, column = 2, padx = 1, pady = 0)


def Program_Keyboard():
	global expression_3
	global dirname
	expression_3 = ""
	dirname=""
	input_text_6.set("Enter name of the person and Press Submit")
	input_text_5.set("firstname_lastname")
	newwin4 = Toplevel(window)
	newwin4.geometry("645x260")
    #newwin4.resizable(0,0)
	input_frame_3 = Frame(newwin4, width = 80, height = 20, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
	input_frame_3.pack(side = TOP,ipady=2)

	input_field_3 = Entry(input_frame_3, font = ('arial', 30, 'bold'), textvariable = input_text_5, width = 30, bg = "#eee", bd = 0, justify = RIGHT)
	input_field_3.grid(row = 0, column = 0,columnspan=8)
	input_field_3.pack(ipady=2) # 'ipady' is internal padding to increase the height of input field

	Label3 = Label(newwin4,textvariable=input_text_6)
	Label3.pack()

	btns_frame_3 = Frame(newwin4, width = 80, height = 100, bg = "grey",bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
	btns_frame_3.pack(side=LEFT,ipadx=1)

	clear_3 = Button(btns_frame_3, text = "Clear", fg = "black", width = 49, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_clear_3()).grid(row = 0, column = 0, columnspan = 5, padx = 0, pady = 1)
	submit_bt_3 = Button(btns_frame_3, text = "Submit", fg = "black", width = 39, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: submit_keyboard()).grid(row = 0, column = 5, columnspan = 4, padx = 0, pady = 1)
	## First row
	q_3 = Button(btns_frame_3, text = "q", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('q')).grid(row = 1, column = 0, padx = 1, pady = 1)
	w_3 = Button(btns_frame_3, text = "w", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('w')).grid(row = 1, column = 1, padx = 1, pady = 1)
	e_3 = Button(btns_frame_3, text = "e", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('e')).grid(row = 1, column = 2, padx = 1, pady = 1)
	r_3 = Button(btns_frame_3, text = "r", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('r')).grid(row = 1, column = 3, padx = 1, pady = 1)
	t_3 = Button(btns_frame_3, text = "t", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('t')).grid(row = 1, column = 4, padx = 1, pady = 1)
	y_3 = Button(btns_frame_3, text = "y", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('y')).grid(row = 1, column = 5, padx = 1, pady = 1)
	u_3 = Button(btns_frame_3, text = "u", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('u')).grid(row = 1, column = 6, padx = 1, pady = 1)
	i_3 = Button(btns_frame_3, text = "i", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('i')).grid(row = 1, column = 7, padx = 1, pady = 1)
	o_3 = Button(btns_frame_3, text = "o", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('o')).grid(row = 1, column = 8, padx = 1, pady = 1)
	


	## Second Row
	p_3 = Button(btns_frame_3, text = "p", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('p')).grid(row = 2, column = 0, padx = 1, pady = 1)
	a_3 = Button(btns_frame_3, text = "a", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('a')).grid(row = 2, column = 1, padx = 1, pady = 1)
	s_3 = Button(btns_frame_3, text = "s", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('s')).grid(row = 2, column = 2, padx = 1, pady = 1)
	d_3 = Button(btns_frame_3, text = "d", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('d')).grid(row = 2, column = 3, padx = 1, pady = 1)
	f_3 = Button(btns_frame_3, text = "f", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('f')).grid(row = 2, column = 4, padx = 1, pady = 1)
	g_3 = Button(btns_frame_3, text = "g", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('g')).grid(row = 2, column = 5, padx = 1, pady = 1)
	h_3 = Button(btns_frame_3, text = "h", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('h')).grid(row = 2, column = 6, padx = 1, pady = 1)
	j_3 = Button(btns_frame_3, text = "j", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('j')).grid(row = 2, column = 7, padx = 1, pady = 1)
	k_3 = Button(btns_frame_3, text = "k", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('k')).grid(row = 2, column = 8, padx = 1, pady = 1)

	## Third Row
	l_3 = Button(btns_frame_3, text = "l", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('l')).grid(row = 3, column = 0, padx = 1, pady = 1)
	z_3 = Button(btns_frame_3, text = "z", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('z')).grid(row = 3, column = 1, padx = 1, pady = 1)
	x_3 = Button(btns_frame_3, text = "x", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('x')).grid(row = 3, column = 2, padx = 1, pady = 1)
	c_3 = Button(btns_frame_3, text = "c", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('c')).grid(row = 3, column = 3, padx = 1, pady = 1)
	v_3 = Button(btns_frame_3, text = "v", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('v')).grid(row = 3, column = 4, padx = 1, pady = 1)
	b_3 = Button(btns_frame_3, text = "b", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('b')).grid(row = 3, column = 5, padx = 1, pady = 1)
	n_3 = Button(btns_frame_3, text = "n", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('n')).grid(row = 3, column = 6, padx = 1, pady = 1)
	m_3 = Button(btns_frame_3, text = "m", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('m')).grid(row = 3, column = 7, padx = 1, pady = 1)
	underscore_3 = Button(btns_frame_3, text = "_", fg = "black", width = 9, height = 2, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_3('_')).grid(row = 3, column = 8, padx = 1, pady = 1)






##
expression = ""
expression_1 = ""
expressionn_2 = ""
expression_3 = ""
dirname = ""
input_text = StringVar()
input_text_1 = StringVar()
input_text_2 = StringVar()
input_text_3 = StringVar()
input_text_4 = StringVar()
input_text_5 = StringVar()
input_text_6 = StringVar()




fun_frame = Frame(window, width = 100, height = 375, bg = "grey",bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
fun_frame.pack(side=LEFT,ipady=0)
# first row
Camera = Button(fun_frame, text = "Camera", fg = "black", width = 20, height = 3, bd = 0, bg = "#fff",activebackground="green",cursor = "hand2", command = lambda: detect(lckdwn)).grid(row = 0, column = 0, columnspan = 1, padx = 1, pady = 1)
Lock = Button(fun_frame, text = "Full Lock", fg = "black", width = 20, height = 3, bd = 0, bg = "#fff" ,activebackground="green", cursor = "hand2", command = lambda: btn_Lock(expression)).grid(row = 1, column = 0, padx = 1, pady = 1,columnspan=1)
SLock = Button(fun_frame, text = "System Lock", fg = "black", width = 20, height = 3, bd = 0, bg = "#fff",activebackground="green", cursor = "hand2", command = lambda: btn_SystemLock(expression)).grid(row = 2, column = 0, padx = 1, pady = 1,columnspan=1)
Pchange = Button(fun_frame, text = "Password Change", fg = "black", width = 20, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: Pass_window()).grid(row = 3, column = 0, padx = 1, pady = 1,columnspan=1)
Program = Button(fun_frame, text = "Program", fg = "black", width = 20, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: Program_Keyboard()).grid(row = 4, column = 0,padx = 1, pady = 1,columnspan=1)
logout = Button(fun_frame, text = "Logout",fg = "black", width = 20, height = 3, bg = "#fff",bd=0,command=window.quit).grid(row = 5, column = 0, columnspan = 1, padx = 1, pady = 1)

input_frame = Frame(window, width = 70, height = 30, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP,ipady=2)


# creating a input field inside the 'Frame'
input_field = Entry(input_frame, font = ('arial', 30, 'bold'), textvariable = input_text, width = 70, bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0,columnspan=3)
input_field.pack(ipady=2) # 'ipady' is internal padding to increase the height of input field


# creating another 'Frame' for the button below the 'input_frame'
btns_frame = Frame(window, width = 70, height = 330, bg = "grey",bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
btns_frame.pack(side=LEFT,ipadx=50)

# first row
clear = Button(btns_frame, text = "Clear", fg = "black", width = 30, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 3, pady = 0)

# second row
seven = Button(btns_frame, text = "7", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)

# third row
four = Button(btns_frame, text = "4", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)

# fourth row
one = Button(btns_frame, text = "1", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)


# fourth row
astk = Button(btns_frame, text = "*", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 4, column = 0,padx = 1, pady = 0)
zero = Button(btns_frame, text = "0", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 1,padx = 1, pady = 0)
hstg = Button(btns_frame, text = "#", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click("#")).grid(row = 4, column = 2, padx = 1, pady = 0)

window.mainloop()







