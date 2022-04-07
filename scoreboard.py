from turtle import Turtle 
#initialize and create scoreboard on the top of screen
ALLIGNMENT="center"
FONT=("arial",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
#Write the scoreboard on the screen
    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.high_score}",align=ALLIGNMENT,font=FONT)
#make score is high score and and restart game by itself
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0    
        self.update_scoreboard()
   
    #def game_over(self):
     #   self.goto(0,0)
      #  self.write(f"GAME OVER", align=ALLIGNMENT,font=FONT)    

#Increas the score by 1 at every collision of food and snake     
    def increase_score(self):
        self.score += 1   
        self.update_scoreboard()
        

