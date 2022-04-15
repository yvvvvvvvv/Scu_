players=['Curry','Jordan','James','Durant','Obama']
playerss=sorted(players)
playersss=sorted(playerss,reverse=True)
print('列印前三位球員')
for x in playerss[:3]:
    print(x)
print('列印後三位球員')
for x in playersss[:3]:print(x)
