import random
import tkinter as tk
from tkinter import simpledialog
from PyDictionary import PyDictionary
import random
import string
import pygame

ROOT = tk.Tk()
ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="KUCC GAME JAM",
                                  prompt="팀명을 입력하세요: ")

# check it out
print("Hello", USER_INP)
################################################
####### 1) variable
score = 0
dictionary=PyDictionary()

screen_width = 900
screen_height = 900

WHITE = (255,255,255)
BLACK = (0,0,0)

done = False
clock = pygame.time.Clock()

isActive = True
isGameOver = False

start_screen = pygame.image.load('images/start_slide.png')
start_screen = pygame.transform.scale(start_screen, (900,900))

item_discribe = pygame.image.load('images/item_discribe.png')
item_discribe = pygame.transform.scale(item_discribe, (900, 900))

game_discribe = pygame.image.load('images/001.png')
game_discribe = pygame.transform.scale(game_discribe, (900, 900))

num_players = pygame.image.load('images/002.png')
num_players = pygame.transform.scale(num_players, (900, 900))

name_players = pygame.image.load('images/003.png')
name_players = pygame.transform.scale(name_players, (900, 900))

num_games = pygame.image.load('images/004.png')
num_games = pygame.transform.scale(num_games, (900, 900))

what_alphabet = pygame.image.load('images/005.png')
what_alphabet = pygame.transform.scale(what_alphabet, (900, 900))

who_win = pygame.image.load('images/006.png')
who_win = pygame.transform.scale(who_win, (900, 900))

get_score = pygame.image.load('images/007.png')
get_score = pygame.transform.scale(get_score, (900, 900))


################################################
####### 2) screen
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("mario in english lecture!")
################################################
####### 3) player
class player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def score_change(self, newscore):
        self.score = newscore
    
    def score_get(self, get):
        self.score += get
    
    def return_score(self):
        return self.score

    def item1(self):
        self.score_change(0)
    
    def item2(self, list_player):
        target=random.choice(list_player)
        target.score_get(-10)
        self.score_get(10)

    def item3(self, list_player):
        target=random.choice(list_player)
        t_score=target.return_score()
        m_score=self.return_score()
        self.score_change(t_score)
        target.score_change(m_score)




###############################################
def get_name(x):
    
    if x < 2 :
        print("bring more your friends!")
    elif x >= 2 :
        for idx in range(x):
            name = simpledialog.askstring(title="KUCC GAME JAM",
                                    prompt="이름을 입력하세요: ")

    return x
###############################################
def sort_player(list_player):
    list_player.sort(key=lambda x: x.return_score, reversed=True)
###############################################
def screen_change(arr, level):
    screen.blit(arr[level], (0,0))
    pygame.display.update()
################################################
def letterCheck(answer, randomList):
   for letter in answer:
        if letter not in randomList: 
            return False
        return True
###############################################
def dictCheck(dictin):
    if isinstance(dictin, dict): 
        print(dictin)
        return True
    else: 
        return False
################################################
def runGame():
    global done, start_screen, item_discribe, num_players
    arr = [start_screen, item_discribe, game_discribe, num_players, 
    name_players, num_games, what_alphabet, who_win, get_score]
    list_player = []
    x = 0
    y = 0
    level = 1
    turns = 0
    screen.blit(start_screen, (x,y))
    pygame.display.update()

    

    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        event=pygame.event.poll()

        if event.type==pygame.quit:
            break
        elif event.type==pygame.MOUSEBUTTONDOWN:
            screen_change(arr, level)
            level += 1

        if level == 4:
            num = simpledialog.askstring(title="KUCC GAME JAM",
                                prompt="플레이어 수를 입력하세요: ")
            screen_change(arr, level)
            level += 1
            
        if level == 5:
            for i in range(int(num)):
                names = simpledialog.askstring(title="KUCC GAME JAM",
                                    prompt="이름을 입력하세요: ")
                new_p = player(names)
                list_player.append(new_p)
                print(list_player[i].name)
            screen_change(arr, level)
            level += 1

        if level == 6:
            turns = simpledialog.askinteger(title="KUCC GAME JAM",
                                    prompt="게임 턴 수를 입력하세요: ")
            screen_change(arr, level)
            level += 1
            
        if level == 7:
            
            randomList = random.sample(string.ascii_lowercase, k=10)
            print(randomList)

            sprite = pygame.sprite.Sprite()
            sprite.image = what_alphabet
            sprite.rect = what_alphabet.get_rect()

            font = pygame.font.SysFont('arial.ttf', 50)
            text = font.render(','.join(randomList), True, BLACK)

            sprite.image.blit(text, (450,450))

            group = pygame.sprite.Group()
            group.add(sprite)
            group.draw(screen)

            pygame.display.flip()
            
            alphacheck=False
            correct=False
            while alphacheck == False or correct==False:
                alphacheck=False
                correct=False
                answer = simpledialog.askstring(title="KUCC GAME JAM", prompt="답: ")
                alphacheck = letterCheck(answer,randomList) 
                correct = dictCheck(dictionary.meaning(answer, disable_errors=True))

            screen_change(arr, level)
            level +=1                           
            
        if level == 8:
            winner = input('')
            for i in range(int(num)):
                if winner == list_player[i].name:
                    break
                else:
                    print('he is not a player!')
        if level>20: 
            break


runGame()
pygame.quit()
