"""
Alexander Hernandez
ENAE380 Final Project
Section 0104
"""

import pygame
import random
from pygame.locals import *
import sys
import math

# Setup for Mouse Input
mainClock = pygame.time.Clock()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)

# Setup for Pygame
pygame.init()
displayWidth = 1440
displayHeight = 805
surface = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Image')

# Set up to display text
font80 = pygame.font.SysFont("Ariel", 80)


class Color:
    black = (0, 0, 0)


def text(font, writing, color):
    return font.render(writing, 1, color)


# Displays images
# Board Images
title_Image = pygame.image.load('Images/Title.jpg')
resized_title = pygame.transform.scale(title_Image, (1440, 805))
campaign_mapImage = pygame.image.load('Images/Campaign_map.jpg')
resized_map = pygame.transform.scale(campaign_mapImage, (1440, 805))
class_screenImage = pygame.image.load('Choices/Class_Screen.png')
resized_class_screen = pygame.transform.scale(class_screenImage, (1440, 805))
gain_healthImage = pygame.image.load('Images/Gained_Health.jpg')
resized_gain_health = pygame.transform.scale(gain_healthImage, (500, 500))
gain_manaImage = pygame.image.load('Images/gain_mana.jpg')
resized_gain_mana = pygame.transform.scale(gain_manaImage, (500, 500))
battle_mapImage = pygame.image.load('Images/battle_map.jpg')
resized_battle_map = pygame.transform.scale(battle_mapImage, (1440, 805))
battle_map_manaImage = pygame.image.load('Images/battle_map_mana.jpg')
resized_battle_map_mana = pygame.transform.scale(battle_map_manaImage, (1440, 805))
background_1Image = pygame.image.load('Images/battle_background_1.png')
resized_background1 = pygame.transform.scale(background_1Image, (150, 150))
background_2Image = pygame.image.load('Images/battle_background_2.png')
resized_background2 = pygame.transform.scale(background_2Image, (150, 150))
background_3Image = pygame.image.load('Images/battle_background3.jpg')
resized_background3 = pygame.transform.scale(background_3Image, (500, 100))

# Player Choices
rogue_die_optionImage = pygame.image.load('Choices/rogue_die_option.jpg')
resized_rogue_die_option = pygame.transform.scale(rogue_die_optionImage, (500, 500))
path_choiceImage = pygame.image.load('Choices/path_choice.jpg')
resized_path_choice = pygame.transform.scale(path_choiceImage, (500, 500))
health_mana_choiceImage = pygame.image.load('Choices/health_mana_choice.jpg')
resized_health_mana_choice = pygame.transform.scale(health_mana_choiceImage, (500, 500))
gain_cardImage = pygame.image.load('Choices/gain_card.jpg')
resized_gain_card = pygame.transform.scale(gain_cardImage, (1440, 805))
replace_cardImage = pygame.image.load('Choices/replace_card.jpg')
resized_replace_card = pygame.transform.scale(replace_cardImage, (1440, 805))
won_Image = pygame.image.load('Images/won_screen.jpg')
resized_won = pygame.transform.scale(won_Image, (1440, 805))
lost_Image = pygame.image.load('Images/lost_screen.jpg')
resized_lost = pygame.transform.scale(lost_Image, (1440, 805))

# Player Images
knight_Image = pygame.image.load('Images/knight_model.png')
resized_knight_Image = pygame.transform.scale(knight_Image, (50, 50))
wizard_Image = pygame.image.load('Images/wizard_model.png')
resized_wizard_Image = pygame.transform.scale(wizard_Image, (50, 50))
rogue_Image = pygame.image.load('Images/rogue_model.png')
resized_rogue_Image = pygame.transform.scale(rogue_Image, (50, 50))

# Die Faces
one_Image = pygame.image.load('Die_Faces/die_one.png')
resized_one_Image = pygame.transform.scale(one_Image, (70, 70))
two_Image = pygame.image.load('Die_Faces/die_two.png')
resized_two_Image = pygame.transform.scale(two_Image, (70, 70))
three_Image = pygame.image.load('Die_Faces/die_three.png')
resized_three_Image = pygame.transform.scale(three_Image, (70, 70))
four_Image = pygame.image.load('Die_Faces/die_four.png')
resized_four_Image = pygame.transform.scale(four_Image, (70, 70))
five_Image = pygame.image.load('Die_Faces/die_five.png')
resized_five_Image = pygame.transform.scale(five_Image, (70, 70))
six_Image = pygame.image.load('Die_Faces/die_six.png')
resized_six_Image = pygame.transform.scale(six_Image, (70, 70))
seven_Image = pygame.image.load('Die_Faces/die_seven.png')
resized_seven_Image = pygame.transform.scale(seven_Image, (70, 70))

# Card Images
emptyImage = pygame.image.load('Battles/Cards/empty_card.png')
resized_empty = pygame.transform.scale(emptyImage, (175, 265))

# General Card Images
axeImage = pygame.image.load('Battles/Cards/axe.png')
resized_axe = pygame.transform.scale(axeImage, (175, 265))
bow_and_arrowImage = pygame.image.load('Battles/Cards/bow_and_arrow.png')
resized_bow_and_arrow = pygame.transform.scale(bow_and_arrowImage, (175, 265))
clubImage = pygame.image.load('Battles/Cards/club.png')
resized_club = pygame.transform.scale(clubImage, (175, 265))
crossbowImage = pygame.image.load('Battles/Cards/crossbow.png')
resized_crossbow = pygame.transform.scale(crossbowImage, (175, 265))
maceImage = pygame.image.load('Battles/Cards/mace.png')
resized_mace = pygame.transform.scale(maceImage, (175, 265))
pitchforkImage = pygame.image.load('Battles/Cards/pitchfork.png')
resized_pitchfork = pygame.transform.scale(pitchforkImage, (175, 265))
punchImage = pygame.image.load('Battles/Cards/punch.png')
resized_punch = pygame.transform.scale(punchImage, (175, 265))
shieldImage = pygame.image.load('Battles/Cards/shield.png')
resized_shield = pygame.transform.scale(shieldImage, (175, 265))
spearImage = pygame.image.load('Battles/Cards/spear.png')
resized_spear = pygame.transform.scale(spearImage, (175, 265))
swordImage = pygame.image.load('Battles/Cards/sword.png')
resized_sword = pygame.transform.scale(swordImage, (175, 265))

# Knight Card Images
battering_ramImage = pygame.image.load('Battles/Cards/Knight/battering_ram.png')
resized_battering_ram = pygame.transform.scale(battering_ramImage, (175, 265))
catapultImage = pygame.image.load('Battles/Cards/Knight/catapult.png')
resized_catapult = pygame.transform.scale(catapultImage, (175, 265))
crusadeImage = pygame.image.load('Battles/Cards/Knight/crusade.png')
resized_crusade = pygame.transform.scale(crusadeImage, (175, 265))
flailImage = pygame.image.load('Battles/Cards/Knight/flail.png')
resized_flail = pygame.transform.scale(flailImage, (175, 265))
hand_cannonImage = pygame.image.load('Battles/Cards/Knight/hand_cannon.png')
resized_hand_cannon = pygame.transform.scale(hand_cannonImage, (175, 265))
lanceImage = pygame.image.load('Battles/Cards/Knight/lance.png')
resized_lance = pygame.transform.scale(lanceImage, (175, 265))
last_standImage = pygame.image.load('Battles/Cards/Knight/last_stand.png')
resized_last_stand = pygame.transform.scale(last_standImage, (175, 265))
shield_bashImage = pygame.image.load('Battles/Cards/Knight/shield_bash.png')
resized_shield_bash = pygame.transform.scale(shield_bashImage, (175, 265))
siegeImage = pygame.image.load('Battles/Cards/Knight/siege.png')
resized_siege = pygame.transform.scale(siegeImage, (175, 265))
volleyImage = pygame.image.load('Battles/Cards/Knight/volley.png')
resized_volley = pygame.transform.scale(volleyImage, (175, 265))

# Wizard Card Images
fireballImage = pygame.image.load('Battles/Cards/Wizard/fireball.png')
resized_fireball = pygame.transform.scale(fireballImage, (175, 265))
lightning_strikeImage = pygame.image.load('Battles/Cards/Wizard/lightning_strike.png')
resized_lightning_strike = pygame.transform.scale(lightning_strikeImage, (175, 265))
divine_interventionImage = pygame.image.load('Battles/Cards/Wizard/divine_intervention.png')
resized_divine_intervention = pygame.transform.scale(divine_interventionImage, (175, 265))
stone_skinImage = pygame.image.load('Battles/Cards/Wizard/stone_skin.png')
resized_stone_skin = pygame.transform.scale(stone_skinImage, (175, 265))
invisibilityImage = pygame.image.load('Battles/Cards/Wizard/invisibility.png')
resized_invisibility = pygame.transform.scale(invisibilityImage, (175, 265))
life_healImage = pygame.image.load('Battles/Cards/Wizard/life_heal.png')
resized_life_heal = pygame.transform.scale(life_healImage, (175, 265))
life_stealImage = pygame.image.load('Battles/Cards/Wizard/life_steal.png')
resized_life_steal = pygame.transform.scale(life_stealImage, (175, 265))
reflectImage = pygame.image.load('Battles/Cards/Wizard/reflect.png')
resized_reflect = pygame.transform.scale(reflectImage, (175, 265))
protectionImage = pygame.image.load('Battles/Cards/Wizard/protection.png')
resized_protection = pygame.transform.scale(protectionImage, (175, 265))
poisonImage = pygame.image.load('Battles/Cards/Wizard/poison.png')
resized_poison = pygame.transform.scale(poisonImage, (175, 265))

