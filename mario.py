import os
import sys
import pygame


pygame.init()
size = width, height = 500, 300
screen = pygame.display.set_mode(size)

FPS = 50
clock = pygame.time.Clock()


lvl_1 = [
    '---------------------------------------------------',
    '---------------------------------------------------',
    '---------------------------------------------------',
    '---------------------------------------------------',
    '---------------------------------------------------',
    '--------0000000000000-x0000000000000000000---------',
    '--------k000000000000--000000000000000000k---------',
    '-----------00000000000000----000000000000----------',
    '--------00000---000--000000000000000000-00---------',
    '--------00000000-0000000-00000--0--00-0000---------',
    '--------00000000000000---00000000000000000---------',
    '--------0000000000000000000000000000000000---------',
    '--------000000000----000000000000000000000---------',
    '--------00000--0000000000000000000000000000--------',
    '--------000000000000000000000k0000000000000--------',
    '--------00-00000000000000000--0000000000000--------',
    '--------00000000000000000000000000000000007--------',
    '----------*-------*-------*****-----****-----------',
    '----------*-------*-------*****-----****-----------',
    '---------------------------------------------------',
    '---------------------------------------------------',
    '---------------------------------------------------'
]


def game_over():
    pygame.init()
    size = width, height = 600, 300
    screen = pygame.display.set_mode(size)


    class Game_over(pygame.sprite.Sprite):
        image = load_image("game_over.jpg")
        image = pygame.transform.scale(image, (600, 300))

        def __init__(self, *group):
            super().__init__(*group)
            self.image = Game_over.image
            self.rect = self.image.get_rect()
            self.rect.x = -600
            self.rect.y = 0

        def update(self, speed):
            if self.rect.x < 0:
                self.rect.x += speed
            if self.rect.x >= 0:
                self.rect.x = 0

    screen.fill('blue')
    all_sprites = pygame.sprite.Group()
    Game_over(all_sprites)
    running = True
    x_pos = 0
    fps = 60
    v = 200
    clock = pygame.time.Clock()
    while running:
        screen.fill('blue')
        all_sprites.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        x_pos = v / fps
        clock.tick(fps)
        all_sprites.update(x_pos)
        pygame.display.flip()
    pygame.quit()


def game_win():
    pygame.init()
    size = width, height = 600, 300
    screen = pygame.display.set_mode(size)


    class Game_over(pygame.sprite.Sprite):
        image = load_image("game_win.jpg")
        image = pygame.transform.scale(image, (600, 300))

        def __init__(self, *group):
            super().__init__(*group)
            self.image = Game_over.image
            self.rect = self.image.get_rect()
            self.rect.x = -600
            self.rect.y = 0

        def update(self, speed):
            if self.rect.x < 0:
                self.rect.x += speed
            if self.rect.x >= 0:
                self.rect.x = 0

    screen.fill('blue')
    all_sprites = pygame.sprite.Group()
    Game_over(all_sprites)
    running = True
    x_pos = 0
    fps = 60
    v = 200
    clock = pygame.time.Clock()
    while running:
        screen.fill('blue')
        all_sprites.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        x_pos = v / fps
        clock.tick(fps)
        all_sprites.update(x_pos)
        pygame.display.flip()
    pygame.quit()


def terminate():
    pygame.quit()
    sys.exit()

def start_screen():
    intro_text = ['LVL 1']

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    alpha_surface = pygame.Surface(fon.get_size(), pygame.SRCALPHA)
    alpha_surface.fill((255, 255, 255, 120))
    fon.blit(alpha_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 70)
    text_coord = 250
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 210
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


start_screen()


class Lava(pygame.sprite.Sprite):
    image_lava = load_image('lava.jpg')
    image_lava = pygame.transform.scale(image_lava, (30, 31))
    image_lava_2 = pygame.transform.flip(image_lava, 0, 1)
    sp_image_lava = [image_lava, image_lava_2]

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Lava.image_lava
        self.rect = self.image_lava.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask_lava = pygame.mask.from_surface(self.image)

    def update(self):
        if int(change_of_personnel) == float(change_of_personnel) and change_of_personnel % 5 == 0:
            self.image = Lava.sp_image_lava[int(change_of_personnel) % 2]


class Platform(pygame.sprite.Sprite):
    image_pl = load_image('kir.png')
    image_pl = pygame.transform.scale(image_pl, (30, 30))

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Platform.image_pl
        self.rect = self.image_pl.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask_platform = pygame.mask.from_surface(self.image)


class Enter(pygame.sprite.Sprite):
    image_enter = load_image('труба.png', -1)
    image_enter = pygame.transform.scale(image_enter, (30, 30))

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Enter.image_enter
        self.rect = self.image_enter.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask_enter = pygame.mask.from_surface(self.image)


class Key(pygame.sprite.Sprite):
    image_key = load_image('k.jpg', -1)
    image_key = pygame.transform.scale(image_key, (34, 34))
    image_key_for_count = pygame.transform.scale(image_key, (40, 40))

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Key.image_key
        self.rect = self.image_key.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask_platform = pygame.mask.from_surface(self.image)
        self.count_key = 0

    def update(self):
        screen.blit(Key.image_key_for_count, (10, 10))
        my_font = pygame.font.SysFont('Comic Sans MS', 25)
        text_surface = my_font.render(str(str(3 - len(key_sprites)) + ' / 3'), False, (0, 0, 0))
        screen.blit(text_surface, (52, 12))
        for k in key_sprites:
            if pygame.sprite.collide_mask(mario, k):
                self.count_key += 1
                k.kill()


