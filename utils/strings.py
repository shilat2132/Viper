import re

def REPLACE(container: str, find: str, replace: str) -> str:
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
    for c in text:
        if ord(c) < 65 or ord(c) > 90:
            return False
    return True


def isLower(text: str) -> bool:
    for c in text:
        if ord(c) < 32 + 65 or ord(c) > 32 + 90:
            return False
    return True


def CONCAT(first: str, last: str) -> str:
    return first + last

# trim
def trim(s):
    return re.sub(r'\s+', ' ', s)

if __name__ == "__main__":
    print(trim("  gvc   gfv  jhg  "))