import pygame,time,random,sys

pygame.init()
#Game Variable
column=row = 25
size = 10
x,y=(column*size)/2,(row*size)/2
snake_length = 1
head_pos=[]
body_pos=[]
direction = 'RIGHT'
change = direction
food =[random.randint(0,column*size),random.randint(0,row*size)]
screen = pygame.display.set_mode([column*size,row*size])
clock =pygame.time.Clock()
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == ord('w'):
                change = 'UP'
            if event.key == ord('s'):
                change = 'DOWN'
            if event.key == ord('a'):
                change = 'LEFT'
            if event.key == ord('d'):
                change = 'RIGHT'

    if change == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        y -= 10
    if direction == 'DOWN':
        y += 10
    if direction == 'LEFT':
        x -= 10
    if direction == 'RIGHT':
        x += 10

    if x > (column*size)-1:
        x = 0
    if y > (row*size)-1:
        y=0
    if x < 0:
        x = column*size-1
    if y < 0:
        y = column*size-1

    screen.fill([0,0,0])
    food_collider = pygame.draw.rect(screen,[200,200,200],[food[0],food[1],size,size])
    snake_index = 0
    body_pos.clear()
    for _ in range(1,snake_length):
        snake_index -= 1
        temp = head_pos[snake_index]
        body_collider = pygame.draw.rect(screen,[100,100,100],[temp[0],temp[1],size,size])
        body_pos.append(body_collider)
    head_collider = pygame.draw.rect(screen,[100,100,100],[x,y,size,size])
    head_pos.append([int(x),int(y)])
    temp_food = food
    for collide in body_pos:
        if head_collider.colliderect(collide):
            snake_length = 1
    if head_collider.colliderect(food_collider):
        food = [random.randint(0,column*size),random.randint(0,row*size)]
        pygame.draw.rect(screen,[100,100,100],[temp_food[0],temp_food[1],size,size])
        snake_length += 1

    pygame.display.flip()
    clock.tick(30)
