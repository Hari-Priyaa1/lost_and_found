from tkinter import BOTH, END, Tk, Toplevel, Listbox, Frame, Label, Entry, Button, messagebox,filedialog
from PIL import Image, ImageTk
import sqlite3 as db
import re
from io import BytesIO
fonts = ('Arial', 16, 'bold')
font2 = ('Young Serif', 20,'bold')
root = Tk()
class Home:
    def __init__(self, root):
        self.root = root
        self.op =Frame(self.root)
        self.op.place(x = 0, y = 0 )
        self.img = Image.open('../assets/logo.jpg')
        self.tk_img = ImageTk.PhotoImage(self.img)
        self.lab_img = Label(self.root,image=self.tk_img,width = 1550,height = 1550)
        self.lab_img.pack(fill = BOTH,expand= True)
        self.lab_img.bind("<Configure>", self.resize_image)
        self.conn_user = db.connect('../Database/user.db')
        self.register = Button(self.root, text = 'REGISTER', font = fonts, command = self.open_register)
        self.register.place(relx=1.0,rely=0.0,x = -20, y = 0,anchor='ne')
        self.login = Button(self.root, text = 'LOGIN', font = fonts, command = self.open_login)
        self.login.place(relx=1.0,rely=0.01,x = -20, y = 40,anchor='ne')
    def resize_image(self,event):
        self.new_width = event.width
        self.new_height = event.height
        self.image_resized = self.img.resize((self.new_width, self.new_height))
        self.photo = ImageTk.PhotoImage(self.image_resized)
        self.lab_img.config(image=self.photo)
        self.lab_img.image = self.photo 
    def open_register(self):
        self.op.forget()
        self.fonts = ('Arial',30,'bold')
        self.entry_fonts = ('Arial',24)
        self.register_frame = Frame(self.root, width = 1550, height = 1550)
        self.register_frame.place(x = 0, y = 0 )
        self.reg_img = Image.open('../assets/background.jpg')
        self.reg_img = self.reg_img.resize((1550, 1550))
        self.tk_reg_img = ImageTk.PhotoImage(self.reg_img)
        self.reg_background = Label(self.register_frame, image=self.tk_reg_img)
        self.reg_background.place(x=0, y=0, relwidth=1, relheight=1)
        self.register_name_label = Label(self.register_frame, text="Name:",font = self.fonts, bg = None)
        self.register_name_entry = Entry(self.register_frame,width = 30,font = self.entry_fonts)
        self.register_name_label.place(x = 350, y = 100)
        self.register_name_entry.place(x = 700, y = 100)
        self.register_regd_label = Label(self.register_frame, text="Regd Number:",font = self.fonts, bg = None)
        self.register_regd_entry = Entry(self.register_frame,width = 30,font = self.entry_fonts)
        self.register_regd_label.place(x = 350, y = 200)
        self.register_regd_entry.place(x = 700, y = 200)
        self.register_email_label = Label(self.register_frame, text="Email:",font = self.fonts, bg = None)
        self.register_email_entry = Entry(self.register_frame,width = 30,font = self.entry_fonts)
        self.register_email_label.place(x = 350, y = 300)
        self.register_email_entry.place(x = 700, y = 300)
        self.register_password_label = Label(self.register_frame, text="Password:",font = self.fonts, bg = None)
        self.register_password_entry = Entry(self.register_frame, show="*",width = 30,font = self.entry_fonts)
        self.register_password_label.place(x = 350, y = 400)
        self.register_password_entry.place(x = 700, y = 400)
        self.register_button = Button(self.register_frame, text="Register", font = self.fonts, command= self.register_user)
        self.register_button.place(x = 600, y = 550)
        self.loginButton=Button(self.register_frame,text='Already registered? Log in',font=('Open Sans',20,'bold underline'),cursor = 'hand2',command=self.open_login)
        self.loginButton.place(x=500,y=650)
    def validate_register_data(self):
        self.name = self.register_name_entry.get()
        self.regd_number = self.register_regd_entry.get()
        self.email = self.register_email_entry.get()
        self.password = self.register_password_entry.get()
        def valid_name(name):
            return name.isalpha()
        def is_valid_regd_number(regd):
            return regd.isalnum() and len(regd) == 10
        def is_valid_email(email):
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            return bool(re.match(pattern, email))
        def is_valid_password(pwd):
            return len(pwd) >= 8
        if not valid_name(self.name):
            return False
        if not is_valid_regd_number(self.regd_number):
            return False
        if not is_valid_email(self.email):
            return False
        if not is_valid_password(self.password):
            return False
        return True
    def register_user(self):
        if self.validate_register_data():
            try:
                self.add_user()
                self.open_login()
            except:
                messagebox.showerror('Error','User already exists!')
        else:
            messagebox.showerror('Error',"Enter valid details!!")
            self.open_register()
    def add_user(self):
        self.user_cursor = self.conn_user.cursor()
        self.user_cursor.execute('CREATE TABLE IF NOT EXISTS users(NAME VARCHAR(255), REGD_NO VARCHAR(10) PRIMARY KEY, EMAIL VARCHAR(255), PASSWORD VARCHAR(255))')
        self.user_cursor.execute('INSERT INTO users (NAME, REGD_NO, EMAIL, PASSWORD) VALUES(?,?,?,?)',(self.name, self.regd_number,self.email,self.password))
        self.conn_user.commit()
        self.conn_user.close()
    def open_login(self):
        self.op.forget()
        self.fonts = ('Arial',30,'bold')
        self.entry_fonts = ('Arial',24)
        self.login_frame = Frame(self.root, width = 1550, height = 1550)
        self.login_frame.place(x = 0, y = 0 )
        self.login_img = Image.open('../assets/background.jpg')
        self.login_img = self.login_img.resize((1550, 1550))
        self.tk_login_img = ImageTk.PhotoImage(self.login_img)
        self.login_background = Label(self.login_frame, image=self.tk_login_img)
        self.login_background.place(x=0, y=0, relwidth=1, relheight=1)
        self.login_email_label = Label(self.login_frame, text="Email:",font = self.fonts)
        self.login_email_entry = Entry(self.login_frame, font = self.entry_fonts)
        self.login_email_label.place(x = 350, y = 200)
        self.login_email_entry.place(x = 700, y = 200)
        self.login_password_label = Label(self.login_frame, text="Password:",font = self.fonts)
        self.login_password_entry = Entry(self.login_frame, show="*",font = self.entry_fonts)
        self.login_password_label.place(x = 350, y = 300)
        self.login_password_entry.place(x = 700, y = 300)
        self.login_button = Button(self.login_frame, text="Login", font = self.fonts,command = self.validate_login)
        self.login_button.place(x = 600, y = 450)
        self.registerButton=Button(self.login_frame,text='New user? Register',cursor = 'hand2',font=('Open Sans',20,'bold underline'),command=self.open_register)
        self.registerButton.place(x=525,y=575)
    def validate_login(self):
        self.login_email = self.login_email_entry.get()
        self.pwd = self.login_password_entry.get()
        self.cursor = self.conn_user.cursor()
        self.cursor.execute('SELECT PASSWORD FROM USERS WHERE email = (?)',(self.login_email,))
        self.info = self.cursor.fetchone()[0]
        if self.pwd == self.info:
            self.data_entry()
        else:
            messagebox.showerror('Invalid login','Enter valid credentials')
    def data_entry(self):
        self.login_frame.forget()
        self.fonts = ('Arial',30,'bold')
        self.entry_fonts = ('Arial',24)
        self.entry_frame = Frame(self.root,width= 1550,height = 1550)
        self.entry_frame.place(x = 0, y = 0)
        self.entry_img = Image.open('../assets/background.jpg')
        self.entry_img = self.entry_img.resize((1550, 1550))
        self.tk_entry_img = ImageTk.PhotoImage(self.entry_img)
        self.entry_background = Label(self.entry_frame, image=self.tk_entry_img)
        self.entry_background.place(x=0, y=0, relwidth=1, relheight=1)
        self.item_label = Label(self.entry_frame, text = 'ITEM:',font = self.fonts)
        self.item_entry = Entry(self.entry_frame,font = self.entry_fonts)
        self.item_label.place(x = 350, y = 100)
        self.item_entry.place(x = 700, y = 100)
        self.item_des_label = Label(self.entry_frame, text = 'DESCRIPTION:',font = self.fonts)
        self.item_des_entry = Entry(self.entry_frame,font = self.entry_fonts)
        self.item_des_label.place(x = 350, y = 200)
        self.item_des_entry.place(x = 700, y = 200)
        self.image_entry = Button(self.entry_frame,text = "UPLOAD IMAGE", font=self.fonts,command = self.select_image)
        self.image_label = Label(self.entry_frame,width = 0, height = 0)
        self.image_label.place(x = 900, y = 300)
        self.image_entry.place(x = 550, y = 300)
        self.is_lost = False
        self.lost = Button(self.entry_frame, text = 'LOST', font = self.fonts, command = self.set_lost)
        self.found = Button(self.entry_frame,text = 'FOUND',font = self.fonts,command = self.enter_to_db)
        self.lost.place(x = 350, y = 450)
        self.found.place(x = 900, y = 450)
        self.conn_item = db.connect('../Database/items.db')
        self.search_item_entry = Entry(self.entry_frame,font = self.entry_fonts)
        self.search_item_entry.place(x = 970,y = 10)
        self.search_button = Button(self.entry_frame,text = "Search",font = ('Arial',15,'bold'), command = self.enter_search)
        self.search_button.place(x = 1350, y = 10)
    def enter_search(self):
        self.search_query = self.search_item_entry.get()
        self.display_search_results(self.search_query)    

    def set_lost(self):
        self.is_lost = True
        self.enter_to_db()
    def select_image(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if self.file_path:
            with open(self.file_path, 'rb') as file:
                self.image_data = file.read()
            self.item_image = Image.open(self.file_path)
            self.item_image = self.item_image.resize((70,70))
            self.tk_item_img = ImageTk.PhotoImage(self.item_image)
            self.image_label.config(image = self.tk_item_img)
            self.image_label.image = self.tk_item_img
    def enter_to_db(self):
        self.item = self.item_entry.get()
        self.item_des = self.item_des_entry.get()
        if self.is_lost:
            self.status = 'LOST'
        else:
            self.status = 'FOUND'
        self.item_cursor = self.conn_item.cursor()
        self.item_cursor.execute('CREATE TABLE IF NOT EXISTS items(EMAIL VARCHAR(255),ITEM VARCHAR(255) NOT NULL,DESCRIPTION VARCHAR(1000) NOT NULL,IMAGE BLOB DEFAULT NULL, STATUS VARCHAR(5))')
        try:
            if self.image_data:
                self.item_cursor.execute('INSERT INTO items (EMAIL,ITEM,DESCRIPTION,IMAGE,STATUS) VALUES(?,?,?,?,?)',(self.login_email,self.item,self.item_des,self.image_data,self.status))
            else:
                self.item_cursor.execute('INSERT INTO items (EMAIL,ITEM,DESCRIPTION,STATUS) VALUES(?,?,?,?)',(self.login_email,self.item,self.item_des,self.status))
        except:
            messagebox.showerror('Invalid Entry','Enter complete details')
        self.conn_item.commit()
        self.display_search_results(self.item)
        
        

    def display_search_results(self,query):
        self.query = query
        self.item_cursor = self.conn_item.cursor()
        self.item_cursor.execute("SELECT ITEM,DESCRIPTION,EMAIL,STATUS FROM items WHERE ITEM LIKE ? OR DESCRIPTION LIKE ?", ('%' + self.query + '%', '%' + self.query + '%'))
        self.search_results = self.item_cursor.fetchall()
        if len(self.search_results) == 0:
            messagebox.showinfo('No Match', 'No results found.')
        else:
            self.search_results_window = Toplevel(root)
            self.search_results_window.title('Search Results',fonts = 'Open Sans')
            self.results_label = Label(self.search_results_window, text='Search Results:')
            self.results_label.pack()
            self.results_listbox = Listbox(self.search_results_window, width=1550, height=1550)
            self.results_listbox.pack()
            x_pos, y_pos = 0,0
            for result in self.search_results:
                self.results_listbox.insert(END, f'Item: {result[0]}\n Description: {result[1]}\n Email: {result[2]}\n Status: {result[3]}')
                self.item_cursor.execute('SELECT data FROM images WHERE item = (?) AND Description = (?) AND Email = (?) AND Status = (?)',(result[0],result[1],result[2],result[3]))  # Assuming the image is stored with id 1
                self.image_data = self.item_cursor.fetchone()[0]
                self.image = Image.open(BytesIO(self.image_data))
                self.image = self.image.resize((50,50))
                self.image = ImageTk.PhotoImage(self.image)
                self.img_label = Label(self.search_results_window,image = self.image)
                self.img_label.pack(x = x_pos, y = y_pos)
                y_pos += 52
            self.conn_item.close()


root.resizable(1550,1550)
root.title('LOST AND FOUND')
home = Home(root)
root.mainloop()