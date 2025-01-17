from tkinter import Tk, Frame, Label, Entry, Button, messagebox
from PIL import Image, ImageTk


fonts = ('Times New Roman.', 10, 'bold')
font2 = ('Young Serif', 20,'bold')
root = Tk()
class Home:
    def __init__(self, root):
        self.root = root
        self.op =Frame(self.root, width = 350, height = 500)
        self.op.place(x = 0, y = 0 )
        self.txt = Label(self.op,text = 'LOST AND FOUND',bg = 'black',fg = 'white',font = font2)
        self.txt.place(x = 100,y= 20)
        self.enter = Button(self.op, text = 'ENTER', font = fonts, command = self.open)
        self.enter.place(x = 140, y = 180)
    def open(self):
        self.op.destroy()
        self.left_up =Frame(self.root, width = 350, height = 300)
        self.left_up.place(x = 0, y = 0 )
        self.lost = Label(self.left_up,text = 'LOST!!!',bg = 'black',fg = 'white',font = fonts)
        self.lost.place(x = 100,y= 20)
    #regd number and entry
        self.regd_no = Label(self.left_up, text = 'REGD NUMBER', fg ='black', font = fonts,width = 12)
        self.regd_no.place(x = 10, y = 50)
        self.regd_no_entry = Entry(self.left_up, width = 10, font = fonts)
        self.regd_no_entry.place(x = 120, y = 50)
    #mob num and entry
        self.mob_no = Label(self.left_up, text = 'MOBILE',  fg ='black', font = fonts, width = 12)
        self.mob_no.place(x = 10, y = 80)
        self.mob_no_entry = Entry(self.left_up, width = 10, font = fonts)
        self.mob_no_entry.place(x = 120, y = 80)
    #lost item and entry
        self.item = Label(self.left_up, text = 'LOST ITEM', fg ='black', font = fonts,width = 12)
        self.item.place(x = 10, y = 110)
        self.item_entry = Entry(self.left_up, width = 15, font = fonts)
        self.item_entry.place(x = 120, y = 110)
    #description and entry
        self.des = Label(self.left_up, text = 'DESCRIPTION',  fg ='black', font = fonts, width = 12)
        self.des.place(x = 10, y = 140)
        self.des_entry = Entry(self.left_up, width = 45,font = fonts)
        self.des_entry.place(x = 10, y = 170)
    #lost submit button
        self.lost_submit_btn = Button(self.left_up, text = 'SUBMIT', font = fonts, command = self.lost_submit)
        self.lost_submit_btn.place(x = 120, y = 200)

    

        self.root = root
        self.left_down =Frame(self.root, width = 350, height = 301)
        self.left_down.place(x = 0, y = 300 )
        self.found = Label(self.left_down ,text = 'FOUND!!!',bg = 'black',fg = 'white',font = fonts)
        self.found.place(x = 100,y= 20)
    #regd number and entry
        self.regd_no = Label(self.left_down, text = 'REGD NUMBER', fg ='black', font = fonts,width = 12)
        self.regd_no.place(x = 10, y = 50)
        self.regd_no_entry = Entry(self.left_down, width = 10, font = fonts)
        self.regd_no_entry.place(x = 120, y = 50)
    #mob num and entry
        self.mob_no = Label(self.left_down, text = 'MOBILE',  fg ='black', font = fonts, width = 12)
        self.mob_no.place(x = 10, y = 80)
        self.mob_no_entry = Entry(self.left_down, width = 10, font = fonts)
        self.mob_no_entry.place(x = 120, y = 80)
    #found item and entry
        self.item = Label(self.left_down, text = 'FOUND ITEM', fg ='black', font = fonts,width = 12)
        self.item.place(x = 10, y = 110)
        self.item_entry = Entry(self.left_down, width = 15, font = fonts)
        self.item_entry.place(x = 120, y = 110)
    #description and entry
        self.des = Label(self.left_down, text = 'DESCRIPTION',  fg ='black', font = fonts, width = 12)
        self.des.place(x = 10, y = 140)
        self.des_entry = Entry(self.left_down, width = 45,font = fonts)
        self.des_entry.place(x = 10, y = 170)
    #found submit button
        self.found_submit_btn = Button(self.left_down, text = 'SUBMIT', font = fonts, command = self.found_submit)
        self.found_submit_btn.place(x = 120, y = 200)

    def lost_submit(self):
           self.left_up.destroy()
           self.left_down.destroy()
           lost_msg = LostMsg(root)
           
           

    def found_submit(self):
           self.left_up.destroy()
           self.left_down.destroy()
           lost_msg = FoundMsg(root)
        
class LostMsg:
    def __init__(self,root):
        self.root = root
        self.frame =Frame(self.root, width = 450, height = 300)
        self.frame.place(x = 0, y = 0 )
        messagebox.showinfo("Item added")
        
class FoundMsg:
    def __init__(self,root):
        self.root = root
        self.frame =Frame(self.root, width = 450, height = 300)
        self.frame.place(x = 0, y = 0 )
        messagebox.showinfo("Item added")


root.geometry('400x550+550+200')
root.title('LOST AND FOUND')
home = Home(root)
root.mainloop()