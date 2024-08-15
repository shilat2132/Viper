
def REPLACE(container, find, replace) -> str:
    if not (type(container) == str) or not (type(container) == str) or not (type(replace) == str):
        raise TypeError
    else:
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
    if not type(text) == str:
        raise TypeError
    else:
        for c in text:
            if ord(c) < 65 or ord(c) > 90:
                return False
        return True


def isLower(text) -> bool:
    if not type(text) == str:
        raise TypeError
    else:
        for c in text:
            if ord(c) < 32 + 65 or ord(c) > 32 + 90:
                return False
        return True


def CONCAT(first, last) -> str:
    if not (type(first) == str) or not (type(last) == str):
        raise TypeError
    return first + last

