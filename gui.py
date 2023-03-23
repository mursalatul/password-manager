import tkinter as tk
import tkinter.messagebox as msgbox

import pgenerator
import pstore

# functions

def logInAsAdmin():
    """
    Create a login pannel for log in as admin.
    this section will work only when user open the app and want to use features
    like save password for the first time. after log in one time it will not work again
    untill the program is closed.
    """
    # functions of logInAsAdmin()
    def checkUserPassOfAdmin():
        f = open('admin.txt', 'r')
        admin_username_from_txt = f.readline()[:-1] # removing last char cause it is \n at last of every line
        admin_password_from_txt = f.readline()[:-1]
        f.close()
        if admin_username_from_txt == admin_username_entry.get() and admin_password_from_txt == admin_password_entry.get():
            # seting asAdmin = True. from now no subwindow need login
            global asAdmin
            asAdmin = True
            msgbox.showinfo("LOGIN", "Complete .")
            login_wn.destroy()
        else:
            msgbox.showinfo("Error", "Wrong username or password")

    # setup tkinter
    login_wn = tk.Tk() # login_wn = login_window
    login_wn.minsize(450, 450)
    login_wn.maxsize(450, 450)
    login_wn.configure(bg="#5DADE2")
    login_wn.title("ADMIN Pannel")

    # username
    #         lable
    admin_username_lable = tk.Label(login_wn, text="Username: ")
    admin_username_lable.grid(row=0, column=0, padx=10, pady=10)
    #         entry
    admin_username_entry = tk.Entry(login_wn)
    admin_username_entry.grid(row=0, column=1, padx=10, pady=10)

    # password
    #         lable
    admin_password_lable = tk.Label(login_wn, text="Password: ")
    admin_password_lable.grid(row=1, column=0, padx=10, pady=10)
    #         entry
    admin_password_entry = tk.Entry(login_wn)
    admin_password_entry.grid(row=1, column=1, padx=10, pady=10)

    # login button
    tk.Button(login_wn, text="Login", command=checkUserPassOfAdmin).grid(row=3, columnspan=2, pady=10)
    
    login_wn.mainloop()

def password_Insert():
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
        if len(username_entry.get()) == 0:
            msgbox.showinfo("Error", "No Username to save!")
        elif len(password_entry.get()) == 0:
            msgbox.showinfo("Error", "No Password to save!")
        else:
            # save data in store
            pstore_obj = pstore.PStore()
            # saving username and password
            pstore_obj.pStore(username_entry.get(), password_entry.get())
            msgbox.showinfo("Done", "Password Saved")
            distoryAndEnable_Save_Button()
    # setup tkinter
    save_wn = tk.Tk() # save_wn = save_window
    save_wn.minsize(450, 450)
    save_wn.maxsize(450, 450)
    save_wn.configure(bg="#5DADE2")

    # home page button
    tk.Button(save_wn, text="HOME", command=distoryAndEnable_Save_Button).grid(row=0, column=0)
    # exit button
    tk.Button(save_wn, text="Exit", command=distoryAndEnable_Save_Button).grid(row=0, column=1)

    # username lable
    username_lable = tk.Label(save_wn, text="Username")
    username_lable.grid(row=1,column=1)

    # username entry
    username_entry = tk.Entry(save_wn)
    username_entry.grid(row=1, column=2)

    # password lable
    password_lable = tk.Label(save_wn, text="Password")
    password_lable.grid(row=2,column=1)

    # password entry
    password_entry = tk.Entry(save_wn)
    password_entry.grid(row=2, column=2)
    # adding generated password
    password_entry.insert(0, generated_password_entry.get())

    # save button
    save_button = tk.Button(save_wn, text="Save", command=checker)
    save_button.grid(row=3, column=1)
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

    # setup tkinter
    window = tk.Tk()
    # window.geometry("500X600")
    window.minsize(550, 550)
    window.maxsize(550, 550)
    window.configure(bg="#5DADE2")

    # heading
    heading = tk.Label(window, text="Password Generator", bg="#5DADE2")
    # heading.grid(rowspan=1, column=2)
    heading.pack()

    password_len_text = tk.Label(window, text="Lenth : ", bg="#5DADE2")
    password_len_text.pack()

    # take lenth from user
    password_len = tk.Entry(window)
    password_len.pack()

    # generate button
    tk.Button(window, text="Generate", command=password_Insert).pack()

    # show generated password
    tk.Label(window, text="Password: ", bg="#5DADE2").pack()
    generated_password_entry = tk.Entry(window)
    generated_password_entry.pack()

    # copy password
    tk.Button(window, text="Copy", command=copy_Pass).pack()

    #save button
    save_button = tk.Button(window, text="Save", command=(savepassword))
    save_button.pack();
    
    # exit program button
    tk.Button(window, text="EXIT", bg="#EC7063", relief="raised", activebackground="#e35e17",command=exit).pack()
    window.mainloop()
