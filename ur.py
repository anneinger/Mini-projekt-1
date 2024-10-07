import pygame
import math
from datetime import datetime

#Start pygame
pygame.init()

#Make a screen
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

#Middle of screen
center = pygame.Vector2(width //2, height //2)

#Colours
blue = (137,207,240)
yellow =(252,239,145)
black = (0,0,0)

#Variables
radius=190
r = 100
angle = -90 #to start the clock hands and numbers at 12 instead of at 3, which is 0 in pygame
font = pygame.font.Font(None,36) #Numbers font
lines = 60

#Main loop
while True:

    #Clean slate
    screen.fill(blue)

    #Black edge
    clock_circle=pygame.draw.circle(screen, black, center,195)

    #Circle
    clock_circle=pygame.draw.circle(screen, yellow, center,190)
    
    #Dot in the middle
    clock_circle=pygame.draw.circle(screen, black, center,5)

    #Number position
    for i in range (1,13):
        x = center[0] + (radius - 30) * math.cos(math.radians(i * 360/12 + angle))  
        y = center[1] + (radius - 30) * math.sin(math.radians(i * 360/12 + angle))

    # Render the number
        number_surface = font.render(str(i), True, (0,0,0)) #render expects a string not numbers, therefore (str(i))
        number_rect = number_surface.get_rect(center=(x, y)) #placing numbers correctly
        
    # Draw the number on the screen
        screen.blit(number_surface, number_rect)

    # Draw the minute and hour marking lines 
    for i in range(lines): # Make 60 lines
        if i % 5 == 0: #Every 5th is a thick line
            line_size = 4
        else: 
            line_size = 2 #The other lines are small
        
        start_x = center.x + (radius - 15) * math.cos(math.radians(i * 360/lines + angle))
        start_y = center.y + (radius - 15) * math.sin(math.radians(i * 360/lines + angle))
        end_x = center.x + (radius) * math.cos(math.radians(i * 360/lines + angle))
        end_y = center.y + (radius) * math.sin(math.radians(i * 360/lines + angle))
        pygame.draw.line(screen,(0,0,0),(start_x,start_y),(end_x,end_y),line_size)

    #Time
    s = datetime.now().second 
    m = datetime.now().minute 
    h = datetime.now().hour 

    #Line for seconds
    x = center[0] + (r + 40) * math.cos(math.radians(angle + 6*s)) # 360/60 = 6 * s to move it 6* pr second
    y = center[1] + (r + 40) * math.sin(math.radians(angle + 6*s))
    end_position_s = (x, y)
    pygame.draw.line(screen,(255,0,0),center,end_position_s,2)

    #Line for minutes
    x = center[0] + (r + 60) * math.cos(math.radians(angle + 6*m))
    y = center[1] + (r + 60) * math.sin(math.radians(angle + 6*m))
    end_position_m = (x, y)
    pygame.draw.line(screen,(0,0,0),center,end_position_m,3)

    #Line for hours
    x = center[0] + r * math.cos(math.radians(angle + 30*(h + m / 60))) # 360/12 = 30 * s to move it 30 * pr hour
    y = center[1] + r * math.sin(math.radians(angle + 30*(h + m / 60))) #(h + m/60) so the line moves with the minutes not only after 1 hour
    end_position_h = (x, y)
    pygame.draw.line(screen,(0,0,0),center,end_position_h,6)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    


