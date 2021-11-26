# 0 = keo
# 1 = la
# 2 = bua


from random import randint
print("---------")
print("choose ( bua, keo, la )")

player = input()
bot = randint(0,2)

if bot == 0:
    bot = "keo"
if bot == 1:
    bot = "la"
if bot == 2:
    bot = "bua"

print("---------")
print("your choice: "+ player)
print("bot choice: "+ bot)
print("---------")


if player == bot:
    print("draw")
else:
    if player == "keo":
        if bot == "la":
            print("win")
        else:
            print("lose")  

    elif player == "la":
        if bot == "keo":
            print("lose")
        else:
            print("win") 

    elif player == "bua":
        if bot == "keo":
            print("win")
        else:
            print("lose")
    else:
        print("wrong input!")
