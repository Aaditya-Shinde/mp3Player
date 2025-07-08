import tkinter as tk
import os
import pygame
import random

def back():
    global songIdx
    global songs
    global backSong

    songIdx -= 2
    songIdx %= len(songs)
    backSong = True

def pauseToggle():
    global paused
    if paused:
        pygame.mixer.music.unpause()
    if not paused:
        pygame.mixer.music.pause()
    paused = not paused
    pauseBtn.config(image=pauseImgs[int(paused)])

def next():
    global nextSong

    nextSong = True

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
backSong = False

pauseImgs = [tk.PhotoImage(file="images/pause.png"), tk.PhotoImage(file="images/unpause.png")]
pauseBtn = tk.Button(frame, image=pauseImgs[0], command=pauseToggle)
pauseBtn.place(x=148, y=30)
paused = False

nextImg = tk.PhotoImage(file="images/next.png")
nextBtn = tk.Button(frame, image=nextImg, command=next)
nextBtn.place(x=183, y=34)
nextSong = False

loopImgs = [tk.PhotoImage(file="images/loop.png"), tk.PhotoImage(file="images/unloop.png")]
loopBtn = tk.Button(frame, image=loopImgs[0], command=loopToggle)
loopBtn.place(x=0, y=10)

closeImgs = [tk.PhotoImage(file="images/close.png"), tk.PhotoImage(file="images/unclose.png")]
closeAfter = tk.Button(frame, image=closeImgs[0], command=closeToggle)
closeAfter.place(x=275, y=10)

def playSong(song):
    pygame.mixer.music.set_volume(0.2)
    print(f"Now playing: {song.split(sep="/")[-1][:-4]}")
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

folderPath = "songs/"
songIdx = 0
songs = []
def getSongs(folder):
    global songs
    for f in os.listdir(folder):
        if f[0] != '.':
            if f.endswith('.mp3'):
                songs.append(folder+f)
            else:
                getSongs(folder+f+'/')
getSongs(folderPath)

random.shuffle(songs)
pygame.mixer.init()
while True: 
    song = songs[songIdx]
    playSong(song)

    while pygame.mixer.music.get_busy() or paused:
        if backSong:
            backSong = False
            break
        if nextSong:
            nextSong = False
            break
        
        try:
            root.title(song.split(sep="/")[-1][:-4])
        except:
            exit(0)
        root.protocol("WM_DELETE_WINDOW", closeToggle)
        root.update()

    songIdx += 1
    if songIdx == len(songs):
        random.shuffle(songs)
        songIdx = 0
