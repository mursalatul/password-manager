import tkinter as tk
import pgenerator
import tkinter.messagebox as msgbox

# custom module
import save_gui

# initializing classes
pass_object = pgenerator.PGenerator()

# functions
def password_Insert():
    generated_password.delete(0, "end")
    if len(password_len.get()) > 0:
        password = pass_object.generator(int(password_len.get()))
        generated_password.insert(0, password)

# def copy_Pass():
#     pass

def copy_Pass():
    try:
        generated_password = generated_password.get() # Get the text from the Entry widget
        root = generated_password.winfo_toplevel() # Get the root window
        root.clipboard_clear() # Clear the clipboard
        root.clipboard_append(generated_password) # Append the text to the clipboard
        msgbox.showinfo("Copy to Clipboard", "Data copied to clipboard!")
    except Exception as e:
        msgbox.showerror("Error", f"Error copying to clipboard: {str(e)}")

# save generated password
def savepassword():
    save_gui.SavePassword(generated_password.get())

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
    # check if the password len is in right format or not in next update. in this version we consider user will input right number

    tk.Label(window, text="Password: ", bg="#5DADE2").pack()
    generated_password = tk.Entry(window)
    generated_password.pack()
    GENERATED_PASSWORD = generated_password

    # copy password
    tk.Button(window, text="Copy", command=copy_Pass).pack()
    #save button
    tk.Button(window, text="Save", command=savepassword).pack()
    # exit program button
    tk.Button(window, text="EXIT", bg="#EC7063", relief="raised", activebackground="#e35e17",command=exit).pack()
    window.mainloop()