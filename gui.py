import pgenerator
# creating all dependencies
pgenerator_obj1 = pgenerator.SetDependencies()
pgenerator_obj1.setFiles()

# build-in  packages
import tkinter as tk
import tkinter.messagebox as msgbox
from  tkinter import ttk 
import sys

# custom headers
import pstore

# functions


# login section starts
def logInAsAdmin():
    """
    Create a login pannel for log in as admin.
    this section will work only when user open the app and want to use features
    like save password for the first time. after log in one time it will not work again
    untill the program is closed.
    """
    # functions of logInAsAdmin()
    
    # 
    def setFocus2admin_password_entry(*args):
        """
        set set the Focus admin_password_entry
        """
        admin_password_entry.focus()

    def modifyText(adminWindowCustomFontForText: tuple, txtObjects: tuple) -> None:
        """
        modify texts of labels
        """
        # ADMIN_WINDOW_TEXT_BG_COLOR: handle the meterial view by giving the text field a solid color in front of the
        #       background color. for setting the meterial view we need to match the bg color 
        #       with the applied solid color.
        ADMIN_WINDOW_TEXT_BG_COLOR = "#6495ED"

        for obj in txtObjects:
            obj.config(font=adminWindowCustomFontForText, highlightbackground=ADMIN_WINDOW_TEXT_BG_COLOR, bg=ADMIN_WINDOW_TEXT_BG_COLOR)


    def adminRegister():
        """
        take username and password and save to admin.txt file
        """
        with open('admin.txt', 'w') as f:
            f.write(admin_username_entry.get()+'\n') # write username
            f.write(admin_password_entry.get()+'\n') # write password
            msgbox.showinfo('Registration Complete', f'You have successfully registered as {admin_username_entry.get()}\U0001F600')
            login_wn.destroy() # destroy logInAsAdmin window

    def adminLogin():
        f = open('admin.txt', 'r')
        admin_username_from_txt = f.readline()[:-1] # removing last char cause it is \n at last of every line
        admin_password_from_txt = f.readline()[:-1] #                           ||
        f.close()
        if admin_username_from_txt == admin_username_entry.get() and admin_password_from_txt == admin_password_entry.get():
            # seting asAdmin = True. from now no subwindow need login
            global asAdmin
            asAdmin = True
            msgbox.showinfo("LOGIN", "Complete .")
            login_wn.destroy() # destroy logInAsAdmin window
        else:
            msgbox.showinfo("Error", "Wrong username or password")
    
    def logInOrRegesterButton():
        """
        check status of admin file. if it has already username and password then
        return login signal. else return register signal
        """
        with open('admin.txt', 'r') as f:
            if len(f.readlines()) == 2: # size will be 2 if and only if user and pass present
                return 'login'
            else:
                return 'Register'
    
    # admin gui maintaining properties
    ADMIN_WINDOW_BG_COLOR = "#5DADE2"
    ADMIN_WINDOW_WIDTH = 280
    ADMIN_WINDOW_HEIGHT = 250
    ADMIN_WINDOW_TEXT_FONT = ("Montserrat", 12)

    # setup tkinter
    login_wn = tk.Tk() # login_wn = login_window
    login_wn.minsize(ADMIN_WINDOW_WIDTH, ADMIN_WINDOW_HEIGHT)
    login_wn.maxsize(ADMIN_WINDOW_WIDTH, ADMIN_WINDOW_HEIGHT)
    login_wn.configure(bg=ADMIN_WINDOW_BG_COLOR)
    login_wn.title("ADMIN Pannel")

    # username
    #         lable
    admin_username_lable = tk.Label(login_wn, text="Username: ", bg=ADMIN_WINDOW_BG_COLOR)
    admin_username_lable.grid(row=0, column=0, padx=10, pady=10)
    #         entry
    admin_username_entry = tk.Entry(login_wn)
    admin_username_entry.grid(row=0, column=1, padx=10, pady=10)
    admin_username_entry.focus()
    admin_username_entry.bind('<Return>', setFocus2admin_password_entry)


    # password
    #         lable
    admin_password_lable = tk.Label(login_wn, text="Password: ", bg=ADMIN_WINDOW_BG_COLOR)
    admin_password_lable.grid(row=1, column=0, padx=10, pady=10)
    #         entry
    admin_password_entry = tk.Entry(login_wn)
    admin_password_entry.grid(row=1, column=1, padx=10, pady=10)

    # modify the text of labels
    modifyText(ADMIN_WINDOW_TEXT_FONT, (admin_username_lable, admin_password_lable))

    # if admin.txt is empty then no log in data is present. in this case program will show
    # register button instead of login button
    if logInOrRegesterButton() == 'login':
        # login button
        tk.Button(login_wn, text="Login", command=adminLogin, font=ADMIN_WINDOW_TEXT_FONT).grid(row=3, columnspan=2, pady=10)
    else:
        # register button
        tk.Button(login_wn, text="Register", command=adminRegister, font=ADMIN_WINDOW_TEXT_FONT).grid(row=3, columnspan=2, pady=10)

    login_wn.mainloop()
    # login section end

