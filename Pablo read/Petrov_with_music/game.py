
from pygame import mixer
import pygame, sys, random
from pygame.locals import*

pygame.init()
mixer.init()
mixer.music.set_volume(0.3)
mixer.music.load("data/bksong.mp3")

# Start playing the song
mixer.music.play()

#------------------ CREATES THE WINDOW FOR THE ENTIRE GAME ---------------------
pygame.display.set_caption('PetroV') #setting Menu's name
screen = pygame.display.set_mode((750, 750)) #creates the window with input sizes
#--------------------------------------------------------------------------------


def main(): #Title screen window is called with main() is called

    background = pygame.image.load('data/menu.png') #background when called == image imported
    
    while True:

        click = False
        
        for event in pygame.event.get(): #When the X button is pressed the window quits
            if event.type == QUIT:
                pygame.mixer.Sound.play(mixer.Sound("data/click.mp3")) #plays given sound
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN: #When the escape key is pressed the window quits
                if event.key == K_ESCAPE:
                    pygame.mixer.Sound.play(mixer.Sound("data/click.mp3")) #plays given sound
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN: #When mousebutton is detected to be down user can click on the screen 
                if event.button == 1:
                    click = True
        
        #Allows the background to stay static on the screen 
        screen.blit(background,(0,0))

        #mx and my are the x and y of where the mouse is at
        mx, my = pygame.mouse.get_pos()
        
        #Creates the boundries of the buttons
        button_1 = pygame.Rect(175, 440, 400, 93)
        button_2 = pygame.Rect(175, 563, 400, 93)

        #If the button and the mouse mx and my collide either the game or control function runs 
        if button_1.collidepoint((mx, my)):
            if click:
                pygame.mixer.Sound.play(mixer.Sound("data/click.mp3")) #plays given sound
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.mixer.Sound.play(mixer.Sound("data/click.mp3")) #plays given sound
                controls()
                
                
        pygame.display.update() #Updates the screen 
 
#........................................................................................................

