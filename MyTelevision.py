#Joebeck Andrew F. Gusi | BSCPE 1-5 | Assignment No.6

# Make the television class
class MYTELEVISION:
    # Tv is initially turned off, default channel and volume
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.on = False
    
    # Def turn on and off
    def turn_on(self):
        self.on = True
    def turn_off(self):
        self.on = False

    # Def get and set channels
    def get_channels(self):
        self.channel = self.channel
    def set_channels(self, channels):
        self.channel = channels

    # Def get and set volume
# Def up and down channels
# Def up and down volume

#end