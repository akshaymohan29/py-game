from turtle import  Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=1
        self.hideturtle()
        self.color("blue")
        self.goto(-250,250)
        self.score_hed()
    def score_hed(self):
        self.clear()
        self.write(f"Score: {self.score}",font=("times",24,"bold"))

    def increase_scor(self):
        self.score+=1
        self.score_hed()


    def game_over(self):
        self.goto(-60,0)
        self.write("GAMEOVER", font=("times", 24, "bold"))