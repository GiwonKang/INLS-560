# https://goheels.com/sports/men-basketball/roster
import pandas as pd

roster = ["Bacot", "Davis", "Cadeau"]
player = {"Last Name": roster,
          "First Name": ["Armando", "RJ", "Elliot"],
          "height": [83, 72, 73],
          "weight": [240, 180, 180]}
data = pd.DataFrame(player)
print(data)