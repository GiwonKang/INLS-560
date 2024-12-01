# https://goheels.com/sports/men-basketball/roster
import pandas as pd

roster = ["Bacot", "Davis", "Cadeau"]
player = {"Last Name": roster}
data = pd.DataFrame(player)
print(data)