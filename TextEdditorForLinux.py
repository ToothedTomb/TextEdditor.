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
from PIL import Image
from PIL import ImageTk
from tkinter import font
from nltk.corpus import words
import re
from tkcolorpicker import askcolor
import nltk
nltk.download('words')
from nltk.corpus import words
#-------------------------------------
word_list = words.words()
print(word_list[:10])
#Making the popups
def check_Spelling(text_widget):
    text = text_widget.get("1.0", "end-1c")
    words_in_text = text.split()
    misspelled = [word for word in words_in_text if word.lower() not in word_list]

    # Clear existing misspelled tags
    for tag in text_widget.tag_names():
        if tag.startswith("misspelled"):
            text_widget.tag_remove(tag, "1.0", "end")

    # Apply misspelled tags
    for word in misspelled:
        start_index = "1.0"
        while True:
            start_index = text_widget.search(word, start_index, nocase=1, stopindex="end")
            if not start_index:
                break
            end_index = f"{start_index}+{len(word)}c"
            text_widget.tag_add("misspelled", start_index, end_index)
            start_index = end_index

    text_widget.tag_config("misspelled", foreground="red")

def whoMadeThisSoftware():
    root = tk.Toplevel()  
    root.resizable(0,0)
    root.title("Who made this software?")
    root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='assets/iconForApp.png'))


    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Who made this software?")
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="Jonathan Steadman has made this software.")
    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)

def WhatIsThisSoftware():
    root = tk.Toplevel()  
    root.resizable(0,0)
    root.title("What is this software?")
    root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='assets/iconForApp.png'))


    labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="What is this software?")
    label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="This software is a free and open source basic text editor for Linux.")
    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)

