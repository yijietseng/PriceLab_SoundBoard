"""
Project: Lab_sound_board
Version: 1.0.0
Author: Yi Jie (Josh) Tseng
Description: This is to remember the awesomeness of our lab members
"""


import tkinter as tk
import pygame, os, sys
from PIL import ImageTk, Image


def play_audio(sound, Name):
    show_pic(Name)
    pygame.mixer.init() 
    # Get the absolute path to the "sounds" directory
    sounds_dir = os.path.join(os.path.dirname(__file__), "sounds")
    
    # Construct the absolute path to the audio file
    audio_path = os.path.join(sounds_dir, f"{sound}.mp3")
    
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()
    pygame.mixer.init()
    
    
def show_pic(Name):
    pic_dir = os.path.join(os.path.dirname(__file__), "Pics")
    img_path = os.path.join(pic_dir, f"{Name}.jpg")
    
    image = Image.open(img_path)
    image = image.resize((350,350), Image.LANCZOS)
    pic = ImageTk.PhotoImage(image)
        
    canv.create_image(0,0, image=pic, anchor="nw")
    canv.image=pic

#-----------------------------------------------------------------------------
    
# Create the main window
window = tk.Tk()
window.title("Sound Board")
window.configure(background='white')

# Set window icon
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    # Running in PyInstaller bundle
    icon_path = os.path.join(sys._MEIPASS, 'Nate.ico')
else:
    # Running in normal Python environment
    icon_path = 'Nate.ico'
window.iconbitmap(default=icon_path)

# Set window size
window.geometry("1000x800")

# Center the window on the screen
window.eval('tk::PlaceWindow . center')

# Configure row and column weights to center the buttons
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure([0, 1, 2, 3, 4, 5], weight=1)


# Labels for each column
label1 = tk.Label(window, text="Nate", font=("Helvetica", 20, "bold"), bg='white')
label2 = tk.Label(window, text="Rebecca", font=("Helvetica", 20, "bold"), bg='white')
label3 = tk.Label(window, text="Esteban", font=("Helvetica", 20, "bold"), bg='white')
label4 = tk.Label(window, text="NoahE", font=("Helvetica", 20, "bold"), bg='white')
label5 = tk.Label(window, text="Elli", font=("Helvetica", 20, "bold"), bg='white')
label6 = tk.Label(window, text="Chad", font=("Helvetica", 20, "bold"), bg='white')
label7 = tk.Label(window, text="Emily", font=("Helvetica", 20, "bold"), bg='white')
label8 = tk.Label(window, text="Random", font=("Helvetica", 20, "bold"), bg='white')
label9 = tk.Label(window, text="Colman", font=("Helvetica", 20, "bold"), bg='white')

# Arrange labels and buttons in a grid layout with three columns
label1.grid(row=0, column=0, pady=0)
label2.grid(row=0, column=1, pady=0)
label3.grid(row=2, column=2, pady=0)
label4.grid(row=0, column=4, pady=0)
label5.grid(row=0, column=2, pady=0)
label6.grid(row=2, column=3, pady=0)
label7.grid(row=2, column=4, pady=0)
label8.grid(row=0, column=5, pady=0)
label9.grid(row=0, column=3, pady=0)

# Create buttons with customizations
font_tuple = ("Helvetica", 9, "bold")
button_width = 20
button_height = 3


canv = tk.Canvas(window, width=350, height=350, bg='white')
canv.grid(row=5, column=2, rowspan=5, columnspan=2)


