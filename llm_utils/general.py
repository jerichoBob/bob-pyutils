import textwrap
import os
import re
import glob
import sys

def print_wrapped(text, width=80):
    prefix = ""
    wrapper = textwrap.TextWrapper(initial_indent=prefix, 
                                   width=width,
                                   subsequent_indent=' '*len(prefix))
    print(wrapper.fill(text))

def shrink(string):
    """
    this sucks out all of the repeated '.' characters in a string, and replaces them with a single instance of '.'.
    used when we're converting pdftext into a single string we can process.
    """
    newstring = re.sub(r"(?is)[\.]+", '.', string)
    newstring = re.sub(r"(?is)[\n\s]+", ' ', newstring)
    newstring = re.sub("\u0000", '', newstring)
    
    return newstring    


def get_path_to_model(model_name):
    return os.path.join(find_models_dir(), model_name)



def find_models_dir(dir=os.path.abspath('.')):
    for name in glob.glob(f'{dir}/*', recursive=True):
        if os.path.isdir(name) and name.endswith("saved_models"):
            return os.path.abspath(name)

    return find_models_dir(os.path.join(dir, "..")) # recursion always carries a little danger with it :D

def find_utils_dir(dir=os.path.abspath('.')):
    for name in glob.glob(f'{dir}/*', recursive=True):
        if os.path.isdir(name) and name.endswith("src/utils"):
            return os.path.abspath(name)

    return find_utils_dir(os.path.join(dir, "..")) # recursion always carries a little danger with it :D

def add_utilsdir_to_path():
    """
    loops over the current PYTHONPATH to see if the utils directory is there.
    If it isn't, it adds it to the path.
    """
    for dirname in sys.path:
        # print(f"dirname: {dirname}")
        if dirname.endswith("src/utils"):
            print("utils already in path")
            return
    print("couldn't find it in the path. Adding it now.")
    utils_dir = find_utils_dir()
    print(f"utils_dir: {utils_dir}")
    sys.path.append(utils_dir)

def unit_tests():
    print(shrink("123....................................455"))
    print(shrink("""123.............
    
    
    
    .......................455"""))
    print(find_models_dir())

if __name__ == "__main__":
    # unit_tests()
    add_utilsdir_to_path()


# Path: src/utils/general.py