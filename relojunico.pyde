vertical_position = 0
color_control = False 

def setup():
    size(600,610)


def draw():
    global vertical_position
    
    background(250)
    
    ellipse(width /1.15, vertical_position, 50, 50)
    if vertical_position > height:
        vertical_position = 0
    else:
        vertical_position = map(second(), 0, 59, 0, height)
    
    if color_control == True:
        fill(255, 0, 0)
    else:
        fill(0, 0, 255)
    

    
    
    ellipse(width / 2, vertical_position, 50, 50)
    if vertical_position > height:
        vertical_position = 0
    else:
        vertical_position = map(minute(), 0, 59, 0, height)
    
    if color_control == True:
        fill(255, 0, 100)
    else:
        fill(255, 0, 255)

    
    ellipse(width / 5, vertical_position, 50, 50)
    if vertical_position > height:
        vertical_position = 0
    else:
        vertical_position = map(hour(), 0, 23, 0, height)
    
    if color_control == True:
        fill(255, 255, 0)
    else:
        fill(0, 255, 255)

    
    line(425, 0,425, 600)
    line(225,0,225,600)
    line(25,0,25,600)
    
def mousePressed(): 
    global color_control
    color_control = not color_control
    



    
