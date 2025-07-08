import tkinter as tk

def back():
    pass

def nextSong():
    pass

def pauseToggle():
    pass

def loopToggle():
    pass

def closeToggle():
    pass


root = tk.Tk()
root.title("       Media Controls")
root.geometry("350x79")
root.eval('tk::PlaceWindow . center')
root.attributes('-topmost', True)

frame = tk.Frame(root, bd=0, width=306, height=60)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

backImg = tk.PhotoImage(file="images/back.png")
backBtn = tk.Button(frame, image=backImg, command=back)
backBtn.place(x=100, y=34)

pauseImg = tk.PhotoImage(file="images/pause.png")
pauseBtn = tk.Button(frame, image=pauseImg, command=pauseToggle)
pauseBtn.place(x=148, y=30)

nextImg = tk.PhotoImage(file="images/next.png")
nextBtn = tk.Button(frame, image=nextImg, command=nextSong)
nextBtn.place(x=183, y=34)

loopImgs = [tk.PhotoImage(file="images/loop.png"), tk.PhotoImage(file="images/unloop.png")]
loopBtn = tk.Button(frame, image=loopImgs[0], command=loopToggle)
loopBtn.place(x=0, y=10)

closeImgs = [tk.PhotoImage(file="images/close.png"), tk.PhotoImage(file="images/unclose.png")]
closeAfter = tk.Button(frame, image=closeImgs[0], command=closeToggle)
closeAfter.place(x=275, y=10)

root.mainloop()
