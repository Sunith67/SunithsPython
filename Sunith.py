import pyttsx3
import pygame
import time
import random
from tkinter import *


def CalCu_lator():

    engine.say("OK, so you have choosen Calculator ")
    engine.say("A screen of Calculator will pop up")
    engine.runAndWait()

    def iCalc(source, side):
        storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
        storeObj.pack(side=side, expand=YES, fill=BOTH)
        return storeObj

    def button(source, side, text, command=None):
        storeObj = Button(source, text=text, command=command)
        storeObj.pack(side=side, expand=YES, fill=BOTH)
        return storeObj

    class app(Frame):
        def __init__(self):
            Frame.__init__(self)
            self.option_add('*Font', 'arial 20 bold')
            self.pack(expand=YES, fill=BOTH)
            self.master.title('Calculator')

            display = StringVar()
            Entry(self, relief=RIDGE, textvariable=display,
                  justify='right'
                  , bd=30, bg="powder blue").pack(side=TOP,
                                                  expand=YES, fill=BOTH)

            for clearButton in (["C"]):
                erase = iCalc(self, TOP)
                for ichar in clearButton:
                    button(erase, LEFT, ichar, lambda
                        storeObj=display, q=ichar: storeObj.set(''))

            for numButton in ("789/", "456*", "123-", "0.+"):
                FunctionNum = iCalc(self, TOP)
                for iEquals in numButton:
                    button(FunctionNum, LEFT, iEquals, lambda
                        storeObj=display, q=iEquals: storeObj
                           .set(storeObj.get() + q))

            EqualButton = iCalc(self, TOP)
            for iEquals in "=":
                if iEquals == '=':
                    btniEquals = button(EqualButton, LEFT, iEquals)
                    btniEquals.bind('<ButtonRelease-1>', lambda e, s=self,
                                                                storeObj=display: s.calc(storeObj), '+')


                else:
                    btniEquals = button(EqualButton, LEFT, iEquals,
                                        lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
                                        (storeObj.get() + s))

        def calc(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("ERROR")

    if __name__ == '__main__':
        app().mainloop()

def Guessss():
    engine.say("OK so you have choosen to play Guessing game")
    engine.say("Guess the correct number and win the Game")
    engine.runAndWait()

    number = random.randint(1, 10)

    player_name = input("Hello, What's your name?")
    number_of_guesses = 0
    print('okay! ' + player_name + ' I am Guessing a number between 1 and 10:')

    while number_of_guesses < 5:
        guess = int(input())
        number_of_guesses += 1
        if guess < number:
            print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
        if guess == number:
            break
    if guess == number:
        print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
    else:
        print('You did not guess the number, The number was ' + str(number))


def Snake_Game():
    engine.say("ok so you have choosen to play Snake game")
    engine.say("All the best.Try to win the game")
    engine.say("start by pressing any arrow")
    engine.runAndWait()
    pygame.init()

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    dis_width = 600
    dis_height = 400

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game by Sunith')

    clock = pygame.time.Clock()

    snake_block = 10
    snake_speed = 15

    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])

    def gameLoop():
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1

        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close == True:
                dis.fill(blue)
                message("You Lost! Press C-Play Again or Q-Quit", red)

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()

    gameLoop()

def Digi_clock():
    engine.say("A screen will pop up showing the time")
    engine.runAndWait()
    app_window = Tk()
    app_window.title("Digital Clock")
    app_window.geometry("420x150")
    app_window.resizable(1, 1)

    text_font = ("Boulder", 68, 'bold')
    background = "#f2e750"
    foreground = "#363529"
    border_width = 25

    label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
    label.grid(row=0, column=1)

    def digital_clock():
        time_live = time.strftime("%H:%M:%S")
        label.config(text=time_live)
        label.after(200, digital_clock)

    digital_clock()
    app_window.mainloop()


engine = pyttsx3.init()

engine.say("Hello there Stranger, I Don't know who you are  So please tell Me Your Name")
engine.runAndWait()

print("Enter Your Name")
MyName = input(">")

engine.say("Hello Buddy,Welcome to Sunith's Lab")
engine.runAndWait()

engine.say("Now a List will be shown Where you have to choose the task you want to do")
engine.say("Enter the Alphabet That shown in the List for preceding further")
engine.runAndWait()

print("What do you want to do \n Write a,b,c,d")
print("a)Open Calculator")
print("b)Play a Guessing Game")
print("c)Play Snake Game")
print("d)Open digital clock")
Stranger_Choose = str(input(">"))

if Stranger_Choose == "a":
    CalCu_lator()
elif Stranger_Choose =="b":
    Guessss()
elif Stranger_Choose == "c":
    Snake_Game()
elif Stranger_Choose == "d":
    Digi_clock()
else:
    print("wrong input")

