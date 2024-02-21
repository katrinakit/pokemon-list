
import csv

pokemons = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

# print(pokemons)

print("Pokemon list command:")
terminator=pokemons.copy()
while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by text in name")
    print("5. Search by length of name")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        a=int(input("please put the pokemons number in:"))
        print(pokemons[a-1])
        # https://www.w3schools.com/python/python_lists_access.asp
        pass
    elif choice == '2':
        terminator.sort()
        print(terminator)
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '3':
        terminator.sort(reverse = True)
        print(terminator)
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '4':
        print("please put the pokemons name/pokemons letter here:")
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/ref_string_startswith.asp
        pass
    elif choice == '5':
        print("please put the pokemons names length here:")
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        pass
    elif choice == '6':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 6")

    print("==========================")
