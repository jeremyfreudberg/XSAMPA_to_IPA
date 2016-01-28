import sys
from tkinter import *
import pyperclip

# unicode!!!
correspondence = {'m':'m',
         'F':'ɱ',
         'n':'n',
         'N':'ŋ',
         'p':'p',
         'b':'b',
         't':'t',
         'd':'d',
         'k':'k',
         'g':'g',
         'q':'q',
         '?':'ʔ',
         'f':'f',
         'v':'v',
         'T':'θ',
         'D':'ð',
         's':'s',
         'z':'z',
         'S':'ʃ',
         'Z':'ʒ',
         'x':'x',
         'G':'ɣ',
         'h':'h',
         'r\\':'ɹ',
         'j':'j',
         'r':'r',
         '4':'ɾ',
         'l':'l',
         'W':'ʍ',
         'w':'w',      
         'i':'i',
         '1':'ɨ',
         '}':'ʉ',
         'u':'u',
         'I':'ɪ',
         'U':'ʊ',
         'e':'e',
         'o':'o',
         '@':'ə',
         'E':'ɛ',
         '3':'ɜ',
         'V':'ʌ',
         'O':'ɔ',
         '{':'æ',
         '6':'ɐ',
         'a':'a',
         'A':'ɑ',
         'Q':'ɒ'}

# The only multichar symbol is 'r\'

def translate(s):
    result = ''
    for i in range(len(s)):
        if s[i] != 'r' and s[i] != '\\':
            try:
                result += correspondence[s[i]]
            except KeyError:
                result = "I don't think that was valid X-SAMPA (for English, anyway)."
                break
        elif s[i] == '\\':
            pass
        else: # s[i] = 'r'
            try:         
                if s[i+1] == '\\':
                    result += correspondence['r\\']
                else:
                    result += correspondence['r']
            except IndexError:
                result += correspondence['r']
                
    return result

try:
    translation = (translate(sys.argv[1]))
except:
    translation = 'No text entered'

def copy_to_clipboard():
    pyperclip.copy(translation)
    
root = Tk()
root.wm_title('Result')
e = Entry(root)
e.insert(0,translation)
e.pack()
b = Button(root, text="Copy to clipboard", command=copy_to_clipboard)
b.pack()
root.mainloop()
            
    
