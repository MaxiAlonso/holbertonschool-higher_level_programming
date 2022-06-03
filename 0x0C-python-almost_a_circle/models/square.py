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

    def __str__(self):
        """
        Returns [Square] (<id>) <x>/<y> - <size>
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
