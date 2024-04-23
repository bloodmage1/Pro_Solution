players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

result = ["mumu", "kai", "mine", "soe", "poe"]

### 시간 초과 ###

for i in callings:
    original = players.index(i) - 1 # index 함수 -> 시간초과. 재정렬
    players.remove(i) 
    players.insert(original, i) 

print(players)


#### 시간 초과 2 ####

# player_positions = {player: index for index, player in enumerate(players)}

# for calling in callings:
#     original_position = player_positions[calling]
#     players.pop(original_position)
#     players.insert(original_position-1, calling) # 운이 나쁘면 시간이 많이 걸릴수 있다.
#     player_positions = {player: index for index, player in enumerate(players)}

### 시간초과 3 ###

# player_positions = {player: index for index, player in enumerate(players)}

# for calling in callings:
#     original_position = player_positions[calling]
#     players.pop(original_position)
#     players = players[:original_position -1] + [calling] + players[original_position -1:]
#     player_positions = {player: index for index, player in enumerate(players)}

# print(players)

###

player_positions1 = {player: index for index, player in enumerate(players)}
player_positions2 = {index: player for index, player in enumerate(players)}

print("player_positions1", player_positions1)
print("player_positions2", player_positions2)

for calling in callings:
    player_positions1[calling] -= 1

    player_positions2[player_positions1[calling] + 1] = player_positions2[player_positions1[calling]]
    player_positions2[player_positions1[calling]] = calling

    player_positions1[player_positions2[player_positions1[calling] + 1]] = player_positions1[calling] + 1

print("")
print("변경 후")
print("player_positions1", player_positions1)
print("player_positions2", player_positions2)

players = [player for player, _ in sorted(player_positions1.items(), key=lambda x: x[1])]

print(players)