# Rogue Card Images
shadowImage = pygame.image.load('Battles/Cards/shadow.png')
resized_shadow = pygame.transform.scale(shadowImage, (175, 265))
daggersImage = pygame.image.load('Battles/Cards/Rogue/daggers.png')
resized_daggers = pygame.transform.scale(daggersImage, (175, 265))
cloakImage = pygame.image.load('Battles/Cards/Rogue/cloak.png')
resized_cloak = pygame.transform.scale(cloakImage, (175, 265))
knockoutImage = pygame.image.load('Battles/Cards/Rogue/knockout.png')
resized_knockout = pygame.transform.scale(knockoutImage, (175, 265))
assassinateImage = pygame.image.load('Battles/Cards/Rogue/assassinate.png')
resized_assassinate = pygame.transform.scale(assassinateImage, (175, 265))
battle_axeImage = pygame.image.load('Battles/Cards/Rogue/battle_axe.png')
resized_battle_axe = pygame.transform.scale(battle_axeImage, (175, 265))
revengeImage = pygame.image.load('Battles/Cards/Rogue/revenge.png')
resized_revenge = pygame.transform.scale(revengeImage, (175, 265))

# Enemy Images
goblinImage = pygame.image.load('Enemies/goblin.png')
resized_goblin = pygame.transform.scale(goblinImage, (250, 400))
banditImage = pygame.image.load('Enemies/bandit.png')
resized_bandit = pygame.transform.scale(banditImage, (250, 400))
serpentImage = pygame.image.load('Enemies/serpent.png')
resized_serpent = pygame.transform.scale(serpentImage, (250, 400))
werewolfImage = pygame.image.load('Enemies/werewolf.png')
resized_werewolf = pygame.transform.scale(werewolfImage, (250, 400))
minotaurImage = pygame.image.load('Enemies/minotaur.png')
resized_minotaur = pygame.transform.scale(minotaurImage, (250, 400))
yetiImage = pygame.image.load('Enemies/yeti.png')
resized_yeti = pygame.transform.scale(yetiImage, (250, 400))

# Miniboss Images
entityImage = pygame.image.load('Enemies/Mini-bosses/entity.png')
resized_entity = pygame.transform.scale(entityImage, (250, 400))
wendigoImage = pygame.image.load('Enemies/Mini-bosses/wendigo.png')
resized_wendigo = pygame.transform.scale(wendigoImage, (250, 400))
entImage = pygame.image.load('Enemies/Mini-bosses/ent.png')
resized_ent = pygame.transform.scale(entImage, (250, 400))
spiderImage = pygame.image.load('Enemies/Mini-bosses/spider.png')
resized_spider = pygame.transform.scale(spiderImage, (250, 400))
sirenImage = pygame.image.load('Enemies/Mini-bosses/siren.png')
resized_siren = pygame.transform.scale(sirenImage, (250, 400))
hydraImage = pygame.image.load('Enemies/Mini-bosses/hydra.png')
resized_hydra = pygame.transform.scale(hydraImage, (250, 400))

# Boss Images
demonImage = pygame.image.load('Enemies/Bosses/demon.png')
resized_demon = pygame.transform.scale(demonImage, (250, 400))
vampireImage = pygame.image.load('Enemies/Bosses/vampire.png')
resized_vampire = pygame.transform.scale(vampireImage, (250, 400))
orcImage = pygame.image.load('Enemies/Bosses/orc.png')
resized_orc = pygame.transform.scale(orcImage, (250, 400))


# Card Functions
# General Cards
def sword():
    return 3


def spear():
    return 4


def shield():
    return 3


def axe():
    return 3


def bow_and_arrow():
    dice = [1, 2, 3]
    value = random.choice(dice)
    return value


def crossbow():
    attack = 2
    penetrate = True
    return attack, penetrate


def punch():
    return 1


def club():
    return 2


def mace():
    return 3


def pitchfork():
    return 2


# Wizard Cards
def fireball(mana):
    if mana < 1:
        attack = 0
        armor = 0
        new_mana = 0
        return attack, armor, new_mana
    elif mana >= 1:
        new_mana = 1
        attack = 5
        armor = 0
        return attack, armor, new_mana


def stone_skin(mana):
    if mana < 2:
        attack = 0
        armor = 0
        new_mana = 0
        return attack, armor, new_mana
    elif mana >= 2:
        new_mana = 2
        armor = 4
        attack = 0
        return attack, armor, new_mana


def divine_intervention(mana):
    if mana < 4:
        attack = 0
        armor = 0
        new_mana = 0
        return attack, armor, new_mana
    elif mana >= 4:
        new_mana = 4
        armor = 0
        attack = 12
        return attack, armor, new_mana


def life_heal(mana):
    if mana >= 3:
        new_mana = 3
        attack = 0
        heal = 4
        penetrate = False
        return attack, heal, new_mana, penetrate
    elif mana < 3:
        attack = 0
        heal = 0
        new_mana = 0
        penetrate = False
        return attack, heal, new_mana, penetrate


def life_steal(mana):
    if mana >= 4:
        new_mana = 4
        dice = [1, 2, 3, 4, 5, 6]
        value = random.choice(dice)
        attack = value
        heal = value
        penetrate = True
        return attack, heal, new_mana, penetrate
    elif mana < 4:
        attack = 0
        heal = 0
        new_mana = 0
        penetrate = False
        return attack, heal, new_mana, penetrate


def protection(mana):
    if mana >= 1:
        attack = 0
        armor = 3
        new_mana = 1
        return attack, armor, new_mana
    elif mana < 1:
        attack = 0
        armor = 0
        new_mana = 0
        return attack, armor, new_mana


def invisibility(mana):
    if mana >= 2:
        new_mana = 2
        attack = 0
        invis = True
        return attack, invis, new_mana
    elif mana < 2:
        new_mana = 0
        attack = 0
        invis = False
        return attack, invis, new_mana


def lightning_strike(mana):
    if mana >= 3:
        new_mana = 3
        attack = 4
        skip = True
        return attack, skip, new_mana
    elif mana < 3:
        new_mana = 0
        attack = 0
        skip = False
        return attack, skip, new_mana


def reflect(mana, damage):
    if mana >= 3:
        new_mana = 3
        attack = damage*2
        return attack, new_mana
    elif mana < 3:
        new_mana = 0
        attack = 0
        return attack, new_mana


def poison(mana):
    if mana >= 2:
        new_mana = 2
        penetrate = True
        return 3, penetrate, new_mana
    elif mana < 2:
        new_mana = 0
        penetrate = False
        return 0, penetrate, new_mana


# Knight Cards
def lance():
    attack = 5
    penetrate = True
    return attack, penetrate


def volley():
    dice = [1, 2, 3, 4, 5, 6]
    value = random.choice(dice)
    attack = 3 + value
    return attack


def hand_cannon():
    attack = 7
    penetrate = True
    dice = [1, 2]
    value = random.choice(dice)
    if value == 1:
        return attack, penetrate
    else:
        attack = 0
        penetrate = 0
        return attack, penetrate


def catapult():
    dice = [1, 2, 3, 4, 5]
    value = random.choice(dice)
    if value == 1 or value == 3 or value == 5:
        return 9
    else:
        return 0


def shield_bash():
    attack = 2
    armor = 2
    mana = 0
    return attack, armor, mana


def crusade():
    dice = [1, 2, 3, 4, 5]
    value = random.choice(dice)
    if value == 1 or value == 2 or value == 3:
        harm = -3
        attack = 0
        return attack, harm
    else:
        harm = 0
        attack = 5
        return attack, harm


def battering_ram():
    return 0


def last_stand(health):
    if health >= 15:
        return 2
    elif health < 15:
        return 12


def flail():
    attack = 3
    dice = [1, 2]
    value = random.choice(dice)
    while value == 1:
        attack += 1
        value = random.choice(dice)
    return attack


def siege(damage):
    attack = math.ceil(damage/2)
    penetrate = True
    return attack, penetrate


# Rogue Cards
def daggers():
    dice = [1, 2, 3, 4, 5, 6]
    value = random.choice(dice)
    attack = 2*value
    return attack


def cloak():
    dice = [1, 2, 3, 4, 5]
    value = random.choice(dice)
    attack = 0
    mana = 0
    if value == 1 or value == 3 or value == 5:
        invis = True
        return attack, invis, mana
    elif value == 2 or value == 4:
        invis = False
        return attack, invis, mana


def knockout():
    dice = list(range(1, 101))
    value = random.choice(dice)
    if value == 50:
        return 100
    else:
        return 2


def assassinate():
    dice = list(range(1, 101))
    value = random.choice(dice)
    if 1 <= value <= 50:
        return 1
    elif 51 <= value <= 75:
        return 3
    elif 76 <= value <= 90:
        return 5
    elif 91 <= value <= 95:
        return 8
    elif 96 <= value <= 99:
        return 10
    elif value == 100:
        return 100


def battle_axe():
    attack = 3
    dice = list(range(1, 101))
    hit1 = 0
    hit2 = 0
    value = random.choice(dice)
    if value <= 55:
        hit1 = 1
    elif value > 55:
        hit1 = 0

    value = random.choice(dice)
    if value <= 55:
        hit2 = 1
    elif value > 55:
        hit2 = 0

    return attack*hit1 + attack*hit2


def shadow():
    attack = 4
    mana = 0
    dice = list(range(1, 11))
    value = random.choice(dice)
    if value <= 3:
        invis = True
        return attack, invis, mana
    elif value > 3:
        invis = False
        return attack, invis, mana


def revenge(damage):
    attack = damage + 3
    return attack


x = 0
y = 0
surface.fill((255, 255, 255))

# Displays Title Screen
surface.blit(resized_title, (0, 0))
pygame.display.update()

# Once title screen is clicked, goes to Class Screen
stage1 = True
while stage1:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                surface.blit(resized_class_screen, (0, 0))
                pygame.display.update()
                stage1 = False

# Initializes where the class choices are on the screen
wizard_area = [150, 450, 250, 675]
knight_area = [525, 900, 250, 675]
rogue_area = [1000, 1325, 250, 675]
class_area = [wizard_area, knight_area, rogue_area]
area_names = ["Wizard", "Knight", "Rogue"]
stage2 = True


