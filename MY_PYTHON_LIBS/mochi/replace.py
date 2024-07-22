def BlankLine():
    import os, inspect
    frame = inspect.stack()[1]
    file_path = os.path.abspath(frame.filename)
    with open(file_path, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        if lines[i].strip() == "":
            count = 0
            if i > 0:
                count = len(lines[i - 1]) - len(lines[i - 1].lstrip())
            lines[i] = "''''''\n"
            lines[i] = " " * count + lines[i]
    with open(file_path, "w") as file:
        file.writelines(lines)


def BlankLineBack():
    import os, inspect
    frame = inspect.stack()[1]
    file_path = os.path.abspath(frame.filename)
    with open(file_path, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        if lines[i].strip() == "''''''":
            lines[i] = "\n"
    with open(file_path, "w") as file:
        file.writelines(lines)
if __name__ == "__main__":
    BlankLineBack()