def password_Insert(*args):
    """
    clean password showing entry and display generated password
    """
    # cleaning password showing entry for new password
    generated_password_entry.delete(0, "end")
    if len(password_len.get()) > 0:
        # initializing object. this object will create required password
        pass_object = pgenerator.PGenerator(int(password_len.get()))
        generated_password_entry.insert(0, str(pass_object.password))


def copy_Pass():
    """
    copy password into clip board and popup status notification
    """
    try:
        root = generated_password_entry.winfo_toplevel() # Get the root window
        root.clipboard_clear() # Clear the clipboard
        # generated_password_entry.get() will be 'Too Short' only if password_len.get() < 4
        if (generated_password_entry.get() != 'Too Short' and generated_password_entry
            .get() != ''):
            root.clipboard_append(generated_password_entry.get()) # Append the text to the clipboard
            msgbox.showinfo("Copy to Clipboard", "Data copied to clipboard!")
        else:
            # cleaning clip board as the it hold 'Too Short' and it is not a password
            root.clipboard_clear()
            msgbox.showinfo("Not a password", "Size of the password should greater than 3!")
    except Exception as e:
        msgbox.showerror("Error", f"Error copying to clipboard: {str(e)}")


def enableSaveButton():
    """
    enable save button
    """
    save_button.config(state=tk.NORMAL)

    
def savePassword():
    """
    popup username and password save page 
    """
    def distoryAndEnable_Save_Button():
        """
        enable savebutton & destroy save_wn
        NOTE: USE ONLY FOR SAVE_WN & INSIDE savePassword()
        """
        enableSaveButton()
        save_wn.destroy()

    # check if username and password present in the entry
    def checker():
        if len(save_wn_username_entry.get()) == 0:
            msgbox.showinfo("Error", "No Username to save!")
        elif len(save_wn_pasword_entry.get()) == 0:
            msgbox.showinfo("Error", "No Password to save!")
        else:
            # save data in store
            pstore_obj = pstore.PStore()
            # saving username and password
            pstore_obj.pStore(save_wn_username_entry.get(), save_wn_pasword_entry.get())
            msgbox.showinfo("Done", "Password Saved")
            distoryAndEnable_Save_Button()
    
    # save_wn gui maintaining properties
    SAVE_WINDOW_BG_COLOR = "#BCF4BB"
    SAVE_WINDOW_WIDTH = 280
    SAVE_WINDOW_HEIGHT = 250
    SAVE_WINDOW_TEXT_FONT = ("Montserrat", 12)

    # setup tkinter
    save_wn = tk.Tk() # save_wn = save_window
    save_wn.minsize(SAVE_WINDOW_WIDTH, SAVE_WINDOW_HEIGHT)
    save_wn.maxsize(SAVE_WINDOW_WIDTH, SAVE_WINDOW_HEIGHT)
    save_wn.title("Save Password")
    save_wn.configure(bg=SAVE_WINDOW_BG_COLOR)

    # home page button
    tk.Button(save_wn, text="HOME", command=distoryAndEnable_Save_Button, bg="#92FA5A", activebackground="#B2FC89").grid(row=0, column=0, padx=10, pady=10)
    # exit button
    tk.Button(save_wn, text="Exit", command=distoryAndEnable_Save_Button, bg="#DCFC6C", activebackground="#D9FF56").grid(row=0, column=1, padx=10, pady=10)

    # username label
    save_wn_username_label = tk.Label(save_wn, text="Username", bg=SAVE_WINDOW_BG_COLOR, font=SAVE_WINDOW_TEXT_FONT)
    save_wn_username_label.grid(row=1,column=0, padx=10, pady=10)

    # username entry
    save_wn_username_entry = tk.Entry(save_wn)
    save_wn_username_entry.grid(row=1, column=1, padx=10, pady=10)

    # password label
    save_wn_pasword_label = tk.Label(save_wn, text="Password", bg=SAVE_WINDOW_BG_COLOR, font=SAVE_WINDOW_TEXT_FONT)
    save_wn_pasword_label.grid(row=2,column=0, padx=10, pady=10)

    # password entry
    save_wn_pasword_entry = tk.Entry(save_wn)
    save_wn_pasword_entry.grid(row=2, column=1, padx=10, pady=10)
    # adding generated password
    save_wn_pasword_entry.insert(0, generated_password_entry.get())

    # save button
    save_wn_save_button = tk.Button(save_wn, text="Save", command=checker, bg="#92FA5A", activebackground="#B2FC89", font=SAVE_WINDOW_TEXT_FONT)
    save_wn_save_button.grid(row=3, columnspan=2, padx=10, pady=10)

    save_wn.mainloop()

