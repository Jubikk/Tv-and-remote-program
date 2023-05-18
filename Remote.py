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

        self.TV1_label = tk.Label(self.TV1_frame, text="The channel of TV1 is 1 and the volume level is 1.")
        self.TV1_label.pack(padx=10, pady=15)

        self.TV2_frame = tk.Frame(self.main)
        self.TV2_frame.pack(pady=10)

        self.TV2_label = tk.Label(self.TV2_frame, text="The channel of TV2 is 1 and the volume level is 1.")
        self.TV2_label.pack(padx=10, pady=15)

        self.channel_up_button = tk.Button(self.main, text="Channel Up", command=self.channel_up)
        self.channel_up_button.pack(pady=10)

        self.channel_down_button = tk.Button(self.main, text="Channel Down", command=self.channel_down)
        self.channel_down_button.pack(pady=10)

        self.volume_up_button = tk.Button(self.main, text="Volume Up", command=self.volume_up)
        self.volume_up_button.pack(pady=10)

        self.volume_down_button = tk.Button(self.main, text="Volume Down", command=self.volume_down)
        self.volume_down_button.pack(pady=10)
    
    def channel_up(self):
        self.TV1.channel_up()
        self.TV2.channel_up()
        self.update_label()

    def channel_down(self):
        self.TV1.channel_down()
        self.TV2.channel_down()
        self.update_label()

    def volume_up(self):
        self.TV1.volume_up()
        self.TV2.volume_up()
        self.update_label()

    def volume_down(self):
        self.TV1.volume_down()
        self.TV2.volume_down()
        self.update_label()
    
    def update_labels(self):
        TV1_channel = self.TV1.get_channel()
        TV1_volume = self.TV1.get_volume()
        self.TV1_label.config(text="TV1's channel is () and volume level is ()".format(TV1_channel, TV1_volume))

        TV2_channel = self.TV2.get_channel()
        TV2_volume = self.TV2.get_volume()
        self.TV2_label.config(text="TV2's channel is () and volume level is ()".format(TV2_channel, TV2_volume))

def main():
    root = tk.Tk()
    root.geometry("400x350")  
    root.title("Remote Control Panel")  
    app = MyRemote(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    