# Once a class is chosen, moves on to the campaign map
while stage2:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                class_index1 = 0
                for i in class_area:
                    class_index2 = 0
                    disp = [0, 0, 0, 0]
                    for j in i:
                        disp[class_index2] = class_area[class_index1][class_index2]
                        class_index2 += 1
                    if pos[0] in range(disp[0], disp[1]) and pos[1] in range(disp[2], disp[3]):
                        model = area_names[class_index1]
                        stage2 = False
                    class_index1 += 1

# Transforms coordinates into single values
total_move = 0
total_move1 = 0
total_move2a = 0
total_move2b = 0
total_move2c = 0
total_move3 = 0

path1_coords = [[30, 724], [80, 700], [110, 687], [143, 677], [175, 660], [202, 647], [232, 628], [256, 610],
                [285, 587], [312, 567], [340, 547], [375, 527], [424, 501]]
path2a_coords = [[424, 501], [393, 453], [349, 428], [302, 397], [245, 370], [195, 340], [145, 318], [107, 277],
                 [99, 227], [113, 180], [140, 136], [185, 95], [245, 62], [311, 48], [377, 42], [446, 34], [511, 34],
                 [561, 38], [608, 40], [658, 54], [709, 65], [768, 77], [821, 87], [868, 108], [914, 139], [945, 168],
                 [1002, 200], [1056, 224]]
path2b_coords = [[424, 501], [462, 467], [475, 452], [487, 434], [495, 418], [512, 404], [528, 386], [545, 368],
                 [566, 352], [591, 339], [615, 328], [638, 317], [663, 307], [685, 300], [714, 295], [741, 288],
                 [769, 282], [796, 275], [819, 268], [840, 267], [864, 266], [886, 263], [912, 264], [936, 268],
                 [961, 274], [985, 279], [1013, 285], [1040, 282]]
path2c_coords = [[424, 501], [451, 550], [472, 587], [504, 616], [545, 641], [583, 661], [624, 670], [671, 675],
                 [718, 672], [769, 652], [811, 635], [850, 616], [881, 587], [918, 557], [963, 537], [1012, 528],
                 [1069, 533], [1121, 549], [1171, 558], [1216, 553], [1255, 533], [1286, 504], [1297, 459], [1277, 420],
                 [1237, 398], [1190, 390], [1153, 366], [1123, 326]]
path3_coords = [[0, 0], [1094, 278], [1163, 271], [1217, 257], [1245, 225], [1234, 192], [1208, 165], [1180, 134],
                [1188, 97], [1225, 82], [1266, 81], [1306, 79], [1332, 53]]
boss_coords = [1347, 14]

decision1 = False
decision2 = False


# Action Functions
def dice_roll(character):
    # Randomly chooses a value between 1 and 6
    dice = [1, 2, 3, 4, 5, 6]
    value = random.choice(dice)
    if character == "Rogue":
        # Initializes the areas for the Rogue's special ability
        subtract_area = [525, 690, 590, 620]
        keep_area = [690, 820, 590, 620]
        add_area = [840, 980, 590, 620]
        ability_area = [keep_area, add_area, subtract_area]
        ability_names = ["keep", "add", "subtract"]
        ability = "ability"

        # Initializes the die faces and where the screen pops up
        die_face = [0, resized_one_Image, resized_two_Image, resized_three_Image, resized_four_Image,
                    resized_five_Image, resized_six_Image, resized_seven_Image]
        surface.blit(resized_rogue_die_option, (500, 150))
        surface.blit(die_face[value], (710, 350))
        pygame.display.update()
        option = True
        while option:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        index1 = 0
                        for i in ability_area:
                            index2 = 0
                            button = [0, 0, 0, 0]
                            for h in i:
                                button[index2] = ability_area[index1][index2]
                                index2 += 1
                            if pos[0] in range(button[0], button[1]) and pos[1] in range(button[2], button[3]):
                                ability = ability_names[index1]
                            index1 += 1
                        if ability == "add":
                            value += 1
                            option = False
                        elif ability == "keep":
                            value = value
                            option = False
                        elif ability == "subtract" and value != 1:
                            value -= 1
                            option = False
    return value


def gain_health(character, health, mana):
    # Initializes the button areas for the choices
    health_area = [510, 745, 290, 525]
    mana_area = [775, 950, 290, 525]
    choice_area = [health_area, mana_area]
    choice_names = ["health", "mana"]
    choice = "none"

    # If the class is a wizard, you get to choose between health and mana
    if character == "Wizard":
        pick = True
        while pick:
            surface.blit(resized_health_mana_choice, (500, 150))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        index1 = 0
                        for i in choice_area:
                            index2 = 0
                            button = [0, 0, 0, 0]
                            for h in i:
                                button[index2] = choice_area[index1][index2]
                                index2 += 1
                            if pos[0] in range(button[0], button[1]) and pos[1] in range(button[2], button[3]):
                                choice = choice_names[index1]
                            index1 += 1
                        if choice == "health":
                            surface.blit(resized_gain_health, (500, 150))
                            pygame.display.update()
                            pygame.time.delay(2000)
                            health += 20
                            mana += 0
                            pick = False
                        elif choice == "mana":
                            surface.blit(resized_gain_mana, (500, 150))
                            pygame.display.update()
                            pygame.time.delay(2000)
                            health += 0
                            mana += 5
                            pick = False
        return health, mana
    # Otherwise you automatically receive health
    else:
        surface.blit(resized_gain_health, (500, 150))
        pygame.display.update()
        pygame.time.delay(2000)
        health += 20
        mana += 0
        return health, mana


def gain_card(deck, index_deck, deck_select, index_deck_select, deck_images, images, move, ind, character):
    # Generates the cards
    # Initializes the length of the deck depending on the character chosen
    if character == "Rogue":
        end = 16
    else:
        end = 19

    if move == 26:
        list1 = range(10, end)
        list2 = range(10, end)
    else:
        list1 = range(0, 9)
        list2 = range(10, end)

    card1 = random.choice(list1)
    card2 = random.choice(list2)

    # Initializes the areas for the card choices
    card_choice1_area = [433, 608, 230, 497]
    card_choice2_area = [862, 1037, 230, 497]
    skip_area = [405, 1062, 630, 720]
    card_choices = [card_choice1_area, card_choice2_area, skip_area]
    card_choice_names = ["card_choice1", "card_choice2", "skip"]
    pick_card = "none"
    selected_card = 0
    card_index = 0

    card1_area = [23, 194, 500, 765]
    card2_area = [199, 369, 500, 765]
    card3_area = [375, 544, 500, 765]
    card4_area = [550, 719, 500, 765]
    card5_area = [725, 894, 500, 765]
    card6_area = [900, 1069, 500, 765]
    card7_area = [1075, 1244, 500, 765]
    card8_area = [1250, 1420, 500, 765]
    card_areas = [card1_area, card2_area, card3_area, card4_area, card5_area, card6_area, card7_area, card8_area]
    card_names = ["0", "1", "2", "3", "4", "5", "6", "7"]

    # Selects the card the player wants
    choice1 = True
    while choice1:
        surface.blit(deck_images[card1], (433, 230))
        surface.blit(deck_images[card2], (862, 230))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    index1 = 0
                    for i in card_choices:
                        index2 = 0
                        button = [0, 0, 0, 0]
                        for h in i:
                            button[index2] = card_choices[index1][index2]
                            index2 += 1
                        if pos[0] in range(button[0], button[1]) and pos[1] in range(button[2], button[3]):
                            pick_card = card_choice_names[index1]
                        index1 += 1
                    if pick_card == "card_choice1":
                        selected_card = card1
                        choice1 = False
                    elif pick_card == "card_choice2":
                        selected_card = card2
                        choice1 = False
                    elif pick_card == "skip":
                        choice1 = False

    # If player does not skip, replaces card of player's choice
    if pick_card != "skip":
        choice2 = True
        while choice2:
            surface.blit(resized_replace_card, (0, 0))
            surface.blit(deck_images[selected_card], (648, 230))
            surface.blit(deck_images[images[0]], (20, 500))
            surface.blit(deck_images[images[1]], (195, 500))
            surface.blit(deck_images[images[2]], (370, 500))
            surface.blit(deck_images[images[3]], (545, 500))
            surface.blit(deck_images[images[4]], (720, 500))
            surface.blit(deck_images[images[5]], (895, 500))
            surface.blit(deck_images[images[6]], (1070, 500))
            surface.blit(deck_images[images[7]], (1245, 500))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        index1 = 0
                        for i in card_areas:
                            index2 = 0
                            button = [0, 0, 0, 0]
                            for h in i:
                                button[index2] = card_areas[index1][index2]
                                index2 += 1
                            if pos[0] in range(button[0], button[1]) and pos[1] in range(button[2], button[3]):
                                pick_card = card_names[index1]
                                card_index = int(pick_card)
                            index1 += 1
                        deck_length = len(deck)
                        # Adds cards to empty slots
                        if card_index >= deck_length:
                            deck.append(deck_select[selected_card])
                            index_deck.insert(ind, index_deck_select[selected_card])
                            ind += 1
                        # Replaces card in an existing slot
                        elif card_index < deck_length:
                            deck[card_index] = deck_select[selected_card]
                            index_deck[card_index] = index_deck_select[selected_card]
                        choice2 = False
    return deck, index_deck, ind


def enemy_deck_builder(enemy_deck, enemy_index):
    # Initializes the enemy's card and index deck
    enemy_card_deck = [sword(), sword(), sword(), sword(), sword(), sword(), sword(), sword(),]
    enemy_index_deck = ["none", "none", "none", "none", "none", "none", "none", "none"]
    initial = 0
    value_list = []
    # Picks a random card to place in the enemy's deck
    while initial < 8:
        dice = list(range(1, 32))
        card_value = random.choice(dice)

        # If the card already exists in the deck, choose a new one so there are no repeats
        while card_value in value_list:
            card_value = random.choice(dice)

        # Adds the card to the deck
        value_list.append(card_value)
        enemy_index_deck[initial] = enemy_index[card_value - 1]
        enemy_card_deck[initial] = enemy_deck[card_value - 1]
        initial += 1

    return enemy_index_deck, enemy_card_deck


