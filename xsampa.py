### REQURIES PYTHON 3 FOR UNICODE SUPPORT!!! ###
### YOU REALLY SHOULD BE ABANDON 2.x BY NOW! ###

import sys
import pyperclip
import json
from tkinter import *

import data as x

def translate(s):
    """
    Loop through the string to convert each character/token
    Halt (and return an error string) if input is invalid

    Certain phones in X-SAMPA are represented by multiple characters!
    """
    result = ''
    for i,current_char in enumerate(s):
        if current_char != 'r' and current_char != '\\':
            try:
                result += x.correspondence[current_char]
            except KeyError:
                result = "I don't think that was valid X-SAMPA (for English, anyway)."
                break
        elif current_char == '\\':
            continue
        else: # current_char = 'r'
            try:         
                if s[i+1] == '\\':
                    result += x.correspondence['r\\']
                else:
                    result += x.correspondence['r']
            except IndexError:
                result += x.correspondence['r']                
    return result



def copy_to_clipboard():
    """ Dummy function needed for Tkinter button """
    pyperclip.copy(translation)
  

def main():
    """ Grab the input text, process, and show result in GUI """
    global translation
    try:
        translation = (translate(sys.argv[1]))
    except IndexError:
        translation = 'No text entered'
    root = Tk()
    root.wm_title('Result')
    e = Entry(root)
    e.insert(0,translation)
    e.pack()
    b = Button(root, text="Copy to clipboard", command=copy_to_clipboard)
    b.pack()
    root.mainloop()

main()