# save generated password
def savepassword():
    if asAdmin:
        save_button.config(state=tk.DISABLED) # disabling the save_button so that no multiple save window open
        savePassword()
    else:
        logInAsAdmin()

if __name__ == "__main__":
    # admin
    asAdmin = False # when user login asAdmin will be true

    # gui maintain variables
    LABEL_FONT_SIZE = 15
    LABEL_FONT_NAME = 'Bookman Old Style'
    
    BUTTON_FONT_NAME = 'Sans-serif'
    BUTTON_FONT_SIZE = 10

    WINDOW_BG_COLOR = "#FEDBD0" ##336F84

    # setup tkinter
    window = tk.Tk()
    # window.geometry("500X600")
    window.minsize(300, 350)
    window.maxsize(300, 350)
    window.configure(bg=WINDOW_BG_COLOR)
    window.title('Password Manager')

    lenth_label = tk.Label(window, text="Lenth : ", bg=WINDOW_BG_COLOR)
    lenth_label.config(font=(LABEL_FONT_NAME, LABEL_FONT_SIZE))
    lenth_label.grid(row=0, column=0, padx=10, pady=20)

    # take lenth from user
    password_len = tk.Entry(window)
    password_len.grid(row=0, column=1, pady=10)
    password_len.focus()
    # blinding the enter key to the 'Generate' key
    password_len.bind('<Return>', password_Insert)

    # generate button
    generate_button = tk.Button(window, text="Generate", bg='#AED7E5', activebackground='#4CB5DA', command=password_Insert)
    generate_button.config(font=(BUTTON_FONT_NAME, BUTTON_FONT_SIZE))
    generate_button.grid(row=1, columnspan=2, padx=10, ipady=5)

    # show generated password
    # label
    password_label = tk.Label(window, text="Password: ", bg=WINDOW_BG_COLOR)
    password_label.config(font=(LABEL_FONT_NAME, LABEL_FONT_SIZE))
    password_label.grid(row=2,column=0, padx=10, pady=10)
    # entry
    generated_password_entry = tk.Entry(window)
    generated_password_entry.grid(row=2, column=1, padx=10, pady=10)

    # copy password
    tk.Button(window, text="Copy", command=copy_Pass, font=(BUTTON_FONT_NAME, BUTTON_FONT_SIZE), bg='#AED7E5', activebackground='#4CB5DA').grid(row=3, column=0,padx=10, pady=10)

    #save button
    save_button = tk.Button(window, text="Save", command=(savepassword), font=(BUTTON_FONT_NAME, BUTTON_FONT_SIZE), bg='#AED7E5', activebackground='#4CB5DA')
    save_button.grid(row=3, column=1, padx=10, pady=10)
    
    # exit program button
    tk.Button(window, text="EXIT", bg="#EC7063", relief="raised", activebackground="#e35e17",command=sys.exit).grid(row=4, columnspan=2, padx=10, pady=10)
    window.mainloop()
