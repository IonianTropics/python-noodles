import hypixel

hypixel.setKeys(['e18dd562-ea8d-44e2-b499-942724ff5e7a'])

player = hypixel.Player('Buddyboyhunt')

name = player.getName()
level = player.getLevel()
rank = player.getRank()
info = player.getPlayerInfo()

print(f'Player info: \n\tName: "{name}"\n\tLevel: {level}\n\tRank: {rank["rank"]}')
print(info)