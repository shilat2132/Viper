
def REPLACE(container: str, find: str, replace: str) -> str:
    """
    Replace all occurrences of find
    :param container: container to be replaced
    :param find: string to be replaced
    :param replace: string to be replaced with
    :return: container with replaced
    """
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


def isUpper(text: str) -> bool:
    """
    Check if text is uppercase
    :param text: text to check
    :return: True if all text is uppercase, False otherwise
    """
    for c in text:
        if ord(c) < 65 or ord(c) > 90:
            return False
    return True


def isLower(text: str) -> bool:
    """
    Check if text is lowercase
    :param text: text to check
    :return: True if all text is lowercase, False otherwise
    """
    for c in text:
        if ord(c) < 32 + 65 or ord(c) > 32 + 90:
            return False
    return True


def CONCAT(first: str, last: str) -> str:
    """
    Concatenate two strings
    :param first: first text
    :param last: second text
    :return: string concatenated
    """
    return first + last
