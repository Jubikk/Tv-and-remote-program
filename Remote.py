#Joebeck Andrew F. Gusi | BSCPE 1-5 | Assignment No.6 (Remote)

# import tkinter and the file
import tkinter as tk
from MyTelevision import MYTELEVISION


# Make the remote class
class MyRemote:
    def __init__(self , main):
        self.main = main
        self.tv1 = MYTELEVISION()
        self.tv2 = MYTELEVISION()

        self.create_remote()
    
    def create_remote(self):
        self.tv1_frame = tk.Frame(self.main)
        self.tv1_frame.pack()




# Def init
# Def widget(create widget)
# Def channel up and down
# Def volume up and down
# Def labels
# Main
