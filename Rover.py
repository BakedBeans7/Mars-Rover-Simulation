import Mars

class Rover:
    
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    
    def __init__(self, terrain):
        self.mars = terrain
        self.x = 0
        self.y = 0
        
    def land(self, newX, newY):
        self.x = newX
        self.y = newY
        
        self.explore()
    
    def explore(self):
        
        found = self.mars.discover(self.x, self.y)
        
        message = str.format("                     Discovered {:^10} at {},{}",found,self.x,self.y)
        print(message)
        
    def move(self, direction):
        
        if (direction == Rover.RIGHT) and (self.y < self.mars.MAX_Y):
            self.y = self.y + 1
            
        elif (direction == Rover.RIGHT) and (self.x <self.mars.MAX_X):
            self.x = self.x + 1
            
        elif (direction == Rover.DOWN) and (self.y > 0):
            self.y = self.y - 1