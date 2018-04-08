import pygame

pygame.init()
screen = pygame.display.set_mode((850, 850))
done = False
is_blue = True

color = (0, 128, 255)
garbageTruckX = 30
garbageTruckY = 30
grateX = 0
grateY = 0
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: garbageTruckY -= 3
    if pressed[pygame.K_DOWN]: garbageTruckY += 3
    if pressed[pygame.K_LEFT]: garbageTruckX -= 3
    if pressed[pygame.K_RIGHT]: garbageTruckX += 3
    if pressed[pygame.K_1]: color = (5, 1, 255)
    if pressed[pygame.K_2]: color = (5, 255, 1)
    if pressed[pygame.K_3]: color = (255, 255, 0)

    screen.fill((0, 0, 0))

    font = pygame.font.SysFont("comicsansms", 21)

    # for i in range(0,85):
    #     pygame.draw.line(screen,(0,0,0),(grateX+i*10,0),(grateX+i*10,850),1)
    #     pygame.draw.line(screen,(0,0,0), (0,grateY+i*10),(850, grateY+i*10), 1)

    pygame.draw.rect(screen, (5, 1, 255), pygame.Rect(50, 750, 100, 100))
    pygame.draw.rect(screen, (5, 255, 1), pygame.Rect(200, 750, 100, 100))
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(350, 750, 100, 100))

    pygame.draw.rect(screen, (139, 69, 19), pygame.Rect(150, 100, 200, 100))
    pygame.draw.rect(screen, (5, 1, 255), pygame.Rect(150, 100, 40, 40))
    pygame.draw.rect(screen, (5, 255, 1), pygame.Rect(230, 100, 40, 40))
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(310, 100, 40, 40))
    label = font.render("House 1", 1, (255, 255, 0))
    screen.blit(label, (220, 180))

    pygame.draw.rect(screen, (139, 69, 19), pygame.Rect(150, 370, 200, 100))
    pygame.draw.rect(screen, (5, 1, 255), pygame.Rect(150, 370, 40, 40))
    pygame.draw.rect(screen, (5, 255, 1), pygame.Rect(230, 370, 40, 40))
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(310, 370, 40, 40))
    label2 = font.render("House 2", 1, (255, 255, 0))
    screen.blit(label2, (220, 450))

    pygame.draw.rect(screen, (139, 69, 19), pygame.Rect(500, 100, 200, 100))
    pygame.draw.rect(screen, (5, 1, 255), pygame.Rect(500, 100, 40, 40))
    pygame.draw.rect(screen, (5, 255, 1), pygame.Rect(580, 100, 40, 40))
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(660, 100, 40, 40))
    label2 = font.render("House 3", 1, (255, 255, 0))
    screen.blit(label2, (570, 180))

    pygame.draw.rect(screen, (139, 69, 19), pygame.Rect(500, 370, 200, 100))
    pygame.draw.rect(screen, (5, 1, 255), pygame.Rect(500, 370, 40, 40))
    pygame.draw.rect(screen, (5, 255, 1), pygame.Rect(580, 370, 40, 40))
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(660, 370, 40, 40))
    label2 = font.render("House 4", 1, (255, 255, 0))
    screen.blit(label2, (570, 450))

    # Roads
    pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(600, 200, 40, 170))
    pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(250, 200, 40, 170))
    pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(250, 270, 350, 40))
    pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(400, 300, 40, 450))
    pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(50, 710, 400, 40))

    pygame.draw.circle(screen, color, (garbageTruckX, garbageTruckY), 25)

    pygame.display.flip()
    clock.tick(60)

    print(garbageTruckX, garbageTruckY)
