import pygame
pygame.init()
W = 1280
H = 720
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Game_2")
bg = pygame.image.load('bg.png').convert()
bg = pygame.transform.scale(bg, (bg.get_width()*2, bg.get_height()*2))
hp_bar = pygame.image.load('hp_bar.png').convert()
house = pygame.image.load('house1.png').convert_alpha()
house = pygame.transform.scale(house, (house.get_width()*2, house.get_height()*2))
idle = pygame.image.load('idle.png').convert_alpha()
idle = pygame.transform.scale(idle, (idle.get_width()*2, idle.get_height()*2))
lastMove = "down"
flastMove = "fdown"
FPS = 30
speed = 5
plHP = 100

rlBorder_r = False
rlBorder_l = False
rlBorder_u = False
rlBorder_d = False

Up = False
Down = False
Left = False
Right = False
plI = False
plII = False
plIII = False
plIV = False


posx = 0
posy = 0

clock = pygame.time.Clock()
#Screen and movement of Player
class screen():
    sc_count = 0
    def __init__(self, x, y, obj, bg):
        #x = -270
        #y = -1218
        self.x = x
        self.y = y
        self.obj = obj
        self.bg = bg
    def draw(self, win):
        #2530 210   1265 105 1905 465

        win.blit(self.obj, (self.x, self.y))


        #pygame.draw.rect(win, (255, 0, 0), (W//2, H//2, 30, 60))
    def Movement(self, win):
        global rlBorder_r
        global rlBorder_l
        global rlBorder_u
        global rlBorder_d
        global speed
        global posx
        global posy
        global Left
        global Right
        global Up
        global Down
        global plI
        global plII
        global plIII
        global plIV



        keys = pygame.key.get_pressed()




        if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT] and rlBorder_d == False and rlBorder_r == False:
            self.y -= speed
            self.x -= speed
            plI = True

        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT] and rlBorder_d == False and rlBorder_l == False:
            self.y -= speed
            self.x += speed
            plII = True

        elif keys[pygame.K_UP] and keys[pygame.K_LEFT] and rlBorder_u == False and rlBorder_l == False:
            self.y += speed
            self.x += speed
            plIII = True

        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT] and rlBorder_u == False and rlBorder_r == False:
            self.y += speed
            self.x -= speed
            plIV = True

        elif keys[pygame.K_o]:
            speed = 20
        elif keys[pygame.K_l]:
            speed = 1
        elif keys[pygame.K_p]:
            speed = 5
        elif keys[pygame.K_LEFT] and rlBorder_l == False:
            Left = True
            self.x += speed
        elif keys[pygame.K_RIGHT] and rlBorder_r == False:
            self.x -= speed
            Right = True

        elif keys[pygame.K_UP] and rlBorder_u == False:
            self.y += speed
            Up = True

        elif keys[pygame.K_DOWN] and rlBorder_d == False:
            self.y -= speed
            Down = True





        #######################
        #############################
        ####################################################
        ####################################################
        ####################################################
        elif keys[pygame.K_KP8]:
            self.y += speed
            posy -= speed
        elif keys[pygame.K_KP5]:
            self.y -= speed
            posy += speed
        elif keys[pygame.K_KP6]:
            self.x -= speed
            posx += speed
        elif keys[pygame.K_KP4]:
            self.x += speed
            posx -= speed
        ####################################################
        ####################################################
        ####################################################
        ####################################################
        else:
            Left = False
            Right = False
            Up = False
            Down = False
        pygame.display.flip()
    def poscount(self):
        global posx
        global posy
        global speed
        global plI
        global plII
        global plIII
        global plIV
        if Left == True:
            posx -= speed * 2
        elif Right == True:
            posx += speed * 2
        elif Up == True:
            posy -= speed * 2
        elif Down == True:
            posy += speed * 2
        elif plI == True:
            posy += speed * 2
            posx += speed * 2
        elif plII == True:
            posy += speed * 2
            posx -= speed * 2
        elif plIII == True:
            posx -= speed * 2
            posy -= speed * 2
        elif plIV == True:
            posx += speed * 2
            posy -= speed * 2


sc1 = screen(-647, -837, bg, True)
house1 = screen(1905, 465, house, False)
#obj_npc1 = screen(700, -60, idle, False)
#posx = self.x - 640
#posy = self.y - 360
#####################################################

