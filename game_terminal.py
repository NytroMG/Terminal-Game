
import random
from time import sleep



class Enemy:
    def __init__(self, name, description, danger_level, damage, enemyhp):
        self.name = name
        self.description = description
        self.danger_level = danger_level
        self.damage = damage
        self.enemyhp = enemyhp

    def encounter(self):
        print(f"You encounter a {self.name}!")
        print(self.description)
        print(f"Danger level: {self.danger_level}")

    def attack(self):
        print(f"The {self.name} attacks you!")

def moving():
    print("You have several planets at your disposal, which one would you like to visit?\n")
    planets = [
        "1) Nova Terra: A barren world with toxic atmosphere, its surface is scorched by constant solar flares.",
        "2) Neo-Eden: Once a lush paradise, now overrun by mutated flora and fauna, harboring dangers at every turn.",
        "3) Hades-9: A desolate wasteland shrouded in perpetual darkness, inhabited by mysterious entities lurking in the shadows.",
        "4) Gaia-Prime: A planet teeming with life, but where nature has turned against its human inhabitants, presenting constant threats.",
        "5) Aridus: A parched desert world, its surface scoured by relentless sandstorms, hiding ancient secrets beneath its dunes."
    ]
    for planet in planets:
        print(planet)
    viaje = int(input("\nChoose one of the numbers to initiate the landing sequence: \n"))
    if viaje in range(1, 6):
        sleep(1.5)
        print("\nInitializing ...")
        sleep(1.5)
        print("Landing ...\n")
        sleep(1.5)
        selected_planet = planets[viaje - 1].split(":")[0].split(")")[1].strip()
        print("Welcome to", selected_planet + "!\n")
        print("Let's explore!\n")
        sleep(1.5)
        return selected_planet 
    else:
        print("\nAn error occurred, please try again.\n")
        return None

def exploring(planet):
    global hp
    global treasures
    print("Exploring", planet, "...\n")
    sleep(1)
    event = random.randint(1 , 15)
    if event < 5:
        print("Oh no! Enemies ahead, get ready for combat.\n")
        hp = combat(hp)
    elif event > 13:
        print("You've found a treasure! We can leave this planet now.\n")
        treasures += 1
        print("Treasures obtained:", int(treasures), "of 3")
        if treasures == 3:
            print("Congratulations, you have found the three components necessary to restore civilization.\n")
            print("Returning home . . . . . .\n")
            exit()
        else:
            selected_planet = moving()
            exploring(selected_planet)
    else:
        print("Everything's fine for now, let's keep exploring.\n")
        avance = input("Do you want to continue exploring? (y/n): \n")
        if avance == "y":
            exploring(planet)
        else:
            print("OK")
            exit()

def combat(player_hp):
    global hp
    global treasures
    enemy_type = random.randint(1, 5)
    enemy = enemies[enemy_type - 1]
    enemy.encounter()
    enemy.attack()
    hpnew = int(player_hp) - int(enemy.damage)
    print("\nYour health is", hpnew)
    enemy_hp = int(enemy.enemyhp)
    print("\nEnemy's health is", enemy_hp)
    hp = hpnew
    
    while enemy_hp > 0 and hp > 0:
        is_protected = random.choice([True, False])
        decision = input("\nWhat do you want to do next? (block, attack, run): \n")
        if decision == "block":
            print("\n")
            enemy.attack()
            print("\nYou've successfully blocked the attack")
            print("\nYour health is", hp)
            hp = int(hpnew) 
        elif decision == "attack":
            if is_protected:
                reflect = random.choice([True, False])
                print("\nThe enemy has blocked your attack")
                if reflect:
                    print("\nBad luck, the enemy has countered your attack")
                    hpnew = int(hpnew) - int(damagebase)
                    print("\nYour health is", hpnew)
                    hp = int(hpnew) 
            else:
                print("\nYou've launched a powerful attack")
                enemy_hp -= int(damagebase)
                if enemy_hp <= 0:
                    print("\nYou have defeated", enemy.name)
                    exploring(selected_planet)
                    hp = int(hpnew)
                else:
                    print("\nEnemy's health is", enemy_hp)
        elif decision == "run":
            hp = int(hpnew)
            print("\nYou've decided to flee from the combat. Attempting to return to exploration.")
            sleep(1)
            running = random.randint(1 , 5)
            if running > 2:
                print("\nExiting combat, you escape without trouble ")
                exploring(selected_planet)
                return
            else:
                print("\nYou failed to escape from combat")
                enemy.attack()
                hpnew = int(hp) - int(enemy.damage)
                print("\nYour health is", hpnew) 
                hp = int(hpnew) 
    if hp <= 0:
        print("\n---------------\n¡GAME OVER!\n---------------\n")
        exit() 
    
    return enemy_hp

print("\nWelcome to this adventure! You won't be disappointed.\n")
print("Amidst the chaos of World War I, a nameless soldier fought valiantly, their exploits lost to history. As the war raged on, humanity faced its darkest hour. A cataclysmic event brought about the end of the world as we knew it.\nThe planet Earth was engulfed in devastation. Cities crumbled, the land fractured, and the skies darkened with ash. Survivors clung to hope, building spacecraft to escape the dying planet. But space, vast and dangerous, had its own threats.\nOur soldier, now a weary war veteran, embarked on a journey through the stars. In the cold void, they faced unimaginable foes, from alien creatures to the twisted remnants of humanity lost in the darkness.\nThroughout it all, the soldier showed courage and determination. They fought to protect loved ones and preserve the hope of a new beginning.\nAnd so, as the universe remained a place of danger and wonder, the soldier pressed on, remembering Earth's days of glory and tragedy while looking towards an uncertain but promising future.\n")

enemies_data = [
    {"name": "Deformed Mutants", "description": "Humans who have been warped by radiation and genetic experiments, now hostile and violent.", "danger_level": "Medium", "damage": "5", "enemy_hp": "10"},
    {"name": "Renegade Combat Robots", "description": "War machines that have been abandoned or have turned rebellious, now hunting down human survivors.", "danger_level": "High", "damage": "8", "enemy_hp": "15"},
    {"name": "Bio-Mechanical Creatures", "description": "Beings created by the fusion of living organisms and technology, endowed with lethal abilities and insatiable voracity.", "danger_level": "High", "damage": "8", "enemy_hp": "15"},
    {"name": "Cult of Dark Worshipers", "description": "Fanatical humans who worship dark entities and perform sacrifices to gain their favor, ready to eliminate any intruder in their territory.", "danger_level": "Medium", "damage": "5", "enemy_hp": "10"},
    {"name": "Mutated Insect Colonies", "description": "Insects that have grown to monstrous sizes due to radiation, now organized into aggressive swarms that infest the darkest and most dangerous places of the world.", "danger_level": "Low", "damage": "3", "enemy_hp": "5"}
]
enemies = [Enemy(data["name"], data["description"], data["danger_level"], data["damage"], data["enemy_hp"]) for data in enemies_data]

hp = 100
damagebase = 4
treasures = 0

play = input("Do you want to start this adventure and live the exploits of our soldier? (y/n): \n")

if hp < 0:
    print("---------------\n¡GAME OVER!\n---------------\n")
    exit()

if play.lower() == "y":
    print("\nGreat! Let's get started.\n")
    selected_planet = None
    try:
        while treasures < 3:
            selected_planet = moving() if selected_planet is None else selected_planet
            treasures = exploring(selected_planet)
    except KeyboardInterrupt:
        print("\nThe game has been interrupted! See you later!\n")




