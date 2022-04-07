from turtle import Screen
from snake import Snake                            #import Snake from snake module 
from food import Food                              #import Food from food module 
from scoreboard import Scoreboard                  
import time
#tim=Turtle()

#create a screen of snake game
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

#make object and call the class Snake(),Food(),Scoreboard()
snake=Snake()
food=Food()
scoreboard=Scoreboard()

#control the movement of segmments(head)    
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()                                    #call function move() from module called snake

                                       
#detect the collision of snake and food
    if snake.head.distance(food)<15:
        scoreboard.increase_score()                 #call the function inrememnt in score by 1 
        food.refresh()                              #if colllision detected the new food will be generated
        snake.extend()                              #if snake takes food new segment will be added in it
#detect the snake is hit in the wall     
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
       scoreboard.reset()  
       snake.reset()                 #call the function to print on the screen game over 

#Detect collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment)<10:     #comparing a distance btw snake(head(seg[0])) and segments(whole segment)
            scoreboard.reset()   
            snake.reset() 

screen.exitonclick()