
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog ,messagebox


window=Tk()
window.title("File Handling")
window.configure(background="pink", relief="solid")
window.geometry("700x500")

def create_file():

    text_file= open('/home/user/Desktop/myweekendactivities.txt', "w")

    text_file.write("Hello :)\n")
    text_file.write("You have just created a text file named My Weekend Activities.\n")

    text_file.close()
    text_file=filedialog.askopenfilename(initialdir="/home/user/Desktop/",title="Open Text File", filetypes=(("Text Files", "*.txt"),))





def clear_function():
    entry1.delete(1.0,END)
    #use this for clearing. use 'destroy' to exit.


#define function to stop and exit the program.
def close_window():
    sure = messagebox.askyesno(title="Alert",message="Are you sure that you want to exit this app?")
    if sure==True:
        window.destroy()
    else:
        return  None


def display_file():
    text_file=open('/home/user/Desktop/myweekendactivities.txt',"r")
    entry1.insert(END, text_file.read())




def append_file():
      text_file= open('/home/user/Desktop/myweekendactivities.txt',"a")
      text_file.write(entry1.get("1.0","end-1c")+"\n")
      text_file.close()





def save_file():
     text_file=open('/home/user/Desktop/myweekendactivities.txt',"w")
     text_file.write(entry1.get(1.0, END))
     text_file.close()



lb1=Label(window,text="My Weekeend Activities:", font="arial 18 bold")
lb1.pack()

lb2=Label(window,text="Remember to clear before adding a text to append.", font="arial 8")
lb2.place(x=220,y=300)

entry1=Text(window,width=40, height=10)
entry1.pack(pady=20)

open_button=Button(window, text="Create Textfile", command=create_file)
open_button.place(x=100,y=260)

display_button=Button(window, text="Display", command=display_file)
display_button.place(x=240,y=260)

append_button=Button(window, text="Append Data", command=append_file)
append_button.place(x=405,y=260)

my_clearbutton=Button(window,text="Clear", command=clear_function)
my_clearbutton.place(x=330,y=260)

exit_button = Button (text = "Exit", command = close_window)
exit_button.place(x=530,y=260)


window.mainloop()

