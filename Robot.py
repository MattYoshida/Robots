class Robot:
    population = 0

    # When you run this program, it will auto-load anything inside the init
    def __init__(self, name):
        self.name = name
        print "(Initializing {})".format(self.name)
        Robot.population = Robot.population + 1   # adds robot to population
        print "There are {} robot(s) left".format(Robot.population)

    def destroy(self):
        print "Don't destroy me, my name is {}".format(self.name)
        print "AAAHHHHHH!"
        Robot.population = Robot.population - 1  # removes robot from population

        if Robot.population == 0:
            print "There are 0 robots left."
        else:
            print "There are {} robot(s) left".format(Robot.population)
            print "The last robot to die was {}".format(self.name)


my_robot = Robot("Name")
thing1 = Robot("Thing 1")
r2d2 = Robot("R2-D2")

my_robot.destroy()
r2d2.destroy()
