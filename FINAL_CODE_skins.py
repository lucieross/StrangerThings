import random
import pygame
import math

pygame.init() #activates pygame

#pip install pygame in terminal to make it work

win_width, win_height = 500, 500
win = pygame.display.set_mode((500, 500)) #creates game screen
pygame.display.set_caption("Stranger Things") #gives game a name

#images
bg = pygame.image.load('Image/bg.png')
cannon_skin = pygame.image.load('Image/cannon.png')
dog_skin = pygame.image.load('Image/dog.png')
demo_skin = pygame.image.load('Image/demo.png')

run = True

#General Variables
lifecount = 3
monsterwall = False
rock_image = pygame.image.load("Image/rock.png")
ywall = 125

# Font
font = pygame.font.SysFont(None, 30)

#Eleven Varibles
Eleven_image_path = "Image/Eleven.png"
Eleven_image = pygame.image.load(Eleven_image_path)
Eleven_image = pygame.transform.scale(Eleven_image, (50, 50))
background_color = (0, 0, 0)

#Draw eleven
def draw_eleven(x, y):

    # Draw Eleven at the updated position
    win.blit(Eleven_image, (x, y))

# Initial position of Eleven
eleven_x = 225
eleven_y = 75
Eleven_speed = 0.25

#Rock Variables
xrock = random.randint(10,490)
yrock = 0
rocklist = []
rock_speed = 0.05
rock_collected = 0


def create_rock():
    scaled_rock = pygame.transform.scale(rock_image, (20, 20))
    win.blit(scaled_rock, (xrock, yrock))
    rock = pygame.Rect(xrock, yrock, 20, 20)

    return rock

#load eggo img
eggo_skin = pygame.image.load('Image/eggo.png')

def create_eggo():
    scaled_eggo_skin = pygame.transform.scale(eggo_skin, (20, 20))
    eggo = win.blit(scaled_eggo_skin,(xrock, yrock))

    return eggo

#Rock list
rocklist = [0,0,0,0,0,0,0,0,0,0]
eggoPosition = random.randint(0,9) # 1 eggo and 9 rocks in list
rocklist[eggoPosition] = 1
collectedEggo = False
rocklistPosition = 0

#Monster list
monsterlist1 = [0, 0, 0, 0, 0]
demogorgonPosition1 = random.randint(0,4) #4 normal monsters and 1 demogorgon in list
monsterlist1[demogorgonPosition1] = 1
ifDemogorgon = False
monsterlistPosition1 = 0

monsterlist2 = [0, 0, 0, 0, 0]
demogorgonPosition2 = random.randint(0,4) #4 normal monsters and 1 demogorgon in list
monsterlist2[demogorgonPosition2] = 1
ifDemogorgon = False
monsterlistPosition2 = 0

monsterlist3 = [0, 0, 0, 0, 0]
demogorgonPosition3 = random.randint(0,4) #4 normal monsters and 1 demogorgon in list
monsterlist3[demogorgonPosition3] = 1
ifDemogorgon = False
monsterlistPosition3 = 0

#Monster Variables
monstertimer1 = 0
monstertimer2 = 0
monstertimer3 = 0

xmonster1 = random.randint(10,490)
ymonster1 = 500

def create_monster1():
    # monster = pygame.draw.rect(win, (0, 0, 255), (xmonster1, ymonster1, 20, 50))
    if monsterlist1[monsterlistPosition1] == 1:
        #monster = pygame.draw.rect(win, (0, 0, 255), (xmonster1, ymonster1, 50, 50))
        scaled_demo = pygame.transform.scale(demo_skin, (43,60))
        monster = win.blit(scaled_demo, (xmonster1, ymonster1))
    else:
        scaled_dog = pygame.transform.scale(dog_skin, (70,53))
        monster = win.blit(scaled_dog, (xmonster1, ymonster1))


    return monster

xmonster2 = random.randint(10,490)
ymonster2 = 500
def create_monster2():
#monster = pygame.draw.rect(win, (255, 0, 0), (xmonster2, ymonster2, 20, 50))
    if monsterlist2[monsterlistPosition2] == 1:
        #monster = pygame.draw.rect(win, (255, 0, 0), (xmonster2, ymonster2, 50, 50))
        scaled_demo = pygame.transform.scale(demo_skin, (43,60))
        monster = win.blit(scaled_demo, (xmonster2, ymonster2))
    else:
        scaled_dog = pygame.transform.scale(dog_skin, (50,33))
        monster = win.blit(scaled_dog, (xmonster2, ymonster2))

    return monster

xmonster3 = random.randint(10,490)
ymonster3 = 500
def create_monster3():
    #monster = pygame.draw.rect(win, (0, 255, 0), (xmonster3, ymonster3, 20, 50))
    if monsterlist3[monsterlistPosition3] == 1:
        #monster = pygame.draw.rect(win, (0, 255, 0), (xmonster3, ymonster3, 50, 50))
        scaled_demo = pygame.transform.scale(demo_skin, (43,60))
        monster = win.blit(scaled_demo, (xmonster3, ymonster3))
    else:
        scaled_dog = pygame.transform.scale(dog_skin, (60,43))
        monster = win.blit(scaled_dog, (xmonster3, ymonster3))

    return monster

xdemogorgon = random.randint(10,490)
ydemogorgon = 500
def create_demogorgon():
    scaled_demo = pygame.transform.scale(demo_skin, (60,43))
    monster = win.blit(scaled_demo, (xdemogorgon, ydemogorgon))
    #monster = pygame.draw.rect(win, (0, 255, 0), (xdemogorgon, ydemogorgon, 50, 50))
    return monster



