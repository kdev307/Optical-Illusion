from turtle import *

# initial state of spinner is null (stable)
state = {'turn': 0}
# Draw fidget spinner


def spin():
    clear()
    # Angle of fidget spinner
    angle = state['turn']/10

    # To rotate in clock wise we use right
    # for Anticlockwise rotation we use left
    right(angle)

    # move the turtle forward by specified distance
    forward(100)

    # draw a dot with diameter 120 using colour red
    dot(120, 'red')

    # move the turtle backward by specified distance
    back(100)

    "second dot"
    right(60)
    forward(100)
    dot(200, 'magenta')
    back(100)

    "third dot"
    right(60)
    forward(100)
    dot(200, 'blue')
    back(100)

    "fourth dot"
    right(60)
    forward(100)
    dot(200, 'cyan')
    back(100)

    "fifth dot"
    right(60)
    forward(100)
    dot(200, 'green')
    back(100)

    "sixth dot"
    right(60)
    forward(100)
    dot(200, 'yellow')
    back(100)

    "seventh dot"
    fillcolor('white')

    update()

# Animate fidget spinner


def animate():
    if state['turn'] > 0:
        state['turn'] -= 1

    spin()
    ontimer(animate, 20)

# Flick fidget spinner


def flick():
    state['turn'] += 40  # acceleration of spinner


# setup window screen
setup(600, 400, 370, 0)
bgcolor("black")

tracer(False)

# wing of fidget spinner
width(0)
color("black")

# keyboard key for the rotation of spinner
onkey(flick, 'space')

listen()
animate()
done()
