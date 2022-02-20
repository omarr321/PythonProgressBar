# This is a simple progressBar class for Python.
# Author - Omar Radwan
# Version 0.8.0

class progressBar:
    # Init function that sets all the varables
    # Inputs:
    #  var Name  - Description                                                               | Default Value
    #  blank     - Sets the empty space of the progress bar                                  | ' '
    #  fill      - Sets the full space of the progress bar                                   | u"\u2588"
    #  length    - Sets the lenght of the progress bar                                       | 20
    #  steps     - Sets how many incurments the bar needs to get to 100%                     | 20
    #  doneMess  - Sets the message displayed at the end of the progress bar when it is full | "-DONE!"
    #  barEnd    - Sets the ends for the progress bar                                        | "|"
    #  inclRet   - If True, includes a '\r' char to the begianning of the progress bar       | True
    #  autoPrint - When you step the progress bar, it prints it out                          | False
    def __init__(self,blank=' ', fill=u"\u2588",length=20,steps=20, doneMess = " -DONE!", barEnd = "|", inclRet = True, autoPrint = False):
        self.spaceBlank = blank
        self.spaceFill = fill
        self.barLen = length
        self.steps = steps
        self.currStep = 0
        self.doneMess = doneMess
        self.barEnd = barEnd
        self.retur = inclRet
        self.print = autoPrint

    # Steps the progress bar one unit
    # Inputs:
    #  var name - Description                                      | Default Value
    #  step     - The number of units to progress the progress bar | 1
    def step(self, step=1):
        if self.currStep < self.steps:
            self.currStep = self.currStep + step
        if self.currStep > self.steps:
            self.currStep = self.steps
        if self.print:
            print(self.toString(),end='')
        
    # Converts the progress bar to a string.
    def toString(self):
        filled = (self.currStep/self.steps)*self.barLen
        empty = self.barLen - filled
        bar = ""
        if self.retur:
            bar = f"\r"
        if (self.currStep == self.steps):
            bar = bar + f"{self.barEnd}{self.spaceFill*round(filled)}{self.spaceBlank*round(empty)}{self.barEnd}{round(self.currStep/self.steps*100.0,2)}%{self.doneMess}"
        else:
            bar = bar + f"{self.barEnd}{self.spaceFill*round(filled)}{self.spaceBlank*round(empty)}{self.barEnd}{round(self.currStep/self.steps*100.0,2)}%"
        return bar
    
    if __name__ == "__main__":
        raise Exception("Class can not be run as main. This class must be imported!")