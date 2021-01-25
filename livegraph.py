"""
===============
Embedding in Tk
===============

"""

from tkinter import *
from tkinter import ttk
import random
import tkinter

from matplotlib.backends.backend_tkagg import  FigureCanvasTkAgg, NavigationToolbar2Tk

from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


GUI = Tk()
GUI.geometry('600x700')
GUI.wm_title("AutoUpdate Graph")




MF1 = Frame(GUI)
MF1.pack()


# toolbar = NavigationToolbar2Tk(canvas, GUI)
# toolbar.update()
# canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#canvas.get_tk_widget().place(x=20,y=20)
#toolbar.pack_forget()


def UpdateData():
	global y
	global canvas
	global cv
	
	try:
		cv.destroy()
	except:
		pass

	# remove line

	# create graph
	fig = Figure(figsize=(6, 5), dpi=100)
	t = [0,1,2,3,4]
	y = []
	for i in range(len(t)):
		d = random.randint(30,70)
		y.append(d)
	label = ['A','B','C','D','E']
	graph = fig.add_subplot(111)
	graph.plot(t, y)
	graph.axis([None, None, 0, 100])


	canvas = FigureCanvasTkAgg(fig, master=MF1)  # A tk.DrawingArea.
	canvas.draw()
	canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

	cv = canvas.get_tk_widget()
	cv.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

	MF1.after(5000,UpdateData)


#button = ttk.Button(master=GUI, text="Update Data", command=UpdateData)
#button.pack(ipadx=20 , ipady=10 ,pady=20)


UpdateData()
GUI.mainloop()
