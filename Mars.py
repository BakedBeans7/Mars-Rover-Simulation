import random

class Mars:
  
  # class variable holds the possible terrain features
  terrain = ["","Mountain","Valley","Lakebed","Alien"]

  # initialize the Mars class with a numeric seed
  def __init__(self, seed):
    
    
    random.seed(seed)     # seed the random number generator
    self.MAX_X = 5        # set the max allowed X coordinate
    self.MAX_Y = 5        # set the max allowed Y coordinate
    
    self.columns = []     # initialize empty list of columns (X direction)
    
    # for each column
    for x in range(0, self.MAX_X + 1):
      self.columns.append([])   # append an empty list that will hold the "Y" direction
      
      # for each row in the "Y" direction
      for y in range(0, self.MAX_Y + 1):
        
        # get a random index into the terrain list
        t = random.randrange(0,len(Mars.terrain))
        
        # add this terrain feature to the current X, Y coordinate
        self.columns[x].append(Mars.terrain[t])
    
  # Rover will call this function to explore a location
  def discover(self, x, y):
  
    # verify valid input
    if (x < 0) or (x > self.MAX_X):
      return "INVALID X"
    if (y < 0) or (y > self.MAX_Y):
      return "INVALID Y"
      
    # get the terrain feature at this location
    found = self.columns[x][y]
    
    if (len(found) == 0):
      return "Nothing"      # translate an empty space to "Nothing"
    else:
      return found          # else return whatever we found
  
  # This handy function will show the full 5 x 5 landscape with axis labels      
  def showLandscape(self):
    
    print("")

    # for each row
    for y in range(self.MAX_Y, -1, -1):
      print(str.format("{:^5}",y),end="")  # print this Y-axis label
      
      # for each column
      for u in range(0, self.MAX_X + 1):
        print(str.format("{:^10}",self.columns[u][y]),end="")
      print("")

    # print some spacing and the bottom axis labels
    print("     ",end="")
    for u in range(0, self.MAX_X + 1):
      print(str.format("{:^10}",u),end="")

    # end with another blank line
    print("")
    print("")    