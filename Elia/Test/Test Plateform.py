import pygame
import PlayerMovement
import Plateform

pygame.init()





screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

running = True

player = PlayerMovement.Player(300,200,50,50)

ground  = pygame.Rect(0,400,500,100)


allPlateforms=[]



P1 = Plateform.Plateform(300, 475, 400, 20, "green",False)
P1.CreatePlateform(allPlateforms)

P2 = Plateform.Plateform(0, 305, 200, 20, "green",False)
P2.CreatePlateform(allPlateforms)

P3 = Plateform.Plateform(600, 400, 200, 20, "green",False)
P3.CreatePlateform(allPlateforms)

P4 = Plateform.Plateform(200, 330, 200, 20, "green",False)
P4.CreatePlateform(allPlateforms)

P5 = Plateform.Plateform(0,0,50,600,"red", True)
P5.CreatePlateform(allPlateforms)

P6 = Plateform.Plateform(450,350, 50,50, "red", True)
P6.CreatePlateform(allPlateforms)





while running: 

    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Autoriser le saut uniquement si le joueur n'est pas déjà en train de sauter
            if not player.isJumping:
                player.isJumping = True
                player.verticalVelocity = -player.jumpForce

    player.Movement()

     

    for i in allPlateforms: 
        if(i.CheckCollision(player.playerRect, player.maxValues)):
            player.PlayerOnGround(i.Rect.top) 



    player.CheckWalls()
    

    if player.posY + player.height >= screen_height :
        player.posX = 300
        player.posY = 200

    # Affichage
    screen.fill("black")

    for i in allPlateforms:
        i.Display(screen)

    player.UpdatePlayer(screen)
    
    pygame.display.update()

pygame.quit() 


