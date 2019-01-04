"""
Goal of this code: Add new items into inventory, and display an inventory list

"""

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():  # k = key (e.g. gold coin, rope) ,  v = value  (e.g. 42, 1)
        print(str(v)+" "+k) #45 gold coin
        item_total=item_total+v #46 = 45 + 1
    print("Total number of items:" + str(item_total))

def addToInventory(inventory,addedItems):
    for i in range(len(addedItems)):
        inv.setdefault(addedItems[i], 0) # set addedItems value into 0
        # inv = {'gold coin':42,'rope':1,'gold coin': 0,'dagger': 0,'gold coin': 0,'gold coin': 0,'ruby': 0}
        inv[addedItems[i]] = inv[addedItems[i]] + 1
        # inv = {'gold coin':45,'rope':1,'dagger': 1,'ruby': 1}
    return inv

inv = {'gold coin':42,'rope':1} #type_dictionary
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby'] #type_list
inv=addToInventory(inv,dragonLoot)
displayInventory(inv)

"""
output:
Inventory:
45 gold coin
1 rope
1 dagger
1 ruby
Total number of items:48
"""