def battle(deck, index_deck, enemy_deck, enemy_index_deck, health, armor, initial_mana, enemy_name, character):
    # Initializes the text that will be used to display health, armor, and mana
    health_indicator = str(health)
    health_output = text(font80, health_indicator, Color.black)
    armor_indicator = str(armor)
    armor_output = text(font80, armor_indicator, Color.black)
    mana_indicator = str(initial_mana)
    mana_output = text(font80, mana_indicator, Color.black)
    not_enough_mana = text(font80, "Not Enough Mana", Color.black)

    # Initializes the card areas / player initial conditions
    card1_area = [23, 194, 500, 765]
    card2_area = [199, 369, 500, 765]
    card3_area = [375, 544, 500, 765]
    card4_area = [550, 719, 500, 765]
    card5_area = [725, 894, 500, 765]
    card6_area = [900, 1069, 500, 765]
    card7_area = [1075, 1244, 500, 765]
    card8_area = [1250, 1420, 500, 765]
    card_areas = [card1_area, card2_area, card3_area, card4_area, card5_area, card6_area, card7_area, card8_area]
    card_names = ["0", "1", "2", "3", "4", "5", "6", "7"]
    no_card = "none"
    card = 0
    mana = int(initial_mana)
    damage = 0

    # Resets wizard cards in order for them to use mana as intended
    if character == "Wizard":
        revised_deck = [sword(), spear(), shield(), axe(), bow_and_arrow(), crossbow(), punch(), club(), mace(),
                        pitchfork(), fireball(mana), lightning_strike(mana), divine_intervention(mana),
                        stone_skin(mana), invisibility(mana), life_heal(mana), life_steal(mana), reflect(mana, damage),
                        protection(mana), poison(mana)]
        revised_index = ["sword", "spear", "shield", "axe", "bow_and_arrow", "crossbow", "punch", "club", "mace",
                         "pitchfork", "fireball", "lightning_strike", "divine_intervention", "stone_skin",
                         "invisibility", "life_heal", "life_steal", "reflect", "protection", "poison"]
        run = 0
        while run < len(deck) - 1:
            new_index = index_deck[run]
            revised_card = revised_index.index(new_index)
            deck[run] = revised_deck[revised_card]
            run += 1

    deck_length = 0
    initial_length = len(deck) - 1
    used_card_list = []

    # Initialize enemy conditions
    enemy_armor = 0
    enemy_mana = 1000
    enemy_health = 15
    all_enemies = ["goblin", "bandit", "serpent", "werewolf", "minotaur", "yeti", "entity", "wendigo", "ent",
                   "spider", "siren", "hydra", "demon", "vampire", "orc"]
    all_enemies_images = [resized_goblin, resized_bandit, resized_serpent, resized_werewolf, resized_minotaur,
                          resized_yeti, resized_entity, resized_wendigo, resized_ent, resized_spider, resized_siren,
                          resized_hydra, resized_demon, resized_vampire, resized_orc]
    enemy_image_index = all_enemies.index(enemy_name)
    enemy_battle_image = 0

    # Chooses the enemy's image depending on the enemy type the player is facing
    if enemy_name == all_enemies[0] or enemy_name == all_enemies[1]:
        enemy_health = 15
        enemy_battle_image = all_enemies_images[enemy_image_index]
    elif enemy_name == all_enemies[2] or enemy_name == all_enemies[3]:
        enemy_health = 20
        enemy_battle_image = all_enemies_images[enemy_image_index]
    elif enemy_name == all_enemies[4] or enemy_name == all_enemies[5]:
        enemy_health = 25
        enemy_battle_image = all_enemies_images[enemy_image_index]
    elif enemy_name == all_enemies[6] or enemy_name == all_enemies[7] or enemy_name == all_enemies[8] \
            or enemy_name == all_enemies[9] or enemy_name == all_enemies[10] or enemy_name == all_enemies[11]:
        enemy_health = 35
        enemy_battle_image = all_enemies_images[enemy_image_index]
    elif enemy_name == all_enemies[12] or enemy_name == all_enemies[13] or enemy_name == all_enemies[14]:
        enemy_health = 50
        enemy_battle_image = all_enemies_images[enemy_image_index]

    # Outputs the stats of the enemy
    enemy_health_indicator = str(enemy_health)
    enemy_health_output = text(font80, enemy_health_indicator, Color.black)
    enemy_armor_indicator = str(enemy_armor)
    enemy_armor_output = text(font80, enemy_armor_indicator, Color.black)
    damage = 0
    attack = 0

    # Initializes the enemy's deck length
    enemy_deck_length = 0
    initial_enemy_index_deck = list(enemy_index_deck)
    initial_enemy_deck = list(enemy_deck)

    # Indicates the health, armor, and mana of the player and enemy, as well as displays the enemy faced
    surface.blit(health_output, (365, 30))
    surface.blit(armor_output, (345, 100))
    if character == "Wizard":
        surface.blit(mana_output, (325, 165))
    surface.blit(enemy_health_output, (1275, 30))
    surface.blit(enemy_armor_output, (1255, 100))
    surface.blit(enemy_battle_image, (550, 30))
    pygame.display.update()

    # Initialize special conditions
    players_poison_truth = False
    opponents_poison_truth = False

    battle_gameplay = True
    while battle_gameplay:
        # Initialize special battle conditions
        players_penetrate = False
        players_invisibility = False
        players_skip = False

        opponents_penetrate = False
        opponents_invisibility = False

        surface.blit(resized_background3, (25, 210))
        pygame.display.update()

        # Initializes key values
        enemy_armor_add = 0
        enemy_poison = 0
        player_poison = 0
        card = 0

        # Enemy picks a card
        enemy_card = random.choice(enemy_index_deck)
        enemy_index_card = enemy_index_deck.index(enemy_card)
        if enemy_index_deck[enemy_index_card] == "sword" or enemy_index_deck[enemy_index_card] == "spear" \
                or enemy_index_deck[enemy_index_card] == "axe" \
                or enemy_index_deck[enemy_index_card] == "bow_and_arrow" \
                or enemy_index_deck[enemy_index_card] == "volley" or enemy_index_deck[enemy_index_card] == "catapult" \
                or enemy_index_deck[enemy_index_card] == "last_stand" or enemy_index_deck[enemy_index_card] == "flail" \
                or enemy_index_deck[enemy_index_card] == "daggers" or enemy_index_deck[enemy_index_card] == "club" \
                or enemy_index_deck[enemy_index_card] == "battle_axe" or enemy_index_deck[enemy_index_card] == "punch" \
                or enemy_index_deck[enemy_index_card] == "mace" or enemy_index_deck[enemy_index_card] == "pitchfork":
            damage = enemy_deck[enemy_index_card]
        elif enemy_index_deck[enemy_index_card] == "shield":
            armor += enemy_deck[enemy_index_card]
            damage = 0
        elif enemy_index_deck[enemy_index_card] == "fireball" or enemy_index_deck[enemy_index_card] == "stone_skin" \
                or enemy_index_deck[enemy_index_card] == "divine_intervention" \
                or enemy_index_deck[enemy_index_card] == "shield_bash"\
                or enemy_index_deck[enemy_index_card] == "protection":
            damage, enemy_armor_add, enemy_mana = enemy_deck[enemy_index_card]
            enemy_armor += enemy_armor_add
        elif enemy_index_deck[enemy_index_card] == "lance" or enemy_index_deck[enemy_index_card] == "hand_cannon" \
                or enemy_index_deck[enemy_index_card] == "crossbow":
            damage, opponents_penetrate = enemy_deck[enemy_index_card]
        elif enemy_index_deck[enemy_index_card] == "crusade":
            damage, harm = enemy_deck[enemy_index_card]
            enemy_health += harm
        elif enemy_index_deck[enemy_index_card] == "life_heal" or enemy_index_deck[enemy_index_card] == "life_steal":
            damage, enemy_heal, enemy_mana, opponents_penetrate = enemy_deck[enemy_index_card]
            enemy_health += enemy_heal
        elif enemy_index_deck[enemy_index_card] == "battering_ram":
            armor = enemy_deck[enemy_index_card]
        elif enemy_index_deck[enemy_index_card] == "invisibility" or enemy_index_deck[enemy_index_card] == "cloak" \
                or enemy_index_deck[enemy_index_card] == "shadow":
            damage, opponents_invisibility, enemy_mana = enemy_deck[enemy_index_card]
        elif enemy_index_deck[enemy_index_card] == "poison":
            enemy_poison, opponents_penetrate, enemy_mana = enemy_deck[enemy_index_card]
            opponents_poison_truth = True

        # Applies only to Wizard: Repeats if there is not enough mana
        mana_cost = True
        while mana_cost:
            if deck_length >= initial_length:
                used_card_list = []
                deck_length = 0
            # Player picks a card
            pick_card = True
            while pick_card:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed()[0]:
                            pos = pygame.mouse.get_pos()
                            index1 = 0
                            for i in card_areas:
                                index2 = 0
                                card_temp = [0, 0, 0, 0]
                                for h in i:
                                    card_temp[index2] = card_areas[index1][index2]
                                    index2 += 1
                                if pos[0] in range(card_temp[0], card_temp[1]) \
                                        and pos[1] in range(card_temp[2], card_temp[3]):
                                    no_card = card_names[index1]
                                    p = str(card_names[index1])
                                    card = int(p)
                                index1 += 1
                            # Player is allowed to use card as long as it has not been used yet and has enough mana
                            if card in used_card_list:
                                pick_card = True
                            elif no_card == "none":
                                pick_card = True
                            elif index_deck[int(no_card)] == "none":
                                pick_card = True
                            elif index_deck[int(no_card)] != "none":
                                pick_card = False

            # Player's card performs it function
            if index_deck[card] == "sword" or index_deck[card] == "spear" or index_deck[card] == "axe" \
                    or index_deck[card] == "bow_and_arrow" or index_deck[card] == "volley" \
                    or index_deck[card] == "catapult" or index_deck[card] == "last_stand" or index_deck[card] == "flail" \
                    or index_deck[card] == "daggers" or index_deck[card] == "knockout" \
                    or index_deck[card] == "assassinate" or index_deck[card] == "battle_axe" or index_deck[card] == "punch" \
                    or index_deck[card] == "club" or index_deck[card] == "mace" or index_deck[card] == "pitchfork":
                attack = deck[card]
                mana_cost = False
            elif index_deck[card] == "shield":
                armor += deck[card]
                attack = 0
                mana_cost = False
            elif index_deck[card] == "fireball" or index_deck[card] == "stone_skin" \
                    or index_deck[card] == "divine_intervention" or index_deck[card] == "shield_bash" \
                    or index_deck[card] == "protection":
                if index_deck[card] == "fireball" and mana < 1 or index_deck[card] == "stone_skin" and mana < 2 \
                        or index_deck[card] == "divine_intervention" and mana < 4 \
                        or index_deck[card] == "protection" and mana < 1:
                    surface.blit(not_enough_mana, (30, 215))
                    pygame.display.update()
                    used_card_list.append(card)
                    deck_length += 1
                    mana_cost = True
                else:
                    attack, armor_add, new_mana = deck[card]
                    mana -= new_mana
                    mana_cost = False
            elif index_deck[card] == "lance" or index_deck[card] == "hand_cannon" or index_deck[card] == "crossbow":
                attack, players_penetrate = deck[card]
                mana_cost = False
            elif index_deck[card] == "crusade":
                attack, harm = deck[card]
                health += harm
                mana_cost = False
            elif index_deck[card] == "life_heal" or index_deck[card] == "life_steal":
                if index_deck[card] == "life_heal" and mana < 3 or index_deck[card] == "life_steal" and mana < 4:
                    surface.blit(not_enough_mana, (30, 215))
                    pygame.display.update()
                    used_card_list.append(card)
                    deck_length += 1
                    mana_cost = True
                else:
                    attack, heal, new_mana, players_penetrate = deck[card]
                    mana -= new_mana
                    health += heal
                    mana_cost = False
            elif index_deck[card] == "battering_ram":
                enemy_armor = deck[card]
                mana_cost = False
            elif index_deck[card] == "invisibility" or index_deck[card] == "cloak" or index_deck[card] == "shadow":
                if index_deck[card] == "invisibility" and mana < 2:
                    surface.blit(not_enough_mana, (30, 215))
                    pygame.display.update()
                    used_card_list.append(card)
                    deck_length += 1
                    mana_cost = True
                else:
                    attack, players_invisibility, new_mana = deck[card]
                    mana -= new_mana
                    mana_cost = False
            elif index_deck[card] == "lightning_strike":
                if mana < 3:
                    surface.blit(not_enough_mana, (30, 215))
                    pygame.display.update()
                    used_card_list.append(card)
                    deck_length += 1
                    mana_cost = True
                else:
                    attack, players_skip, new_mana = deck[card]
                    mana -= new_mana
                    mana_cost = False
            elif index_deck[card] == "poison":
                if mana < 2:
                    surface.blit(not_enough_mana, (30, 215))
                    pygame.display.update()
                    used_card_list.append(card)
                    deck_length += 1
                    mana_cost = True
                else:
                    player_poison, players_penetrate, new_mana = deck[card]
                    mana -= new_mana
                    mana_cost = False

            # Cards that depend on damage taken
            if index_deck[card] == "reflect":
                if mana < 3:
                    surface.blit(not_enough_mana, (30, 215))
                    pygame.display.update()
                    used_card_list.append(card)
                    deck_length += 1
                    mana_cost = True
                else:
                    attack, new_mana = reflect(mana, damage)
                    mana -= new_mana
                    mana_cost = False
            elif index_deck[card] == "siege":
                attack, players_penetrate = siege(damage)
                mana_cost = False
            elif index_deck[card] == "revenge":
                attack = revenge(damage)
                mana_cost = False

        # Player skips the enemy's turn, forcing them to waste their card
        if players_skip == True:
            damage = 0
            enemy_armor -= enemy_armor_add
            opponents_invisibility = False
            opponents_poison_truth = False
            enemy_poison = 0

        # If the player is not invisibility, and its armor is not penetrated, then it takes a normal amount of damage
        if players_invisibility == False:
            if opponents_penetrate == False:
                if armor > 0:
                    if damage >= armor:
                        damage -= armor
                        armor = 0
                    elif damage < armor:
                        armor -= damage
                        damage = 0
        # If the player is invisible, it takes no damage
        else:
            damage = 0

        # If the enemy is not invisibility, and its armor is not penetrated, then it takes a normal amount of damage
        if opponents_invisibility == False:
            if players_penetrate == False:
                if enemy_armor > 0:
                    if attack >= enemy_armor:
                        attack -= enemy_armor
                        enemy_armor = 0
                    elif attack < enemy_armor:
                        enemy_armor -= attack
                        attack = 0
        # If the enemy is invisible, it takes no damage
        else:
            attack = 0

        # Calculates the enemy's remaining health
        enemy_health -= attack + player_poison

        # Ends the battle if the enemy's health is below zero
        if enemy_health <= 0:
            battle_gameplay = False

        # Calculates the player's remaining health
        health -= damage + enemy_poison

        # Player stats
        health_indicator = str(health)
        health_output = text(font80, health_indicator, Color.black)
        armor_indicator = str(armor)
        armor_output = text(font80, armor_indicator, Color.black)
        mana_indicator = str(mana)
        mana_output = text(font80, mana_indicator, Color.black)

        # Enemy stats
        enemy_health_indicator = str(enemy_health)
        enemy_health_output = text(font80, enemy_health_indicator, Color.black)
        enemy_armor_indicator = str(enemy_armor)
        enemy_armor_output = text(font80, enemy_armor_indicator, Color.black)

        # Displays stats on the screen after every round
        surface.blit(resized_background1, (340, 25))
        surface.blit(resized_background2, (1245, 25))
        surface.blit(health_output, (365, 30))
        surface.blit(armor_output, (345, 100))
        if character == "Wizard":
            surface.blit(resized_background1, (315, 155))
            surface.blit(mana_output, (325, 165))
        surface.blit(enemy_health_output, (1275, 30))
        surface.blit(enemy_armor_output, (1255, 100))
        surface.blit(enemy_battle_image, (550, 30))
        pygame.display.update()

        # If the player's health is below zero, then the battle ends
        if health <= 0:
            battle_gameplay = False

        # Runs if the player uses the poison card
        if players_poison_truth == True:
            player_poison -= 1
            if player_poison == 0:
                players_poison_truth = False

        # Runs if the enemy uses the poison card
        if opponents_poison_truth == True:
            enemy_poison -= 1
            if enemy_poison == 0:
                opponents_poison_truth = False

        # Creates a list of used player cards to prevent being able to use same card twice in a row
        used_card_list.append(card)
        if deck_length >= initial_length:
            used_card_list = []
            deck_length = 0
        deck_length += 1

        # Creates a list of used enemy cards to prevent being able to use same card twice in a row
        del enemy_index_deck[enemy_index_card]
        del enemy_deck[enemy_index_card]
        if enemy_deck_length >= 7:
            enemy_index_deck = list(initial_enemy_index_deck)
            enemy_deck = list(initial_enemy_deck)
            enemy_deck_length = 0
        else:
            enemy_deck_length += 1
    return health


