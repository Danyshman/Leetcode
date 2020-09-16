from collections import deque
def canReach(arr, start):
    queue = deque([start])
    visited = set()
    while queue:
        idx = queue.popleft()
        if arr[idx] == 0:
            return True
        for i in [idx+arr[idx], idx-arr[idx]]:
            if 0 <= i < len(arr):
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
    return False

print(canReach(arr = [3,0,2,1,2], start = 2))