#Level
level = 5

run = True #Indicates pygame is running

# infinite loop when game is active

while run:
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.

    for event in pygame.event.get():
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.

        if event.type == pygame.QUIT:
            # it will make exit the while loop
            run = False

#screen setup
    win.fill((60,60,60))  # colour of the game screen
    win.blit(cannon_skin, (225, 75, 50, 50))  # cannon
    pygame.draw.line(win, (255, 0, 0), [0, ywall], [500, ywall], 5)  # dividing line


# Render text for collected rocks
    text = font.render("Rocks Collected: " + str(rock_collected), True, (255, 255, 255))
    win.blit(text, (10, 10))


# Check for rock collection
    if rocklist[rocklistPosition] == 0:
        create_rock()
        ifEggo = False
        if yrock <= 105: #if above wall, move rock down
            yrock += rock_speed

    elif rocklist[rocklistPosition] == 1:
        create_eggo()
        ifEggo = True
        if yrock <= 105: #if above wall, move rock down
            yrock += rock_speed

    if rocklistPosition == 9: #resets list when the end is reached
        rocklist = [0,0,0,0,0,0,0,0,0,0]
        eggoPosition = random.randint(0,9)
        rocklist[eggoPosition] = 1
        rocklistPosition = 0


# Check if Eleven collects the rock
    if yrock >= 75 and yrock <= 125:
        if eleven_x <= xrock <= eleven_x + 50:
            if ifEggo == True:
                    print("Eggo Collected!")
                    # Reset the rock position to make another fall
                    xrock = random.randint(10, 490)
                    yrock = 0
                    rocklist[rocklistPosition]
                    rocklistPosition += 1 # Iterate through rocklist
                    collectedEggo = True
            if rock_collected < 5 and ifEggo == False:  # Check if Eleven has collected less than 5 rocks
                rock_collected += 1 # Add on to the number of rocks collected
                print("Rock collected:", rock_collected)
                # Reset the rock position to make another fall
                xrock = random.randint(10, 490)
                yrock = 0
                rocklistPosition += 1
                rocklist[rocklistPosition] # Iterate through rocklist

    if collectedEggo == True: #resets all monsters
        ymonster1 = 500
        xmonster1 = random.randint(10,490)
        ymonster2 = 500
        xmonster2 = random.randint(10,490)
        ymonster3 = 500
        xmonster3 = random.randint(10,490)
        monstertimer1 = 0
        monstertimer2 = 0
        monstertimer3 = 0
        collectedEggo = False

# Monster 1 spawn

    if ymonster1 >= 126 and monstertimer1 <= 375:
        monster1 = create_monster1()
        ymonster1 -= 0.1  # later, do this as - level speed
        monstertimer1 += 0.1 # takes approx. 375 to get to line
        monstertimer2 += 0.1
        monstertimer3 += 0.1

    else:
        ymonster1 = 500
        xmonster1 = random.randint(10,490)
        monstertimer1 = 0

    if math.floor(ymonster1) == ywall:
        monsterlistPosition1 += 1


# Monster 2 spawn

    if ymonster2 >= 126 and monstertimer2 >= 187.5 and level >= 3 and level <= 4 or ymonster2 >= 126 and monstertimer2 >= 125 and level == 5: #monster timer being different for different levels allows monsters to be evenly spaced
        monster2 = create_monster2()
        ymonster2 -= 0.1  # later, do this as - level speed
    else:
        ymonster2 = 500
        xmonster2 = random.randint(10,490)

    if math.floor(ymonster2) == ywall:
            monsterlistPosition2 += 1


# Monster 3 spawn

    if ymonster3 >= 126 and monstertimer3 >= 250 and level == 5:
        monster3 = create_monster3()
        ymonster3 -= 0.1  # later, do this as - level speed
    else:
        ymonster3 = 500
        xmonster3 = random.randint(10,490)

    if math.floor(ymonster3) == ywall:
            monsterlistPosition3 += 1


#Reset List

    if monsterlistPosition1 == 4: #resets list when the end is reached
        monsterlist1 = [0, 0, 0, 0, 0]
        demogorgonPosition1 = random.randint(0,4) #4 normal monsters and 1 demogorgon in list
        monsterlist1[demogorgonPosition1] = 1
        monsterlistPosition1 = 0


    if monsterlistPosition2 == 4: #resets list when the end is reached
        monsterlist2 = [0, 0, 0, 0, 0]
        demogorgonPosition2 = random.randint(0,4) #4 normal monsters and 1 demogorgon in list
        monsterlist2[demogorgonPosition2] = 1
        monsterlistPosition2 = 0


    if monsterlistPosition3 == 4: #resets list when the end is reached
        monsterlist3 = [0, 0, 0, 0, 0]
        demogorgonPosition3 = random.randint(0,4) #4 normal monsters and 1 demogorgon in list
        monsterlist3[demogorgonPosition3] = 1
        monsterlistPosition3 = 0


#moving eleven
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and eleven_x - Eleven_speed > 0:
        eleven_x -= Eleven_speed
    if keys[pygame.K_RIGHT] and eleven_x + Eleven_speed + 50 < win_width:
        eleven_x += Eleven_speed

    draw_eleven(eleven_x, eleven_y)

# Refresh the window
    pygame.display.update()

pygame.quit()
