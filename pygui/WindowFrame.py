"""
    {PyGUI}  Copyright (C) {2016}  {Caleb Marshall}
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.
"""

import Tkinter

class WindowFrame(Tkinter.Frame):

    def __init__(self, id, parent=None, **kw):
        self._id = id

        Tkinter.Frame.__init__(self, master=parent, **kw)

    def load(self):
        pass

    def unload(self):
        pass

    def destroy(self):
        pass