"""
    {PyGUI}  Copyright (C) {2016}  {Caleb Marshall}
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.
"""

class ObjectManager(object):
    __slots__ = (
        '_parent', '_objects', '_object_id')

    def __init__(self, parent=None):
        self._parent = parent
        self._objects = {}
        self._object_id = 0

    def get_object_id(self):
        self._object_id += 1; return self._object_id

    def create(self, object_class, *args, **kwargs):
        if not callable(object_class):
            raise Exception("Cannot create object with class instance <%r>" % (
                object_class,))

        object = object_class(self.get_object_id(), parent=self._parent, 
            *args, **kwargs)

        # call "load" on object instance.
        object.load()

        # store the newly created object in the list of objects.
        self._objects[object._id] = object

    def delete(self, object_id):
        if object_id not in self._objects.keys():
            raise Exception("Cannot delete an object with id <%d> that doesn't exist!" % (
                object_id,))

        object = self._objects[object_id]

        # call "unload" on the object instance, then call delete.
        try:
            object.unload()
        finally:
            object.delete()

        # remove the instance from the list of objects.
        del self._objects[object_id]

    def destroy(self):
        self._parent = None
        self._objects = None
        self._object_id = 0

        # delete class variables to conserve memory.
        del self._parent
        del self._objects
        del self._object_id