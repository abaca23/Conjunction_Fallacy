# imports every file form tkinter and tkinter.ttk
##Now has finish screen and moving pacman
##5.21.23

from tkinter import *
from tkinter.ttk import *
import random

f = open('Data','a')

class main:
   def __init__(self, master = None):
      self.master = master
      self.x = 0
      self.y = 0
      global MV
      global ra
      global rounds
      global light
      global point

      MV = 0
      rounds = 1
      point = 0
      
      #canvas
      self.canvas = Canvas(self.master, height = 350, width = 700, bg = '#1b1b38')
      #pacman
      self.sb = self.canvas.create_rectangle(
         725, 10, 600, 40, outline = 'blue', width ='4', fill = 'white')
      self.pm = self.canvas.create_arc(
	 325, 150, 375, 200, start = 30, extent = 305, fill = "yellow")
      #apple
      self.b = self.canvas.create_oval(
         50, 150, 100, 200, fill = 'red')
      #organe
      self.o = self.canvas.create_oval(
         600, 150, 650, 200, fill = 'orange')

      if rounds == 1:
         rb = Button(self.master, text = 'again', command = lambda: create(self))
         rb.pack()
      else:
         rb = Button(self.master, text = 'again', command = lambda: create(self), status = disabled)
         rb.pack()

      global ra
      light = random.randint(1,2)
      if light == 1:
         ra = 1
         self.l = self.canvas.create_oval(
            325,25,375,75, fill = 'yellow')
      elif light == 2:
         ra = 2
         self.l = self.canvas.create_oval(
            325,25,375,75, fill = 'black')

      global rbg
      rbg = random.randint(1,2)
      
      if rbg == 1:
         self.canvas.configure(bg = '#0b1942')
      elif rbg == 2:
         self.canvas.configure(bg = '#6c7ba3')

      if rounds == 1:
         self.canvas.delete('all')
         self.canvas.configure(bg = 'white')
         start = Button(self.master, text = 'Start', command = lambda: create(self))
         self.canvas.create_text(
            350,50,
            text = 'This is an impulse based game. \n Dont think too much, the light on top tells you what to do. \n You have 5 seconds',
            fill = 'black', font = ('Helvetica','15', 'bold'), justify='center')
         self.canvas.create_text(
            350, 225,
            text ='Colors and Answers: \n \n -Yellow means the apple is correct.\t -Red means the orange is correct. \n \n \n \n \n BACKGROUNDS DONT MATTER',
            fill ='black', font = ('Helvetica','15', 'bold'), justify='center')
         self.canvas.create_text(50, 193,text = 'Yellow', fill = 'yellow',font = ('Helvetica','15', 'bold'))
         self.canvas.create_text(390, 193,text = 'Red', fill = 'Red',font = ('Helvetica','15', 'bold'))
      else:
         rb = Button(self.master, text = 'start', command = lambda: create(self))
                  
      self.canvas.pack(expand = True)

      self.movement()
      
      def create(self):
         global rounds
         global point
         
         rounds += 1

         
         #rid or all
         rb.destroy()
         self.canvas.delete('all')
         #changes background
         self.canvas.configure(bg = '#1b1b38')
         #scoreboard
         self.sb = self.canvas.create_rectangle(
            675, 10, 550, 60, outline = 'blue', width ='4', fill = 'white')
         self.sbt = self.canvas.create_text(
            580, 40, text = point, fill = 'black', font=('Helvetica 25 bold'))
         self.sbt = self.canvas.create_text(
            640, 40, text = 'points', fill = 'black', font=('Helvetica 15 bold'))
         #pacman
         self.pm = self.canvas.create_arc(
	    325, 150, 375, 200, start = 30, extent = 305, fill = "yellow")
         #apple
         self.b = self.canvas.create_oval(
            50, 150, 100, 200, fill = 'red')
         #organe
         self.o = self.canvas.create_oval(
            600, 150, 650, 200, fill = 'orange'
         global MV
         MV = 0
         
         global ra
         
         if point >= 5:
            ra = 0
            self.canvas.create_rectangle(320,20,380,80, fill = 'red')
            f.write(str(ra) + ':')
         else:
            light = random.randint(1,2)
            if light == 1:
               ra = 1 #left
               f.write(str(ra) + ':')
               self.l = self.canvas.create_oval(
                  325,25,375,75, fill = 'yellow')
               self.canvas.create_rectangle(310,20,390,30, fill = 'brown')
               cpoint = [310, 20, 310, 80, 315,80,320,70,325,70,330,60, 330, 20, 370, 20, 370, 60, 375, 70, 380, 70, 385, 80, 390, 80, 390, 20, 300, 20]
               self.c = self.canvas.create_polygon(cpoint, fill = 'red')

            elif light == 2:
               ra = 2
               f.write(str(ra))
               self.l = self.canvas.create_oval(
                  325,25,375,75, fill = 'black')
               self.canvas.create_rectangle(310,20,390,30, fill = 'brown')
               cpoint = [310, 20, 310, 80, 315,80,320,70,325,70,330,60, 330, 20, 370, 20, 370, 60, 375, 70, 380, 70, 385, 80, 390, 80, 390, 20, 300, 20]
               self.c = self.canvas.create_polygon(cpoint, fill = 'red')

         global rbg
         rbg = random.randint(1,2)

         if rbg == 1:
            self.canvas.configure(bg = '#0b1942')
            f.write( '----dark----')
         elif rbg == 2:
            self.canvas.configure(bg = '#6c7ba3')
            f.write('----light----')

         self.canvas.after(5000, lambda: create(self))
         
   def movement(self):
      self.canvas.move(self.pm, self.x, self.y)
      
      # for motion in negative x direction
   def left(self, event):
      global ga
      global point
      global rounds
      ga = 1
      global MV
      if MV == -11 or MV == 11:
         if ga == ra or ra == 0:
            f.write('1 \n')
            point = rounds - 1
            self.canvas.delete('all')
            self.canvas.configure(bg='green')
            self.text = self.canvas.create_text(350, 175, text = 'COMPLETE', fill = 'black')
         else:
            point = 0
            rounds = 1
            f.write('1 \n')
            self.canvas.delete('all')
            self.canvas.configure(bg = 'red')
            self.bgs = self.canvas.create_rectangle(50, 200, 300, 290, fill ='black')
            self.pm = self.canvas.create_arc(
	    150, 225, 250, 275, start = 225, extent = 90, fill = "#c0c90a")
            
            points = [100, 230, 110, 210, 140, 210, 150, 230, 150, 280, 100, 280]
            self.canvas.create_polygon(points, fill = "blue")
            self.text = self.canvas.create_text(350,175,text='FAILED',font=("Helvetica",25, 'bold'), fill = 'black')
      else:
         MV = MV - 1
         self.canvas.move(self.pm, -20, 0)
      # for motion in positive x direction
   def right(self, event):
      global ga
      ga = 2
      global MV
      global point
      global rounds
      
      if MV == -11 or MV == 11:
         if ga == ra or ra == 0:
            f.write('2 \n')
            point = rounds - 1
            self.canvas.delete('all')
            self.canvas.configure(bg='green')
            self.text = self.canvas.create_text(350, 175, text = 'COMPLETE', fill = 'black')
         else:
            f.write('2 \n')
            point = 0
            rounds = 1
            self.canvas.delete('all')
            self.canvas.configure(bg = 'red')
            self.bgs = self.canvas.create_rectangle(50, 200, 300, 290, fill = 'black')
            self.pm = self.canvas.create_arc(
	    150, 225, 250, 275, start = 225, extent = 90, fill = "#c0c90a")
            
            points = [100, 230, 110, 210, 140, 210, 150, 230, 150, 280, 100, 280]
            self.canvas.create_polygon(points, fill = "blue")
            self.text = self.canvas.create_text(350,175,text='FAILED',font=("Helvetica",25, 'bold'), fill = 'black')
            
      else:
         MV = MV + 1
         self.canvas.move(self.pm, 20, 0)
      
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

   f.write('\n \n \n')
   f.close()
