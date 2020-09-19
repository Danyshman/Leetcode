class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        words = sentence.split()
        for i, word in enumerate(words):
            for j in range(len(words[i])):
                if words[i][:j] in dictionary:
                    words[i] = words[i][:j]
        return ' '.join(words)