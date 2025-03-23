import random

## Gameboard:

def create_board():
    return [["O" for _ in range(10)] for _ in range(10)]

def print_board(board):
    # Print the column labels shifted one space to the left for proper alignment
    print("   A B C D E F G H I J")  
    for i, row in enumerate(board, start=1):
        # Print the row number with a proper left-aligned space and then the row content
        print(f"{i:<2} {' '.join(row)}")

## Ship Placement:

def place_ships(hidden_board, ship_sizes):
    ships = []
    for size in ship_sizes:
        placed = False
        while not placed:
            direction = random.choice(["horizontal", "vertical"])
            if direction == "horizontal":
                row = random.randint(0, 9)
                col = random.randint(0, 10 - size)
                if all(hidden_board[row][col + i] == "O" for i in range(size)):
                    for i in range(size):
                        hidden_board[row][col + i] = "S"
                    ships.append({"size": size, "hits": 0, "coords": [(row, col + i) for i in range(size)]})
                    placed = True
            else:  # vertical
                row = random.randint(0, 10 - size)
                col = random.randint(0, 9)
                if all(hidden_board[row + i][col] == "O" for i in range(size)):
                    for i in range(size):
                        hidden_board[row + i][col] = "S"
                    ships.append({"size": size, "hits": 0, "coords": [(row + i, col) for i in range(size)]})
                    placed = True
    return ships


## Player Input:

def convert_input_to_indices(input_guess):
    row = int(input_guess[0]) - 1
    col = ord(input_guess[1].upper()) - ord('A')
    return row, col

def is_valid_guess(guess, board):
    if len(guess) != 2:
        return False
    try:
        row, col = convert_input_to_indices(guess)
        return 0 <= row < 10 and 0 <= col < 10 and board[row][col] not in ("*", "X")
    except:
        return False

## Situation Report and Ship Status:

def report_status(attempts, ships):
    print(f"\nYou have made {attempts} attempts.")
    for ship in ships:
        status = "Sunk" if ship["hits"] == ship["size"] else "Damaged" if ship["hits"] > 0 else "Intact"
        print(f"{ship_name(ship['size'])}: [{'-' * ship['hits']}{'+' * (ship['size'] - ship['hits'])}] {status}")

def ship_name(size):
    names = {
        1: "Mine Ship (1 square)",
        2: "Submarine (2 squares)",
        3: "Frigate (3 squares)",
        4: "Destroyer (4 squares)",
        5: "Battleship (5 squares)"
    }
    return names.get(size, f"Ship ({size} squares)")

## Game Cycle:

def main():
    print(">>> Let's Play Battleship!\n")
    #print("Note: During the game, press 'r' to get a status report, and 'q' to quit.")
    board = create_board()
    hidden_board = create_board()
    ships = place_ships(hidden_board, ship_sizes=[1, 2, 3, 4, 5])  # Ship sizes
    print_board(board)

    attempts = 0
    while True:
        guess = input(f"\n{attempts + 1}. Enter your prediction: ").strip()

        
        if guess.lower() == 'q':
            print("Game Over. Goodbye!")
            break
        elif guess.lower() == 'r':
            report_status(attempts, ships)
            continue

        if not is_valid_guess(guess, board):
            print(f"[{guess}] Invalid or repeated coordinates. Try again.")
            continue

        row, col = convert_input_to_indices(guess)
        attempts += 1

        if hidden_board[row][col] == "S":
            print(f"[{guess}] Hit!")
            board[row][col] = "*"
            for ship in ships:
                if (row, col) in ship["coords"]:
                    ship["hits"] += 1
                    break
        else:
            print(f"[{guess}] Miss!")
            board[row][col] = "X"
        
        print_board(board)

        if all(ship["hits"] == ship["size"] for ship in ships):
            print("All ships have been sunk! Congratulations!")
            break

if __name__ == "__main__":
    main()
