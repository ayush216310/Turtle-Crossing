import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
# screen.bgcolor("white")
screen.tracer(0)
player = Player()
car_manager = CarManager()
screen.listen()
screen.onkeypress(fun=player.move_foward, key="Up")
screen.onkey(fun=player.move_backward, key="Down")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scoreboard.update_score()
    car_manager.create_car()
    screen.update()
    car_manager.move_car()
    for i in car_manager.all_cars:
        if player.distance(i) < 20:
            scoreboard.game_over()
            game_is_on = False
    check = player.check_move()
    if check == True:
        scoreboard.increase_score()
        car_manager.increase_speed()


screen.exitonclick()