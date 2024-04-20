"""Drawing A Commercial Airplane In A Night Sky Filled With Stars. Attempting above and beyond, breaking up complex functions, by breaking up the creation of the wings into 2 distinct functions, and attempting above and beyond, try something fun by creating a scene that needed more than 4 components, 6 to be exact."""


from turtle import Turtle, colormode, done, Screen
colormode(255)


def draw_airplane_fuselage(airplane: Turtle, x: float, y: float, size: float) -> None:
    """Drawing the fuselage of the airplane as a rectangle."""
    airplane.color("white")
    airplane.penup()
    airplane.goto(x, y)
    airplane.pendown()

    # Drawing the fuselage of the airplane and making it gray in color
    airplane.begin_fill()
    airplane.fillcolor((240, 240, 240))  # gray
    for _ in range(2):
        airplane.forward(180 * size)  # Establishing the length of the plane
        airplane.left(90)
        airplane.forward(30 * size)  # Establishing the height of the plane
        airplane.left(90)
    airplane.end_fill()


def draw_airplane_nosecone(airplane: Turtle, x: float, y: float, size: float) -> None:
    """Drawing the nosecone of the airplane as a semicircle."""
    airplane.penup()
    airplane.goto(x, y)
    airplane.pendown()

    # Draw the nosecone of the airplane
    airplane.begin_fill()
    airplane.fillcolor((240, 240, 240))  # Making the nosecone the same color as the fuselage (gray)
    airplane.circle(15 * size, -180)  # Establish the radius of the nosecone (semicircle) so it fits
    airplane.end_fill()


def draw_airplane_tail(airplane: Turtle, x: float, y: float, size: float) -> None:
    """Draw the tail of the airplane as a right triangle."""
    airplane.penup()
    airplane.goto(x + 167, y + 58)  # Adjusting location of tail
    airplane.pendown()

    # Drawing the tail of the airplane
    airplane.begin_fill()
    airplane.fillcolor((128, 0, 0))  # Making the tail a different color than the fuselage (red)
    airplane.setheading(225)
    airplane.forward(40 * size)
    airplane.left(135)
    airplane.forward(40 * size)
    airplane.left(90)
    airplane.forward(40 * size)
    airplane.end_fill()


def draw_left_wing(airplane: Turtle, x: float, y: float, size: float) -> None:
    """Drawing the left wing of the airplane."""
    airplane.penup()
    airplane.goto(x + 115, y - 300)
    airplane.pendown()

    # Drawing the left wing of the airplane
    airplane.begin_fill()
    airplane.fillcolor((240, 240, 240))  # Making the left wing the same color as the fuselage (gray)
    airplane.setheading(90)
    airplane.forward(260 * size)
    airplane.forward(60 * size)
    airplane.left(90)
    airplane.forward(60 * size)
    airplane.end_fill()


def draw_right_wing(airplane: Turtle, x: float, y: float, size: float) -> None:
    """Drawing the right wing of the airplane."""
    airplane.penup()
    airplane.goto(x + 58, y + 10)
    airplane.pendown()

    # Drawing the right wing of the airplane
    airplane.begin_fill()
    airplane.fillcolor((240, 240, 240))  # Making the right wing the same color as the fuselage (gray)
    airplane.setheading(360)
    airplane.forward(28 * size)
    airplane.forward(28 * size)
    airplane.left(90)
    airplane.forward(290 * size)
    airplane.end_fill()


def draw_star(star: Turtle, x: float, y: float, size: float) -> None:
    """Draw a singular star."""
    star.penup()
    star.goto(x, y)
    star.pendown()

    # Drawing a star
    star.begin_fill()
    star.fillcolor("yellow")
    for elem in range(5):
        star.forward(25 * size)
        star.right(144)
    star.end_fill()


def draw_stars_recursive(star_turtle: Turtle, stars: list):
    """Draw stars recursively."""
    if stars:
        x, y, size = stars[0]
        draw_star(star_turtle, x, y, size)
        draw_stars_recursive(star_turtle, stars[1:])


def main() -> None:
    """Draw the full scene with a commercial airplane in the night sky with stars."""
    screen = Screen()
    screen.bgcolor("darkblue")  # Establish a background night sky color of dark blue

    airplane_turtle: Turtle = Turtle()  # Create a turtle for the airplane
    airplane_turtle.speed(0)  # Set the maximum speed
    airplane_turtle.hideturtle()  # Hide the default turtle

    # Draw the airplane fuselage, nosecone, and tail
    draw_airplane_fuselage(airplane_turtle, -100, 0, 1)
    draw_airplane_nosecone(airplane_turtle, -100, 0, 1)
    draw_airplane_tail(airplane_turtle, -100, 0, 1)
    draw_left_wing(airplane_turtle, -100, 0, 1)
    draw_right_wing(airplane_turtle, -100, 0, 1)

    # Draw the stars in the sky
    star_turtle = Turtle()  # Create a turtle for the stars
    star_turtle.speed(0)  # Set the maximum speed
    star_turtle.hideturtle()  # Hide the default turtle

    stars = [(-200, 100, 0.5), (150, -50, 0.7), (-50, 150, 0.4)]
    draw_stars_recursive(star_turtle, stars)

    done()


if __name__ == "__main__":
    main()