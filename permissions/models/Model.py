from db import database


class Model:

    def __init__(self, permissions):
        self.seq = 0
        self.permissions = permissions
        self.name = type(self).__name__.lower()
        if self.name not in database:
            database[self.name] = {}
        self._objects = database[self.name]

    def incr_seq(self):
        self.seq += 1
        return self.seq

    def writer(self, action):
        if "w" in self.permissions[self.name]:
            action(self)
        else:
            message = "User does not have permission to read object"
            raise AttributeError(message)

    def reader(self, action):
        if "r" in self.permissions[self.name]:
            return action(self)
        else:
            message = "User does not have permission to write object"
            raise AttributeError(message)

    def add(self, obj, update=False):
        def cb(self):
            self._objects[self.incr_seq()] = obj
        self.writer(cb)
        return self.seq

    def delete(self, obj_id):
        def cb(self):
            self._objects.pop(obj_id)
        return self.writer(cb)

    def get(self, obj_id):
        def cb(self):
            return self._objects[obj_id]
        return self.reader(cb)
    
    def update(self, obj_id, field, value):
        obj = self.get(obj_id)
        def cb(self):
            obj[field] = value
        self.writer(cb)
 

