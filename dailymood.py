
name = input("Enter Your Name: ")
mood = input("How do you feel? happy/sad/stressed/mad:")
energy = int(input("Rate your energy from 1 to 10: "))

if energy <=4: 
    print("Sorry your feeling this way")

elif energy >=5:
    print("You are having a good day") 

else: 
    print("Do something you enjoy")

    if mood == "happy": 
        advice == "Your doing great"
    elif mood == "sad":
        advice == "Don't worry, it'll get better"
    elif mood == "stressed":
        advice == "Do something to unwind"
    elif mood == "mad":
        advice == "Do something to cool down"
    else: 
        advice == "Do what makes you feel best"

        import datetime 
        today = datetime.datetime.now()
