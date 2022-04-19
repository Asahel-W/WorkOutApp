from datetime import date

today = date.today()


class Controller:
    def __init__(self):
        print("Controller !")

    def new_weight(self, weight, current_date=today.strftime("%d/%m/%Y")):
        print("The new weight", weight, "was added on", current_date)
