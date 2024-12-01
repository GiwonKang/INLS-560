import pandas as pd

# test 2
player = {"Last Name": ["Bacot", "Davis", "Cadeau", "Martinez", "Johnson", "Kim", "Patel", "Carter", "Smith", "Rivera"],
          "First Name": ["Armando", "RJ", "Elliot", "Sofia", "Lian", "Minji", "Aarav", "Olivia", "Ethan", "Isabella"],
          "height": [83,72,73, 53, 58, 50, 56, 54, 60, 52],
          "weight": [240,180,180, 127, 158, 119, 149, 143, 176, 130]
          }
data = pd.DataFrame(player)

# bmi = weight in kg/ height in meters squared
data["bmi"] = (data["weight"]/2.205)/((data["height"]/39.37)**2)

# Round BMI to 2 decimal places
data["bmi"] = data["bmi"].round(2)

print(data)

data.to_csv("bmi.csv")