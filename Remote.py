#Joebeck Andrew F. Gusi | BSCPE 1-5 | Assignment No.6 (Remote)

# import tkinter and the file
import tkinter as tk
from MyTelevision import MYTELEVISION


# Make the remote class
class MyRemote:
    # Def init
    def __init__(self , main):
        self.main = main
        self.TV1 = MYTELEVISION()
        self.TV2 = MYTELEVISION()

        self.create_remote()

    # Def widget(create widget/remote)
    def create_remote(self):
        self.TV1_frame = tk.Frame(self.main)
        self.TV1_frame.pack(pady=10)

        self.TV1_label = tk.Label(self.tv1_frame, text="The channel of TV1 is 1 and the volume level is 1.")
        self.TV1_label.pack(padx=10, pady=15)

        self.TV2_frame = tk.Frame(self.main)
        self.TV2_frame.pack(pady=10)

        self.TV2_label = tk.Label(self.tv2_frame, text="The channel of TV2 is 1 and the volume level is 1.")
        self.TV2_label.pack(padx=10, pady=15)

        self.channel_up_button = tk.Button(self.main, text="Channel Up", command=self.channel_up)
        self.channel_up_button.pack(pady=10)

        self.channel_down_button = tk.Button(self.main, text="Channel Down", command=self.channel_down)
        self.channel_down_button.pack(pady=10)

        self.volume_up_button = tk.Button(self.main, text="Volume Up", command=self.volume_up)
        self.volume_up_button.pack(pady=10)

        self.volume_down_button = tk.Button(self.main, text="Volume Down", command=self.volume_down)
        self.volume_down_button.pack(pady=10)
