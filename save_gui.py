import tkinter as tk
import tkinter.messagebox as msgbox

def SavePassword(password):
    # check if username and password present in the entry
    def checker():
        if len(username_entry.get()) == 0:
            msgbox.showinfo("Error", "No Username to save!")
        elif len(password_entry.get()) == 0:
            msgbox.showinfo("Error", "No Password to save!")
        else:
            # save data in store
            msgbox.showinfo("Done", "Password Saved")
            save_wn.destroy() # as password is saved successfully

    # setup tkinter
    save_wn = tk.Tk()
    # save_wn.geometry("500X600")
    save_wn.minsize(450, 450)
    save_wn.maxsize(450, 450)
    save_wn.configure(bg="#5DADE2")

    # home page button
    home_button = tk.Button(save_wn, text="HOME", command=save_wn.destroy)
    home_button.grid(row=0, column=0)
    # exit button
    tk.Button(save_wn, text="Exit", command=save_wn.destroy).grid(row=0, column=1)

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
    password_entry.insert(0, password)

    # save button
    save_button = tk.Button(save_wn, text="Save", command=checker)
    save_button.grid(row=3, column=1)

    save_wn.mainloop()

# SavePassword()