# Initializes the truth statement for main while loop
play = True
choose = "None"

# Initializes Player Stats
player_health = 100
player_armor = 0
if model == "Wizard":
    player_mana = 10
else:
    player_mana = 0
player_damage = 0
opponent_mana = 1000
opponent_health = 20

# Defines cards for each class
wizard_cards = [sword(), spear(), shield(), axe(), bow_and_arrow(), crossbow(), punch(), club(), mace(), pitchfork(),
                fireball(player_mana), lightning_strike(player_mana), divine_intervention(player_mana),
                stone_skin(player_mana), invisibility(player_mana), life_heal(player_mana), life_steal(player_mana),
                reflect(player_mana, player_damage), protection(player_mana), poison(player_mana)]
wizard_index_cards = ["sword", "spear", "shield", "axe", "bow_and_arrow", "crossbow", "punch", "club", "mace",
                      "pitchfork", "fireball", "lightning_strike", "divine_intervention", "stone_skin", "invisibility",
                      "life_heal", "life_steal", "reflect", "protection", "poison"]
wizard_card_images = [resized_sword, resized_spear, resized_shield, resized_axe, resized_bow_and_arrow,
                      resized_crossbow, resized_punch, resized_club, resized_mace, resized_pitchfork, resized_fireball,
                      resized_lightning_strike, resized_divine_intervention, resized_stone_skin, resized_invisibility,
                      resized_life_heal, resized_life_steal, resized_reflect, resized_protection, resized_poison,
                      resized_empty]

knight_cards = [sword(), spear(), shield(), axe(), bow_and_arrow(), crossbow(), punch(), club(), mace(), pitchfork(),
                lance(), shield_bash(), crusade(), catapult(), hand_cannon(), siege(player_damage), volley(),
                battering_ram(), flail(), last_stand(player_health)]
knight_index_cards = ["sword", "spear", "shield", "axe", "bow_and_arrow", "crossbow", "punch", "club", "mace",
                      "pitchfork", "lance", "shield_bash", "crusade", "catapult", "hand_cannon", "siege", "volley",
                      "battering_ram", "flail", "last_stand"]
knight_card_images = [resized_sword, resized_spear, resized_shield, resized_axe, resized_bow_and_arrow,
                      resized_crossbow, resized_punch, resized_club, resized_mace, resized_pitchfork, resized_lance,
                      resized_shield_bash, resized_crusade, resized_catapult, resized_hand_cannon, resized_siege,
                      resized_volley, resized_battering_ram, resized_flail, resized_last_stand, resized_empty]

rogue_cards = [sword(), spear(), shield(), axe(), bow_and_arrow(), crossbow(), punch(), club(), mace(), pitchfork(),
               daggers(), cloak(), knockout(), assassinate(), revenge(player_damage), battle_axe(), shadow()]
