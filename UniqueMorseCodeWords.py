def uniqueMorseRepresantations(words):
    morse_alphabeat = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",
                       "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    ans = set()
    for word in words:
        transformation = ''
        for i in range(len(word)):
            transformation += morse_alphabeat[ord(word[i])-97]
        ans.add(transformation)
    return len(ans)



print(uniqueMorseRepresantations(words = ["gin", "zen", "gig", "msg"]))



