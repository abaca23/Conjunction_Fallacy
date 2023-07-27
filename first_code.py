# imports every file form tkinter and tkinter.ttk
##Now has finish screen and moving pacman
##5.21.23

from tkinter import *
from tkinter.ttk import *


class main:
   def __init__(self, master = None):
      self.master = master
      self.x = 0
      self.y = 0
      global MV
      MV = 0

      #canvas
      self.canvas = Canvas(self.master, height = 350, width = 700, bg = '#1b1b38')
      #pacman
      self.pm = self.canvas.create_arc(
	 325, 150, 375, 200, start = 30, extent = 305, fill = "yellow")
      #apple
      self.b = self.canvas.create_oval(
         50, 150, 100, 200, fill = 'red')
      #organe
      self.o = self.canvas.create_oval(
         600, 150, 650, 200, fill = 'orange')
      rb = Button(self.master, text = 'again', command = lambda: create(self))
      rb.place(relx = 1, rely = 1, anchor = 's')

      self.canvas.pack(expand = True)

      self.movement()

      
   
      def create(self):
         #rid or all
         self.canvas.delete('all')
         #changes background
         self.canvas.configure(bg = '#1b1b38')
         #pacman
         self.pm = self.canvas.create_arc(
	    325, 150, 375, 200, start = 30, extent = 305, fill = "yellow")
         #apple
         self.b = self.canvas.create_oval(
            50, 150, 100, 200, fill = 'red')
         #organe
         self.o = self.canvas.create_oval(
            600, 150, 650, 200, fill = 'orange')
         global MV
         MV = 0
   
   def movement(self):
      self.canvas.move(self.pm, self.x, self.y)
      
      # for motion in negative x direction
   def left(self, event):
      global MV
      if MV <= -23 or MV >= 23:
         self.canvas.delete('all')
         self.canvas.configure(bg='green')
         self.text = self.canvas.create_text(350, 175, text = 'COMPLETE', fill = 'black')
      else:
         MV = MV - 1
         self.canvas.move(self.pm, -10, 0)
      # for motion in positive x direction
   def right(self, event):
      global MV
      if MV <= -23 or MV >= 23:
         self.canvas.delete('all')
         self.canvas.configure(bg='green')
         self.text = self.canvas.create_text(350, 175, text = 'COMPLETE', fill = 'black')
      else:
         MV = MV + 1
         self.canvas.move(self.pm, 10, 0)
      
if __name__ == "__main__":

   # object of class Tk, responsible for creating
   # a tkinter toplevel window
   master = Tk()
   master.geometry("700x350")
   gfg = main(master)

   # This will bind arrow keys to the tkinter
   # toplevel which will navigate the image or drawing
   master.bind("<KeyPress-Left>", lambda e: gfg.left(e))
   master.bind("a", lambda e: gfg.left(e))
   master.bind("<KeyPress-Right>", lambda e: gfg.right(e))
   master.bind("d", lambda e: gfg.right(e))
   master.bind('q', lambda e: master.quit())
   
   # Infinite loop breaks only by interrupt
   mainloop()
