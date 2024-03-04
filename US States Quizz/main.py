import turtle
import pandas
import text

screen = turtle.Screen()
screen.setup(725,491)
screen.title("US States Quizz")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

score = 0

date = pandas.read_csv("50_states.csv")
states = date["state"].to_list()
dict = date.to_dict()

answers_list = []
name_list = []

while score != 50:
    answer = screen.textinput(f"{score} / 50 Guess the State", "What is another state's name?")
    answer = answer.title()

    if answer in states and answer not in answers_list:
        x = dict["x"][states.index(answer)]
        y = dict["y"][states.index(answer)]
        answers_list.append(text.Text(answer, x, y))
        answers_list.append(answer)
        score += 1


text.Text("You won!", 0, 0, 20)
screen.exitonclick()