class Mario(pygame.sprite.Sprite):
    image_mario_place = load_image('mario_place.jpg', -1)
    image_mario_place = pygame.transform.scale(image_mario_place, (20, 30))
    image_mario_run_1_left = load_image('mario_run_1.jpg', -1)
    image_mario_run_1_left = pygame.transform.scale(image_mario_run_1_left, (20, 30))

    image_mario_run_2_left = load_image('mario_run_2.jpg', -1)
    image_mario_run_2_left = pygame.transform.scale(image_mario_run_2_left, (20, 30))

    image_mario_run_3_left = load_image('mario_run_3.jpg', -1)
    image_mario_run_3_left = pygame.transform.scale(image_mario_run_3_left, (20, 30))

    image_mario_jump_right = load_image('mario_jump.jpg', -1)
    image_mario_jump_right = pygame.transform.scale(image_mario_jump_right, (20, 30))

    image_mario_run_1_right = pygame.transform.flip(image_mario_run_1_left, 1, 0)

    image_mario_run_2_right = pygame.transform.flip(image_mario_run_2_left, 1, 0)

    image_mario_run_3_right = pygame.transform.flip(image_mario_run_3_left, 1, 0)

    image_mario_jump_left = pygame.transform.flip(image_mario_jump_right, 1, 0)

    image_mario_place_left = pygame.transform.flip(image_mario_place, 1, 0)

    an_charge = 0.1
    an_run_left = [image_mario_run_1_left,
                   image_mario_run_2_left,
                   image_mario_run_3_left]
    an_run_right = [image_mario_run_1_right,
                    image_mario_run_2_right,
                    image_mario_run_3_right]

    def __init__(self):
        super().__init__(mario_sprite, f_sprite)
        self.image = Mario.image_mario_place
        self.rect = self.image.get_rect()
        self.rect.x = 260
        self.rect.y = 550
        self.mask_mario = pygame.mask.from_surface(self.image)
        self.xmoving = 0
        self.ymoving = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли Mario
        self.direct_moving = 1

    def update(self, left, right, up, all_sprites):
        if up:
            if self.onGround:
                self.ymoving = -mario_jump
        if left:
            self.xmoving = -mario_speed  # Лево = x- n
            if left and up:
                self.image = Mario.image_mario_jump_left
            else:
                if int(change_of_personnel) == float(change_of_personnel):
                    self.image = Mario.an_run_right[int(change_of_personnel) % 3]
            self.direct_moving = 1
        if right:
            self.xmoving = mario_speed  # Право = x + n
            if right and up:
                self.image = Mario.image_mario_jump_right
            else:
                if int(change_of_personnel) == float(change_of_personnel):
                    self.image = Mario.an_run_left[int(change_of_personnel) % 3]
            self.direct_moving = -1
        if not (left or right):  # стоим, когда нет указаний идти
            self.xmoving = 0
            if self.direct_moving == -1:
                self.image = Mario.image_mario_place
            elif self.direct_moving == 1:
                self.image = Mario.image_mario_place_left
        if not self.onGround:
            self.ymoving += mario_attraction
        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.ymoving
        self.collide(0, self.ymoving, all_sprites)
        self.rect.x += self.xmoving  # переносим свои положение на xvel
        self.collide(self.xmoving, 0, all_sprites)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.ymoving = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.ymoving = 0  # и энергия прыжка пропадает


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


def im_load_lvl():
    for i in range(level_width):
        for j in range(level_height):
            if lvl_1[j][i] == '-':
                Platform(i * 30, j * 30, all_sprites, f_sprite)
            elif lvl_1[j][i] == '*':
                Lava(i * 30, j * 30 - 1, lava_sprites, f_sprite)
            elif lvl_1[j][i] == 'k':
                Key(i * 30, j * 30 - 4, key_sprites, f_sprite)
            elif lvl_1[j][i] == '7':
                Enter(i * 30, j * 30, enter_sprite, f_sprite)



width, height = 500, 300
size = width, height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mario")
screen.fill(pygame.Color('lightblue'))
running = True
f_sprite = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
lava_sprites = pygame.sprite.Group()
key_sprites = pygame.sprite.Group()
enter_sprite = pygame.sprite.Group()
level_width = len(lvl_1[0])
level_height = len(lvl_1)
im_load_lvl()
mario_speed = 5
mario_jump = 7
mario_attraction = 0.3
mario_sprite = pygame.sprite.Group()
mario = Mario()
left, right = False, False
up = False
change_of_personnel = 0.5
camera = Camera()
while running:
    screen.fill(pygame.Color('lightblue'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            left = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            right = True
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            right = False
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            left = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            up = True
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            up = False
    # изменяем ракурс камеры
    camera.update(mario)
    # обновляем положение всех спрайтов
    for sprite in f_sprite:
        camera.apply(sprite)
    all_sprites.draw(screen)
    mario_sprite.draw(screen)
    lava_sprites.draw(screen)
    key_sprites.draw(screen)
    enter_sprite.draw(screen)
    key_sprites.update()
    mario_sprite.update(left, right, up, all_sprites)
    lava_sprites.update()
    change_of_personnel += 0.5
    pygame.display.flip()
    clock.tick(FPS)
    if pygame.sprite.spritecollideany(mario, lava_sprites, collided=None):
        running = False
        game_over()
    if pygame.sprite.spritecollideany(mario, enter_sprite, collided=None) and len(key_sprites) == 0:
        game_win()


pygame.quit()