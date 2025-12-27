from tkinter import *

###### MAIN WINDOW #######
window = Tk()  ## create a new window

window.title("first tkinte")  # the title of that window
window.geometry("1200x900") # the size of the window



#######ADD LABEL(TEXT)#########
label = Label(window, text="Tic, Tac, Toe!", font=("Arial", 86)) #add  a text ,his font style and his size
label.pack(pady=10,padx = 10) # the way we put the text in the window ( like margine X and Y )

####### ENTRY ( text input ) ########
entry = Entry(window, font=("Arial", 24)) # make a place to write the input
entry.pack() 

def show_inut():  # a function that change the label to the input text
    user_input = entry.get()  # write the input text
    label.config(text=user_input) 


####### CREATE A BUTTON ########
button = Button(window, text="show output", command=show_inut) # add he button and make it do the text change function
button.pack(pady=10)  # the way we put the button in the window ( like margine X and Y )

####### SELECT CHOICE (Radio button) #########
var = StringVar()  # show the choosen choice

rb1 = Radiobutton(window, text="Choice 1", variable=var, value="1")  # choice 1
rb2 = Radiobutton(window, text="Choice 2", variable=var, value="2")  # choice 2

rb1.pack()
rb2.pack()

def show_choice():
    print("the user choose:", var.get())


#######RUN THE PROGRAM ########
window.mainloop() # the program loop