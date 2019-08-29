import sys
import numpy as np
import cv2
from PIL import ImageTk
import numpy as np
import matplotlib.pyplot as plt

import PIL.Image
from tkinter import *
from tkinter import filedialog
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import GUIsupport


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    GUIsupport.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    GUItcl_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None



class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font16 = "-family {Sitka Heading} -size 11 -weight bold -slant" \
                 " roman -underline 0 -overstrike 0"
        font17 = "-family {Times New Roman} -size 14 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font18 = "-family PMingLiU-ExtB -size 11 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font19 = "-family {Great Vibes} -size 48 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"

        top.geometry("880x800+471+162")
        top.title("Welcome To Dernier Cri")
        top.configure(background="#d81c42")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.023, rely=0.488, relheight=0.469
                          , relwidth=0.938)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#0c0c05")
        self.Frame1.configure(width=825)

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.085, rely=0.133, height=236, width=222)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Uploaded Image''')
        self.Label4.configure(width=222)

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.133, rely=0.827, height=43, width=136)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#8500dd")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font16)
        self.Button1.configure(foreground="#fffdfc")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Upload Image''')
        self.Button1.configure(width=136)

        def open_file():
        
            result = filedialog.askopenfile(initialdir="/", title="Choose your Dressed Image",
                                            filetypes=(("jpeg files", ".jpg"), ("all files", "*.*")))
            print(result)
            s = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=(("jpeg file", "*.jpg"),("All Files", "*.*") ))
            print(s)
            filepath=""
            filepath=str(s)
            print(filepath)
            img = cv2.imread(filepath)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            #plt.title('Correct Display after converting with cv2.COLOR_BGR2RGB')
           # plt.imshow(img_rgb)
            #plt.xticks([])
            #plt.yticks([])
            #plt.show()
            cv2.imshow('img_rgb',img)
            
            cv2.waitKey(0)
            cv2.destroyAllWindows()
           # canvas = Canvas(root, width = 500, height = 500)
           # canvas.pack()
           # img = ImageTk.PhotoImage(PIL.Image.open(filepath))
           # canvas.create_image(20, 20, anchor=NW, image=img)
            
            
            #for c in result:
             #   print(c)

        self.Button1.configure(command = lambda:open_file())

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.4, rely=0.24, height=166, width=222)
        self.Label5.configure(activeforeground="#010005")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self._img1 = tk.PhotoImage(file="C:/Users/Lenovo/Desktop/ghnata2/images.jpg")
        self.Label5.configure(image=self._img1)
        self.Label5.configure(text='''Label''')
        self.Label5.configure(width=222)

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.691, rely=0.16, height=236, width=232)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Final Image''')
        self.Label6.configure(width=232)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.034, rely=0.088, height=286, width=252)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self._img2 = tk.PhotoImage(file="C:/Users/Lenovo/Desktop/ghnata2/hello.jpg")
        self.Label1.configure(image=self._img2)
        self.Label1.configure(text='''Label''')
        self.Label1.configure(width=252)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.375, rely=0.038, height=106, width=452)
        self.Label2.configure(background="#d81c42")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font19)
        self.Label2.configure(foreground="#ffe8fb")
        self.Label2.configure(text='''Dernier Cri''')
        self.Label2.configure(width=452)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.42, rely=0.15, height=46, width=372)
        self.Label3.configure(background="#d81c42")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font18)
        self.Label3.configure(foreground="#8afff7")
        self.Label3.configure(text='''" YOUR OWN VIRTUAL WARDROBE "''')
        self.Label3.configure(width=372)

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.33, rely=0.238, height=106, width=572)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self._img3 = tk.PhotoImage(file="C:/Users/Lenovo/Desktop/ghnata2/Capture.jpg")
        self.Label7.configure(image=self._img3)
        self.Label7.configure(text='''Label''')
        self.Label7.configure(width=572)

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.398, rely=0.4, height=46, width=442)
        self.Label8.configure(background="#d81c42")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font=font17)
        self.Label8.configure(foreground="#c7fff2")
        self.Label8.configure(text='''<< SWAP CLOTHES WITH JUST A CLICK >>''')
        self.Label8.configure(width=442)


if __name__ == '__main__':
    vp_start_gui()
