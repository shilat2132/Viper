def REPLACE(container, find, replace) -> str:
    """
    Replaces all occurrences of a 'find' within the 'container' with 'replace'.

    Parameters:
    container (str): The original string where the replacement will occur.
    find (str): The substring to search for in the container.
    replace (str): The substring to replace the found substring.

    Returns:
    str: The modified string with all occurrences of 'find' replaced by 'replace'.
    """
    if not isinstance(container, str) or not isinstance(find, str) or not isinstance(replace, str):
        raise TypeError("arguments must be strings")
    
    containerSize = len(container)
    findSize = len(find)
    replaceSize = len(replace)
    i = 0
    for _ in range(containerSize):
        if i > containerSize - findSize:
            break
        text = container[i:i + findSize]
        if text == find:
            preText = container[:i]
            postText = container[i + findSize:]
            container = preText + replace + postText
            containerSize = len(container)
            i = i + replaceSize
        else:
            i = i + 1
    return container


def isUpper(text) -> bool:
    """
    Checks if all characters in a string are uppercase.

    Parameters:
    text (str): The string to check.

    Returns:
    bool: True if all characters are uppercase, False otherwise.
    """
    
    if not isinstance(text, str):
        raise TypeError("argument must be a string")

    for c in text:
        if ord(c) < 65 or ord(c) > 90:
            return False
    return True


def isLower(text) -> bool:
    """
    Checks if all characters in a string are lowercase.

    Parameters:
    text (str): The string to check.

    Returns:
    bool: True if all characters are lowercase, False otherwise.
    """
    
    if not isinstance(text, str):
        raise TypeError("argument must be a string")

    for c in text:
        if ord(c) < 32 + 65 or ord(c) > 32 + 90:
            return False
    return True


def CONCAT(first, last) -> str:
    """
    Concatenates two strings into one.

    Parameters:
    first (str): The first string.
    last (str): The second string.

    Returns:
    str: The concatenated string.
    """

    if not isinstance(first, str) or not isinstance(last, str):
        raise TypeError("argument must be a string")
    return first + last
