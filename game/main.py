import pygame
from game import constants as con


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    con.WINDOW.blit(con.SPACE, (0,0))
    pygame.draw.rect(con.WINDOW, con.BLACK, con.BORDER)

    red_health_text = con.HEALTH_FONT.render("HEALTH: " + str(red_health), 1, con.WHITE)
    yellow_health_text = con.HEALTH_FONT.render("HEALTH: " + str(yellow_health), 1, con.WHITE)
    con.WINDOW.blit(red_health_text, (con.WIDTH - red_health_text.get_width() - 10, 10))
    con.WINDOW.blit(yellow_health_text, (10, 10))

    con.WINDOW.blit(con.YELLOW_SPACESHIP, (yellow.x, yellow.y))
    con.WINDOW.blit(con.RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(con.WINDOW, con.RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(con.WINDOW, con.YELLOW, bullet)

    pygame.display.update()


def winner(text):
    draw_text = con.WINNER_FONT.render(text, 1, con.WHITE)
    con.WINDOW.blit(draw_text, (con.WIDTH/2 - draw_text.get_width() / 2, con.HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - con.VEL > 0:  # LEFT
        yellow.x -= con.VEL
    if keys_pressed[pygame.K_d] and yellow.x + con.VEL + yellow.width < con.BORDER.x:  # RIGHT
        yellow.x += con.VEL
    if keys_pressed[pygame.K_w] and yellow.y - con.VEL > 0:  # UP
        yellow.y -= con.VEL
    if keys_pressed[pygame.K_s] and yellow.y + con.VEL + yellow.height < con.HEIGHT - 15:  # DOWN
        yellow.y += con.VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - con.VEL > con.BORDER.x + con.BORDER.width:  # LEFT
        red.x -= con.VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + con.VEL + red.width < con.WIDTH:  # RIGHT
        red.x += con.VEL
    if keys_pressed[pygame.K_UP] and red.y - con.VEL > 0:  # UP
        red.y -= con.VEL
    if keys_pressed[pygame.K_DOWN] and red.y + con.VEL + red.height < con.HEIGHT - 15:  # DOWN
        red.y += con.VEL

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += con.BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(con.RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > con.WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= con.BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(con.YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def main():
    red = pygame.Rect(700, 300, con.SPACESHIP_WIDTH, con.SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, con.SPACESHIP_WIDTH, con.SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    run = True
    while run:
        clock.tick(con.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # Fire bullets of yellow spaceship
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and len(yellow_bullets) < con.MAX_BULLETS: #YELLOW BULLET
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    con.BULLET_FIRE_SOUND.play()
                #Fire bullets of red spaceship
                if event.key == pygame.K_RSHIFT and len(red_bullets) < con.MAX_BULLETS: #RED BULLET
                    bullet = pygame.Rect(red.x , red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    con.BULLET_FIRE_SOUND.play()
            #Health of users
            if event.type == con.RED_HIT:
                red_health -= 1
                con.BULLET_HIT_SOUND.play()
            if event.type == con.YELLOW_HIT:
                yellow_health -= 1
                con.BULLET_HIT_SOUND.play()
        #Winning title
        winner_text = ""
        if red_health == 0:
            winner_text = "yellow Wins !"

        if yellow_health == 0:
            winner_text = "Red Wins !"

        if winner_text != "":
            con.WINNING_SOUND.play()
            winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
    #TODO: ask the user if he want to restart the game
    main() #Restarting the game after someone win


if __name__ == "__main__":
    main()