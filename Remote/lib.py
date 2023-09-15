class Television:
    #Contructor
    def __init__(self, on, channel, volume, muted):
        self.on = on
        self.channel = channel
        self.volume = volume
        self.muted = muted
    
    # Tv On/off
    def tvOnOff(self):
        if self.on:
            self.on = False
        else:
            self.on = True

    # Alle get metoder
    def getCh(self):
        return self.channel
    
    def getVol(self):
        return self.volume
    
    def getMuted(self):
        return self.muted
    
    # Channel Up/Down
    def chUp(self):
        self.channel += 1
    def chDown(self):
        self.channel -= 1

    # Volume Up/Down
    def volUp(self):
        self.volume += 1
    def volDown(self):
        self.volume -= 1

    # Mute
    def mute(self):
        if self.muted:
            self.muted = False
        else:
            self.muted = True