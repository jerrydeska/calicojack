import random
import time

print("===CalicoJack===\n")

dealer_num = []
player_num = []
stand = False

dealer_num.append(random.randint(1, 10))
player_num.append(random.randint(1, 10))

while not stand:
    print("==============")
    print("Dealer Number: ", end="")
    print(*dealer_num)
    print("Total: " + str(sum(dealer_num)) + "\n")

    player_num.append(random.randint(1, 10))
    print("Your Number: ", end="")
    print(*player_num)
    print("Total: " + str(sum(player_num)) + "\n")

    if sum(player_num) == 21:
        print("You Won!")
        exit()
    elif sum(player_num) < 21:
        decision = input("1. Hit\n2. Stand\nChoice: ")
        if decision == "2":
            stand = True
    else:
        print("You Lost!")
        exit()

while sum(dealer_num) <= sum(player_num):
    dealer_num.append(random.randint(1, 10))
    time.sleep(3)
    print("==============")
    print("Dealer Number: ", end="")
    print(*dealer_num)
    print("Total: " + str(sum(dealer_num)) + "\n")

    print("Your Number: ", end="")
    print(*player_num)
    print("Total: " + str(sum(player_num)))

    if sum(dealer_num) == sum(player_num):
        rand = random.randint(1, 10)
        chance = 21 - sum(dealer_num)
        if chance < rand:
            time.sleep(3)
            break

print("==============")
if sum(dealer_num) == 21:
    print("You Lost!")
elif sum(dealer_num) < 21:
    if sum(dealer_num) == sum(player_num):
        print("Tie!")
    elif sum(dealer_num) > sum(player_num):
        print("You Lost!")
    else:
        print("You Won!")
else:
    print("You Won!")
