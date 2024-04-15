
import Rover
import Mars

seed = input("Please enter an integer to generate the Martian landscape: ")

# create Mars object with numeric seed to select landscape
mars = Mars.Mars(seed)

# print the Martian map
mars.showLandscape()

# create a Rover object 
r = Rover.Rover(mars)

# land the Rover at location 2, 2
r.land(2,2)

# prompt the user for 5 input directions
for turn in range(0,5):
  
  direction = input("Awaiting Command (U, R, D, L): ")
  direction = direction.upper()
  
  # move the rover in the requested direction
  if (direction == "U"):
    r.move(Rover.Rover.UP)
  elif (direction == "R"):
    r.move(Rover.Rover.RIGHT)
  elif (direction == "D"):
    r.move(Rover.Rover.DOWN)
  elif (direction == "L"):
    r.move(Rover.Rover.LEFT)
  else:
    print("BEEP - ERROR - DOES NOT COMPUTE")