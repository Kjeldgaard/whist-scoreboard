from player import Player
from game import Game


def main():
    whist = Game()
    whist.begin_game()

    while True:
        choice = input("Next step: (a)dd round, (e)nd game?: ")
        match choice:
            case "a":
                whist.add_round()
            case "e":
                print("Game over, final results:")
                whist.print_scores()
                break
            case _:
                print("Invalid choice")

    print(f"Money to account: {whist.get_to_account():.2f}")


if __name__ == "__main__":
    main()