def game(): #Game window that pops up when the start butn is pressed
  #------------------ CREATES THE WINDOW ---------------------

  ### Sets the width and height ###
  width = 750
  height = 750
  bbounce = mixer.Sound("data/brickbounce.mp3")
  pbounce = mixer.Sound("data/bounce.mp3")
  #initialize tallies for the number of lives and the score
  score = 0
  lives = 5

  #background when called == image imported
  background = pygame.image.load('data/bg.png') 

  ### Runs the window given the height and adds title ###
  screen = pygame.display.set_mode((width,height))
  #pygame.display.set_caption('Breakout')
  

  #------------------ DEFINE COLORS --------------------------

  ### Background color ###
  bg = (48, 58, 74)

  ### Ball color ###
  red =random.randint(50,255)
  green =random.randint(50,255)
  blue =random.randint(50,255)

  ## Brick Color ##
  bred =random.randint(75,255)
  bgreen =random.randint(75,255)
  bblue =random.randint(75,255)

  ### Platform color ###
  white = (215, 218, 223)

  #------------------ OBJECTS -------------------------------

  # randomly assigns a place for the ball to spawn given a certain space
  x= random.randint(width-width+10,width-20) 
  y= random.randint(height//2,height//3+height//3)


  mylist = [-5,5] #A list of which x direction the ball can go at a speed of 3
  ball = Rect(x,y,20,20)
  dx = random.choice((mylist)) #sets the x "speed" of the ball
  dy = -5 #sets the y "speed" of the ball 


  #makes block list
  block_list = [pygame.Rect(25 + 120 * i, 80 + 70 * j, 100, 50) for i in range(6) for j in range(4)]

  #makes color list for bricks
  color_list = [(bred, bgreen, bblue) for i in range(6) for j in range(4)]


  #Platform attributes
  platform_len = 100 #Entire length of the plat
  plat_width = 15 #width of the plat 
  plat = Rect(width//2 - platform_len//2,height//5*4, platform_len, plat_width) # X, Y, length and width
  platDX = 0 # Speed of the platform (Amount of pixels that get added making it look like it is moving)

  #Ball's attributes
  radi = 15

  
  clock = pygame.time.Clock() #Pygame function allowing for the refresh of the frame per second
  fps = 60 #Rate at which the screen refreshes
  run = True

  #COMMENT 
  def block_collision(dx, dy, ball, rect):
      if dx > 0:
          delta_x = ball.right - rect.left
      else:
          delta_x = rect.right - ball.left
      if dy > 0:
          delta_y = ball.bottom - rect.top
      else:
          delta_y = rect.bottom - ball.top

      if abs(delta_x - delta_y) < 10:
          dx, dy = -dx, -dy
      elif delta_x > delta_y:
          dy = -dy
      elif delta_y > delta_x:
          dx = -dx
      return dx, dy
    
  #------------------ Main Program Loop for GAME ---------------------
  
  while run:
    #controls the time the screen refreshes per second
    clock.tick(fps)
    
    for event in pygame.event.get():# When the user clicks the X button the game will stop running
      if event.type == pygame.QUIT:
          pygame.mixer.Sound.play(mixer.Sound("data/click.mp3")) #plays given sound
          pygame.quit()
          sys.exit()
      if event.type == pygame.KEYDOWN: #When the user clicks the esc button the game will stop running
          if event.key == pygame.K_ESCAPE:
              pygame.mixer.Sound.play(mixer.Sound("data/click.mp3")) #plays given sound
              run = False

    #..................... Draws Objects ....................
    #Draws background
    screen.fill(bg) #(colored background)
    screen.blit(background,(0,0)) #Allows the bg to stay there constantly
    
    #draws the score and lives tally on the top of the screen
    pygame.draw.line(screen, "white", [0, 38], [800, 38], 2)
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, 'white')
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(lives), 1, "white")
    screen.blit(text, (625, 10))
  
    #draws bricks
    [pygame.draw.rect(screen,color_list[color], block) for color, block in enumerate(block_list)]

    #Draws the platform on screen
    pygame.draw.rect(screen,white,plat)
  
    #Draws the Ball on screen
    pygame.draw.ellipse(screen,(red,green,blue),ball)
    #................................................................


    #------------------- Working Mechanics of how the game works -------------------

    # When a key is pressed the Dx value is added making it "move"
    if event.type == KEYDOWN:
      if event.key == K_RIGHT:
        platDX = 7

      if event.key == K_LEFT:
        platDX = -7

    if event.type == KEYUP: #When no key is pressed the Dx is set back to 0
      if event.key == K_RIGHT or event.key == K_LEFT:
        platDX = 0

    #Controls the speed of the ball and platform by adding values of dx, dy, and Dx
    plat.x += platDX
    ball.x += dx 
    ball.y += dy

    # Covers the collision with the wall
    if ball.y<38:
        dy *= -1
    elif ball.y> height-25:
      dy *= -1
      lives = lives - 1
      if lives == 0:
        lives = lives - 1
        pygame.time.wait(500)
        #Stops the Game when Lives is 0 
        run=False
        replay(score,lives)
    
    #If the ball goes beyond the given limts the direction of the mall changes 
    if ball.x<0 or ball.x>width-20:
        dx *= -1
              

    #Controls the limits of how far the platform can go
    if plat.x<0:
      plat.x *= 0
    elif plat.x>width-platform_len:
      plat.x=width-platform_len

    # Covers the collision with the ball and the platform 
    if ball.colliderect(plat):
      if ball.centerx <= plat.x or ball.centerx>= plat.x +10:
        if ball.centery <= plat.y or ball.centery>= plat.y +10:
          dy = dy * -1
          pygame.mixer.Sound.play(bbounce) #plays given sound
          

    #makes index
    hit_index = ball.collidelist(block_list)
    #checks index 
    # checks index of bricks, to see if hit by ball and is then erased if hit
    if hit_index != -1:
        hit_rect = block_list.pop(hit_index)
        hit_color = color_list.pop(hit_index)
        dx, dy = block_collision(dx, dy, ball, hit_rect)
        score = score + 1
        pygame.mixer.Sound.play(pbounce) #plays given sound
        
        
    if score == 24:
        pygame.time.wait(500)
        run=False
        wreplay(score,lives)    

  #updates the screen 
    pygame.display.flip()
  

#........................................................................................................

