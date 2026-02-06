import random

def Risk(rounds):
    attacker_count = 0
    defender_count = 0

    for i in range(rounds):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)

        d_rolls = [d1, d2]
        d_rolls.sort(reverse=True)

        best_defender1, best_defender2 = d_rolls[:2]

        a1 = random.randint(1,6)
        a2 = random.randint(1,6)
        a3 = random.randint(1,6)

        a_rolls = [a1, a2, a3]
        a_rolls.sort(reverse=True)

        best_attacker1, best_attacker2 = a_rolls[:2]

        if best_attacker1 > best_defender1:
            attacker_count += 1
        else:
            defender_count += 1

        if best_attacker2 > best_defender2:
            attacker_count += 1
        else:
            defender_count += 1


    total_points = defender_count + attacker_count
    defender_percentage = (defender_count / total_points) * 100
    attacker_percentage = (attacker_count / total_points) * 100

    print(f"The percetage of the attacker winning a battle are: {attacker_percentage}")
    print(f"The percentage of the defender winning a battle is: {defender_percentage}")
          
Risk(1000000)

    