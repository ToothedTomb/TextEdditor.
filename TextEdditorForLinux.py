# Importing Required libraries & Modules
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import CENTER, ttk, messagebox
from tkinter import Tk, Label, Button
import tkinter as tk
import tkinter
import os
import sys
#-------------------------------------
#Making the popups
def whoMadeThisSoftware():
    root = tk.Toplevel()  
    root.resizable(0,0)
    root.title("Who made this software?")
    root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='icon.png'))


    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Who made this software?")
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Jonathan Steadman has made this software.")
    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="#367cca",activebackground='pink', command = root.destroy)
    B1.pack()

def WhatIsThisSoftware():
    root = tk.Toplevel()  
    root.resizable(0,0)
    root.title("What is this software?")
    root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='icon.png'))


    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="What is this software?")
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="This software is a free and open source basic text edditor for Linux and FreeBSD.")
    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="#367cca",activebackground='pink', command = root.destroy)
    B1.pack()

def KeyboardShortcuts():
      root = tk.Toplevel()  
      root.resizable(0,0)
      root.title("Keyboard shortcuts.")
      root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='icon.png'))


      labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Keyboard shortcuts.")
      label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="'Control + C' will copy the text.")
      label2 = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="'Control + V' will paste the text.")      
      labelTitle.pack(side="top",fill="x",pady=1)
      label.pack(side="top", fill="x", pady=2)
      label2.pack(side="top", fill="x", pady=3)
      B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="#367cca",activebackground='pink', command = root.destroy)
      B1.pack()

