#!/usr/bin/python3
"""
Class Square that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instanitation
        """

        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        To get size
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        To set size
        """

        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns [Square] (<id>) <x>/<y> - <size>
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute:
        """

        count = 0

        if args is not None and len(args) != 0:
            for key in self.__dict__:
                if count >= len(args):
                    break
                if key == "_Rectangle__height":
                    continue
                else:
                    setattr(self, key, args[count])
                    count += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a
        """
        dic_sq = {}
        dic_sq["id"] = self.id
        dic_sq["size"] = self.size
        dic_sq["x"] = self.x
        dic_sq["y"] = self.y

        return dic_sq
