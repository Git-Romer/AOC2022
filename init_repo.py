import os

users = [
    'gilles',
    'markus'
]

for user in users: # Creating directories for specific users
    os.mkdir('./' + user)

for folder in range(1,26): # Creating folders for each day for each user
    for user in users:
        os.mkdir(os.path.join('./' + user, 'Day_' + str(folder)))