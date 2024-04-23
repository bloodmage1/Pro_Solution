record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]



def solution(record):
    progress = []
    player = {}
    guide = []
    for i in record:
        if i.startswith("Enter") or i.startswith("Change"):
            act, user_id, nickname =i.split()
            player[user_id] = nickname
            
            progress.append((act, user_id))
                    
        elif i.startswith("Leave"):
            act, user_id = i.split()        
            del(player[user_id])
            
            progress.append((act, user_id))
            

    for act, id in progress:
        if act == "Enter":
            guide.append("{}님이 들어왔습니다.".format(player[id]))
        if act == "Leave":
            guide.append("{}님이 나갔습니다.".format(player[id]))

    return guide
    
print(solution(record))
# print(player)
# print(guide)

