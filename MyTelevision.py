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
    def up_channel(self):
        if self.channel and self.on < 120:
            self.channel += 1
    def down_channel(self):
        if self.channel and self.on > 1:
            self.channel -= 1
    
    # Def up and down volume
    

#end