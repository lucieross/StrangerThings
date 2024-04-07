import random
import pygame
import math

pygame.init() #activates pygame

#pip install pygame in terminal to make it work

win_width, win_height = 500, 500
bg = pygame.image.load('Image/bg.png')

win = pygame.display.set_mode((win_width, win_height)) #creates game screen
pygame.display.set_caption("Stranger Things") #gives game a name

# Font
font = pygame.font.SysFont('comicsans', 20)

# Colors
background_color = (0, 0, 0)
projectile_color = (255, 255, 255)
monster_color = (0, 255, 0)

#images
bg = pygame.image.load('Image/bg.png')
cannon_skin = pygame.image.load('Image/cannon.png')
dog_skin = pygame.image.load('Image/dog.png')
demo_skin = pygame.image.load('Image/demo.png')
eggo_skin = pygame.image.load('Image/eggo.png')

#General Variables
lifecount = 3
monsterwall = False
rock_image = pygame.image.load("Image/rock.png")
ywall = 125
score = 0

#Eleven Varibles
Eleven_image_path = "Image/Eleven.png"
Eleven_image = pygame.image.load(Eleven_image_path)
Eleven_image = pygame.transform.scale(Eleven_image, (50, 50))

# Cannon
cannon_width, cannon_height = 50, 75
cannon_x = (win_width - cannon_width) // 2
cannon_y = 0
cannon_x_left = 225
cannon_x_right = 275

# Projectiles
projectiles = []
projectile_radius = 5
projectile_speed = 8

# Gravity
gravity = 0.5

# Score
score = 0

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

#Projectiles Functions
def fire_projectile():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    angle = math.atan2(mouse_y - cannon_y, mouse_x - (cannon_x + cannon_width / 2))
    velocity_x = math.cos(angle) * projectile_speed
    velocity_y = math.sin(angle) * projectile_speed
    if mouse_x<255:
        projectiles.append([cannon_x_left, cannon_height, velocity_x, velocity_y])
    else:
        projectiles.append([cannon_x_right, cannon_height, velocity_x, velocity_y])

def draw_projectiles():
    for projectile in projectiles:
        pygame.draw.circle(win, projectile_color, (int(projectile[0]), int(projectile[1])), projectile_radius)

def move_projectiles():
    for projectile in projectiles:
        projectile[0] += projectile[2]
        projectile[1] += projectile[3]
        projectile[3] += gravity  # Apply gravity

#Draw eleven
def draw_eleven(x, y):
    win.blit(Eleven_image, (x, y)) #Draw Eleven at the updated position

#Rock functions
def create_rock():
    scaled_rock = pygame.transform.scale(rock_image, (20, 20))
    win.blit(scaled_rock, (xrock, yrock))
    rock = pygame.Rect(xrock, yrock, 20, 20)
  
    return rock

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
    #monster = pygame.draw.rect(win, (0, 0, 255), (xmonster1, ymonster1, 20, 50))
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

#Draw MAIN
def redrawGameWindow():
    win.blit(bg, (0,0))

    text = font.render('Score: ' + str(score), 1,(0,255,0))
    win.blit(text, (0,0))

    pygame.draw.line(win, (255, 255, 255), [0, cannon_height], [win_width, cannon_height], 5)

    draw_projectiles()

    pygame.display.update()

def check_collisions():
    global monsterlist1, monsterlist2, monsterlist3, projectiles
    for monster in monsterlist1[:]:
        for projectile in projectiles[:]:
            if monster.colliderect(pygame.Rect(projectile[0] - projectile_radius, projectile[1] - projectile_radius, projectile_radius * 2, projectile_radius * 2)):
                monsterlist1.remove(monster)
                projectiles.remove(projectile)
                score += 1
    for monster in monsterlist2[:]:
        for projectile in projectiles[:]:
            if monster.colliderect(pygame.Rect(projectile[0] - projectile_radius, projectile[1] - projectile_radius, projectile_radius * 2, projectile_radius * 2)):
                monsterlist2.remove(monster)
                projectiles.remove(projectile)
                score += 1
    for monster in monsterlist3[:]:
        for projectile in projectiles[:]:
            if monster.colliderect(pygame.Rect(projectile[0] - projectile_radius, projectile[1] - projectile_radius, projectile_radius * 2, projectile_radius * 2)):
                monsterlist3.remove(monster)
                projectiles.remove(projectile)
                score += 1