def Borders():
    global rlBorder_r
    global rlBorder_l
    global rlBorder_u
    global rlBorder_d
    global posx
    global posy
    #верхний левый 1860 -384
    #верхний правый 2170 -384
    #нижний левый 1858 902
    #нижний правый 2174 902
    rlBorder_r = False
    rlBorder_l = False
    rlBorder_u = False
    rlBorder_d = False
    if ((posy >= -384) and (posy < -384 + 15) and (posx >= 1860) and (posx <= 2170)) or (posy >= 2674) or\
    ((posy >= 1254) and (posy < 1254 + 15) and (posx >= 1852) and (posx <= 2158)):
        rlBorder_d = True
    else:
        rlBorder_d = False

    if ((posx <= 2170) and (posx > (2170 - 15)) and (posy >= -384) and (posy <= 902)) or (posx <= -314) or\
    ((posx <= 2158) and (posx > (2158 - 15)) and (posy >= 1254) and (posy <= 2742)):
        rlBorder_l = True
    else:
        rlBorder_l = False

    if ((posy <= 902) and (posy >= (902 - 15)) and (posx >= 1860) and (posx <= 2170)) or (posy <= -316) or\
    ((posy <= 2742) and (posy >= (2742 - 15)) and (posx >= 1852) and (posx <= 2158)):
        rlBorder_u = True
    else:
        rlBorder_u = False

    if ((posx >= 1860) and (posx < 1860 + 15) and (posy <= 902) and (posy >= -384)) or (posx >= 4626) or\
    ((posx >= 1852) and (posx < 1852 + 15) and (posy <= 2742) and (posy >= 1254)):
        rlBorder_r = True
    else:
        rlBorder_r = False
##############################################
##############################################

    if ((npc1.fposy >= -384) and (npc1.fposy < -384 + 9) and (npc1.fposx >= 1860) and (npc1.fposx <= 2170)) or (npc1.fposy >= 2674) or\
    ((npc1.fposy >= 1254) and (npc1.fposy < 1254 + 9) and (npc1.fposx >= 1852) and (npc1.fposx <= 2158)):
        npc1.fBorder_d = True
    else:
        npc1.fBorder_d = False

    if ((npc1.fposx <= 2170) and (npc1.fposx > (2170 - 9)) and (npc1.fposy >= -384) and (npc1.fposy <= 902)) or (npc1.fposx <= -314) or\
    ((npc1.fposx <= 2158) and (npc1.fposx > (2158 - 9)) and (npc1.fposy >= 1254) and (npc1.fposy <= 2742)):
        npc1.fBorder_l = True
    else:
        npc1.fBorder_l = False

    if ((npc1.fposy <= 902) and (npc1.fposy >= (902 - 9)) and (npc1.fposx >= 1860) and (npc1.fposx <= 2170)) or (npc1.fposy <= -316) or\
    ((npc1.fposy <= 2742) and (npc1.fposy >= (2742 - 9)) and (npc1.fposx >= 1852) and (npc1.fposx <= 2158)):
        npc1.fBorder_u = True
    else:
        npc1.fBorder_u = False

    if ((npc1.fposx >= 1860) and (npc1.fposx < 1860 + 9) and (npc1.fposy <= 902) and (npc1.fposy >= -384)) or (npc1.fposx >= 4626) or\
    ((npc1.fposx >= 1852) and (npc1.fposx < 1852 + 9) and (npc1.fposy <= 2742) and (npc1.fposy >= 1254)):
        npc1.fBorder_r = True
    else:
        npc1.fBorder_r = False



#верхний левый 1852 1254
#верхний правый  2158 1254
#нижний левый  1852 2742
#нижний правый 2158 2742






#####################################################
class Animation():
    def __init__(self, count, x, y, Player):
        self.count = count
        self.x = x
        self.y = y
        self.Player = Player
    def anim(self, win):
        global lastMove
        global Left
        global Right
        global Up
        global Down
        global plI
        global plII
        global plIII
        global plIV
