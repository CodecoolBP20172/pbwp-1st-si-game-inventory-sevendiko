# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

from collections import Counter, OrderedDict
import csv

# Displays the inventory.
def display_inventory(inventory):
    print("Inventory:")
    for key in inventory:
        print(inventory[key], key)
    print("Total values of elements: %d \n" % sum(inventory.values()))

# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    mylist = []
    for key in added_items:  # key = elem neve
        if key in mylist:
            continue
        else:
            if key != ' ':
                mylist.append(key)
                count = added_items.count(key)  # count = egyes elemek darabszáma
            if key in inventory:
                inventory[key] += count
            else:
                inventory[key] = count

# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def lenght(x):
    maxlenght = 0
    for element in x:
        lenght = len(element)
        if lenght > maxlenght:
            maxlenght = lenght
    return maxlenght


def keywithmaxval(d):
    v = list(d.values())
    k = list(d.keys())
    return len(str(v[v.index(max(v))]))


def print_table(inv, order):
    if order == "count,desc":
        inv = OrderedDict(sorted(inv.items(), key=lambda t: t[1], reverse=True))
    elif order == "count,asc":
        inv = OrderedDict(sorted(inv.items(), key=lambda t: t[1]))
    print("Inventory:" "\n")
    x = longest + biggestvaluelenght + DECORATION_STRING_LENGTH
    print(" " * biggestvaluelenght + 'count' + " " * longest + 'item name')
    print('-' * x)
    for key in inv:
        print(str(inv[key]).rjust(biggestvaluelenght + 5, " "), end="")
        print(str(key).rjust(longest + 9, " "), end="\n")
    print("-" * x)
    print("Total values of elements: %d" % sum(inventory.values()))

# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inv, filename="import_inventory.csv"):
    with open(filename, 'r') as inputstream:
        for line in inputstream:
            currentline = line.split(",")
        inv = add_to_inventory(inv, currentline)


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    outputlist = []
    for key in inventory:
        value = 0
        while value < inventory[key]:
            outputlist.append(key)
            value += 1
    with open(filename, "w", newline="") as outputstream:
        writer = csv.writer(outputstream)
        writer.writerow(outputlist)

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(inventory, dragon_loot)
DECORATION_STRING_LENGTH = 14
display_inventory(inventory)
longest = lenght(inventory)
biggestvaluelenght = keywithmaxval(inventory)
import_inventory(inventory, 'items.csv')
print_table(inventory, None)
export_inventory(inventory, 'export_inventory.csv')

