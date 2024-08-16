# print
def output(*stringToPrint):
    print(*stringToPrint)


def rangeTuple(end, start=0):
    """
        Generates a range tuple from start to end(end not included).

        Parameters:
        end (int): The end of the range.
        start (int, optional): The start of the range. Defaults to 0.

        Returns:
        range: A range object.
        """
    
    if isinstance(end, int) and isinstance(start, int):
       if end<=start:
           raise ValueError("starting index of range function should be smaller than ending index")
       return range(start, end)
    raise TypeError("range function can only take integers as parameters")