def KeyboardShortcuts():
      root = tk.Toplevel()  
      root.resizable(0,0)
      root.title("Keyboard shortcuts.")
      root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='assets/iconForApp.png'))


      labelTitle = ttk.Label(root,font=("Ubuntu", 26,"bold","underline"),anchor='center', text="Keyboard shortcuts.")
      label = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="'Control + C' will copy the text.")
      label2 = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="'Control + V' will paste the text.")      
      label3 = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="'Control + O' will allow you to open a document.")
      label4 = ttk.Label(root,font=("Ubuntu", 16,"bold",),anchor='center', text="'Control + S' will save your document.")

      labelTitle.pack(side="top",fill="x",pady=1)
      label.pack(side="top", fill="x", pady=2)
      label2.pack(side="top", fill="x", pady=3)
      label3.pack(side="top", fill="x", pady=4)
      label4.pack(side="top",fill="x",pady=5)



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
    self.root.title("Basic Text Editor 9.0!")
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
    self.titlebar.pack(side=TOP,fill=BOTH)
    # Calling Settitle Function
    self.settitle()

    # Packing status bar to root window
    # Initializing Status
    
    self.title.set("Please save or open a document.")

    # Creating Menubar
    self.menubar = Menu(self.root,font=("Ubuntu",23,"bold"),activebackground="pink")
    #Icons on the nav bar
    File_image = Image.open("assets/folder.png")
    File_image = File_image.resize((36, 36))
    File_icon = ImageTk.PhotoImage(File_image)

    Edit_image = Image.open("assets/edit.png")
    Edit_image = Edit_image.resize((36,36))
    Edit_icon = ImageTk.PhotoImage(Edit_image)

    About_image = Image.open("assets/info.png")
    About_image = About_image.resize((36,36))
    About_icon = ImageTk.PhotoImage(About_image)
    #Icons on the subheading of the nav bar
    New_Document_image = Image.open("assets/new-document.png")
    New_Document_image = New_Document_image.resize((36,36))
    New_Document_icon = ImageTk.PhotoImage(New_Document_image)

    Open_Document_image = Image.open("assets/open-folder-with-document.png")
    Open_Document_image= Open_Document_image.resize((36,36))
    Open_Document_icon = ImageTk.PhotoImage(Open_Document_image)
    
    
    Save_Document_image = Image.open("assets/save.png")
    Save_Document_image= Save_Document_image.resize((36,36))
    Save_Document_icon = ImageTk.PhotoImage(Save_Document_image)

    SaveAs_Document_image = Image.open("assets/save.png")
    SaveAs_Document_image= SaveAs_Document_image.resize((36,36))
    SaveAs_Document_icon = ImageTk.PhotoImage(SaveAs_Document_image)


    Cut_Image = Image.open("assets/scissors.png")
    Cut_Image= Cut_Image.resize((36,36))
    Cut_icon = ImageTk.PhotoImage(Cut_Image)

    Copy_Image = Image.open("assets/copy.png")
    Copy_Image= Copy_Image.resize((36,36))
    Copy_Icon = ImageTk.PhotoImage(Copy_Image)

    Undo_Image = Image.open("assets/undo-circular-arrow.png")
    Undo_Image = Undo_Image.resize((36,36))
    Undo_Icon = ImageTk.PhotoImage(Undo_Image)
    

    Font_Image = Image.open("assets/font.png")
    Font_Image = Font_Image.resize((36,36))
    Font_Icon = ImageTk.PhotoImage(Font_Image)

    Bold_Image = Image.open("assets/font-style-bold.png")
    Bold_Image = Bold_Image.resize((36,36))
    Bold_Icon = ImageTk.PhotoImage(Bold_Image)

    Italic_Image = Image.open("assets/italic-font.png")
    Italic_Image = Italic_Image.resize((36,36))
    Italic_Icon = ImageTk.PhotoImage(Italic_Image)

    Marker_Image = Image.open("assets/marker.png")
    Marker_Image = Marker_Image.resize((36,36))
    Marker_Icon = ImageTk.PhotoImage(Marker_Image)

    Underline_Image = Image.open("assets/underline.png")
    Underline_Image = Underline_Image.resize((36,36))
    Underline_Icon = ImageTk.PhotoImage(Underline_Image)

    BiggerFont_Image = Image.open("assets/up-arrow.png")
    BiggerFont_Image = BiggerFont_Image.resize((36,36))
    BiggerFont_Icon = ImageTk.PhotoImage(BiggerFont_Image)
    
    SmallerFont_Image = Image.open("assets/down-arrow.png")
    SmallerFont_Image = SmallerFont_Image.resize((36,36))
    SmallerFont_Icon = ImageTk.PhotoImage(SmallerFont_Image)
    
    Strickthrough_Image = Image.open("assets/strikethrough.png")
    Strickthrough_Image = Strickthrough_Image.resize((36,36))
    Strickthrough_Icon = ImageTk.PhotoImage(Strickthrough_Image)

    Spell_Image = Image.open("assets/spell.png")
    Spell_Image = Spell_Image.resize((36,36))
    Spell_Icon = ImageTk.PhotoImage(Spell_Image)
    # Configuring menubar on root window
    self.root.config(menu=self.menubar)
    # Creating File Menu
    self.filemenu = Menu(self.menubar,font=("Ubuntu",23,"bold"),activebackground="pink",tearoff=0)
    # Adding New file Command
    self.filemenu.add_command(image=New_Document_icon, label="New",compound=tk.LEFT,command=self.newfile)
    self.New_Document_icon = New_Document_icon
    # Adding Open file Command
    self.filemenu.add_command(image=Open_Document_icon,label="Open",compound=LEFT,command=self.openfile)
    self.Open_Document_icon = Open_Document_icon

    # Adding Save File Command
    self.filemenu.add_command(image=Save_Document_icon,label="Save", compound=LEFT,command=self.savefile)
    self.Save_Document_icon = Save_Document_icon
    # Adding Save As file Command
    self.filemenu.add_command(image=SaveAs_Document_icon,label="Save As", compound=LEFT,command=self.saveasfile)
    self.SaveAs_Document_icon = SaveAs_Document_icon

    # Cascading filemenu to menubar
    self.menubar.add_cascade(image=File_icon, compound=tk.LEFT, menu=self.filemenu)
    self.file_icon = File_icon
    # Creating Edit Menu
    self.editmenu = Menu(self.menubar,font=("Ubuntu",23,"bold"),activebackground="pink",tearoff=0)
    # Adding Cut text Command
    self.editmenu.add_command(label="Cut",image=Cut_icon,compound=tk.LEFT,command=self.cut)
    self.Cut_icon = Cut_icon
    # Adding Copy text Command
    self.editmenu.add_command(label="Copy",image=Copy_Icon,compound=tk.LEFT,command=self.copy)
    self.Copy_Icon = Copy_Icon
    # Adding Paste text command
    self.editmenu.add_command(label="Paste",image=Copy_Icon,compound=tk.LEFT,command=self.paste)
    self.Copy_Icon = Copy_Icon
    # Adding Seprator
    self.editmenu.add_separator()
    # Adding Undo text Command
    self.editmenu.add_command(label="Undo",image =Undo_Icon, compound=tk.LEFT,command=self.undo)
    self.Undo_Icon = Undo_Icon
    self.editmenu.add_separator()
    self.editmenu.add_command(label="Spelling errors",image=Spell_Icon, compound=tk.LEFT,command=self.check_spelling)
    self.Spell_Icon = Spell_Icon



    # Cascading editmenu to menubar
    self.menubar.add_cascade(image=Edit_icon, compound=tk.LEFT, menu=self.editmenu)
    self.Edit_icon = Edit_icon

    self.about = Menu(self.menubar,font=("Ubuntu",23,"bold"),activebackground="pink",tearoff=0)
    self.fontsSetting = Menu(self.menubar,font=("Ubuntu",23,"bold"),activebackground="pink",tearoff=0)

    self.menubar.add_cascade(image=Font_Icon, compound=tk.LEFT, menu=self.fontsSetting)
    self.Font_Icon = Font_Icon

    self.menubar.add_cascade(image=About_icon,menu=self.about)
    self.About_icon = About_icon
    self.about.add_command(label="About this software?",image=About_icon,compound=tk.LEFT,command=WhatIsThisSoftware)
    self.About_icon = About_icon

    self.about.add_command(label="Who made this software?",image=About_icon,compound=tk.LEFT,command= whoMadeThisSoftware)
    self.About_icon = About_icon    
    self.about.add_command(label="Keyboard shortcuts",image=About_icon,compound=tk.LEFT,command= KeyboardShortcuts)
    self.About_icon = About_icon



    # Creating Help Menu
    self.helpmenu = Menu(self.menubar,font=("Ubuntu",23,"bold"),activebackground="pink",tearoff=0)
    # Creating Scrollbar





    scrol_y = Scrollbar(self.root,orient=VERTICAL,background="#367cca", activebackground="pink",width="20")
    # Creating Text Area
    self.FontSize = 20
    
    self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("ubuntu",size:=self.FontSize),relief=GROOVE)
    # Packing scrollbar to root window
    scrol_y.pack(side=RIGHT,fill=Y)
    # Adding Scrollbar to text area
    scrol_y.config(command=self.txtarea.yview)
    # Packing Text Area to root window
    self.txtarea.pack(fill=BOTH,expand=1)
  # Defining settitle function
    self.underline = font.Font(family="ubuntu",size=self.FontSize,underline=89)
    self.italic_font = font.Font(family="ubuntu",size=self.FontSize,slant="italic")
    self.bold_font = font.Font(family="ubuntu", size=self.FontSize, weight='bold')
    self.Strikethrough = font.Font(family="ubuntu",size=self.FontSize,overstrike=89)

    def update_fonts():
      self.txtarea.configure(font=font.Font(family="Ubuntu",size=self.FontSize))
      self.italic_font = font.Font(family="ubuntu",size=self.FontSize,slant="italic")
      self.bold_font = font.Font(family="ubuntu", size=self.FontSize, weight='bold')
      self.underline = font.Font(family="ubuntu",size=self.FontSize,underline=89)
      self.Strikethrough = font.Font(family="ubuntu",size=self.FontSize,overstrike=89)

    def increaseFont():
        self.FontSize += 10
        update_fonts()
      #self.txtarea.tag_config(size=self.FontSize)
    def decreaseFont():
       self.FontSize -= 10
       update_fonts()
    def underline_text():
      try:
        if self.txtarea.tag_ranges(tk.SEL):
          current_tags = self.txtarea.tag_names("sel.first")
          if "underline" in current_tags:
            self.txtarea.tag_remove("underline", "sel.first", "sel.last")
          else:
            self.txtarea.tag_add("underline", "sel.first", "sel.last")
            self.txtarea.tag_configure("underline", font=self.underline)
      except tk.TclError:
            pass  # No text selected or other error
    #self.bold_font = font.Font(family="ubuntu", size=20, weight='bold')
    def bold_text():
       try:
        if self.txtarea.tag_ranges(tk.SEL):
          current_tags = self.txtarea.tag_names("sel.first")
          if "bold" in current_tags:
            self.txtarea.tag_remove("bold", "sel.first", "sel.last")
          else:
            self.txtarea.tag_add("bold", "sel.first", "sel.last")
            self.txtarea.tag_configure("bold", font=self.bold_font)
       except tk.TclError:
            pass  # No text selected or other error
    def italic_text():
       try:
        if self.txtarea.tag_ranges(tk.SEL):
          current_tags = self.txtarea.tag_names("sel.first")
          if "italic" in current_tags:
            self.txtarea.tag_remove("italic", "sel.first", "sel.last")
          else:
            self.txtarea.tag_add("italic", "sel.first", "sel.last")
            self.txtarea.tag_configure("italic", font=self.italic_font)
       except tk.TclError:
            pass  # No text selected or other error
    # Future update need to do a lot of config with the text area lol. 
    # self.underline_font= font.Font(family="Ubuntu",size=20, underline=1
    def add_highlighter():
       try:
        if self.txtarea.tag_ranges(tk.SEL):
          color = askcolor()[1]
          if color:
             tag_name = f"highlight_{color}"
             self.txtarea.tag_add(tag_name, "sel.first", "sel.last")
             self.txtarea.tag_config(tag_name, background=color)
            #self.txtarea.tag_config("start", background= "pink")
       except tk.TclError:
            pass  # No text selected or other error
    def Strikethrough():
       try:
        if self.txtarea.tag_ranges(tk.SEL):
          current_tags = self.txtarea.tag_names("sel.first")
          if "strikethrough" in current_tags:
            self.txtarea.tag_remove("strikethrough", "sel.first", "sel.last")
          else:
            self.txtarea.tag_add("strikethrough", "sel.first", "sel.last")
            self.txtarea.tag_config("strikethrough", font=self.Strikethrough)
       except tk.TclError:
            pass  # No text selected or other error
    def RightClickMenu(e):
       my_menu.tk_popup(e.x_root, e.y_root)
    
    my_menu = Menu(self.menubar,font=("Ubuntu",23,"bold"),activebackground="pink",tearoff=0)

    # Adding Copy text Command
    my_menu.add_command(label="Copy",image=Copy_Icon,compound=tk.LEFT,command=self.copy)
    self.Copy_Icon = Copy_Icon
    # Adding Paste text command
    my_menu.add_command(label="Paste",image=Copy_Icon,compound=tk.LEFT,command=self.paste)
    self.Copy_Icon = Copy_Icon

    my_menu.add_command(label="Cut",image=Cut_icon,compound=tk.LEFT,command=self.cut)
    self.Cut_icon = Cut_icon
    my_menu.add_separator()
    my_menu.add_command(label="Spelling errors",image=Spell_Icon, compound=tk.LEFT,command=self.check_spelling)
    self.Spell_Icon = Spell_Icon



    # Adding Seprator
    # Adding Undo text Command
  
    # Cascading editmenu to menubar
    self.fontsSetting.add_command(label="Bold",image=Bold_Icon,compound=tk.LEFT,command=bold_text)
    self.Bold_Icon = Bold_Icon
    self.fontsSetting.add_command(label="Italic",image= Italic_Icon, compound=tk.LEFT,command=italic_text )
    self.Italic_Icon = Italic_Icon
    self.fontsSetting.add_command(label="Highlight",image=Marker_Icon,compound=tk.LEFT, command=add_highlighter)
    self.Marker_Icon = Marker_Icon
    self.fontsSetting.add_command(label="Underline",image=Underline_Icon, compound=tk.LEFT,command=underline_text)
    self.Underline_Icon = Underline_Icon
    self.fontsSetting.add_command(label="Strikethrough",image=Strickthrough_Icon, compound=tk.LEFT,command=Strikethrough)
    self.Strickthrough_Icon = Strickthrough_Icon
    self.fontsSetting.add_command(label="Bigger Text",image=BiggerFont_Icon, compound=tk.LEFT, command=increaseFont)
    self.BiggerFont_Icon = BiggerFont_Icon
    self.fontsSetting.add_command(label="Smaller Text",image=SmallerFont_Icon,compound=tk.LEFT,command=decreaseFont)
    self.SmallerFont_Icon = SmallerFont_Icon
    self.root.bind('<Control-s>', self.savefile)
    self.root.bind('<Control-o>',self.openfile)
    self.root.bind('<Button-3>',RightClickMenu)


  
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
      root.title("Opened successfully.")
      root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='assets/iconForApp.png'))


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
      root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='assets/iconForApp.png'))


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
      root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='assets/iconForApp.png'))


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
      root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='assets/iconForApp.png'))


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
  def check_spelling(self,*args):
    check_Spelling(self.txtarea)
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
      else:
        # Clearing Text Area
        self.txtarea.delete("1.0",END)
        # Updating filename as None
        self.filename = None
        # Calling Set title
        self.settitle()
        # Updating Status
    except Exception as e:
      return()
root = tk.Tk()
# Passing Root to TextEditor Class
TextEditor(root)
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='assets/iconForApp.png'))
# Root Window Looping

#This will show a popup when the user press the exit button
def on_closing():
    root = tk.Toplevel()  
    root.resizable(0,0)
    root.title("Confirm to exit the software:")
    root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='assets/iconForApp.png'))


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