rogue_index_cards = ["sword", "spear", "shield", "axe", "bow_and_arrow", "crossbow", "punch", "club", "mace",
                     "pitchfork", "daggers", "cloak", "knockout", "assassinate", "revenge", "battle_axe", "shadow"]
rogue_card_images = [resized_sword, resized_spear, resized_shield, resized_axe, resized_bow_and_arrow,
                     resized_crossbow, resized_punch, resized_club, resized_mace, resized_pitchfork, resized_daggers,
                     resized_cloak, resized_knockout, resized_assassinate, resized_revenge, resized_battle_axe,
                     resized_shadow, resized_empty]

enemy_cards = [sword(), spear(), shield(), axe(), bow_and_arrow(), crossbow(), punch(), club(), mace(), pitchfork(),
               fireball(opponent_mana), divine_intervention(opponent_mana), stone_skin(opponent_mana),
               invisibility(opponent_mana), life_heal(opponent_mana), life_steal(opponent_mana),
               protection(opponent_mana), poison(opponent_mana), lance(), shield_bash(), crusade(), catapult(),
               hand_cannon(), volley(), battering_ram(), flail(), last_stand(opponent_health), daggers(), cloak(),
               battle_axe(), shadow()]
enemy_index_cards = ["sword", "spear", "shield", "axe", "bow_and_arrow", "crossbow", "punch", "club", "mace",
                     "pitchfork", "fireball", "divine_intervention", "stone_skin", "invisibility", "life_heal",
                     "life_steal", "protection", "poison", "lance", "shield_bash", "crusade", "catapult",
                     "hand_cannon", "volley", "battering_ram", "flail", "last_stand", "daggers", "cloak",
                     "battle_axe", "shadow"]

# Picks the correct class for the player and creates their starting deck
if model == "Wizard":
    # Initializes the player's deck and index deck
    user = resized_wizard_Image
    players_deck = []
    players_index_deck = ["none", "none", "none", "none", "none", "none", "none", "none"]
    initial = 0
    # Generates the first 4 cards as general cards
    while initial < 4:
        dice = list(range(1, 11))
        value = random.choice(dice)
        players_index_deck[initial] = wizard_index_cards[value - 1]
        players_deck.append(wizard_cards[value - 1])
        initial += 1

    # Generates the fifth card as a wizard card
    dice = list(range(11, 21))
    value = random.choice(dice)
    players_index_deck[initial] = wizard_index_cards[value - 1]
    players_deck.append(wizard_cards[value - 1])
    chosen_deck = wizard_cards
    chosen_index = wizard_index_cards
    chosen_images = wizard_card_images
elif model == "Rogue":
    # Initializes the player's deck and index deck
    user = resized_rogue_Image
    players_deck = []
    players_index_deck = ["none", "none", "none", "none", "none", "none", "none", "none"]
    initial = 0
    # Generates the first 4 cards as general cards
    while initial < 4:
        dice = list(range(1, 11))
        value = random.choice(dice)
        players_index_deck[initial] = rogue_index_cards[value - 1]
        players_deck.append(rogue_cards[value - 1])
        initial += 1

    # Generates the fifth card as a rogue card
    dice = list(range(11, 18))
    value = random.choice(dice)
    players_index_deck[initial] = rogue_index_cards[value - 1]
    players_deck.append(rogue_cards[value - 1])
    chosen_deck = rogue_cards
    chosen_index = rogue_index_cards
    chosen_images = rogue_card_images
else:
    # Initializes the player's deck and index deck
    user = resized_knight_Image
    players_deck = []
    players_index_deck = ["none", "none", "none", "none", "none", "none", "none", "none"]
    initial = 0
    # Generates the first 4 cards as general cards
    while initial < 4:
        dice = list(range(1, 11))
        value = random.choice(dice)
        players_index_deck[initial] = knight_index_cards[value - 1]
        players_deck.append(knight_cards[value - 1])
        initial += 1

    # Generates the fifth card as a knight card
    dice = list(range(11, 21))
    value = random.choice(dice)
    players_index_deck[initial] = knight_index_cards[value - 1]
    players_deck.append(knight_cards[value - 1])
    chosen_deck = knight_cards
    chosen_index = knight_index_cards
    chosen_images = knight_card_images

# Initializes each list of enemies
enemies = ["goblin", "bandit", "serpent", "werewolf", "minotaur", "yeti"]
minibosses_north = ["entity", "wendigo"]
minibosses_west = ["ent", "spider"]
minibosses_south = ["siren", "hydra"]
bosses = ["demon", "vampire", "orc"]

# Creates the initial board game map
surface.blit(resized_map, (0, 0))
surface.blit(resized_one_Image, (40, 40))
surface.blit(user, (30, 724))
pygame.display.update()

# Index for Player Index in Gain Card Function
gc_index = 5

