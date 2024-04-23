user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]

banned_id = ["fr*d*", "abc1**"]

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]

# banned_id = ["*rodo", "*rodo", "******"]

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]

# banned_id = ["fr*d*", "*rodo", "******", "******"]

from itertools import permutations

def check(user_id, banned_id):
    for i in range(len(banned_id)):
        if len(user_id[i]) != len(banned_id[i]):
            return False

        for j in range(len(user_id[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != user_id[i][j]:
                return False

    return True

user_list = list(permutations(user_id, len(banned_id)))

banned_list = []

for i in user_list:
    if check(i, banned_id):
        i = set(i)
        if i not in banned_list:
            banned_list.append(i)
    else:
        continue

# for i in user_list:
#     if not check(i, banned_id):
#         continue
#     else:
#         i = set(i)
#         if i not in banned_list:
#             banned_list.append(i)

print(len(banned_list))
        



