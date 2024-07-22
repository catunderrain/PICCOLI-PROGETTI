def Info(add=None):
    import os, inspect
    frame = inspect.stack()[1]
    file_path = os.path.abspath(frame.filename)
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    if content[5:12] == "CATINFO":
        info = ''
    else:
        if add != None:
            info = rf"""'''
#CATINFO#______________________________________________________________________________________________________________
Author: Cat Underrain
Email: catunderrainvn@gmail.com
{add}
_______________________________________________________________________________________________________________________
'''
"""
        else:
            info = r"""'''
#CATINFO#______________________________________________________________________________________________________________
Author: Cat Underrain
Email: catunderrainvn@gmail.com
_______________________________________________________________________________________________________________________
'''
"""
    modified_content = info + content
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(modified_content)