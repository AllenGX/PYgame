import pygame, sys

pygame.init()
size = width, height = 600, 400
speed = [1, 1]
Black = 0, 0, 0
fps = 300
fClock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("壁球game")
ball = pygame.image.load("1.gif")  # 导入图像
ballRect = ball.get_rect()  # 通过图像绘制矩形

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0] / abs(speed[0]))
            elif event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
    ballRect = ballRect.move(speed)
    if ballRect.left < 0 or ballRect.right > width:
        speed[0] = -speed[0]
    if ballRect.top < 0 or ballRect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(Black)  # 为背景填充颜色
    screen.blit(ball, ballRect)  # 在矩形位置绘制图像
    pygame.display.update()
    fClock.tick(fps)  # 设置刷新时间   每秒钟300次
