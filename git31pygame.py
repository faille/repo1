hero = Actor("hero")
box = Actor("box")
avatar = Actor("butterfly")
bg = Actor("bg")

HEIGHT = hero.height * 10
WIDTH = 1000

hero.bottom = HEIGHT
hero.left = 10

box.bottom = HEIGHT
box.left = WIDTH / 2

avatar.bottom = HEIGHT / 2
avatar.left = WIDTH / 2

speed_x = 0
speed_y = 0

def draw():
    #screen.clear()
    #screen.fill((0, 150, 255))
    screen.blit("bg",(0,HEIGHT - bg.height))
    screen.draw.text("Hello!", (avatar.right, avatar.top+100), fontsize=80)
    screen.draw.line((avatar.right, avatar.bottom), (avatar.right+50, avatar.bottom -50), color=(255,255,255))
    box.draw()
    hero.draw()
    avatar.draw()

def update():
    global speed_y

    hero.left += speed_x
    hero.top += speed_y

    if hero.right > WIDTH:
        hero.right = WIDTH
    elif hero.left < 10:
        hero.left = 10
    if hero.bottom > HEIGHT:
        speed_y = 0
        hero.bottom = HEIGHT
    if box.collidepoint(hero.pos):
        sounds.hit.play()

def on_key_down(key):
    global speed_x
    global speed_y

    if key == keys.RIGHT:
        speed_x = 4
        hero.image = "hero"
    elif key == keys.LEFT:
        speed_x = -4
        hero.image = "hero-flip"
    elif key == keys.UP:
        speed_y = -4
def on_key_up(key):
    global speed_x
    global speed_y

    if key == keys.RIGHT or key == keys.LEFT:
        speed_x = 0
    if key == keys.UP:
        speed_y = 3

def on_mouse_down(pos):
    if box.collidepoint(pos):
        box.image = "skeleton-fish"
#thomas@panopticgame.com et bastien@panopticgame.com