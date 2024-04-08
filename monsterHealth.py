import math
import pygame

pygame.init() #activates pygame
#pip install pygame in terminal to make it work

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Monster Health")
clock = pygame.time.Clock()

screenWidth = 500
screenHeight = 500

cannon_width, cannon_height = 50,50
cannon_x = (screenWidth - cannon_width) // 2
cannon_y = 50

score = 0

#images
bg = pygame.image.load('Image/bg.png')
char = pygame.image.load('Image/Eleven.png')
char = pygame.transform.scale(char, (50, 50))
cannon = pygame.image.load('Image/cannon.png')
dog_skin = pygame.image.load('Image/dog.png')
dog_skin = pygame.transform.scale(dog_skin, (70,50))
demo_skin = pygame.image.load('Image/demo.png')
demo_skin = pygame.transform.scale(demo_skin, (80,120))

#character(eleven) class
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10

    def draw(self, win):
        win.blit(char,(self.x,self.y))


#enemy(demodog) class
class dog(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.vel = 3
        self.path = [self.y, self.end]
        self.hitbox = (self.x+15, self.y, 55, 50)
        self.health = 0
        self.visible = True

    def draw(self,win):
        #self.move()
        if self.visible:
            win.blit(dog_skin,(self.x, self.y))

        self.hitbox = (self.x +15, self.y, 55, 50)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def hit(self):
        global score
        if self.visible:
            if self.health > 0:
                self.health -= 1
            else:
                self.visible = False
                print('killed dog')
                bullets.pop(bullets.index(bullet))
                score += 1

# #enemy1 = dog(50,300,0,0,110)
#     def move(self):
#         if self.vel > 0:
#             if self.y + self.vel > self.path[1]:
#                 self.y -= self.vel
#             else:
#                 self.vel = self.vel * -1
#         else:
#             if self.y - self.vel > self.path[0]:
#                 self.y += self.vel
#             else:
#                 self.vel = self.vel * -1


#boss(demogorgon) class
class demo(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.vel = 3
        self.path = [self.y, self.end]
        self.hitbox = (self.x, self.y, 45, 60)
        self.health = 2
        self.visible = True

    def draw(self,win):
        #self.move()
        if self.visible:
            win.blit(demo_skin,(self.x, self.y))

        self.hitbox = (self.x, self.y, 45, 60)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def hit(self):
        global score
        if self.visible:
            if self.health > 0:
                self.health -= 1
                print('hit boss')
                bullets.pop(bullets.index(bullet))
            else:
                self.visible = False
                print('killed boss')
                bullets.pop(bullets.index(bullet))
                score += 5
            

    # def move(self):
    #     if self.vel > 0:
    #         if self.y + self.vel < self.path[1]:
    #             self.y += self.vel
    #         else:
    #             self.vel = self.vel * -1
    #     else:
    #         if self.y - self.vel > self.path[0]:
    #             self.y += self.vel
    #         else:
    #             self.vel = self.vel * -1

# class projectile(object):
#     def __init__(self, x, y, radius, color):
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.color = color
#         self.angle = math.atan2(self.mouseY - cannon_y, self.mouseX - (cannon_x + cannon_width / 2))
#         self.velX = math.cos(self.angle) * projectile_speed
#         self.velY = math.sin(self.angle) * projectile_speed
#         self.mouseX, self.mouseY = pygame.mouse.get_pos()

#     def draw(self, win):
#         pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

projectile_speed = 8
#fires cannon
def fire_projectile():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    angle = math.atan2(mouse_y - cannon_y, mouse_x - (cannon_x + cannon_width / 2))
    velocity_x = math.cos(angle) * projectile_speed
    velocity_y = math.sin(angle) * projectile_speed
    #cannon fired only when mouse is below platform
    if mouse_y > 50:
        bullets.append([cannon_x + cannon_width // 2, cannon_height, velocity_x, velocity_y])


#draw main
def redrawGameWindow():
    #draw background
    win.blit(bg,(0,0))
    #draw cannon
    win.blit(cannon,(cannon_x, cannon_y))
    #draw character
    eleven.draw(win)
    #draw enemies
    enemy1.draw(win)
    enemy2.draw(win)
    enemy3.draw(win)
    boss.draw(win)
    #draw score
    text = font.render('Score: ' + str(score), 1, (255,255,255))
    win.blit(text, (390,10))
    #draw bullets
    for bullet in bullets:
        pygame.draw.circle(win, (255,255,255), (int(bullet[0]), int(bullet[1])+cannon_y), 5)
    #draw platform
    pygame.draw.line(win, (0, 0, 0), [0, 100], [500, 100], 5)

    pygame.display.update()

#main loop
font = pygame.font.SysFont('none', 30)
eleven = player(225,50,50,50)
#enemy starting top posision (-,110,-,-,-)
enemy1 = dog(50,300,0,0,460)
enemy2 = dog(150,300,64,64,460)
enemy3 = dog(250,300,64,64,460)
boss = demo(400,300,64,64,460)
bullets = []
run = True

while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #checks for left mouse click
            if event.button == 1:
                fire_projectile()

    #move bullet
    for bullet in bullets:
        if bullet[1]-5  < enemy1.hitbox[1] + enemy1.hitbox[3] and bullet[1]+5  > enemy1.hitbox[1]:
            if bullet[0]+5  > enemy1.hitbox[0] and bullet[0]-5  < enemy1.hitbox[0] + enemy1.hitbox[2]:
                enemy1.hit()
                
        if bullet[1]-5  < enemy2.hitbox[1] + enemy2.hitbox[3] and bullet[1]+5  > enemy2.hitbox[1]:
            if bullet[0]+5  > enemy2.hitbox[0] and bullet[0]-5  < enemy2.hitbox[0] + enemy2.hitbox[2]:
                enemy2.hit()
                
        if bullet[1]-5  < enemy3.hitbox[1] + enemy3.hitbox[3] and bullet[1]+5  > enemy3.hitbox[1]:
            if bullet[0]+5  > enemy3.hitbox[0] and bullet[0]-5  < enemy3.hitbox[0] + enemy3.hitbox[2]:
                enemy3.hit()
                
        if bullet[1]-5  < boss.hitbox[1] + boss.hitbox[3] and bullet[1]+5  > boss.hitbox[1]:
            if bullet[0]+5  > boss.hitbox[0] and bullet[0]-5  < boss.hitbox[0] + boss.hitbox[2]:
                boss.hit()
                
        bullet[0] += bullet[2] # update x pos
        bullet[1] += bullet[3] # update y pos

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and eleven.x > eleven.vel:
        eleven.x-=eleven.vel
    if keys[pygame.K_RIGHT] and eleven.x < screenWidth - eleven.width - eleven.vel:
        eleven.x+=eleven.vel

    redrawGameWindow()

pygame.quit()
