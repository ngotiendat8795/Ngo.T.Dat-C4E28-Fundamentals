inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twin', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell', 'strange barry', 'lint']

inventory['backpack'].remove("dagger")
print(inventory['backpack'])

inventory['gold'] = inventory['gold'] + 50

print(inventory)