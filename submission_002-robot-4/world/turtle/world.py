import turtle
import random
import world

turtle_reference = turtle.Turtle()
#this  made a new list of fake obs tha had no detection
obstacles = world.obstacles.get_obstacles()
# print(obstacles)
turtle_obstacles = []


# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def bootup(obs):
    global position_x, position_y
    position_y = 0
    position_x = 0
    turtle_reference.penup()
    turtle_reference.goto(-100,200)
    turtle_reference.pendown()
    turtle_reference.color('red')
    turtle_reference.goto(100,200)
    turtle_reference.goto(100,-200)
    turtle_reference.goto(-100,-200)
    turtle_reference.goto(-100,200)
    turtle_reference.penup()

    turtle_reference.home()
    turtle_reference.setheading(90)
    draw_obstacle(obs)    

def draw_obstacle(obs):
    """Draws the obstacles's x and y coordinates """
    # print(obs)
    for ob in obs:
        turtle_reference.goto(ob[0],ob[1])
        turtle_reference.pendown()
        turtle_reference.begin_fill()
        for i in range(4):
            turtle_reference.forward(4)
            turtle_reference.left(90)
        turtle_reference.end_fill()
        turtle_reference.penup()
        turtle_reference.home()
    turtle_reference.left(90)


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')

def obstacle_check(x,y):
    if world.obstacles.is_path_blocked(position_x, position_y, x, y):
        return True
    elif world.obstacles.is_position_blocked(x,y):
        return True
    else:
        return False


def update_position(steps, current_direction_index):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        x = obstacle_check(new_x,new_y)
        if x == False:
            position_x = new_x
            position_y = new_y
            turtle_reference.goto(new_x,new_y)
            return True, ''
        else:
            return False, 'obstacle'
    return False, 'border'


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y

def print_obstacles(obstacle):
    print("There are some obstacles:")
    for obs in obstacle:
        print(f"- At position {obs[0]},{obs[1]} (to{ obs[0]+4},{obs[1]+4})")

