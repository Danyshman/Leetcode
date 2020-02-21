class TimeMap:

    def __init__(self):
        self.d_key_timestamps = {}
        self.d_key_timestamp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d_key_timestamp[key + '_' + str(timestamp)] = value
        if self.d_key_timestamps.get(key, False):
            self.d_key_timestamps[key].append(timestamp)
        else:
            self.d_key_timestamps[key] = [timestamp]

    def get(self, key: str, timestamp: int) -> str:
        if self.d_key_timestamp.get(key + '_' + str(timestamp), False):
            return self.d_key_timestamp[key + '_' + str(timestamp)]
        if self.d_key_timestamps.get(key, False):
            index = self.fls(timestamp, self.d_key_timestamps[key])
            return '' if (index == -1) else self.d_key_timestamp[key + '_' + str(self.d_key_timestamps[key][index])]
        return ''

    #     Find first less value or -1
    def fls(self, val, arr):
        left, right, ans = 0, len(arr) - 1, -1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < val:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)