##########################################################
        idle = pygame.image.load('idle.png').convert_alpha()
        walk1 = pygame.image.load('walk1.png').convert_alpha()
        walk2 = pygame.image.load('walk2.png').convert_alpha()
        walk3 = pygame.image.load('walk3.png').convert_alpha()

        idle =pygame.transform.scale(idle, (idle.get_width()*2, idle.get_height()*2))
        walk1 = pygame.transform.scale(walk1, (walk1.get_width()*2, walk1.get_height()*2))
        walk2 = pygame.transform.scale(walk2, (walk2.get_width()*2, walk2.get_height()*2))
        walk3 = pygame.transform.scale(walk3, (walk3.get_width()*2, walk3.get_height()*2))



        idle_down = idle
        walk1_down = walk1
        walk2_down = walk2
        walk3_down = walk3

        idle_up = pygame.transform.flip(idle, 0, 1)
        walk1_up = pygame.transform.flip(walk1, 0, 1)
        walk2_up = pygame.transform.flip(walk2, 0, 1)
        walk3_up = pygame.transform.flip(walk3, 0, 1)

        idle_left = pygame.transform.rotate(idle_up, 90)
        walk1_left = pygame.transform.rotate(walk1_up, 90)
        walk2_left = pygame.transform.rotate(walk2_up, 90)
        walk3_left = pygame.transform.rotate(walk3_up, 90)

        idle_right = pygame.transform.rotate(idle_up, -90)
        walk1_right = pygame.transform.rotate(walk1_up, -90)
        walk2_right = pygame.transform.rotate(walk2_up, -90)
        walk3_right = pygame.transform.rotate(walk3_up, -90)

        idle_I = pygame.transform.rotate(idle_right, -45)
        walk1_I = pygame.transform.rotate(walk1_right, -45)
        walk2_I = pygame.transform.rotate(walk2_right, -45)
        walk3_I = pygame.transform.rotate(walk3_right, -45)

        idle_II = pygame.transform.rotate(idle_left, 45)
        walk1_II = pygame.transform.rotate(walk1_left, 45)
        walk2_II = pygame.transform.rotate(walk2_left, 45)
        walk3_II = pygame.transform.rotate(walk3_left, 45)

        idle_III = pygame.transform.rotate(idle_left, -45)
        walk1_III = pygame.transform.rotate(walk1_left, -45)
        walk2_III = pygame.transform.rotate(walk2_left, -45)
        walk3_III = pygame.transform.rotate(walk3_left, -45)

        idle_IV = pygame.transform.rotate(idle_right, 45)
        walk1_IV = pygame.transform.rotate(walk1_right, 45)
        walk2_IV = pygame.transform.rotate(walk2_right, 45)
        walk3_IV = pygame.transform.rotate(walk3_right, 45)







        walkRight = [walk1_right, walk2_right, walk3_right, walk1_right, walk2_right, walk3_right]
        walkLeft = [walk1_left, walk2_left, walk3_left, walk1_left, walk2_left, walk3_left]
        walkUp = [walk1_up, walk2_up, walk3_up, walk1_up, walk2_up, walk3_up]
        walkDown = [walk1_down, walk2_down, walk3_down, walk1_down, walk2_down, walk3_down]
        walkI = [walk1_I, walk2_I, walk3_I, walk1_I, walk2_I, walk3_I]
        walkII = [walk1_II, walk2_II, walk3_II, walk1_II, walk2_II, walk3_II]
        walkIII = [walk1_III, walk2_III, walk3_III, walk1_III, walk2_III, walk3_III]
        walkIV = [walk1_IV, walk2_IV, walk3_IV, walk1_IV, walk2_IV, walk3_IV]
