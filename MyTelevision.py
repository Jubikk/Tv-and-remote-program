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
    def get_channel(self):
        return self.channel
    def set_channel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    # Def up and down channels
    def channel_up(self):
        if self.on and self.channel < 120:
            self.channel += 1
    def channel_down(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    # Def get and set volume
    def get_volume(self):
        return self.volume
    def set_volume(self, volume):
        if self.on and 1 <= volume <= 7:
            self.volume = volume
    
    # Def up and down volume
    def volume_up(self):
        if self.on and self.volume < 7:
            self.volume += 1
    def volume_down(self):
        if self.on and self.volume > 1:
            self.volume -= 1
            
#end of the code