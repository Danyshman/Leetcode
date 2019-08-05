def findOccurrences(text, first ,second):
    answer = []
    text_array = text.split(' ')
    for i in range(len(text_array)-2):
        if text_array[i] == first and text_array[i+1] == second:
            answer.append(text_array[i+2])
    return answer