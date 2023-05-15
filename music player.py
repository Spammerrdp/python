import PySimpleGUI as sg
import pygame.mixer
sg.theme("default")
pygame.mixer.init()
b = [[sg.Text("select song:", size =(15, 3),auto_size_text=True), sg.FileBrowse(), sg.Submit()]]
w1 = sg.Window("",b)
w1.read()
gg = (w1.read()[1])
gg= str(gg['Browse']).replace("/","\\\\")
print(gg)
if gg != '':
    pygame.mixer.music.load(gg)
else:
    pygame.mixer.music.load("K:\\song1.mp3")
p = pygame.mixer.music
while True:
    k = [[sg.Text('double tap', size =(15, 3),auto_size_text=True,), sg.Button("Play"),sg.Button("Pause"),sg.Button("exit"),sg.Button("resume")]]
    w = sg.Window("",k)
    w.read()
    va = str(w.read()[0]).upper()
    if va == "PLAY":
        pygame.mixer.music.play()
    elif va == "PAUSE":
        p.pause()
    elif va == "EXIT":
        p.stop()
        break
    elif va == "RESUME":
        p.unpause()
