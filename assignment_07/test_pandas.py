import pandas as pd

player = {"Last Name": ["Bacot", "Davis", "Cadeau"],
          "First Name": ["Armando", "RJ", "Elliot"],
          "height": [83,72,73],
          "weight": [240,180,180]
          }
data = pd.DataFrame(player)

# bmi = weight in kg/ height in meters squared
data["bmi"] = (data["weight"]/2.205)/((data["height"]/39.37)**2)

print(data)

data.to_csv("bmi.csv")