# Nate
button1 = tk.Button(window, text="Wuh\nHappened?!", command=lambda: play_audio("wuh-happened", 'Nate'), width=button_width, height=button_height, bg="red", fg="white", font=font_tuple)
button7 = tk.Button(window, text="I don't know", command=lambda: play_audio("I-dont-know", 'Nate'), width=button_width, height=button_height, bg="black", fg="white", font=font_tuple)
button8 = tk.Button(window, text="BuhBye now", command=lambda: play_audio("BuhBye-Now", 'Nate'), width=button_width, height=button_height, bg="magenta", fg="white", font=font_tuple)
button9 = tk.Button(window, text="Wuh Z'up\nChief?", command=lambda: play_audio("Wuh-up-Cheif", 'Nate'), width=button_width, height=button_height, bg="cyan", fg="black", font=font_tuple)
button10 = tk.Button(window, text="Ravecca", command=lambda: play_audio("Ravecca", 'Nate'), width=button_width, height=button_height, bg="Brown", fg="white", font=font_tuple)
button11 = tk.Button(window, text="Chocolate", command=lambda: play_audio("Chocolate", 'Nate'), width=button_width, height=button_height, bg="pink", fg="black", font=font_tuple)
button12 = tk.Button(window, text="Grumble", command=lambda: play_audio("Grumble", 'Nate'), width=button_width, height=button_height, bg="Maroon", fg="white", font=font_tuple)
button13 = tk.Button(window, text="Just Us", command=lambda: play_audio("Just-Us", 'Nate'), width=button_width, height=button_height, bg="darkgreen", fg="white", font=font_tuple)
button29 = tk.Button(window, text="Hraaaah", command=lambda: play_audio("Braaaah", 'Nate'), width=button_width, height=button_height, bg="lightcoral", fg="black", font=font_tuple)

button1.grid(row=1, column=0, padx=15, pady=13, sticky="nsew")
button7.grid(row=2, column=0, padx=15, pady=13, sticky="nsew")
button8.grid(row=3, column=0, padx=15, pady=13, sticky="nsew")
button9.grid(row=4, column=0, padx=15, pady=13, sticky="nsew")
button10.grid(row=5, column=0, padx=15, pady=13, sticky="nsew")
button11.grid(row=6, column=0, padx=15, pady=13, sticky="nsew")
button12.grid(row=7, column=0, padx=15, pady=13, sticky="nsew")
button13.grid(row=8, column=0, padx=15, pady=13, sticky="nsew")
button29.grid(row=9, column=0, padx=15, pady=13, sticky="nsew")

# Rebecca
button4 = tk.Button(window, text="Go away! 1", command=lambda: play_audio("go-away", 'Rebecca'), width=button_width, height=button_height, bg="yellow", fg="black", font=font_tuple)
button5 = tk.Button(window, text="Go aWay! 2", command=lambda: play_audio("Go_away_Rebecca", 'Rebecca'), width=button_width, height=button_height, bg="forestgreen", fg="white", font=font_tuple)
button23 = tk.Button(window, text="Wuh u\nwant 4 me?", command=lambda: play_audio("wuh_u_want_4_me_Rebecca", 'Rebecca'), width=button_width, height=button_height, bg="orange", fg="black", font=font_tuple)
button30 = tk.Button(window, text="Prove it", command=lambda: play_audio("prove-it", 'Rebecca'), width=button_width, height=button_height, bg="gainsboro", fg="black", font=font_tuple)
button31 = tk.Button(window, text="Fudge", command=lambda: play_audio("fudge", 'Rebecca'), width=button_width, height=button_height, bg="steelblue", fg="black", font=font_tuple)

button4.grid(row=1, column=1, padx=15, pady=13, sticky="nsew")
button5.grid(row=2, column=1, padx=15, pady=13, sticky="nsew")
button23.grid(row=3, column=1, padx=15, pady=13, sticky="nsew")
button30.grid(row=4, column=1, padx=15, pady=13, sticky="nsew")
button31.grid(row=5, column=1, padx=15, pady=13, sticky="nsew")

# Esteban
button24 = tk.Button(window, text="Come in", command=lambda: play_audio("comein", 'Esteban'), width=button_width, height=button_height, bg="skyblue", fg="black", font=font_tuple)
button26 = tk.Button(window, text="Shut up Chad", command=lambda: play_audio("shut-up-chad", 'Esteban'), width=button_width, height=button_height, bg="limegreen", fg="black", font=font_tuple)

button24.grid(row=3, column=2, padx=15, pady=13, sticky="nsew")
button26.grid(row=4, column=2, padx=15, pady=13, sticky="nsew")

# Chad
button2 = tk.Button(window, text="Disgusting!!!", command=lambda: play_audio("Disgusting_Chad", 'Chad'), width=button_width, height=button_height, bg="green", fg="white", font=font_tuple)
button3 = tk.Button(window, text="Tuesday", command=lambda: play_audio("Tuesday_Chad", 'Chad'), width=button_width, height=button_height, bg="blue", fg="white", font=font_tuple)

button2.grid(row=3, column=3, padx=15, pady=13, sticky="nsew")
button3.grid(row=4, column=3, padx=15, pady=13, sticky="nsew")

