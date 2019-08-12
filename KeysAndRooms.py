def canVisitAllRooms(rooms):
    used_keys = []
    unused_keys = [0]
    while True:
        temp_storage = []
        if len(unused_keys) == 0:
            break
        for i in range(len(unused_keys)):
            for key in rooms[unused_keys[i]]:
                if key not in unused_keys and key not in used_keys:
                    unused_keys.append(key)
            temp_storage.append(unused_keys[i])
        for used_key in temp_storage:
            unused_keys.remove(used_key)
            used_keys.append(used_key)
    for i in range(len(rooms)):
        if i not in used_keys:
            return False
    return True



print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))