# Main Game
while play:
    # Initializes truth statements for while loops
    diceroll = True
    choice = True
    action = True

    # Action 1: Roll the die to determine where on the board you land
    while diceroll:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    board_die = [40, 110, 43, 110]
                    path_x = 0
                    path_y = 0
                    if pos[0] in range(board_die[0], board_die[1]) and pos[1] in range(board_die[2], board_die[3]):
                        # Rolls the dice and prints the die face on the board
                        roll = dice_roll(model)
                        face = [0, resized_one_Image, resized_two_Image, resized_three_Image, resized_four_Image,
                                resized_five_Image, resized_six_Image, resized_seven_Image]
                        # Calculates the total distance the player moves and places the model on that spot
                        total_move += roll
                        if total_move >= 40:
                            decision2 = True
                        if total_move <= 12:
                            total_move1 += roll
                            path_x = path1_coords[total_move1][0]
                            path_y = path1_coords[total_move1][1]
                        elif total_move > 12 and decision1 == False:
                            # Change to mouse input
                            while choice:
                                # Initializes areas for path choice buttons
                                north_area = [600, 900, 280, 330]
                                west_area = [600, 900, 395, 455]
                                south_area = [600, 900, 520, 580]
                                choice_area = [north_area, west_area, south_area]
                                choice_names = ["North", "West", "South"]

                                # Displays pop up asking for path choice
                                surface.blit(resized_path_choice, (500, 150))
                                pygame.display.update()

                                # Allows the player to select the path of their choice
                                for event in pygame.event.get():
                                    if event.type == MOUSEBUTTONDOWN:
                                        if pygame.mouse.get_pressed()[0]:
                                            pos = pygame.mouse.get_pos()
                                            index1 = 0
                                            for i in choice_area:
                                                index2 = 0
                                                path_choice = [0, 0, 0, 0]
                                                for h in i:
                                                    path_choice[index2] = choice_area[index1][index2]
                                                    index2 += 1
                                                if pos[0] in range(path_choice[0], path_choice[1]) \
                                                        and pos[1] in range(path_choice[2], path_choice[3]):
                                                    choose = choice_names[index1]
                                                index1 += 1
                                            # Initializes coordinates to correspond to the Northern Passage
                                            if choose == "North":
                                                total_move2 = total_move - 12
                                                total_move2a += total_move2
                                                path2_coords = path2a_coords
                                                path_x = path2_coords[total_move2][0]
                                                path_y = path2_coords[total_move2][1]
                                                decision1 = True
                                                choice = False
                                            # Initializes coordinates to correspond to the Westward Trail
                                            elif choose == "West":
                                                total_move2 = total_move - 12
                                                total_move2b += total_move2
                                                path2_coords = path2b_coords
                                                path_x = path2_coords[total_move2][0]
                                                path_y = path2_coords[total_move2][1]
                                                decision1 = True
                                                choice = False
                                            # Initializes coordinates to correspond to the Southern Pathway
                                            elif choose == "South":
                                                total_move2 = total_move - 12
                                                total_move2c += total_move2
                                                path2_coords = path2c_coords
                                                path_x = path2_coords[total_move2][0]
                                                path_y = path2_coords[total_move2][1]
                                                decision1 = True
                                                choice = False
                        # Chooses which path the character moves based on the player's choice
                        # Final initialization of all coordinates for the campaign map
                        elif 12 < total_move < 40 and decision2 == False:
                            total_move2 += roll
                            if choose == "North":
                                total_move2a += roll
                            elif choose == "West":
                                total_move2b += roll
                            elif choose == "South":
                                total_move2c += roll
                            path_x = path2_coords[total_move2][0]
                            path_y = path2_coords[total_move2][1]
                        elif 40 <= total_move < 52:
                            total_move3 = total_move - 39
                            path_x = path3_coords[total_move3][0]
                            path_y = path3_coords[total_move3][1]
                        elif total_move >= 52:
                            path_x = boss_coords[0]
                            path_y = boss_coords[1]
                        # Updates the screen to show where the player is on the board
                        surface.blit(resized_map, (0, 0))
                        surface.blit(face[roll], (40, 40))
                        surface.blit(user, (path_x, path_y))
                        pygame.display.update()
                        diceroll = False

    # Action 2: Implement the desired action that correspond to that board spot
    while action:
        # First determines the path that the player decides to go
        if choose == "North" or choose == "None":
            # Four types of actions
            # Action 1: Gain Health or Mana
            if total_move == 7 or total_move2a == 10 and total_move < 40 or total_move2a == 15 and total_move < 40 \
                    or total_move2a == 21 and total_move < 40 or total_move == 40 or total_move == 49:
                # Runs the gain health function
                player_health, player_mana = gain_health(model, player_health, player_mana)

                # Updates the screen back to the campaign map
                surface.blit(resized_map, (0, 0))
                surface.blit(face[roll], (40, 40))
                surface.blit(user, (path_x, path_y))
                pygame.display.update()
                action = False

            # Action 2: Gain a card
            elif total_move == 4 or total_move == 8 or total_move2a == 1 and total_move < 40 \
                    or total_move2a == 5 and total_move < 40 or total_move2a == 12 and total_move < 40 \
                    or total_move2a == 22 and total_move < 40:
                # Initializes the player's deck so that it can be outputted as images
                if model == "Knight":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = knight_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 20
                            battle_images.append(card_select)
                        deck_empty_index += 1
                elif model == "Wizard":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = wizard_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 20
                            battle_images.append(card_select)
                        deck_empty_index += 1
                elif model == "Rogue":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = rogue_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 17
                            battle_images.append(card_select)
                        deck_empty_index += 1

                surface.blit(resized_gain_card, (0, 0))
                pygame.display.update()
                # Player gains a card after winning the battle
                players_deck, players_index_deck, gc_index = gain_card(players_deck, players_index_deck, chosen_deck,
                                                                       chosen_index, chosen_images, battle_images,
                                                                       total_move, gc_index, model)

                # Updates the screen back to the campaign map
                surface.blit(resized_map, (0, 0))
                surface.blit(face[roll], (40, 40))
                surface.blit(user, (path_x, path_y))
                pygame.display.update()

                action = False

            # Action 3: Fight an enemy
            elif total_move == 3 or total_move == 5 or total_move == 9 or total_move == 11 \
                    or total_move2a == 3 and total_move < 40 or total_move2a == 6 and total_move < 40 \
                    or total_move2a == 7 and total_move < 40 or total_move2a == 9 and total_move < 40 \
                    or total_move2a == 13 and total_move < 40 or total_move2a == 14 and total_move < 40 \
                    or total_move2a == 16 and total_move < 40 or total_move2a == 17 and total_move < 40 \
                    or total_move2a == 19 and total_move < 40 or total_move2a == 24 and total_move < 40 \
                    or total_move2a == 26 and total_move < 40 or total_move == 41 or total_move == 44 \
                    or total_move == 46 or total_move == 47 or total_move == 50 or total_move >= 52:
                # Chooses the type of enemy based on where on the board the player is
                # Miniboss
                if total_move2a == 14 and total_move < 40:
                    enemy = random.choice(minibosses_north)
                # Boss
                if total_move >= 52:
                    enemy = random.choice(bosses)
                # Common Enemy
                else:
                    enemy = random.choice(enemies)

                # Initializes the corresponding enemy's deck
                opponent_index_deck, opponent_deck = enemy_deck_builder(enemy_cards, enemy_index_cards)

                # Initializes the player's deck so that it can be outputted as images
                if model == "Wizard":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = wizard_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 20
                            battle_images.append(card_select)
                        deck_empty_index += 1

                    # Outputs the player's cards onto the screen
                    surface.blit(resized_battle_map_mana, (0, 0))
                    surface.blit(wizard_card_images[battle_images[0]], (20, 500))
                    surface.blit(wizard_card_images[battle_images[1]], (195, 500))
                    surface.blit(wizard_card_images[battle_images[2]], (370, 500))
                    surface.blit(wizard_card_images[battle_images[3]], (545, 500))
                    surface.blit(wizard_card_images[battle_images[4]], (720, 500))
                    surface.blit(wizard_card_images[battle_images[5]], (895, 500))
                    surface.blit(wizard_card_images[battle_images[6]], (1070, 500))
                    surface.blit(wizard_card_images[battle_images[7]], (1245, 500))
                    pygame.display.update()
                elif model == "Knight":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = knight_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 20
                            battle_images.append(card_select)
                        deck_empty_index += 1

                    # Outputs the player's cards onto the screen
                    surface.blit(resized_battle_map, (0, 0))
                    surface.blit(knight_card_images[battle_images[0]], (20, 500))
                    surface.blit(knight_card_images[battle_images[1]], (195, 500))
                    surface.blit(knight_card_images[battle_images[2]], (370, 500))
                    surface.blit(knight_card_images[battle_images[3]], (545, 500))
                    surface.blit(knight_card_images[battle_images[4]], (720, 500))
                    surface.blit(knight_card_images[battle_images[5]], (895, 500))
                    surface.blit(knight_card_images[battle_images[6]], (1070, 500))
                    surface.blit(knight_card_images[battle_images[7]], (1245, 500))
                    pygame.display.update()
                elif model == "Rogue":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = rogue_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 17
                            battle_images.append(card_select)
                        deck_empty_index += 1

                    # Outputs the player's cards onto the screen
                    surface.blit(resized_battle_map, (0, 0))
                    surface.blit(rogue_card_images[battle_images[0]], (20, 500))
                    surface.blit(rogue_card_images[battle_images[1]], (195, 500))
                    surface.blit(rogue_card_images[battle_images[2]], (370, 500))
                    surface.blit(rogue_card_images[battle_images[3]], (545, 500))
                    surface.blit(rogue_card_images[battle_images[4]], (720, 500))
                    surface.blit(rogue_card_images[battle_images[5]], (895, 500))
                    surface.blit(rogue_card_images[battle_images[6]], (1070, 500))
                    surface.blit(rogue_card_images[battle_images[7]], (1245, 500))
                    pygame.display.update()

                # Runs the battle function
                player_health = battle(players_deck, players_index_deck, opponent_deck, opponent_index_deck,
                                       player_health, player_armor, player_mana, enemy, model)

                if player_health <= 0:
                    # Displays "You lost" screen
                    surface.blit(resized_lost, (0, 0))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    play = False
                elif player_health > 0:
                    # Displays "You won" screen after defeating the final boss
                    if total_move >= 52:
                        surface.blit(resized_won, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        play = False
                        break
                    surface.blit(resized_gain_card, (0, 0))
                    pygame.display.update()
                    # Player gains a card after winning the battle
                    players_deck, players_index_deck, gc_index = gain_card(players_deck, players_index_deck,
                                                                           chosen_deck, chosen_index,
                                                                           chosen_images, battle_images,
                                                                           total_move, gc_index, model)
                    # Updates the screen back to the campaign map
                    surface.blit(resized_map, (0, 0))
                    surface.blit(face[roll], (40, 40))
                    surface.blit(user, (path_x, path_y))
                    pygame.display.update()

                action = False

            # No Action
            else:
                action = False

        elif choose == "West" or choose == "None":
            # Action 1: Gain Health or Mana
            if total_move == 7 or total_move2b == 5 and total_move < 40 or total_move2b == 11 and total_move < 40 \
                    or total_move2b == 16 and total_move < 40 or total_move2b == 21 and total_move < 40\
                    or total_move2b == 25 and total_move < 40 or total_move == 40 or total_move == 49:
                # Runs the Gain Health/Mana function
                player_health, player_mana = gain_health(model, player_health, player_mana)

                # Updates the screen back to the campaign map
                surface.blit(resized_map, (0, 0))
                surface.blit(face[roll], (40, 40))
                surface.blit(user, (path_x, path_y))
                pygame.display.update()
                action = False

            # Action 2: Gain a card
            elif total_move == 4 or total_move == 8 or total_move2b == 4 and total_move < 40 \
                    or total_move2b == 13 and total_move < 40 or total_move2b == 18 and total_move < 40 \
                    or total_move2b == 24 and total_move < 40:
                # Initializes the player's deck so that it can be outputted as images
                if model == "Knight":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = knight_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 20
                            battle_images.append(card_select)
                        deck_empty_index += 1
                elif model == "Wizard":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = wizard_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 20
                            battle_images.append(card_select)
                        deck_empty_index += 1
                elif model == "Rogue":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = rogue_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 17
                            battle_images.append(card_select)
                        deck_empty_index += 1

                # Player gains a card
                surface.blit(resized_gain_card, (0, 0))
                pygame.display.update()
                players_deck, players_index_deck, gc_index = gain_card(players_deck, players_index_deck, chosen_deck,
                                                                       chosen_index, chosen_images, battle_images,
                                                                       total_move, gc_index, model)

                # Updates the screen back to the campaign map
                surface.blit(resized_map, (0, 0))
                surface.blit(face[roll], (40, 40))
                surface.blit(user, (path_x, path_y))
                pygame.display.update()

                action = False

            # Action 3: Fight an enemy
            elif total_move == 3 or total_move == 5 or total_move == 9 or total_move == 11 \
                    or total_move2b == 2 and total_move < 40 or total_move2b == 6 and total_move < 40 \
                    or total_move2b == 9 and total_move < 40 or total_move2b == 10 and total_move < 40 \
                    or total_move2b == 14 and total_move < 40 or total_move2b == 17 and total_move < 40 \
                    or total_move2b == 19 and total_move < 40 or total_move2b == 23 and total_move < 40 \
                    or total_move2b == 26 and total_move < 40 or total_move == 41 or total_move == 44 \
                    or total_move == 46 or total_move == 47 or total_move == 50 or total_move >= 52:

                # Chooses the type of enemy based on where on the board the player is
                # Miniboss
                if total_move2b == 14 and total_move < 40:
                    enemy = random.choice(minibosses_west)
                # Boss
                if total_move >= 52:
                    enemy = random.choice(bosses)
                # Common Enemy
                elif total_move2b != 14:
                    enemy = random.choice(enemies)

                # Initializes the corresponding enemy's deck
                opponent_index_deck, opponent_deck = enemy_deck_builder(enemy_cards, enemy_index_cards)

                # Initializes the player's deck so that it can be outputted as images
                if model == "Wizard":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = wizard_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 20
                            battle_images.append(card_select)
                        deck_empty_index += 1

                    # Outputs the player's cards onto the screen
                    surface.blit(resized_battle_map_mana, (0, 0))
                    surface.blit(wizard_card_images[battle_images[0]], (20, 500))
                    surface.blit(wizard_card_images[battle_images[1]], (195, 500))
                    surface.blit(wizard_card_images[battle_images[2]], (370, 500))
                    surface.blit(wizard_card_images[battle_images[3]], (545, 500))
                    surface.blit(wizard_card_images[battle_images[4]], (720, 500))
                    surface.blit(wizard_card_images[battle_images[5]], (895, 500))
                    surface.blit(wizard_card_images[battle_images[6]], (1070, 500))
                    surface.blit(wizard_card_images[battle_images[7]], (1245, 500))
                    pygame.display.update()
                elif model == "Knight":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = knight_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 20
                            battle_images.append(card_select)
                        deck_empty_index += 1

                    # Outputs the player's cards onto the screen
                    surface.blit(resized_battle_map, (0, 0))
                    surface.blit(knight_card_images[battle_images[0]], (20, 500))
                    surface.blit(knight_card_images[battle_images[1]], (195, 500))
                    surface.blit(knight_card_images[battle_images[2]], (370, 500))
                    surface.blit(knight_card_images[battle_images[3]], (545, 500))
                    surface.blit(knight_card_images[battle_images[4]], (720, 500))
                    surface.blit(knight_card_images[battle_images[5]], (895, 500))
                    surface.blit(knight_card_images[battle_images[6]], (1070, 500))
                    surface.blit(knight_card_images[battle_images[7]], (1245, 500))
                    pygame.display.update()
                elif model == "Rogue":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = rogue_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 17
                            battle_images.append(card_select)
                        deck_empty_index += 1

                    # Outputs the player's cards onto the screen
                    surface.blit(resized_battle_map, (0, 0))
                    surface.blit(rogue_card_images[battle_images[0]], (20, 500))
                    surface.blit(rogue_card_images[battle_images[1]], (195, 500))
                    surface.blit(rogue_card_images[battle_images[2]], (370, 500))
                    surface.blit(rogue_card_images[battle_images[3]], (545, 500))
                    surface.blit(rogue_card_images[battle_images[4]], (720, 500))
                    surface.blit(rogue_card_images[battle_images[5]], (895, 500))
                    surface.blit(rogue_card_images[battle_images[6]], (1070, 500))
                    surface.blit(rogue_card_images[battle_images[7]], (1245, 500))
                    pygame.display.update()

                # Runs the battle function
                player_health = battle(players_deck, players_index_deck, opponent_deck, opponent_index_deck,
                                       player_health, player_armor, player_mana, enemy, model)

                if player_health <= 0:
                    # Displays "You lost" screen
                    surface.blit(resized_lost, (0, 0))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    play = False
                elif player_health > 0:
                    # Displays "You won" screen after defeating the final boss
                    if total_move >= 52:
                        surface.blit(resized_won, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        play = False
                        break
                    surface.blit(resized_gain_card, (0, 0))
                    pygame.display.update()
                    # Player gains a card after winning the battle
                    players_deck, players_index_deck, gc_index = gain_card(players_deck, players_index_deck,
                                                                           chosen_deck, chosen_index,
                                                                           chosen_images, battle_images,
                                                                           total_move, gc_index, model)
                    # Updates the screen back to the campaign map
                    surface.blit(resized_map, (0, 0))
                    surface.blit(face[roll], (40, 40))
                    surface.blit(user, (path_x, path_y))
                    pygame.display.update()

                action = False

            # No Action
            else:
                action = False

        elif choose == "South" or choose == "None":
            # Action 1: Gain Health or Mana
            if total_move == 7 or total_move2c == 6 and total_move < 40 or total_move2c == 18 and total_move < 40 \
                    or total_move == 40 or total_move == 49:
                # Runs Gain Health/Mana function
                player_health, player_mana = gain_health(model, player_health, player_mana)

                # Updates the screen back to the campaign map
                surface.blit(resized_map, (0, 0))
                surface.blit(face[roll], (40, 40))
                surface.blit(user, (path_x, path_y))
                pygame.display.update()
                action = False

            # Action 2: Gain a card
            elif total_move == 4 or total_move == 8 or total_move2c == 2 and total_move < 40 \
                    or total_move2c == 9 and total_move < 40 or total_move2c == 13 and total_move < 40\
                    or total_move2c == 20 and total_move < 40 or total_move2c == 24 and total_move < 40 \
                    or total_move2c == 27 and total_move < 40:
                # Creates a list with the images that correspond to the player's cards
                if model == "Knight":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = knight_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 20
                            battle_images.append(card_select)
                        deck_empty_index += 1
                elif model == "Wizard":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = wizard_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 20
                            battle_images.append(card_select)
                        deck_empty_index += 1
                elif model == "Rogue":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = rogue_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 17
                            battle_images.append(card_select)
                        deck_empty_index += 1

                # Runs the Gain Card function
                surface.blit(resized_gain_card, (0, 0))
                pygame.display.update()
                players_deck, players_index_deck, gc_index = gain_card(players_deck, players_index_deck, chosen_deck,
                                                                       chosen_index, chosen_images, battle_images,
                                                                       total_move, gc_index, model)

                # Updates the screen back to the campaign map
                surface.blit(resized_map, (0, 0))
                surface.blit(face[roll], (40, 40))
                surface.blit(user, (path_x, path_y))
                pygame.display.update()

                action = False

            # Action 3: Fight an enemy
            elif total_move == 3 or total_move == 5 or total_move == 9 or total_move == 11 \
                    or total_move2c == 1 and total_move < 40 or total_move2c == 4 and total_move < 40 \
                    or total_move2c == 7 and total_move < 40 or total_move2c == 11 and total_move < 40 \
                    or total_move2c == 14 and total_move < 40 or total_move2c == 16 and total_move < 40 \
                    or total_move2c == 19 and total_move < 40 or total_move2c == 23 and total_move < 40 \
                    or total_move2c == 24 and total_move < 40 or total_move2c == 25 and total_move < 40 \
                    or total_move == 41 or total_move == 44 or total_move == 46 or total_move == 47 \
                    or total_move == 50 or total_move >= 52:
                # Chooses the type of enemy based on where on the board the player is
                # Miniboss
                if total_move2c == 14 and total_move < 40:
                    enemy = random.choice(minibosses_north)
                # Boss
                if total_move >= 52:
                    enemy = random.choice(bosses)
                # Common Enemy
                else:
                    enemy = random.choice(enemies)

                # Initializes the corresponding enemy's deck
                opponent_index_deck, opponent_deck = enemy_deck_builder(enemy_cards, enemy_index_cards)

                # Initializes the player's deck so that it can be outputted as images
                if model == "Wizard":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = wizard_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 20
                            battle_images.append(card_select)
                        deck_empty_index += 1

                    # Outputs the player's cards onto the screen
                    surface.blit(resized_battle_map_mana, (0, 0))
                    surface.blit(wizard_card_images[battle_images[0]], (20, 500))
                    surface.blit(wizard_card_images[battle_images[1]], (195, 500))
                    surface.blit(wizard_card_images[battle_images[2]], (370, 500))
                    surface.blit(wizard_card_images[battle_images[3]], (545, 500))
                    surface.blit(wizard_card_images[battle_images[4]], (720, 500))
                    surface.blit(wizard_card_images[battle_images[5]], (895, 500))
                    surface.blit(wizard_card_images[battle_images[6]], (1070, 500))
                    surface.blit(wizard_card_images[battle_images[7]], (1245, 500))
                    pygame.display.update()
                elif model == "Knight":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = knight_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 20
                            battle_images.append(card_select)
                        deck_empty_index += 1

                    # Outputs the player's cards onto the screen
                    surface.blit(resized_battle_map, (0, 0))
                    surface.blit(knight_card_images[battle_images[0]], (20, 500))
                    surface.blit(knight_card_images[battle_images[1]], (195, 500))
                    surface.blit(knight_card_images[battle_images[2]], (370, 500))
                    surface.blit(knight_card_images[battle_images[3]], (545, 500))
                    surface.blit(knight_card_images[battle_images[4]], (720, 500))
                    surface.blit(knight_card_images[battle_images[5]], (895, 500))
                    surface.blit(knight_card_images[battle_images[6]], (1070, 500))
                    surface.blit(knight_card_images[battle_images[7]], (1245, 500))
                    pygame.display.update()
                elif model == "Rogue":
                    deck_index = 0
                    battle_images = []
                    # Displays the correct card based on the function it calls
                    while deck_index < len(players_deck):
                        card_select = rogue_index_cards.index(players_index_deck[deck_index])
                        battle_images.append(card_select)
                        deck_index += 1
                    deck_empty_index = len(players_deck)
                    # Displays an empty card if there are no functions present
                    while deck_empty_index < 8:
                        if players_index_deck[deck_empty_index] == "none":
                            card_select = 17
                            battle_images.append(card_select)
                        deck_empty_index += 1

                    # Outputs the player's cards onto the screen
                    surface.blit(resized_battle_map, (0, 0))
                    surface.blit(rogue_card_images[battle_images[0]], (20, 500))
                    surface.blit(rogue_card_images[battle_images[1]], (195, 500))
                    surface.blit(rogue_card_images[battle_images[2]], (370, 500))
                    surface.blit(rogue_card_images[battle_images[3]], (545, 500))
                    surface.blit(rogue_card_images[battle_images[4]], (720, 500))
                    surface.blit(rogue_card_images[battle_images[5]], (895, 500))
                    surface.blit(rogue_card_images[battle_images[6]], (1070, 500))
                    surface.blit(rogue_card_images[battle_images[7]], (1245, 500))
                    pygame.display.update()

                # Runs the battle function
                player_health = battle(players_deck, players_index_deck, opponent_deck, opponent_index_deck,
                                       player_health, player_armor, player_mana, enemy, model)

                if player_health <= 0:
                    # Displays "You lost" screen
                    surface.blit(resized_lost, (0, 0))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    play = False
                elif player_health > 0:
                    # Displays "You won" screen after defeating the final boss
                    if total_move >= 52:
                        surface.blit(resized_won, (0, 0))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        play = False
                        break
                    # Player gains a card if they win the battle
                    surface.blit(resized_gain_card, (0, 0))
                    pygame.display.update()
                    players_deck, players_index_deck, gc_index = gain_card(players_deck, players_index_deck,
                                                                           chosen_deck, chosen_index,
                                                                           chosen_images, battle_images,
                                                                           total_move, gc_index, model)
                    # Updates the screen back to the campaign map
                    surface.blit(resized_map, (0, 0))
                    surface.blit(face[roll], (40, 40))
                    surface.blit(user, (path_x, path_y))
                    pygame.display.update()
                action = False

            # No Action
            else:
                action = False
