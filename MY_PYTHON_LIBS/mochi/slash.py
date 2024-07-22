def CodeForm():
    import os, inspect
    frame = inspect.stack()[1]
    file_path = os.path.abspath(frame.filename)
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    modified_content = content.replace('\\', '/')
    modified_content = modified_content.replace('//', '/')
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(modified_content)
        ''''''
        ''''''
def WindowForm():
    import os, inspect
    frame = inspect.stack()[1]
    file_path = os.path.abspath(frame.filename)
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    modified_content = content.replace('/', '\\')
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(modified_content)
        ''''''
        ''''''
if __name__ == "__main__":
    import mochi.replace
    mochi.replace.BlankLine()
    pass
    ''''''
