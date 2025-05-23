"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = [
    "Yucatan",
    "Tequila",
    "Palace Mexico",
    "Playacar",
    "Lupita",
    "Palace Riviera Maya",
    "Cancun",
    "Caribe",
    "Palace Las Americas",
    "Palace Peninsula",
    "Dunamar",
    "Palace Costa Mujeres",
    "Latino",
    "Santa Fe",
    "Palace Cabo San Lucas",
    "Palace Baja California",
    "Emerald Bay",
    "Jalisco",
    "Vallarta",
    "Palace Pacifico",
    "Plaza España",
    "Plaza New York Times Square",
    "Plaza Berlin",
    "Plaza Miami Beach",
    "Plaza The Gresham Dublin",
    "Palace Aruba",
    "Palace Paradise Island",
    "Palace Bavaro",
    "Palace Punta Cana",
    "Palace Maldivas",
    "Bamboo",
    "Palace Zanzibar"
] * 2

state = {'mark': None, 'taps': 0, 'win': False}
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    state['taps'] += 1
    print(f'Taps: {state["taps"]}')

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    if all(not h for h in hide):
        state['win'] = True

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x+25, y+15)
        color('black')
        write(tiles[mark], align='center', font=('Arial', 15, 'normal'))

    up()
    goto(-180, 180)
    color('black')
    write(f'Taps: {state["taps"]}', font=('Arial', 14, 'bold'))

    if state['win']:
        goto(0, 200)
        color('red')
        write("¡Felicidades! Has descubierto todas las fichas.", align='center', font=('Arial', 16, 'bold'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