# NoahE
button6 = tk.Button(window, text="Hasta la pasta", command=lambda: play_audio("pasta_Noah", 'Noah'), width=button_width, height=button_height, bg="purple", fg="white", font=font_tuple)

button6.grid(row=1, column=4, padx=15, pady=13, sticky="nsew")

# Coleman
button33 = tk.Button(window, text="Chat GPT~", command=lambda: play_audio("chat-gtp",'Coleman'), width=button_width, height=button_height, bg="tomato", fg="black", font=font_tuple)

button33.grid(row=1, column=3, padx=15, pady=13, sticky="nsew")


# Elli
button27 = tk.Button(window, text="Heh?!", command=lambda: play_audio("Heh", 'Elli'), width=button_width, height=button_height, bg="mediumseagreen", fg="black", font=font_tuple)

button27.grid(row=1, column=2, padx=15, pady=13, sticky="nsew")


# Emily
button15 = tk.Button(window, text="One Mome", command=lambda: play_audio("one-mome",'Emily'), width=button_width, height=button_height, bg="coral", fg="black", font=font_tuple)
button16 = tk.Button(window, text="Hold pls", command=lambda: play_audio("hold-pulse",'Emily'), width=button_width, height=button_height, bg="khaki", fg="black", font=font_tuple)
button17 = tk.Button(window, text="Frick\non a stick", command=lambda: play_audio("freak-on-a-stick",'Emily'), width=button_width, height=button_height, bg="orchid", fg="black", font=font_tuple)

button15.grid(row=3, column=4, padx=15, pady=13, sticky="nsew")
button16.grid(row=4, column=4, padx=15, pady=13, sticky="nsew")
button17.grid(row=5, column=4, padx=15, pady=13, sticky="nsew")


# Random
button14 = tk.Button(window, text="What?!", command=lambda: play_audio("what", 'question-mark'), width=button_width, height=button_height, bg="Silver", fg="black", font=font_tuple)
button18 = tk.Button(window, text="LOL", command=lambda: play_audio("minion_laugh", 'question-mark'), width=button_width, height=button_height, bg="navajowhite", fg="black", font=font_tuple)
button19 = tk.Button(window, text="Surprise!", command=lambda: play_audio("surprise", 'question-mark'), width=button_width, height=button_height, bg="yellow green", fg="black", font=font_tuple)
button20 = tk.Button(window, text="Are you\nsingle?", command=lambda: play_audio("are-you-single", 'question-mark'), width=button_width, height=button_height, bg="darkgreen", fg="white", font=font_tuple)
button21 = tk.Button(window, text="Eh...No...", command=lambda: play_audio("eh-no", 'question-mark'), width=button_width, height=button_height, bg="royalblue", fg="black", font=font_tuple)
button22 = tk.Button(window, text="Oh my\ngoodness!", command=lambda: play_audio("oh-my-goodness", 'question-mark'), width=button_width, height=button_height, bg="indianred", fg="black", font=font_tuple)
button25 = tk.Button(window, text="YEAH~~~", command=lambda: play_audio("yeah", 'question-mark'), width=button_width, height=button_height, bg="darkorchid", fg="black", font=font_tuple)
button28 = tk.Button(window, text="Awwww", command=lambda: play_audio("Aww", 'question-mark'), width=button_width, height=button_height, bg="darkred", fg="white", font=font_tuple)
button32 = tk.Button(window, text="Bello", command=lambda: play_audio("bello", 'question-mark'), width=button_width, height=button_height, bg="khaki", fg="black", font=font_tuple)


button14.grid(row=1, column=5, padx=15, pady=13, sticky="nsew")
button18.grid(row=2, column=5, padx=15, pady=13, sticky="nsew")
button19.grid(row=3, column=5, padx=15, pady=13, sticky="nsew")
button20.grid(row=4, column=5, padx=15, pady=13, sticky="nsew")
button21.grid(row=5, column=5, padx=15, pady=13, sticky="nsew")
button22.grid(row=6, column=5, padx=15, pady=13, sticky="nsew")
button25.grid(row=7, column=5, padx=15, pady=13, sticky="nsew")
button28.grid(row=8, column=5, padx=15, pady=13, sticky="nsew")
button32.grid(row=9, column=5, padx=15, pady=13, sticky="nsew")


# Run the Tkinter event loop
window.mainloop()
