import random
import string
import tkinter as tk
import time
from tkinter import messagebox, simpledialog

import pygame
from PyDictionary import PyDictionary

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

clock = pygame.time.Clock()

isActive = True
isGameOver = False

start_screen = pygame.image.load('images/start_slide.png')
start_screen = pygame.transform.scale(start_screen, (screen_width,screen_height))

item_discribe = pygame.image.load('images/item_discribe.png')
item_discribe = pygame.transform.scale(item_discribe, (screen_width, screen_height))

game_discribe = pygame.image.load('images/001.png')
game_discribe = pygame.transform.scale(game_discribe, (screen_width, screen_height))

num_players = pygame.image.load('images/002.png')
num_players = pygame.transform.scale(num_players, (screen_width, screen_height))

name_players = pygame.image.load('images/003.png')
name_players = pygame.transform.scale(name_players, (screen_width, screen_height))

num_games = pygame.image.load('images/004.png')
num_games = pygame.transform.scale(num_games, (screen_width, screen_height))

what_alphabet = pygame.image.load('images/005.png')
what_alphabet = pygame.transform.scale(what_alphabet, (screen_width, screen_height))

who_win = pygame.image.load('images/006.png')
who_win = pygame.transform.scale(who_win, (screen_width, screen_height))

get_score = pygame.image.load('images/007.png')
get_score = pygame.transform.scale(get_score, (screen_width, screen_height))

item1 = pygame.image.load('images/008.png')
item1 = pygame.transform.scale(item1, (screen_width, screen_height))

item2 = pygame.image.load('images/009.png')
item2 = pygame.transform.scale(item2, (screen_width, screen_height))

item3 = pygame.image.load('images/010.png')
item3 = pygame.transform.scale(item3, (screen_width, screen_height))

fn = pygame.image.load('images/011.png')
fn = pygame.transform.scale(fn, (screen_width, screen_height))

results = pygame.image.load('images/012.png')
results = pygame.transform.scale(results, (screen_width, screen_height))

yes_button = pygame.image.load('images/yesbutton.png')
yes_button = pygame.transform.scale(yes_button, (100, 100))

no_button = pygame.image.load('images/nobutton.png')
no_button = pygame.transform.scale(no_button, (100, 100))
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
    list_player.sort(key = lambda x: x.score, reverse = True)
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
    global done, start_screen, item_discribe, num_players,name_players, num_games, what_alphabet, who_win, get_score, item1, item2, item3, fn, results, winner
    arr = [start_screen, item_discribe, game_discribe, num_players, 
    name_players, num_games, what_alphabet, who_win, get_score, item1,
    item2, item3, fn, results]
    player_list = []
    name_set = set()
    x = 0
    y = 0
    level = 1
    turns = 0
    winner = 0
    button_w=63
    button_h=30
    screen.blit(start_screen, (x,y))
    pygame.display.update()


    while not isGameOver:
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
                player_list.append(new_p)
                print(player_list[i].name)
                name_set.add(names)

            screen_change(arr, level)
            level += 1

        if level == 6:
            turns = simpledialog.askinteger(title="KUCC GAME JAM",
                                    prompt="게임 턴 수를 입력하세요: ")
            turns = int(turns)
            screen_change(arr, level)
            level += 1
        
        for i in range(turns):
            if level == 7:
                print(i, turns)
                what_alphabet = pygame.image.load('images/005.png')
                what_alphabet = pygame.transform.scale(what_alphabet, (screen_width, screen_height))

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
                
                alphacheck = False
                correct = False
                while alphacheck == False or correct==False:
                    alphacheck = False
                    correct = False
                    answer = simpledialog.askstring(title="KUCC GAME JAM", prompt="답: ")
                    alphacheck = letterCheck(answer,randomList) 
                    correct = dictCheck(dictionary.meaning(answer, disable_errors=True))

                screen_change(arr, level)
                level +=1  

            if level == 8:
                plname = simpledialog.askstring(title="KUCC GAME JAM", prompt="맞춘 사람: ")
                if plname in name_set:
                    for j in range(len(player_list)):
                        if(player_list[j].name==plname):
                            winner=j
                            break
                    get = random.randint(-50,53)
                    if get <= 50:
                        player_list[winner].score_get(get)
                        messagebox.showinfo(title = "KUCC GAME JAM", message = f"{get}점을 획득합니다!")
                        level = 7
                        if i == turns-1:
                            level = 12
                        continue
                    elif get == 51:
                        level = 9
                    elif get == 52:
                        level = 10
                    elif get == 53:
                        level = 11
                else:
                    print('he is not a player!')
            
            if level==9:
                screen_change(arr, level)
                player_list[winner].item1()
                level=7
                continue

            if level==10:
                screen_change(arr, level)
                player_list[winner].item2()
                level=7
                continue
            
            if level==11:
                screen_change(arr, level)
                screen.blit(yes_button, (300, 500))
                screen.blit(no_button, (500, 500))
                pygame.display.update()
                click = pygame.mouse.get_pressed()
                mouse = pygame.mouse.get_pos()
                if click[0] and 300 + button_w>=mouse[0]>= 300 and 500 + button_h>=mouse[1]>=500:
                    level = 7
                    target = player_list[winner].item3()
                    result = target.name+" 플레이어와 점수를 교환합니다.\n"
                    result += player_list[winner].name+": "+str(player_list[winner].score)+"점\n"
                    result += target.name+": "+str(target.score)+"점\n"
                    messagebox.showinfo("KUCC GAME JAM", result)
                    continue
                elif click[0] and 500+button_w>=mouse[0]>=500 and 500 + button_h>= mouse[1]>=500:
                    level = 7
                    continue
                else:
                    i -= 1
                    continue
    
            if level==12:
                screen_change(arr, level)
                time.sleep(1)
                sort_player(player_list)
                result = ""
                for i in range(len(player_list)):
                    result += str(i+1)+"등: "+player_list[i].name+"("+str(player_list[i].score)+"점)\n"
                    if i > 2:
                        break
                messagebox.showinfo(title = "Congratulation!", message = result)
                break

        if level > 20: 
            break


runGame()
pygame.quit()
