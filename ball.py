import tkinter,time,random



window = tkinter.Tk()
window.title("Шарик")
window.resizable(0,0)
canvas = tkinter.Canvas(window,width = 500,height = 400)
canvas.pack()
window.update()


class Ball:
    def __init__(self, canvas,platform,count, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="red")
        self.current_x = random.choice((-2,-1,1,2)) 
        self.current_y = -1
        self.canvas.move(self.ball,245,100)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.platform = platform
        self.count = count


    def hit_pl(self,ball_pos):
        coord_pl = self.canvas.coords(self.platform.platform)
        if ball_pos[2]>= coord_pl[0]and\
           ball_pos[0]<= coord_pl[2] and\
           coord_pl[3]>= ball_pos[1] and\
           coord_pl[3]<= ball_pos[3]:
           self.count.count()
           return True
        
        return False
            

    def draw(self):
        self.canvas.move(self.ball,self.current_x,self.current_y)
        coord = self.canvas.coords(self.ball)
        if self.hit_pl(coord):
            self.current_y = -2
        if coord[1]<0:
            self.current_y= 2

        elif coord[3]>self.canvas_height:
            self.current_y =0
            self.current_x = 0
            self.canvas.create_text(150,100,text="Вы проиграли")


        if coord[0]<=0:
            self.current_x = 2

        elif coord[2]>=self.canvas_width:
            self.current_x = -2


class Platform:
    def __init__(self,canvas):
        self.canvas = canvas
        self.platform = self.canvas.create_rectangle(0,0,100,10, fill="white")
        self.canvas.move(self.platform,200,300)
        self.current_x = 0

        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas_width = self.canvas.winfo_width()

    def turn_right(self,event):
        coord = self.canvas.coords(self.platform)

        
        if coord[2]<self.canvas_width:
            self.current_x = 2

        

    def turn_left(self,event):
        coord = self.canvas.coords(self.platform)
        
        if coord[0]>0:
            self.current_x = -2

    def draw(self):
        self.canvas.move(self.platform,self.current_x,0)
        coord = self.canvas.coords(self.platform)

        if coord[2]>=self.canvas_width:
            self.current_x = 0
        elif coord[0]<=0:
            self.current_x = 0

class Count():
    def draw(self):
        self.canvas.itemconfig(self.text,text=str(self.i))
    def __init__(self,canvas):
        self.canvas = canvas
        self.text = self.canvas.create_text(400,10,text="0")
        self.i = 0
    def count(self):
        self.i+=1
        


platform = Platform(canvas)
count = Count(canvas)
ball = Ball(canvas,platform,count, 10, 10, 25, 25)
def mainloop():
    while True:
        ball.draw()
        platform.draw()
        count.draw()
        window.update_idletasks()
        window.update()
        time.sleep(0.01)
mainloop()
