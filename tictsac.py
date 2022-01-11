numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def main ():
    table()
    move()

def table():
    print(numbers[0], "|", numbers[1], "|", numbers[2])
    print("----------")
    print(numbers[3], "|", numbers[4], "|", numbers[5])
    print("----------")
    print(numbers[6], "|", numbers[7], "|", numbers[8])
    print("")

def move():
    player = next("o")
    while not(score(numbers)):
       moving = int(input(f"{player} turn to choose a square (1-9): "))

       for row in numbers:
           if moving == numbers[0]:
              numbers[0] = player
              player = next(player)
              table()

       for row in numbers:
           if moving == numbers[1]:
              numbers[1] = player
              player = next(player)
              table()

       for row in numbers:
           if moving == numbers[2]:
              numbers[2] = player
              player = next(player)
              table()

       for row in numbers:
           if moving == numbers[3]:
              numbers[3] = player
              player = next(player)
              table()

       for row in numbers:
           if moving == numbers[4]:
              numbers[4] = player
              player = next(player)
              table()

       for row in numbers:
           if moving == numbers[5]:
              numbers[5] = player
              player = next(player)
              table()

       for row in numbers:
           if moving == numbers[6]:
              numbers[6] = player
              player = next(player)
              table()

       for row in numbers:
           if moving == numbers[7]:
              numbers[7] = player
              player = next(player)
              table()

       for row in numbers:
           if moving == numbers[8]:
              numbers[8] = player
              player = next(player)
              table()
    print("Thanks for playing")
    table()
    


def next(now_playing):
    if now_playing == "o":
        return "x"
    elif now_playing == "x":
        return "o"



def score(tables):
    return (tables[0] == tables[1] == tables[2] or
            tables[3] == tables[4] == tables[5] or
            tables[6] == tables[7] == tables[8] or
            tables[0] == tables[3] == tables[6] or
            tables[1] == tables[4] == tables[7] or
            tables[2] == tables[5] == tables[8] or
            tables[0] == tables[4] == tables[8] or
            tables[2] == tables[4] == tables[6])
        

if __name__ == "__main__":
    main()