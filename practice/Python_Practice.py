
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for i in counties_dict.items():
    print(f'{i[0]} has {i[1]} registered voters.')

voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
               {"county": "Denver", "registered_voters": 463353},
               {"county": "Jefferson", "registered_voters": 432438}]

print('\n\n')

for i in voting_data:
    print(f'{i["county"]} has {i["registered_voters"]} registered voters.')
