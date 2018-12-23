import pygame, sys

pygame.init()
size = width, height = 600, 400
speed = [1, 1]
Black = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("壁球game")
ball = pygame.image.load("1.gif")  # 导入图像
ballRect = ball.get_rect()  # 通过图像绘制矩形

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if ballRect.left < 0 or ballRect.right > width:
        ballRect = ballRect.move(speed[0], speed[1])
        speed[0] = -speed[0]
    if ballRect.top < 0 or ballRect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(Black)  # 为背景填充颜色
    screen.blit(ball, ballRect)  # 在矩形位置绘制图像
    pygame.display.update()