# Function to display a 'game over' text for a few seconds
def show_game_over():
    game_over_text = font.render("GAME OVER!", True, (255,0,0))
    text_rect = game_over_text.get_rect(center=(win_width // 2, win_height // 2))
    win.blit(game_over_text, text_rect)
    pygame.display.flip()
    pygame.time.delay(3000)

# Function to display a 'you won' text if game is finished
def show_you_won():
    you_won_text = font.render("CONGRATULATIONS, YOU WON!", True, (255,0,0))
    text_rect = you_won_text.get_rect(center=(win_width // 2, win_height // 2))
    win.blit(you_won_text, text_rect)
    pygame.display.flip()
    pygame.time.delay(3000)

# Function to display a 'level is completed' text
def level_is_completed():
    level_completed_text = font.render("LEVEL IS COMPLETED", True, (255,0,0))
    text_rect = level_completed_text.get_rect(center=(win_width // 2, win_height // 2))
    win.blit(level_completed_text, text_rect)
    pygame.display.flip()
    pygame.time.delay(3000)   



#Level
level = 1

run = True #Indicates pygame is running
#clock = pygame.time.Clock()

# infinite loop when game is active

while run:
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.

    #clock.tick(60)

    for event in pygame.event.get():
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.

        if event.type == pygame.QUIT:
            # it will make exit the while loop
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                fire_projectile()
    
    #spawn_timer -= 1
    #if spawn_timer <= 0:
        #create_monster()
        #spawn_timer = spawn_delay

    move_projectiles()
    #check_collisions()

#screen setup
    win.blit(bg, (0,0))

    text = font.render('Score: ' + str(score), True,(255,255,255))
    win.blit(text, (2,20))
    win.blit(cannon_skin, (225, 75, 50, 50))  # cannon
    pygame.draw.line(win, (255, 255, 255), [0, ywall], [500, ywall], 5)  # dividing line

    #draw_cannon()
    draw_projectiles()

# Render text for collected rocks
    text = font.render("Rocks Collected: " + str(rock_collected), True, (255, 255, 255))
    win.blit(text, (2, 0))

# Render text for level
    level_text = font.render("Level: " + str(level), True, (255, 255, 255))
    win.blit(level_text, (425, 0))

# Render text for life counter
    life_text = font.render("Lives: " + str(lifecount), True, (255, 255, 255))
    win.blit(life_text, (425,20))

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
        lifecount -= 1

    
# Monster 2 spawn

    if ymonster2 >= 126 and monstertimer2 >= 187.5 and level >= 3 and level <= 4 or ymonster2 >= 126 and monstertimer2 >= 125 and level == 5: #monster timer being different for different levels allows monsters to be evenly spaced
        monster2 = create_monster2() 
        ymonster2 -= 0.1  # later, do this as - level speed
    else:
        ymonster2 = 500
        xmonster2 = random.randint(10,490)

    if math.floor(ymonster2) == ywall:
            monsterlistPosition2 += 1
            lifecount -= 1
        

# Monster 3 spawn

    if ymonster3 >= 126 and monstertimer3 >= 250 and level == 5:
        monster3 = create_monster3() 
        ymonster3 -= 0.1  # later, do this as - level speed
    else:
        ymonster3 = 500
        xmonster3 = random.randint(10,490)

    if math.floor(ymonster3) == ywall:
            monsterlistPosition3 += 1
            lifecount -= 1
        

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

    if keys[pygame.K_a] and eleven_x - Eleven_speed > 0:  
        eleven_x -= Eleven_speed
    if keys[pygame.K_d] and eleven_x + Eleven_speed + 50 < win_width: 
        eleven_x += Eleven_speed

    draw_eleven(eleven_x, eleven_y)  

# Changing levels
    if (score > 0) & (score % (level*5) == 0):
        #if game is finished, display a you won text then reset the game
        if level == 5:
            show_you_won()
            lifecount = 3
            score = 0
            rock_collected = 0
            level = 1

        level_is_completed()
        level += 1
        lifecount += 1
        score = 0 

# Resets the game 
    if lifecount<=0:
        show_game_over()
        lifecount = 3
        score = 0
        rock_collected = 0
        level = 1

# Refresh the window
    pygame.display.update()
pygame.quit()