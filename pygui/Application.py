"""
    {PyGUI}  Copyright (C) {2016}  {Caleb Marshall}
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.
"""

import Tkinter
from pygui.ObjectManager import ObjectManager

class Application(Tkinter.Tk):

    def __init__(self, baseName=None):
        self._destroyed = False
        self._title = None
        self._object_manager = ObjectManager(self)

        Tkinter.Tk.__init__(self, baseName=baseName, sync=1)

    def request(self, identifier, *args, **kwargs):
        # todo: handle internal requests.
        pass

    def set_title(self, title):
        if not _title:
            self._title = title

        self.master.title(str(title))

    def get_title(self):
        return self._title

    def mainloop(self):
        while not self._destroyed:
            # update each frame on screen, override Tk method
            # because it's extremely slow and unresponsive.
            self.update()

    def destroy(self):
        self._destroyed = True
        self._title = None

        # destroy the object manager, then set variable to "None".
        self._object_manager.destroy()
        self._object_manager = None

        # delete class variables to conserve memory.
        del self._destroyed
        del self._title
        del self._object_manager

        Tkinter.Tk.destroy(self)