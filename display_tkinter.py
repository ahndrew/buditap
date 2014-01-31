#display_tkinter
from Tkinter import *
import Tkinter
import PIL.Image
import PIL.ImageTk

self.pil_image=PIL.Image.open('mostinteresting.jpeg') 
self.tk_img=PIL.ImageTk.PhotoImage(self.pil_image)
self.drawn = self.canvas.create_image(self.centre_x, self.centre_y,image=self.tk_img, anchor=CENTER,tag='pp-content')