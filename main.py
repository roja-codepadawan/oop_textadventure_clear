import random
import time

def main():
  global HP, ATK, MP, main, lv, clas
  pick_class()
  status_class()
  village()

x = 0

def dungeon():
  global x
  if x == 0:
    print(f'\nWelcome to DUNGEON!')
    x += 1
  time.sleep(1)
  print(f'\nYou are at DUNGEON level {lv}\nFinish the quiz to go to the next level') #!!!
  time.sleep(1)

  questions = ["\nWhat color are apples?\n(1) Red\n(2) Orange\n> ",
                 "\nWhat color are bananas?\n(1) Red\n(2) Yellow\n> ",
                 "What is 1 + 1 + = ?\n(1) 1900\n(2) window :))\n> ",
                 "x^2 + 2x + 1 = 0. Find x?\n(1) 1\n(2) -1\n> ",
                 "Find the area of a rectangle know that w = 5 and l = 5?\n(1) 25\n(2) 36\n> ",
                 "What is the derivative of x^2?\n(1) 2x\n(2) 2x^(-1)\n> ",
                 "Find v known that s = 2m and t = 1s and v = s/t\n(1) 2m/s\n(2) 2ft/s\n> ",
                 "4x + 10 = x - 7. Find x =?\n> ",
                 "2(4-y) - 3(y+3) = -11. Find y=?\n> ",
                 "What does LOL mean?\n(1) laughing out loud\n(2) cry to the pillow\n> ",
                 "What is the formula of surface area of a sphere?\n(1) 4pir^3/3\n(2) 4pir^2\n> ",
                 "What is gravitational acceleration at Earth surface?\n(1) 9.8\n(2) 98n> ",
                 "What is the relationship between F,a, and m?\n(1) a = F*m \n(2) F = m*a\n> ",
                 "What is pressure?\n(1) Normal Force over Area \n(2) Newton over coulomb \n> ",
                 "What is photosynthesis equation?\n(1) Zn + HCl ---> ZnCl2 + H \n(2) 6CO2 + 6H2O → C6H12O6 + 6O2. \n> ",
                 "I pledge allegiance to the ____ of the United States of America, and to the republic for which it stands, one nation under God, indivisible, with liberty and justice for all. \nFill in the blank: "
                 ]

  answer = ["1", "2", "2", "2", "1", "1", "1", "-17/3", "2", "1", "2", "1", "2", "1", "2", "flag"]

  def monster(n):
    global HP, MP, ATK, lv
    score = 0
    for num1 in range(n):
      num1 = random.randint(0, 16)
      main = input(questions[num1])
      if main == (answer[num1]):
        time.sleep(0.5)
        print(f'Congrats! It`s correct!')
        time.sleep(1)
        score += 1
      else:
        HP -= 5
        time.sleep(0.5)
        print(f'It`s wrong! You get attacked.\nHP:{HP} -5')
        time.sleep(1)
        status_print()
        time.sleep(2)
        if HP <= 0:
          game_over()
        while True:
          main = input(f'\nWhat do you want to do?\n1). Go to Village\n2). Continue Dungeon\n> ')
          if main == "1":
            village()
            break
          elif main == "2":
            dungeon()
            break
          else:
            print("\n\nDon't make typo ☠️☠️☠️")
            continue

      if score == lv:
        print(f'\nYou finished level {lv}')
        time.sleep(1)
        lv = lv + 1
        if lv == 11:
          game_over()
        print(f'\nYour current level is {lv}')
        time.sleep(1)
        print(f'\nHP +10, MP +10, ATK +10')
        time.sleep(1)
        HP += 10
        MP += 10
        ATK += 10
        status_print()
        time.sleep(1)
        dungeon()

  monster(lv)

def village():
  global main
  print(f'\nYou are in the Village. In Village, you can be healed\nYour goal is to reach Dungeon level 10. Good luck!')
  time.sleep(2)
  while True:
    main = input(f'\nWhat do you want to do?\n1). Heal (status reset at current level)\n2). Go to Dungeon\n> ')
    if main == "1":
      status_heal()
      break
    elif main == "2":
      dungeon()
      break
    else:
      print(f'\n\nDon`t make typo ☠️☠️☠️')
      continue

def pick_class():
    global main, HP, MP, ATK, clas, lv
    lv = 1
    while True:
      main = input(f'Choose your class:\n1). Swordsman\n2). Archery\n3). Mage\n> ')
      if main == "1":
        clas = "swordsman"
        print(f'\nYou now are a {clas.capitalize()}')
        break
      elif main == "2":
        clas = "archery"
        print(f'\nYou now are a {clas.capitalize()}')
        break
      elif main == "3":
        clas = "mage"
        print(f'\nYou now are a {clas.capitalize()}')
        break
      else:
        print(f'\n\nDon`t make typo ☠️☠️☠️')
        continue

def status_class():
  global main, HP, MP, ATK, lv, clas
  if clas == "swordsman":
      HP = 20
      MP = 5
      ATK = 20
      lv = 1
  elif clas == "archery":
      HP = 5
      MP = 5
      ATK = 5
      lv = 1
  elif clas == "mage":
      HP = 5
      MP = 30
      ATK = 5
      lv = 1
  time.sleep(1)
  print(f'\n{clas.capitalize()}`s status:')
  time.sleep(1)
  print(f'HP:{HP}\nMP:{MP}\nATK:{ATK}')
  time.sleep(1)

def status_heal():
  global HP, MP, ATK, main
  if clas == "swordsman":
    HP = 20 + 10 * (lv - 1)
    MP = 5 + 10 * (lv - 1)
    ATK = 20 + 10 * (lv - 1)
  elif clas == "archery":
    HP = 5 + 10 * (lv - 1)
    MP = 5 + 10 * (lv - 1)
    ATK = 5 + 10 * (lv - 1)
  elif clas == "mage":
    HP = 5 + 10 * (lv - 1)
    MP = 30 + 10 * (lv - 1)
    ATK = 5 + 10 * (lv - 1)

  print("\nYou are healed!")
  time.sleep(2)
  status_print()
  time.sleep(4)
  while True:
    main = input(f'\nWhat do you want to do?\n1). Heal (status reset at current level)\n2). Go to Dungeon\n> ')
    if main == "1":
      status_heal()
      break
    elif main == "2":
      dungeon()
      break
    else:
      print(f'\n\nDon`t make typo ☠️☠️☠️')
      continue

def status_change(hp, mp):
  global main, HP, MP, ATK
  HP = HP + hp
  MP = MP + mp
  if HP <= 0:
    game_over()

def status_print():
    print(f'\nCurrent status\nHP:{HP}\nMP:{MP}\nATK:{ATK}')

def game_over():
  global lv
  lv -= 1
  if lv <= 0:
    print(f'Game Over!')
    exit()
  elif lv == 10:
    print(f'Good job! You finished the game! You are very patient!')
    exit()
  else:
    print(f'\n Your HP = 0\nGame Over!\n But you are the main character, so you cannot die here :)\nYou are teleport to village and your level decreases by 1')
    village()

if __name__ == '__main__':
  main()