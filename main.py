import pygame
import random
import pygame as pg
from os import path
pygame.init()

yellow = (255, 255, 50)
black = (50, 60, 50)
red = (255, 0, 10)
green = (5, 255, 65)
green1 = (0, 95, 30)

snd_dir = path.join(path.dirname(__file__), 'snd')

display_width = 700
display_height = 400

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_body = 10
snake_speed = 10

font_style = pygame.font.SysFont("arial", 25)
score_font = pygame.font.SysFont("arial", 36)
settings_font = pygame.font.SysFont("arial", 36)


def score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    display.blit(value, [5, 360])


def snake(snake_body, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_body, snake_body])


def message(msg, color):
    messg = font_style.render(msg, True, color)
    display.blit(messg, [display_width / 6, display_height / 3])


def gameloop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    length_snake = 1

    food_x = round(random.randrange(0, display_width - snake_body) / 10.0) * 10.0
    food_y = round(random.randrange(0, display_height - snake_body) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            display.fill(red)
            message("Defeat! Press E-continue play again or Q-quit", yellow)
            score(length_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_e:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_body
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_body
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_body
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_body
                    x1_change = 0

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(green1)
        pygame.draw.rect(display, red, [food_x, food_y, snake_body, snake_body])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > length_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_body, snake_List)
        score(length_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, display_width - snake_body) / 10.0) * 10.0
            food_y = round(random.randrange(0, display_height - snake_body) / 10.0) * 10.0
            length_snake += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()


menu = pygame.display.set_mode((800, 600))
menu.fill((0, 180, 210))


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, menu, outline=None):
        if outline:
            pygame.draw.rect(menu, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(menu, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('arial', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            menu.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


def Menu():
    menu = pygame.display.set_mode((display_width, display_height))
    snake_screen = pg.image.load('screensnake2.png')
    snake_rect = snake_screen.get_rect(bottomright=(700, 400))
    menu.blit(snake_screen, snake_rect)
    greenButton.draw(menu, (0, 0, 0))
    redButton.draw(menu, (0, 0, 0))
    donateButton.draw(menu, (0, 0, 0))
    settingButton.draw(menu, (0, 0, 0))
    pg.display.update()


def Game():
    menu.fill((0, 0, 0))


greenButton = button((0, 255, 85), 230, 150, 250, 50, "Start")
redButton = button((255, 45, 0), 230, 210, 250, 50, "Quit")
donateButton = button((255, 255, 85), 230, 270, 250, 50, "Donate")
returnButton = button((255, 0, 10), 230, 310, 250, 50, "Return")
settingButton = button((80, 0, 50), 230, 330, 250, 50, "Settings")
Buttonfive = button((255, 245, 95), 230, 130, 250, 50, "5")
Buttonten = button((255, 245, 95), 230, 220, 250, 50, "10")
Buttontwenty = button((255, 245, 95), 230, 310, 250, 50, "20")
escButton = button((255, 245, 95), 0, 15, 200, 43, "Escape")
game_state = "menu"
run = True


def donate():
    don = pygame.display.set_mode((display_width, display_height))
    don.fill((0, 0, 0))
    returnButton.draw(don, (100, 100, 10))
    card = pg.image.load('card2.png')
    card_rect = card.get_rect(bottomright=(560, 300))
    don.blit(card, card_rect)
    pg.display.update()
    pg.time.delay(20)


def setting():
    settings = pygame.display.set_mode((display_width, display_height))
    settings.fill((70, 30, 210))
    Buttonfive.draw(settings, (200, 100, 10))
    Buttonten.draw(settings, (200, 150, 10))
    Buttontwenty.draw(settings, (200, 200, 10))
    escButton.draw(settings, (200, 150, 10))

    f1 = pygame.font.SysFont("arial", 36)
    text1 = f1.render('Choose snake speed:', True,
                      (255, 245, 50))
    settings.blit(text1, (210, 55))

while run:
    if game_state == "menu":
        Menu()
    elif game_state == "game":
        Game()
    elif game_state == "donate":
        donate()
    elif game_state == "setting":
        setting()
    pygame.display.update()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if game_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if greenButton.isOver(pos):
                    pg.mixer.music.load('Sound_07133.mp3')
                    pg.mixer.music.play()
                    gameloop()
                    game_state = "game"
                if redButton.isOver(pos):
                    print("Sorry, you left the game:(")
                    run = False
                    pygame.quit()
                    quit()
                if donateButton.isOver(pos):
                    donate()
                    game_state = "donate"
                if settingButton.isOver(pos):
                    setting()
                    game_state = "setting"

            if event.type == pygame.MOUSEMOTION:
                if greenButton.isOver(pos):
                    greenButton.color = (105, 105, 105)
                else:
                    greenButton.color = (0, 255, 0)
                if redButton.isOver(pos):
                    redButton.color = (105, 105, 105)
                else:
                    redButton.color = (255, 0, 0)
                if donateButton.isOver(pos):
                    donateButton.color = (105, 105, 105)
                else:
                    donateButton.color = (255, 255, 85)
                if settingButton.isOver(pos):
                   settingButton.color = (105, 105, 105)
                else:
                   settingButton.color = (80, 0, 50)

        if game_state == "donate":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if returnButton.isOver(pos):
                    Menu()
                    game_state = "menu"
            if event.type == pygame.MOUSEMOTION:
                if returnButton.isOver(pos):
                    returnButton.color = (105, 105, 105)
                else:
                    returnButton.color = (255, 255, 85)
        if game_state == "setting":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Buttonfive.isOver(pos):
                    snake_speed = 5
                if Buttonten.isOver(pos):
                    snake_speed = 10
                if Buttontwenty.isOver(pos):
                    snake_speed = 20
                if escButton.isOver(pos):
                    Menu()
                    game_state = "menu"
            if event.type == pygame.MOUSEMOTION:
                if Buttonfive.isOver(pos):
                    Buttonfive.color = (105, 105, 105)
                else:
                    Buttonfive.color = (255, 245, 95)
                if Buttonten.isOver(pos):
                    Buttonten.color = (105, 105, 105)
                else:
                    Buttonten.color = (255, 245, 95)
                if Buttontwenty.isOver(pos):
                    Buttontwenty.color = (105, 105, 105)
                else:
                    Buttontwenty.color = (255, 245, 95)
                if escButton.isOver(pos):
                    escButton.color = (105, 105, 105)
                else:
                    escButton.color = (255, 245, 95)
