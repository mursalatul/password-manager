import tkinter as tk
import tkinter.messagebox as msgbox

import pgenerator
import pstore

# functions
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
    save_button.config(state=tk.DISABLED) # disabling the save_button so that no multiple save window open
    savePassword()

if __name__ == "__main__":
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