def controls(): #Control window that pops up when the ctrl butn is pressed
    running = True
    while running:
        #loads the ctrl.png 
        screen.blit(pygame.image.load('data/ctrl.png'),(0,0))

        for event in pygame.event.get(): #When the X button is pressed the window quits
            if event.type == QUIT:
                pygame.mixer.Sound.play(mixer.Sound("data/click.mp3")) #plays given sound
                running = False
            if event.type == KEYDOWN: #When the escape key is pressed the window quits
                if event.key == K_ESCAPE:
                    pygame.mixer.Sound.play(mixer.Sound("data/click.mp3")) #plays given sound
                    running = False
        #updates the screen 
        pygame.display.flip()

#........................................................................................................

def replay(x,y): #Replay and Quit window that pops up when the user loses
    running = True

    while running:
        #background when called == image imported
        screen.blit(pygame.image.load('data/gameover.png'),(0,0))
        
        white = (254,245,233)

        #---------- Text that prints the Score and lives -----------
        font = pygame.font.Font(None, 45)
        text = font.render("SCORE:", 5, white)
        screen.blit(text, (208,250))

        text = font.render("LIVES:", 5, white)
        screen.blit(text, (450,250))

        font = pygame.font.Font(None, 200)
        text = font.render(str(x), 5, white)
        screen.blit(text, (185,280))
        text = font.render("0", 5, white)
        screen.blit(text, (460,280))
        #------------------------------------------------------------------------

        click = False
        for event in pygame.event.get(): #When the X button is pressed the window quits
            if event.type == MOUSEBUTTONDOWN: #When mousebutton is detected to be down user can click on the screen 
                if event.button == 1:
                    click = True

        #mx and my are the x and y of where the mouse is at
        mx, my = pygame.mouse.get_pos()
        
        #Creates the boundries of the buttons
        button_1 = pygame.Rect(76, 462, 254, 147)
        button_2 = pygame.Rect(425, 462, 254, 147)


        #If the button and the mouse mx and my collide either the game or control function runs 
        if button_1.collidepoint((mx, my)):
            if click:
                pygame.mixer.Sound.play(mixer.Sound("data/click.mp3")) #plays given sound
                running = False
                main()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.mixer.Sound.play(mixer.Sound("data/click.mp3")) #plays given sound
                running = False
                game()
                
                
                
        pygame.display.update() #Updates the screen 
        #updates the screen 
        pygame.display.flip()
        208, 250
 
#........................................................................................................

def wreplay(x,y): #Replay and Quit window that pops up for when the game is won
    running = True

    while running:
        if y == 5:
            screen.blit(pygame.image.load('pics/spwinner.png'),(0,0))
        elif y != 5:
            screen.blit(pygame.image.load('pics/winner.png'),(0,0))
        white = (254,245,233)

        #---------- Text that prints the Score and lives -----------
        font = pygame.font.Font(None, 45)
        text = font.render("SCORE:", 5, white)
        screen.blit(text, (208,250))

        text = font.render("LIVES:", 5, white)
        screen.blit(text, (450,250))

        font = pygame.font.Font(None, 200)
        text = font.render("24", 5, white)
        screen.blit(text, (195,280))
        text = font.render(str(y), 5, white)
        screen.blit(text, (460,280))
        #-----------------------------------------------------------------

        click = False
        for event in pygame.event.get(): #When the X button is pressed the window quits
            if event.type == MOUSEBUTTONDOWN: #When mousebutton is detected to be down user can click on the screen 
                if event.button == 1:
                    click = True

        #mx and my are the x and y of where the mouse is at
        mx, my = pygame.mouse.get_pos()
        
        #Creates the boundries of the buttons
        button_1 = pygame.Rect(76, 462, 254, 147)
        button_2 = pygame.Rect(425, 462, 254, 147)

        #If the button and the mouse mx and my collide either the game or control function runs 
        if button_1.collidepoint((mx, my)):
            if click:
                pygame.mixer.Sound.play(mixer.Sound("data/click.mp3")) #plays given sound
                running = False
                main()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.mixer.Sound.play(mixer.Sound("data/click.mp3")) #plays given sound
                running = False
                game()
                
                
                
        pygame.display.update() #Updates the screen 
        #updates the screen 
        pygame.display.flip()
        208, 250

if __name__ == "__main__":
    main()