from prettyTables import Table

table = Table()
print(table)


table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'water'])
table.add_column('Type', ['Electric', 'water', 'Fire'])
print(table)