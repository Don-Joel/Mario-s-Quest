import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
lvl1_enemies = []


track_1 = gamebox.from_image(camera.x, camera.y, "https://www.mariowiki.com/images/6/60/ShyGuyBazaar.png")
track_1.scale_by(1.4)
track_2 = gamebox.from_image(camera.x, camera.y, "https://files.gamebanana.com/img/ss/maps/58a7634e23dc0.jpg")
track_3 = gamebox.from_image(camera.x, camera.y, """https://img00.deviantart.net/4d6c/i/2016/065/4/4/bowser_threat_trial__lava__by_slayton16-d9qh5on.png""")
track_3.scale_by(1.2)
winner_track = gamebox.from_image(camera.x, 500,
                                  """https://i.pinimg.com/originals/ab/06/96/ab0696490548d256860551ec49fa8ba1.jpg""")
winner_track.scale_by(1.35)
ticks = 0
score = 0
game_on = False
character = gamebox.from_image(camera.x, 500, "https://icons.iconarchive.com/icons/ph03nyx/super-mario/256/Retro-Mario-2-icon.png")
character.scale_by(0.2)
coins = []
background_number = 1
level = 1


def start_game(keys):
    """

    :param keys: keys used to start the game
    :return: the game begins
    """
    if background_number == 1:
        loading_screen(keys)
    elif background_number == 2:
        intro(keys)


def loading_screen(keys):
    """

    :param keys: keys used to start the game
    :return: once the keys are hit, the player gets transferred to the intro screen
    """
    global ticks
    global background_number
    ticks += 1
    camera.clear("Black")
    background_intro = gamebox.from_image(camera.x, camera.y, """https://cdn.donmai.us/sample/6c/b0/__princess_peach_mario_bowser_toad_goomba_and_12_more_mario_and_2_more_drawn_by_vinny_dingitydingus__sample-6cb0771328909a4f155403385c0ebee1.jpg""")
    background_intro.scale_by(1.2)
    text = "Press SPACE BAR to Begin"
    loading_screen_text = gamebox.from_text(400, 320, text, 60, "white", bold=False)
    game_name = "Mario's Quest"
    name_text = " Joel Tavarez"
    game_title = gamebox.from_text(400, 230, game_name, 85, "white", italic=True, bold=True)
    names = gamebox.from_text(400, 450, name_text, 45, "cyan", bold=False)
    camera.draw(background_intro)
    camera.draw(game_title)
    camera.draw(loading_screen_text)
    camera.draw(names)

    if pygame.K_SPACE in keys:
        background_number += 1


def intro(keys):
    """

    :param keys: the keys pressed to start playing the game
    :return: the game starts
    """
    global game_on
    global ticks
    global background_number
    ticks += 1
    if game_on is False:
        camera.clear("black")
        text_1 = '''BOOM! Bowser has just kidnapped Princess Peach and plans'''
        text_2 = '''to murder her! Bowser and Peach are in a kingdom far away'''
        text_3 = '''from Mario. If Mario doesn't arrive in time, Bowser murders'''
        text_4 = '''Peach. Knowing that Mario is on his way to the kingdom, Bowser has'''
        text_5 = '''set enemies to help prevent Mario from interfering with the murder.'''
        text_6 = '''The enemies will spawn in two of three lanes. Mario has to dodge the'''
        text_7 = '''enemies and stay in a safe lane where there are no enemies. If '''
        text_8 = '''Mario touches any of the enemies, the game ends. The last level will'''
        text_9 = '''consist of Bowser attempting to kill Mario. If Mario dies during'''
        text_10 = '''any of these levels, the game is over. Mario is operated with the right'''
        text_11 = '''and left keys. Lastly, Mario has 270 seconds to get through all levels, meaning'''
        text_12 = '''each level lasts 90s. For each coin Mario picks up, time goes faster. Good Luck!'''

        intro_text_1 = gamebox.from_text(400, 100, text_1, 30, "white", bold=False)
        intro_text_2 = gamebox.from_text(400, 130, text_2, 30, "white", bold=False)
        intro_text_3 = gamebox.from_text(400, 160, text_3, 30, "white", bold=False)
        intro_text_4 = gamebox.from_text(400, 190, text_4, 30, "white", bold=False)
        intro_text_5 = gamebox.from_text(400, 220, text_5, 30, "white", bold=False)
        intro_text_6 = gamebox.from_text(400, 250, text_6, 30, "white", bold=False)
        intro_text_7 = gamebox.from_text(400, 280, text_7, 30, "white", bold=False)
        intro_text_8 = gamebox.from_text(400, 310, text_8, 30, "white", bold=False)
        intro_text_9 = gamebox.from_text(400, 340, text_9, 30, "white", bold=False)
        intro_text_10 = gamebox.from_text(400, 370, text_10, 30, "white", bold=False)
        intro_text_11 = gamebox.from_text(400, 400, text_11, 30, "white", bold=False)
        intro_text_12 = gamebox.from_text(400, 430, text_12, 30, "white", bold=False)

        instructions = gamebox.from_text(400, 480, "Use the LEFT or RIGHT keys to Play", 40, "white", bold=True)

        camera.draw(instructions)
        camera.draw(intro_text_1)
        camera.draw(intro_text_2)
        camera.draw(intro_text_3)
        camera.draw(intro_text_4)
        camera.draw(intro_text_5)
        camera.draw(intro_text_6)
        camera.draw(intro_text_7)
        camera.draw(intro_text_8)
        camera.draw(intro_text_9)
        camera.draw(intro_text_10)
        camera.draw(intro_text_11)
        camera.draw(intro_text_12)

        if pygame.K_RIGHT in keys:
            game_on = True

        if pygame.K_LEFT in keys:
            game_on = True


