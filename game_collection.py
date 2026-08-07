"""
COMP 1150 Final Project
Game Collection Manager

This program allows users to manage a collection of video games.
Users can add, search, update, delete, save, and load games.
"""

collection = {}

#Adding a game to the collection
def add_game():
    """Adds a new game to the collection."""

    name = input("Enter the game title: ")
    genre = input("Enter the genre: ")
    rating = float(input("Enter the rating (1-10): "))
    price = float(input("Enter the price: $"))

    collection[name] = {
        "Genre": genre,
        "Rating": rating,
        "Price": price
    }

    print("\nGame added!")
    print(collection)


#Search for a game in the collection
def find_game():
    """Finds a game in the collection."""

    name = input("\nEnter the game title: ").strip()

    if name in collection:
        print("\nGame Found!")
        print(f"Title: {name}")
        print(f"Genre: {collection[name]['Genre']}")
        print(f"Rating: {collection[name]['Rating']}")
        print(f"Price: ${collection[name]['Price']:.2f}")
    else:
        print("Game not found.")


#Viewing all games in the collection
def view_games():
    """Displays every game in the collection."""

    if len(collection) == 0:
        print("\nYour collection is empty.")
        return

    print("\nYour Game Collection")
    print("------------------------")

    for game in collection:
        print(f"\nTitle: {game}")
        print(f"Genre: {collection[game]['Genre']}")
        print(f"Rating: {collection[game]['Rating']}")
        print(f"Price: ${collection[game]['Price']:.2f}")


#Updating a game in the collection
def update_game():
    """Updates information about a game."""

    name = input("\nEnter the game title to update: ").strip()

    if name not in collection:
        print("Game not found.")
        return

    print("\nEnter the new information.")

    genre = input("New Genre: ").strip()
    rating = float(input("New Rating: "))
    price = float(input("New Price: $"))

    collection[name]["Genre"] = genre
    collection[name]["Rating"] = rating
    collection[name]["Price"] = price

    print("Game updated successfully!")


#Delete a game from the collection
def delete_game():
    """Deletes a game from the collection."""

    name = input("\nEnter the game title to delete: ").strip()

    if name in collection:
        del collection[name]
        print("Game deleted.")
    else:
        print("Game not found.")    


#Display statistics about the collection
def statistics():
    """Shows information about the collection."""

    if len(collection) == 0:
        print("\nNo games in your collection.")
        return

    total = len(collection)

    total_rating = 0

    highest_price = 0
    expensive_game = ""

    for game in collection:
        total_rating += collection[game]["Rating"]

        if collection[game]["Price"] > highest_price:
            highest_price = collection[game]["Price"]
            expensive_game = game

    average = total_rating / total

    print("\nCollection Statistics")
    print("------------------------")
    print(f"Total Games: {total}")
    print(f"Average Rating: {average:.1f}")
    print(f"Most Expensive Game: {expensive_game}")
    print(f"Price: ${highest_price:.2f}")


#Display the main menu
def display_menu():

    print("\n===========================")
    print(" GAME COLLECTION MANAGER")
    print("===========================")
    print("1. Add Game")
    print("2. Find Game")
    print("3. View All Games")
    print("4. Update Game")
    print("5. Delete Game")
    print("6. Statistics")
    print("7. Quit")


#Main function to run the program
def main():

    while True:

        display_menu()

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_game()

        elif choice == "2":
            find_game()

        elif choice == "3":
            view_games()

        elif choice == "4":
            update_game()

        elif choice == "5":
            delete_game()

        elif choice == "6":
            statistics()

        elif choice == "7":
            print("\nThank you for using Game Collection Manager!")
            break

        else:
            print("Invalid choice. Please try again.")

#Testing

if __name__ == "__main__":
    main()