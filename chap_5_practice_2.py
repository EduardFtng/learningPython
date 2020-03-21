# Fantasy Game Inventory

# My Dictionary
myBag = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# My List
dragonLoot = ['gold coin', 'gold coin', 'dagger', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0

    for k, v in inventory.items():
        item_total += v
        print(str(v) + " " + k)
    
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):    
    for i in addedItems:
        if i not in inventory:
                inventory[i] = 1
        else:
                inventory[i] += 1
                
    return inventory


myPocket = {'gold coin': 2, 'smal stone': 1}
chestLoot = ['gold coin', 'dagger', 'gold coin',]

displayInventory(myBag)
myBag = addToInventory(myBag, dragonLoot)
displayInventory(myBag)
