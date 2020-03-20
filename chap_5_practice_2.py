# Fantasy Game Inventory

myBag = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'gold coin', 'dagger', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0

    for k, v in inventory.items():
        item_total += v
        print(str(v) + " " + str(k))
    
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    
    for k, v in inventory.items():
        for i in range(len(addedItems)):
            if i in k:
                v += 1
            else:

    
    return



myBag = addToInventory(myBag, dragonLoot)
displayInventory(myBag)
