from pygame import mixer
from tkinter import *
from tkinter import filedialog
import os
from tkinter import ttk

root = Tk()

mixer.init()

root.geometry("400x400")
root.title("Music Player")

def select_folder():
  global files
  folder_name = filedialog.askdirectory()

  os.chdir(folder_name)
  files = os.listdir()

  for file in files:
    list_box.insert(END, file)

def play_music():
    song_name = files[list_box.curselection()[0]]
    mixer.music.load(song_name)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def unpause_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def volume_controller(x):
    mixer.music.set_volume(int(width_slider.get())/10)

Label(text = "Music player", font="italic 15 bold").pack(pady=5)

Button(text="Select Folder", command=select_folder).pack(pady=5)

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = BOTH)
list_box = Listbox(root)
list_box.pack(expand = YES, fill = "both")
list_box.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = list_box.yview)

frame = Frame()
frame.pack()
frame1 = Frame()
frame1.pack(pady=10)

Label(frame, text="Control Panel", font="italic 15 bold", fg="black").pack(pady=5, side=LEFT)

width_slider = ttk.Scale(frame, from_ = 1, to = 10, orient = HORIZONTAL, length = 100, value = 0, command=volume_controller)

width_slider.pack(pady = 10, padx = 20)

play = Button(frame1, text="Play", width=10, relief="solid", fg="red", command=play_music)
play.pack(side = RIGHT)

pause = Button(frame1, text="Pause", width=10, relief="solid", fg="blue", command=pause_music)
pause.pack(side=LEFT, padx=10)

unpause = Button(frame1, text="Unpause", width=10, relief="solid", fg="green", command=unpause_music)
unpause.pack(side=LEFT)

stop = Button(frame1, text="Stop", width=10, relief="solid", fg="orange", command=stop_music)
stop.pack(padx=5)

root.mainloop()