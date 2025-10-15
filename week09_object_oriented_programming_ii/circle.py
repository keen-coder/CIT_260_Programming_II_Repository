class Circle:
    # Class constants for RGB color values
    RED: tuple[int, int, int] = (255, 0, 0)
    GREEN: tuple[int, int, int] = (0, 255, 0)
    BLUE: tuple[int, int, int] = (0, 0, 255)
    BLACK: tuple[int, int, int] = (0, 0, 0)

    def __init__(self, radius: float, color: tuple[int, int, int]) -> None:
        self.__set_radius(radius)
        self.__color: tuple[int, int, int] = color

    def set_color(self, color: tuple[int, int, int]) -> None:
        # NOTE: The following if / else structure is not necessary. You can complete this method
        # with one line of code (self.__color = color), but I wanted to show how 
        # you could use the class constants in a Method to determine different choices. You will 
        # do something similar on the NPC assignment for this week. 
        
        # Using Python's new Match statements:
        # Play around with this structure and research how to use it on your own.
        match color:
            case Circle.RED:
                # Code for red choice
                pass
            case Circle.GREEN:
                 # Code for green choice
                pass
            case Circle.BLUE:
                 # Code for blue choice
                pass
            case Circle.BLACK:
                # Code for black choice
                pass

        # Using if statements.
        if color == Circle.RED:
            # Code for red choice
            pass
        elif color == Circle.GREEN:
            # Code for green choice
            pass
        elif color == Circle.BLUE:
            # Code for blue choice
            pass
        elif color == Circle.BLACK:
            # Code for black choice
            pass

    def set_radius(self, radius: float) -> None:
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        else:
            self.__radius: float = radius

    def __str__(self):
        output =    f'Radius:\t{self.__radius}\n'
        output +=   f'Color:\t{self.__color}'
        
        return output
                 