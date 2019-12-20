import re
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import *
class REASS:
	def __init__(self):
		self.root=Tk()
		self.root.title("regexp")
		self.screen= ScrolledText(self.root,font=("tahoma",12),bd=7,insertbackground="black", selectbackground="blue")
		self.screen.grid(row=0,column=0, columnspan=5)
		self.Count=IntVar()
		self.sec_screen=Entry(self.root, font=("arial",14, "bold"), bd=7)
		self.sec_screen.grid(row=2, column=0, columnspan=5, sticky=NSEW)
		self.button=Button(self.root, width="6", height="2", text="SEND", command=self.Send)
		self.button.grid(row=4, column=2, sticky=NSEW)
		self.root.mainloop()

	def Send(self):
		
		try:
			self.screen.tag_remove(SEL, "1.0", END)
			entryText=(self.sec_screen.get())
			rootText=self.screen.get("1.0", "end-1c")
			if entryText:
				r1=re.findall(entryText,rootText)
				if r1:
					start=self.screen.search(entryText, "1.0",END, count=self.Count) #The count variable retrieves the length of the searched word when its get()
					entryTextLen=self.Count.get()
					toChar="+%dc" %(entryTextLen)
					while start:
						#to readily go to the Text field
						self.screen.focus()
						endSelect= start + toChar
						self.screen.tag_add(SEL,start,endSelect)
						self.screen.see(INSERT)
						start=self.screen.search(entryText, endSelect,END, count=self.Count) #The count variable retrieves the length of the searched word when its get()
				else:
					showerror("Error", "text not found")
			else:
					showerror("Error", "Nothing to search")
		except Exception as e:
			showinfo(message=e)
		
ch=REASS()


'''
This is 20 weeks’ report of my Industrial Training at NIKE CENTER FOR ART AND CULTURE which is located at Dada Estate, Osogbo, Osun State, Nigeria.
The Student Industrial Work Experience Scheme, SIWES which is fully supported by the Federal Government is a skill acquisition programme designed to expose students to Industrial work situation and principle of operation they are likely to meet in their lines of career after graduation.
'''