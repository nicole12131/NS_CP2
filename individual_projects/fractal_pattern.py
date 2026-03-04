# NS 1st Fractal Pattern 
import turtle
# Draw a filled triangle
def draw_triangle(t, size, color):
    t.fillcolor(color)
    t.begin_fill()

    for i in range(3):
        t.forward(size)
        t.left(120)

    t.end_fill()



# Recursive Sierpinski function
def sierpinski(t, size, depth, color):
    # Base case
    if depth == 0:
        draw_triangle(t, size, color)
    else:
        # Bottom left
        sierpinski(t, size / 2, depth - 1, color)

        # Bottom right
        t.forward(size / 2)
        sierpinski(t, size / 2, depth - 1, color)

        # Top
        t.backward(size / 2)
        t.left(60)
        t.forward(size / 2)
        t.right(60)

        sierpinski(t, size / 2, depth - 1, color)

        # Return to original position
        t.left(60)
        t.backward(size / 2)
        t.right
# Main
def main():
    print("Welcome to the Sierpinski Triangle Generator!")
    print("This program creates a Sierpinski Triangle fractal using recursion.")

    # Get recursion depth
    while True:
        try:
            depth = int(input("Enter recursion depth (1-5): "))
            if 1 <= depth <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.")
        except:
            print("Invalid input. Please enter a number.")

    # Get color
    color = input("Enter triangle color (e.g., red, blue, green): ")

    print("Generating Sierpinski Triangle...")

    # Set up turtle
    screen = turtle.Screen()
    screen.title("Sierpinski Triangle")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, -150)
    t.pendown()

    # Draw fractal
    sierpinski(t, 400, depth, color)

    print("Fractal generated successfully!")
    input("Press Enter to exit the program.")

    screen.bye()


# Run program
main()