def mario():
    """

    :return: mario as a sprite sheet/ animation
    """
    global ticks
    global character

    camera.draw(character)


def player_movement(keys):
    """

    :param keys: the keys used to manuvuer mario
    :return: mario moves left or right of the screen
    """
    global character
    global sheet
    if game_on:
        if pygame.K_RIGHT in keys:
            character.x += 250
            keys.remove(pygame.K_RIGHT)
        if pygame.K_LEFT in keys:
            character.x -= 250
            keys.remove(pygame.K_LEFT)
        if character.left < camera.left + 125:
            character.left = camera.left + 125
        if character.right > camera.right - 125:
            character.right = camera.right - 125
        mario()


def score_count():
    """

    :return: displays the time/score of the game. After the score/ time is 90, the level changes.
    """
    global score
    global game_on
    global level
    if game_on:
        score += 1
        fixed_score = str(int(score // 30))
        camera.draw(gamebox.from_text(400, 50, fixed_score, 40, "orange", bold=True))
        if (score // 30) >= 90:
            level += 1
            score = 0


def enemieslvl1():
    """

    :return: first level enemies are created, drop from the top of the screen, and then get removed once it passes
    mario's location
    """
    global lvl1_enemies
    global ticks
    ticks += 1
    rand_1 = random.randrange(60, 200)
    rand_2 = random.randrange(60, 200)
    rand_3 = random.randrange(60, 200)
    if game_on:
        if ticks % rand_1 == 0:
            enemy_1 = gamebox.from_image(camera.x, camera.top, """https://icons.iconarchive.com/icons/ph03nyx/super-mario/256/Goomba-icon.png""")
            enemy_1.scale_by(0.2)
            if rand_1 != rand_2:
                lvl1_enemies.append(enemy_1)
        if ticks % rand_2 == 0:
            enemy_2 = gamebox.from_image(150, camera.top, """https://icons.iconarchive.com/icons/ph03nyx/super-mario/256/Goomba-icon.png""")
            enemy_2.scale_by(0.2)
            lvl1_enemies.append(enemy_2)
        if ticks % rand_3 == 0:
            enemy_3 = gamebox.from_image(650, camera.top, """https://icons.iconarchive.com/icons/ph03nyx/super-mario/256/Goomba-icon.png""")
            enemy_3.scale_by(0.2)
            if rand_2 != rand_3 or rand_1 != rand_3:
                lvl1_enemies.append(enemy_3)

        for enemy in lvl1_enemies:
            camera.draw(enemy)
            enemy.y += 8
            if enemy.y > character.y:
                lvl1_enemies.remove(enemy)


def enemieslvl2():
    """

    :return: second level enemies are created, drop from the top of the screen, and then get removed once it passes
    mario's location
    """
    global lvl1_enemies
    global ticks
    ticks += 1
    rand_1 = random.randrange(60, 200)
    rand_2 = random.randrange(60, 200)
    rand_3 = random.randrange(60, 200)
    if game_on:
        if ticks % rand_1 == 0:
            enemy_1 = gamebox.from_image(camera.x, camera.top, """https://vignette.wikia.nocookie.net/mario/images/8/8a/Boo_Artwork_-_Mario_Party_7.png""")
            enemy_1.scale_by(0.15)
            if rand_1 != rand_2:
                lvl1_enemies.append(enemy_1)
        if ticks % rand_2 == 0:
            enemy_2 = gamebox.from_image(150, camera.top, """https://vignette.wikia.nocookie.net/mario/images/8/8a/Boo_Artwork_-_Mario_Party_7.png""")
            enemy_2.scale_by(0.15)
            lvl1_enemies.append(enemy_2)
        if ticks % rand_3 == 0:
            enemy_3 = gamebox.from_image(650, camera.top, """https://vignette.wikia.nocookie.net/mario/images/8/8a/Boo_Artwork_-_Mario_Party_7.png""")
            enemy_3.scale_by(0.15)
            if rand_2 != rand_3 or rand_1 != rand_3:
                lvl1_enemies.append(enemy_3)
        for enemy in lvl1_enemies:
            camera.draw(enemy)
            enemy.y += 12
            if enemy.y > character.y:
                lvl1_enemies.remove(enemy)


def enemieslvl3():
    """

    :return: third level enemies are created, drop from the top of the screen, and then get removed once it passes
    mario's location
    """
    global lvl1_enemies
    global ticks
    ticks += 1
    rand_1 = random.randrange(60, 200)
    rand_2 = random.randrange(60, 200)
    rand_3 = random.randrange(60, 200)
    if game_on:
        if ticks % rand_1 == 0:
            enemy_1 = gamebox.from_image(camera.x, camera.top, """https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/Bowser_-_New_Super_Mario_Bros_2.png/220px-Bowser_-_New_Super_Mario_Bros_2.png""")
            enemy_1.scale_by(0.3)
            if rand_1 != rand_2:
                lvl1_enemies.append(enemy_1)

        if ticks % rand_2 == 0:
            enemy_2 = gamebox.from_image(150, camera.top, """https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/Bowser_-_New_Super_Mario_Bros_2.png/220px-Bowser_-_New_Super_Mario_Bros_2.png""")
            enemy_2.scale_by(0.3)
            lvl1_enemies.append(enemy_2)
        if ticks % rand_3 == 0:
            enemy_3 = gamebox.from_image(650, camera.top, """https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/Bowser_-_New_Super_Mario_Bros_2.png/220px-Bowser_-_New_Super_Mario_Bros_2.png""")
            enemy_3.scale_by(0.3)
            if rand_2 != rand_3 or rand_1 != rand_3:
                lvl1_enemies.append(enemy_3)

        for enemy in lvl1_enemies:
            camera.draw(enemy)
            enemy.y += 16
            if enemy.y > character.y:
                lvl1_enemies.remove(enemy)


def coin_countlvl1():
    """

    :return: the coins from level one are created and removed if Mario doesn't collect them
    """
    global ticks
    global score
    ticks += 1
    if game_on:
        if ticks % random.randrange(40, 80) == 0:
            coin_1 = gamebox.from_image(camera.x, camera.top, """http://icons.iconarchive.com/icons/ph03nyx/super-mario/256/Retro-Coin-icon.png""")
            coin_1.scale_by(0.1)
            coins.append(coin_1)
        if ticks % random.randrange(40, 80) == 0:
            coin_2 = gamebox.from_image(150, camera.top, """http://icons.iconarchive.com/icons/ph03nyx/super-mario/256/Retro-Coin-icon.png""")
            coin_2.scale_by(0.1)
            coins.append(coin_2)
        if ticks % random.randrange(40, 80) == 0:
            coin_3 = gamebox.from_image(650, camera.top, """http://icons.iconarchive.com/icons/ph03nyx/super-mario/256/Retro-Coin-icon.png""")
            coin_3.scale_by(0.1)
            coins.append(coin_3)

        for coin in coins:
            camera.draw(coin)
            coin.y += 8
            if character.touches(coin):
                score *= 1.05
                coins.remove(coin)
            if coin.y > camera.bottom:
                coins.remove(coin)


def coin_countlvl2():
    """

    :return: the coins from level two are created and removed if Mario doesn't collect them
    """
    global ticks
    global score
    ticks += 1
    if game_on:
        if ticks % random.randrange(40, 70) == 0:
            coin_1 = gamebox.from_image(camera.x, camera.top, """http://icons.iconarchive.com/icons/ph03nyx/super-mario/256/Retro-Coin-icon.png""")
            coin_1.scale_by(0.1)
            coins.append(coin_1)
        if ticks % random.randrange(40, 70) == 0:
            coin_2 = gamebox.from_image(150, camera.top, """http://icons.iconarchive.com/icons/ph03nyx/super-mario/256/Retro-Coin-icon.png""")
            coin_2.scale_by(0.1)
            coins.append(coin_2)
        if ticks % random.randrange(40, 70) == 0:
            coin_3 = gamebox.from_image(650, camera.top, """http://icons.iconarchive.com/icons/ph03nyx/super-mario/256/Retro-Coin-icon.png""")
            coin_3.scale_by(0.1)
            coins.append(coin_3)

        for coin in coins:
            camera.draw(coin)
            coin.y += 12
            if character.touches(coin):
                score *= 1.05
                coins.remove(coin)
            if coin.y > camera.bottom:
                coins.remove(coin)


def coin_countlvl3():
    """

    :return: the coins from level three are created and removed if Mario doesn't collect them
    """
    global ticks
    global score
    ticks += 1
    if game_on:
        if ticks % random.randrange(40, 60) == 0:
            coin_1 = gamebox.from_image(camera.x, camera.top, """http://icons.iconarchive.com/icons/ph03nyx/super-mario/256/Retro-Coin-icon.png""")
            coin_1.scale_by(0.1)
            coins.append(coin_1)
        if ticks % random.randrange(40, 60) == 0:
            coin_2 = gamebox.from_image(150, camera.top, """http://icons.iconarchive.com/icons/ph03nyx/super-mario/256/Retro-Coin-icon.png""")
            coin_2.scale_by(0.1)
            coins.append(coin_2)
        if ticks % random.randrange(40, 60) == 0:
            coin_3 = gamebox.from_image(650, camera.top, """http://icons.iconarchive.com/icons/ph03nyx/super-mario/256/Retro-Coin-icon.png""")
            coin_3.scale_by(0.1)
            coins.append(coin_3)

        for coin in coins:
            camera.draw(coin)
            coin.y += 16
            if character.touches(coin):
                score *= 1.05
                coins.remove(coin)
            if coin.y > camera.bottom:
                coins.remove(coin)


def endgame(keys):
    """

    :param keys: key hit to restart the game
    :return: displays "game over" and game ends. Player has the option to hit a key and play again.
    """
    global game_on
    global background_number
    global level
    global score
    for enemy in lvl1_enemies:
        if character.touches(enemy):
            background_number += 1
            camera.draw(gamebox.from_text(400, 250, "GAME OVER!", 60, "Red", bold=True))
            camera.draw(gamebox.from_text(camera.x, camera.y + 100, "Press Space to Play Again", 70, "red", italic=True,
                                          bold=True))
            game_on = False
        if pygame.K_SPACE in keys:
            score = 0
            level = 1
            game_on = True
            lvl1_enemies.remove(enemy)


def level1(keys):
    """

    :param keys: keys used to play level one
    :return: level one is played
    """
    global level
    global ticks
    global score
    camera.draw(track_1)
    player_movement(keys)
    coin_countlvl1()
    score_count()
    if (score // 30) <= 90 and (score // 30) >= 60:
        level1_complete = gamebox.from_text(camera.x, camera.y, "Prepare for the Next Level",
                                            40, "white", italic=True, bold=True)
        camera.draw(level1_complete)
    enemieslvl1()
    start_game(keys)
    endgame(keys)


def level2(keys):
    """
    :param keys: keys used to play level two
    :return: level two is played
    """
    global level
    global ticks
    global score
    camera.draw(track_2)
    player_movement(keys)
    coin_countlvl2()
    score_count()
    if (score // 30) <= 90 and (score // 30) >= 60:
        level2_complete = gamebox.from_text(camera.x, camera.y, " Prepare For Next Level", 40,
                                            "white", italic=True, bold=True)
        camera.draw(level2_complete)
    enemieslvl2()
    endgame(keys)


def level3(keys):
    """

    :param keys: keys used to play level three
    :return: level three is played
    """
    global level
    global ticks
    global score
    camera.draw(track_3)
    player_movement(keys)
    coin_countlvl3()
    score_count()
    enemieslvl3()
    endgame(keys)


def tick(keys):
    """
    this is the main function
    :param keys: keys used throughout the entire game
    :return: runs the entire game
    """
    global level
    global ticks
    global lvl1_enemies
    global score
    ticks += 1
    if level == 1:
        level1(keys)
    elif level == 2:
        level2(keys)
    elif level == 3:
        level3(keys)
    elif level == 4:
        camera.draw(winner_track)
        win = gamebox.from_text(camera.x, camera.y-50, "YOU WIN!", 80, "cyan", italic=True, bold=True)
        win_2 = gamebox.from_text(camera.x, camera.y+20, "PRINCESS PEACH IS SAVED!!!!", 60, "cyan", italic=True,
                                  bold=True)
        play_again = gamebox.from_text(camera.x, camera.y + 80, "Press Space to Play Again", 60, "cyan", italic=True,
                                       bold=True)
        camera.draw(play_again)
        camera.draw(win)
        camera.draw(win_2)
        if pygame.K_SPACE in keys:
            level -= 3

    camera.display()


frames = 60
gamebox.timer_loop(frames, tick)

