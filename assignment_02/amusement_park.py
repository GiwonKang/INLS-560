# This lesson covers that order matters when using elif in some situation.
age = 101

if age < 4:
    print("Admission is $0.")

elif age < 18:    
    print("Admission is $25.")

elif age > 100:
    print("Admission is $0 and you get a free beer!")

elif age > 60:    
    print("Admission is $35.")

# This is not oging to work here. Put before age 60.(sixty)
#elif age > 100:
#    print("Admission is $0 and you get a free beer!")

else:
    print("Admission cost is $40.")