#-------------------------------------
#Customzing the scrollbar
# Defining TextEditor Class
class TextEditor:
  # Defining Constructor
  def __init__(self,root):
    # Assigning root
    self.root = root
    self.root.configure(bg='pink')  
    # Title of the window
    self.root.title("Basic Text Edditor 4.0!")
    # Window Geometry
    # Initializing filename
    self.filename = None
    # Declaring Title variable
    self.title = StringVar()
    # Declaring Status variable
    # Creating Statusbar
    # Creating Titlebar


    self.titlebar = Label(self.root,textvariable=self.title,font=("Ubuntu",15,"bold"),bd=2,relief=GROOVE)
    # Packing Titlebar to root window
    self.titlebar.pack(side=BOTTOM,fill=BOTH)
    # Calling Settitle Function
    self.settitle()

    # Packing status bar to root window
    # Initializing Status
    
    self.title.set("Please save or open a document.")

    # Creating Menubar
    self.menubar = Menu(self.root,font=("Ubuntu",23,"bold"),activebackground="pink")
    # Configuring menubar on root window
    self.root.config(menu=self.menubar)
    # Creating File Menu
    self.filemenu = Menu(self.menubar,font=("Ubuntu",23,"bold"),activebackground="pink",tearoff=0)
    # Adding New file Command
    self.filemenu.add_command(label="New",command=self.newfile)
    # Adding Open file Command
    self.filemenu.add_command(label="Open",command=self.openfile)
    # Adding Save File Command
    self.filemenu.add_command(label="Save",command=self.savefile)
    # Adding Save As file Command
    self.filemenu.add_command(label="Save As",command=self.saveasfile)
    # Cascading filemenu to menubar
    self.menubar.add_cascade(label="File", menu=self.filemenu)
    # Creating Edit Menu
    self.editmenu = Menu(self.menubar,font=("Ubuntu",23),activebackground="pink",tearoff=0)
    # Adding Cut text Command
    self.editmenu.add_command(label="Cut",command=self.cut)
    # Adding Copy text Command
    self.editmenu.add_command(label="Copy",command=self.copy)
    # Adding Paste text command
    self.editmenu.add_command(label="Paste",command=self.paste)
    # Adding Seprator
    self.editmenu.add_separator()
    # Adding Undo text Command
    self.editmenu.add_command(label="Undo",command=self.undo)
    # Cascading editmenu to menubar
    self.menubar.add_cascade(label="Edit", menu=self.editmenu)
    self.about = Menu(self.menubar,font=("Ubuntu",23),activebackground="pink",tearoff=0)


    self.menubar.add_cascade(label="About",menu=self.about)
    self.about.add_command(label="About this software?",command=WhatIsThisSoftware)
    self.about.add_command(label="Who made this software?",command= whoMadeThisSoftware)
    self.about.add_command(label="Keyboard shortcuts",command= KeyboardShortcuts)



    # Creating Help Menu
    self.helpmenu = Menu(self.menubar,font=("Ubuntu",23),activebackground="pink",tearoff=0)
    # Creating Scrollbar
    scrol_y = Scrollbar(self.root,orient=VERTICAL,background="#367cca", activebackground="pink",width="20")
    # Creating Text Area
    self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("ubuntu",20),relief=GROOVE)
    # Packing scrollbar to root window
    scrol_y.pack(side=RIGHT,fill=Y)
    # Adding Scrollbar to text area
    scrol_y.config(command=self.txtarea.yview)
    # Packing Text Area to root window
    self.txtarea.pack(fill=BOTH,expand=1)
  # Defining settitle function
  def settitle(self):
    # Checking if Filename is not None
    if self.filename:
      # Updating Title as filename
      self.title.set(self.filename)
      # Updating Title as Untitled
  # Defining New file Function
  def newfile(self,*args):
    # Clearing the Text Area
    self.txtarea.delete("1.0",END)
    # Updating filename as None
    self.filename = None
    # Calling settitle funtion
    self.settitle()
    # updating status
    self.status.set("You have created a new file.")
  # Defining Open File Funtion
  def openfile(self,*args):
    # Exception handling
    try:
      # Asking for file to open
      self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py"),("HTML file","*.html"),("CSS file","*.css"),("Javascript","*js")))
      # checking if filename not none
      if self.filename:
        # opening file in readmode
        infile = open(self.filename,"r")
        # Clearing text area
        self.txtarea.delete("1.0",END)
        # Inserting data Line by line into text area
        for line in infile:
          self.txtarea.insert(END,line)
        # Closing the file  
        infile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("The text document has opened successfully")
    except Exception as e:
      root = tk.Toplevel()  
      root.resizable(0,0)
      root.title("Opened sucessfully.")
      root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='icon.png'))


      labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Opened successfully.")
      label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="This document was opened sucessfully.")
      labelTitle.pack(side="top",fill="x",pady=1)
      label.pack(side="top", fill="x", pady=2)
      B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="#367cca",activebackground='pink', command = root.destroy)
      B1.pack()
  # Defining Save File Funtion
  def savefile(self,*args):
    # Exception handling
    try:
      # checking if filename not none
      if self.filename:
        # Reading the data from text area
        data = self.txtarea.get("1.0",END)
        # opening File in write mode
        outfile = open(self.filename,"w")
        # Writing Data into file
        outfile.write(data)
        # Closing File
        outfile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("This text document has saved successfully")
      else:
        self.saveasfile()
    except Exception as e:
      root = tk.Toplevel()  
      root.resizable(0,0)
      root.title("This document was saved.")
      root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='icon.png'))


      labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Saved successfully.")
      label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="This document was saved. :)")
      labelTitle.pack(side="top",fill="x",pady=1)
      label.pack(side="top", fill="x", pady=2)
      B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="#367cca",activebackground='pink', command = root.destroy)
      B1.pack()
  # Defining Save As File Funtion
  def saveasfile(self,*args):
    # Exception handling

    try:
      # Asking for file name and type to save
      untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py"),("HTML file","*.html"),("CSS file","*.css"),("Javascript","*js"),("C++","*cpp")))
      # Reading the data from text area
      data = self.txtarea.get("1.0",END)
      # opening File in write mode
      outfile = open(untitledfile,"w")
      # Writing Data into file
      outfile.write(data)
      # Closing File
      outfile.close()
      # Updating filename as Untitled
      self.filename = untitledfile
      # Calling Set title
      self.settitle()
      # Updating Status
      root = tk.Toplevel()  
      root.resizable(0,0)
      root.title("This document was saved.")
      root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='icon.png'))


      labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Saved successfully.")
      label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="This document was saved. :)")
      labelTitle.pack(side="top",fill="x",pady=1)
      label.pack(side="top", fill="x", pady=2)
      B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="#367cca",activebackground='pink', command = root.destroy)
      B1.pack()
    except Exception as e:
      root = tk.Toplevel()  
      root.resizable(0,0)
      root.title("Sorry there was a problem :(")
      root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='icon.png'))


      labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Failed to save.")
      label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Please try to save this document again.")
      labelTitle.pack(side="top",fill="x",pady=1)
      label.pack(side="top", fill="x", pady=2)
      B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="#367cca",activebackground='pink', command = root.destroy)
      B1.pack()
  # Defining Cut Funtion
  def cut(self,*args):
    self.txtarea.event_generate("<<Cut>>")
  # Defining Copy Funtion
  def copy(self,*args):
          self.txtarea.event_generate("<<Copy>>")
  # Defining Paste Funtion
  def paste(self,*args):
    self.txtarea.event_generate("<<Paste>>")
  # Defining Undo Funtion
  def undo(self,*args):
    # Exception handling
    try:
      # checking if filename not none
      if self.filename:
        # Clearing Text Area
        self.txtarea.delete("1.0",END)
        # opening File in read mode
        infile = open(self.filename,"r")
        # Inserting data Line by line into text area
        for line in infile:
          self.txtarea.insert(END,line)
        # Closing File
        infile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Undone Successfully")
      else:
        # Clearing Text Area
        self.txtarea.delete("1.0",END)
        # Updating filename as None
        self.filename = None
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Undone Successfully")
    except Exception as e:
      root = tk.Toplevel()  
      root.resizable(0,0)
      root.title("Sorry there was a problem :(")
      root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='icon.png'))


      labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Failed to undo.")
      label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Please try again.")
      labelTitle.pack(side="top",fill="x",pady=1)
      label.pack(side="top", fill="x", pady=2)
      B1 = tk.Button(root, text="Exit",font=("ubuntu",28),bg="#367cca",activebackground='pink', command = root.destroy)
      B1.pack()# Creating TK Container
root = tk.Tk()
# Passing Root to TextEditor Class
TextEditor(root)
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='icon.png'))
# Root Window Looping

#This will show a popup when the user press the exit button
def on_closing():
    root = tk.Toplevel()  
    root.resizable(0,0)
    root.title("Confirm to exit the software:")
    root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='icon.png'))


    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Confirm to exit the software:")

    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Are you sure you want to leave this software?")
    label2 = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="If you did not save. Then you will lose data. Please save now!")

    labelTitle.pack(side="top",fill="x",pady=1)
    label2.pack(side="top", fill="x", pady=2)
    label.pack(side="top", fill="x", pady=3)


    B1 = tk.Button(root, text="Yes",font=("ubuntu",28),bg="#367cca",activebackground='pink', command = root.quit)

    B2 = tk.Button(root, text="No",font=("ubuntu",28),bg="#367cca",activebackground='pink', command = root.destroy)
    B1.pack(side=tkinter.LEFT, anchor=CENTER)
    B2.pack(side=tkinter.RIGHT, anchor=CENTER)

#When you press the control S will ask if you where you want to save the document

#This will make the on_closing function work
root.protocol("WM_DELETE_WINDOW", on_closing)




root.mainloop()

