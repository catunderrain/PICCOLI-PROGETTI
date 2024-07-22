import mochi.replace
import mochi.slash
''''''
''''''
def __init__(p=None):
    msg = """
    ______________________________________________________________________
    ''''''
    ______________________________________________________________________
    """
    if p == 1:
        print(msg)
    return msg
    ''''''
    ''''''
def VSCodeFoldUnfold(p=None):
    msg = """
    ______________________________________________________________________
    Fold: Ctrl + K + 0
    Unfold: Ctrl + K + J
    ______________________________________________________________________
    """
    if p == 1:
        print(msg)
    return msg
    ''''''
    ''''''
def RawString(p=None):
    msg = """
    ______________________________________________________________________
    This is raw string, it help paste the dir link in window without error
    r"..."
    ______________________________________________________________________
    """
    if p == 1:
        print(msg)
    return msg
    ''''''
    ''''''
if __name__ == "__main__":
    __init__(1)
    import mochi
    mochi.replace.BlankLine()
    pass