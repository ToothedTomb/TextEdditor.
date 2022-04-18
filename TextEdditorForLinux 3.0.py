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

# Defining TextEditor Class
class TextEditor:
  # Defining Constructor
  def __init__(self,root):
    # Assigning root
    self.root = root
    self.root.configure(bg='pink')  
    # Title of the window
    self.root.title("Basic Text Edditor 3.0!")
    # Window Geometry
    # Initializing filename
    self.filename = None
    # Declaring Title variable
    self.title = StringVar()
    # Declaring Status variable
    self.status = StringVar()
    # Creating Titlebar
    self.titlebar = Label(self.root,textvariable=self.title,font=("Ubuntu",15,"bold"),bd=2,relief=GROOVE)
    # Packing Titlebar to root window
    self.titlebar.pack(side=BOTTOM,fill=BOTH)
    # Calling Settitle Function
    self.settitle()
    # Creating Statusbar
    self.statusbar = Label(self.root,textvariable=self.status,font=("Ubuntu",20,"bold"),bd=2,relief=GROOVE)
    # Packing status bar to root window
    self.statusbar.pack(side=TOP,fill=BOTH)
    # Initializing Status
    self.status.set("Welcome to Basic Text Edditor For Linux and FreeBSD.")
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
    # Adding Seprator
    self.filemenu.add_separator()
    # Adding Exit window Command
    self.filemenu.add_command(label="Exit",command=self.exit)
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
    self.about.add_command(label="About",command=self.AboutThisSoftware)
    self.about.add_command(label="Creator of this software",command=self.creatorofthesoftware)


    # Creating Help Menu
    self.helpmenu = Menu(self.menubar,font=("Ubuntu",23),activebackground="pink",tearoff=0)
    # Creating Scrollbar
    scrol_y = Scrollbar(self.root,orient=VERTICAL)
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
      messagebox.showerror("Failed the open this file!",e)
  # Defining Save File Funtion
  def AboutThisSoftware(self):
    tkinter.messagebox.showinfo("About this software:","This is a free and open source software that is a lightweight text edditor for FreeBSD and Linux. This software was written with Python.") 
  def creatorofthesoftware(self):
    tkinter.messagebox.showinfo("Who made this software:","This software has been made by Jonathan Steadman.") 

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
      messagebox.showerror("Failed to save. (Please save it again)!",e)
  # Defining Save As File Funtion
  def saveasfile(self,*args):
    # Exception handling
    try:
      # Asking for file name and type to save
      untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py"),("HTML file","*.html"),("CSS file","*.css"),("Javascript","*js")))
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
      self.status.set("This text document has been saved!")
    except Exception as e:
      messagebox.showerror("Failed to save. (Please save it again)!",e)
  # Defining Exit Funtion
  def exit(self,*args):
    op = messagebox.askyesno("Note:","Please save before you leave. :)")
    if op>0:
      self.root.destroy()
    else:
      return
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
      messagebox.showerror("Failed to undo",e)
# Creating TK Container
root = tk.Tk()
# Passing Root to TextEditor Class
TextEditor(root)
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='icon.png'))
# Root Window Looping





root.mainloop()
