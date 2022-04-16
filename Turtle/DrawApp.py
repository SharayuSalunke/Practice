import turtle #Turtle is a library allows to draw differnt shapes

def main():
    filename = input("Please enter drwaing filename with file extension: ") # Here we are getting text file where drawing commands are stored.

    t = turtle.Turtle() # Here t is a object of Turtle class
    screen = t.getscreen()

    file = open(filename, "r") # Here we are opening the file given by user in "r" or read only mode

    for line in file:
        text = line.strip()# to get rid off any balnk spaces in line
        commandList = text.split(",") # creating list of words/commands separated by ","
        command = commandList[0] # will contain 1st command of every line

        if command == "goto":
            x = float(commandList[1]) # as per our syntax in a commandline second value after goto will be value of x
            y = float(commandList[2]) # as per our syntax in a commandline third value after goto will be value of y
            linewidth = float(commandList[3])# as per our syntax in a commandline forth value after goto will be value of linewidth
            color = commandList[4].strip()
            t.width(linewidth)
            t.pencolor(color)
            t.goto(x,y)

        elif command == "circle":
            radius = float(commandList[1])
            linewidth = float(commandList[2])
            color = commandList[3].strip()
            t.width(linewidth)
            t.pencolor(color)
            t.circle(radius)

        elif command == "beginfill":
            color = commandList[1].strip()
            t.fillcolor(color)
            t.begin_fill()

        elif command == "endfill":
            t.end_fill()

        elif command == "penup":
            t.penup()

        elif command == "pendown":
            t.pendown()
        else:
            print("Unknown command found in file : ", command)

    file.close() # close text file

    t.ht() # hide turtle GUI

    screen.exitonclick()
    print("Programm execution commpleted")

if __name__ == "__main__":
    main()


