import pygame
import random
import math

pygame.init() #Activates game


win_width, win_height = 500, 500
win = pygame.display.set_mode((win_width, win_height)) #creates game screen
pygame.display.set_caption("Stranger Things") #gives game a name

# Colors
background_color = (0, 0, 0)
cannon_color = (255, 0, 0)
projectile_color = (255, 255, 255)
monster_color = (0, 255, 0)

# Cannon
cannon_width, cannon_height = 50, 50
cannon_x = (win_width - cannon_width) // 2
cannon_y = 0

# Projectiles
projectiles = []
projectile_radius = 5
projectile_speed = 8

# Monsters
monsters = []
monster_width, monster_height = 20, 20
monster_speed = 2
spawn_delay = 60  # Delay between monster spawns
spawn_timer = spawn_delay

# Font
font = pygame.font.SysFont(None, 30)

# Functions

#Draws Cannon
def draw_cannon():
    pygame.draw.rect(win, cannon_color, (cannon_x, cannon_y, cannon_width, cannon_height))

#Fires Cannon
def fire_projectile():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    angle = math.atan2(mouse_y - cannon_y, mouse_x - (cannon_x + cannon_width / 2))
    velocity_x = math.cos(angle) * projectile_speed
    velocity_y = math.sin(angle) * projectile_speed
    projectiles.append([cannon_x + cannon_width // 2, cannon_height, velocity_x, velocity_y])

def draw_projectiles():
    for projectile in projectiles:
        pygame.draw.circle(win, projectile_color, (int(projectile[0]), int(projectile[1])), projectile_radius)

def move_projectiles():
    for projectile in projectiles:
        projectile[0] += projectile[2]  # Update x position
        projectile[1] += projectile[3]  # Update y position

#Creates monsters
def create_monster():
    x = random.randint(0, win_width - monster_width)
    monsters.append(pygame.Rect(x, win_height - monster_height, monster_width, monster_height))

def draw_monsters():
    for monster in monsters:
        pygame.draw.rect(win, monster_color, monster)

def move_monsters():
    for monster in monsters:
        monster.y -= monster_speed  # Update to move upwards


#Checks if the rock has hit the cannon
def check_collisions():
    global monsters, projectiles
    for monster in monsters[:]:
        for projectile in projectiles[:]:
            if monster.colliderect(pygame.Rect(projectile[0] - projectile_radius, projectile[1] - projectile_radius, projectile_radius * 2, projectile_radius * 2)):
                monsters.remove(monster)
                projectiles.remove(projectile)

# Main loop
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                fire_projectile()

    spawn_timer -= 1
    if spawn_timer <= 0:
        create_monster()
        spawn_timer = spawn_delay

    move_projectiles()
    move_monsters()
    check_collisions()

    win.fill(background_color)
    pygame.draw.line(win, (255, 0, 0), [0, cannon_height], [win_width, cannon_height], 5)  
    draw_cannon()
    draw_projectiles()
    draw_monsters()

    pygame.display.update()

pygame.quit()