#####################################################################
#####################################################################
        Up = False
        Down = False
        Left = False
        Right = False
        plI = False
        plII = False
        plIII = False
        plIV = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and keys[pygame.K_LEFT] and self.Player == True:
            plIII = True
        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT] and self.Player == True:
            plIV = True
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and self.Player == True:
            plI = True
        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT] and self.Player == True:
            plII = True

        elif keys[pygame.K_LEFT] and self.Player == True:
            Left = True





        elif keys[pygame.K_RIGHT] and self.Player == True:
            Right = True
        elif keys[pygame.K_UP] and self.Player == True:
            Up = True
        elif keys[pygame.K_DOWN] and self.Player == True:
            Down = True

        else:
            Left = False
            Right = False
            Up = False
            Down = False
            plI = False
            plII = False
            plIII = False
            plIV = False
        if self.count + 1 >= 30:
            self.count = 0

        elif plI == True:
            win.blit(walkI[self.count // 5], (self.x, self.y))
            self.count += 1
            lastMove = "downI"

        elif plII == True:
            win.blit(walkII[self.count // 5], (self.x, self.y))
            self.count += 1
            lastMove = "downII"

        elif plIII == True:
            win.blit(walkIII[self.count // 5], (self.x, self.y))
            self.count += 1
            lastMove = "upIII"

        elif plIV == True:
            win.blit(walkIV[self.count // 5], (self.x, self.y))
            self.count += 1
            lastMove = "upIV"

        elif Up == True:
            win.blit(walkUp[self.count // 5], (self.x, self.y))
            self.count += 1
            lastMove = "up"

        elif Down == True:
            win.blit(walkDown[self.count // 5], (self.x, self.y))
            self.count += 1
            lastMove = "down"

        elif Left == True:
            win.blit(walkLeft[self.count // 5], (self.x, self.y))
            self.count += 1
            lastMove = "left"

        elif Right == True:
            win.blit(walkRight[self.count // 5], (self.x, self.y))
            self.count += 1
            lastMove = "right"

        else:
            if lastMove == "right":
                win.blit(idle_right, (self.x, self.y))
            elif lastMove == "downI":
                win.blit(idle_I, (self.x, self.y))
            elif lastMove == "downII":
                win.blit(idle_II, (self.x, self.y))
            elif lastMove == "upIII":
                win.blit(idle_III, (self.x, self.y))
            elif lastMove == "upIV":
                win.blit(idle_IV, (self.x, self.y))

            elif lastMove == "up":
                win.blit(idle_up, (self.x, self.y))
            elif lastMove == "left":
                win.blit(idle_left, (self.x, self.y))
            else:
                win.blit(idle, (self.x, self.y))
        #pygame.display.update()
        #pygame.display.flip()




##############
PlAnim = Animation(0, W // 2, H // 2, True)


class npc():
    def __init__(self, x, y, fcount, fposx, fposy, fBorder_r, fBorder_l, fBorder_d, fBorder_u, hp):
        self.x = x
        self.y = y
        self.fcount = fcount
        self.fposx = fposx
        self.fposy = fposy
        self.fBorder_r = fBorder_r
        self.fBorder_u = fBorder_u
        self.fBorder_l = fBorder_l
        self.fBorder_d = fBorder_d
        self.hp = hp

    def foe(self, win):
        global posx
        global posy
        global Left
        global Right
        global Up
        global Down
        global flastMove

        fleft, fright, fup, fdown = False, False, False, False
        f_I, f_II, f_III, f_IV = False, False, False, False
        fspeed = 3
        #pygame.draw.rect(win, (255, 0, 0), (700, 200, 30, 30))
        if self.x < 630 and self.fBorder_r == False and self.y == 350:
            self.fposx += fspeed * 2
            self.x += fspeed
            fright = True


        elif self.y < 350 and (self.fBorder_u == False) and self.x == 630:
            self.fposy += fspeed * 2
            self.y += fspeed
            fdown = True


        elif self.x > 650 and self.fBorder_l == False and self. y == 350:
            self.fposx -= fspeed * 2
            self.x -= fspeed
            fleft = True


        elif self.y > 370 and self.fBorder_d == False and self.x == 630:
            self.fposy -= fspeed * 2
            self.y -= fspeed
            fup = True

        elif self.x < 630 and self.y < 350 and self.fBorder_r == False and self.fBorder_d == False:
            f_I = True
            self.x += fspeed
            self.y += fspeed

        elif self.x > 630 and self.y < 350 and self.fBorder_d == False and self.fBorder_l == False:
            f_II = True
            self.x -= fspeed
            self.y += fspeed

        elif self.x > 630 and self.y > 350 and self.fBorder_u == False and self.fBorder_l == False:
            f_III = True
            self.x -= fspeed
            self.y -= fspeed

        elif self.x < 630 and self.y >= 350 and self.fBorder_u == False and self.fBorder_r == False:
            f_IV == True
            self.x += fspeed
            self.y -= fspeed

        else:
            fleft, fright, fup, fdown = False, False, False, False
        if Left:
            self.x += speed
        elif Right:
            self.x -= speed
        elif Up:
            self.y += speed
        elif Down:
            self.y -=speed

##################################################
        ###########################################
        fidle = pygame.image.load('fidle.png').convert_alpha()
        fwalk1 = pygame.image.load('fwalk1.png').convert_alpha()
        fwalk2 = pygame.image.load('fwalk2.png').convert_alpha()
        fwalk3 = pygame.image.load('fwalk3.png').convert_alpha()

        fidle =pygame.transform.scale(fidle, (fidle.get_width()*2, fidle.get_height()*2))
        fwalk1 = pygame.transform.scale(fwalk1, (fwalk1.get_width()*2, fwalk1.get_height()*2))
        fwalk2 = pygame.transform.scale(fwalk2, (fwalk2.get_width()*2, fwalk2.get_height()*2))
        fwalk3 = pygame.transform.scale(fwalk3, (fwalk3.get_width()*2, fwalk3.get_height()*2))



        fidle_down = fidle
        fwalk1_down = fwalk1
        fwalk2_down = fwalk2
        fwalk3_down = fwalk3

        fidle_up = pygame.transform.flip(fidle, 0, 1)
        fwalk1_up = pygame.transform.flip(fwalk1, 0, 1)
        fwalk2_up = pygame.transform.flip(fwalk2, 0, 1)
        fwalk3_up = pygame.transform.flip(fwalk3, 0, 1)

        fidle_left = pygame.transform.rotate(fidle_up, 90)
        fwalk1_left = pygame.transform.rotate(fwalk1_up, 90)
        fwalk2_left = pygame.transform.rotate(fwalk2_up, 90)
        fwalk3_left = pygame.transform.rotate(fwalk3_up, 90)


        fidle_right = pygame.transform.rotate(fidle_up, -90)
        fwalk1_right = pygame.transform.rotate(fwalk1_up, -90)
        fwalk2_right = pygame.transform.rotate(fwalk2_up, -90)
        fwalk3_right = pygame.transform.rotate(fwalk3_up, -90)

        fidle_1 = pygame.transform.rotate(fidle_right, -45)
        fwalk1_1 = pygame.transform.rotate(fwalk1_right, -45)
        fwalk2_1 = pygame.transform.rotate(fwalk2_right, -45)
        fwalk3_1 = pygame.transform.rotate(fwalk3_right, -45)

        fwalkRight = [fwalk1_right, fwalk2_right, fwalk3_right, fwalk1_right, fwalk2_right, fwalk3_right]
        fwalkLeft = [fwalk1_left, fwalk2_left, fwalk3_left, fwalk1_left, fwalk2_left, fwalk3_left]
        fwalkUp = [fwalk1_up, fwalk2_up, fwalk3_up, fwalk1_up, fwalk2_up, fwalk3_up]
        fwalkDown = [fwalk1_down, fwalk2_down, fwalk3_down, fwalk1_down, fwalk2_down, fwalk3_down]
        fwalkI = [fwalk1_1, fwalk2_1, fwalk3_1, fwalk1_1, fwalk2_1, fwalk3_1]



        if self.fcount + 1 >= 30:
            self.fcount = 0
        elif fup == True:
            win.blit(fwalkUp[self.fcount // 5], (self.x, self.y))
            self.fcount += 1
            flastMove = "fup"

        elif fdown == True:
            win.blit(fwalkDown[self.fcount // 5], (self.x, self.y))
            self.fcount += 1
            flastMove = "fdown"

        elif fleft == True:
            win.blit(fwalkLeft[self.fcount // 5], (self.x, self.y))
            self.fcount += 1
            flastMove = "fleft"

        elif fright == True:
            win.blit(fwalkRight[self.fcount // 5], (self.x, self.y))
            self.fcount += 1
            flastMove = "fright"
        elif f_I == True:
            win.blit(fwalkI[self.fcount // 5], (self.x, self.y))
            self.fcount += 1
            flastMove = "fdown"

        else:
            if flastMove == "fright":
                win.blit(fidle_right, (self.x, self.y))
            elif flastMove == "fup":
                win.blit(fidle_up, (self.x, self.y))
            elif flastMove == "fleft":
                win.blit(fidle_left, (self.x, self.y))
            else:
                win.blit(fidle, (self.x, self.y))

####################################################################################################
##########################################################################################




npc1 = npc(640, 360, 0, 0, 0, False, False, False, False, 10)
npc2 = npc(750, 450,  0, 110, 90, False, False, False, False, 10)
def fnpc():
    if npc1.x == npc2.x:
        npc2.x = npc2.x - 10
    elif npc1.y == npc2.y:
        npc2.y = npc2.y - 10
def drawWindow():
    global plHP
    #Borders()
    sc1.draw(win)
    sc1.Movement(win)
    sc1.poscount()
    PlAnim.anim(win)
    #npc1.foe(win)
    #npc2.foe(win)


    #########################
    #house1.draw(win)
    #house1.Movement(win)


    #obj_npc1.draw(win)
    #obj_npc1.Movement(win)

    #npc1.draw(win)


    win.blit(hp_bar, (5, 5))
    pygame.draw.rect(win, (255, 0, 0), (8, 8, plHP, 30))
    ####################
    RED = (255, 0, 0)
    YELLOW =(239, 228, 176)
    f_sys = pygame.font.SysFont('calibri', 20)
    params = [posx, posy,'|',sc1.x, sc1.y ,speed]
    win_text = f_sys.render(str(params), 1, RED, YELLOW)
    pos = win_text.get_rect(center=(W - 120, H - 15))
    win.blit(win_text, pos)
    pygame.display.flip()
    ######################

    #pygame.display.update()
    #pygame.draw.rect(win, (255, 0, 0), (W//2, H//2, 20, 20))


#



flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #flRunning - False
    clock.tick(FPS)
    #Borders()
    drawWindow()
    fnpc()
    Borders()

    #print('up',rlBorder_u,'down', rlBorder_d,'left', rlBorder_l,'right', rlBorder_r)
    print(npc1.fposx, npc1.fposy)




pygame.quit()
