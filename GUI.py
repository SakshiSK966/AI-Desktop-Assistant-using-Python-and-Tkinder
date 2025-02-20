from tkinter import *
from PIL import Image,ImageTk
import Speech_to_text
import action

root = Tk()
root.title("AI Assistant")
root.geometry("570x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")


# ask Function
def ask():
    user_val = Speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END,'User------>'+user_val+"\n")
    if bot_val != None:
        text.insert(END,"BOT<-----"+str(bot_val)+"\n")
    if bot_val == 'ok' :
        root.quit()

# send Function
def send():
    user_input = entry.get()
    bot = action.Action(user_input)
    text.insert(END,'User---->'+user_input+"\n")
    if bot != None:
        text.insert(END,"BOT<-----"+str(bot)+"\n")
    if bot == 'ok':
        root.quit()
        
# delete Function
def del_text():
    text.delete('1.0',"end")

# Frame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=1, padx=55, pady=10)

# Label
text_label = Label(frame, text="AI Assistant", font=("Comic Sans MS", 14, "bold"), bg="#356696")
text_label.grid(row=0, column=0, padx=20, pady=10)

image = ImageTk.PhotoImage(Image.open("Image/Image4.png"))
image_label = Label(frame , image=image)
image_label.grid(row = 1, column=0,pady=20)

# Adding a text widget
text = Text(root,font=("courier 10 bold"),bg="#356696")
text.grid(row=2,column=0)
text.place(x=100,y=400,width=375,height=100)

# Adding entry widget
entry = Entry(root , justify=CENTER)
entry.place(x=100,y=520,width=370,height=30)

# Button 1
button1 = Button(root,text="ASK",bg="#356696",pady=16,padx=30,borderwidth=3,relief=SOLID,command=ask)
button1.place(x=70,y=575)

# Button 2
button2 = Button(root,text="SEND",bg="#356696",pady=16,padx=30,borderwidth=3,relief=SOLID,command=send)
button2.place(x=400,y=575)

# Button 3
button3 = Button(root,text="Delete",bg="#356696",pady=16,padx=30,borderwidth=3,relief=SOLID,command=del_text)
button3.place(x=225,y=575)

# Start Tkinter loop
root.mainloop()
