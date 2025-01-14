import os
import random
import queue
import threading
from concurrent.futures import ThreadPoolExecutor

def print_menu() -> str:
    """Function to display the menu and get user choice."""
    choice = input("1. Create Arrays\n"
                   "2. Execute Algorithm\n"
                   "3. Show Results\n"
                   "4. Exit Program\n")
    return choice

def creating_arrays_dialogue():
    """Function to handle the dialogue for creating arrays."""
    mode: str = input("Choose array creation mode:\n"
                      "1. Automatic\n"
                      "2. Manual\n"
                      "Your choice: ")
    if mode == "1":
        return auto_generating_arrays()
    elif mode == "2":
        return self_creating_arrays()
    else:
        input("Invalid option.\nPress any key to continue.")
        return

def auto_generating_arrays() -> list:
    """Generates three one-dimensional arrays with random numbers."""
    size = random.randint(2, 10)
    return [list(random.randint(1, 10) for _ in range(size)) for _ in range(3)]

def self_creating_arrays():
    """Manually creates arrays based on user input."""
    arrays = [[], [], []]
    try:
        arrays_size: int = int(input("Enter the size of the arrays: "))
    except ValueError:
        input("Invalid size input!\nPress any key to continue.")
        return
    for index, array in enumerate(arrays):
        for _ in range(arrays_size):
            try:
                array.append(int(input(f"Enter number for array {index + 1}: ")))
            except ValueError:
                input("You must enter numbers only.\nPress any key to continue.")
                return
    return arrays

def checking_digits(arrays: list):
    """Algorithm to check if the condition is met."""
    results = []
    for i in range(len(arrays[0])):
        sum_ab = arrays[0][i] + arrays[1][i]
        if sum_ab == arrays[2][i]:
            min_value = min(arrays[0][i], arrays[1][i], arrays[2][i])
            result = (arrays[0][i] + arrays[1][i] + arrays[2][i]) ** min_value
            results.append(result)
    return results

def show_results(result: list):
    """Displays the results."""
    if not result:
        input("No numbers found that meet the conditions.\nPress any key to continue...")
        return
    print("The following numbers were found:")
    for res in result:
        print(res)
    input("Press any key to continue...")

def quitting():
    """Exits the program."""
    exit()

def calculate_and_display_results(arrays):
    """Calculates results in a separate thread."""
    results = checking_digits(arrays)
    show_results(results)

if __name__ == "__main__":
    while True:
        os.system("cls")
        user_choice = print_menu()
        if user_choice == "1":
            needed_arrays = creating_arrays_dialogue()
        elif user_choice == "2":
            if needed_arrays:
                threading.Thread(target=calculate_and_display_results, args=(needed_arrays,)).start()
            else:
                input("You need to create arrays first!\nPress any key to continue...")
        elif user_choice == "3":
            if 'results' in locals():
                show_results(results)
            else:
                input("No results available yet!\nPress any key to continue...")
        elif user_choice == "4":
            quitting()
