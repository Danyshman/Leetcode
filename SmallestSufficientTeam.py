def smallestSufficientTeam(req_skills, people):
    best_choice = []
    for i in range(len(people)):
        best_choice.append([people[i], i])
    ans = [i for i in range(len(people))]
    for i in range(len(best_choice)):
        temp = [best_choice[i][1]]
        best_choice[i] = best_choice[i][0]
        choice_len = len(best_choice[i])
        choice_index = 0
        while len(best_choice[i]) < len(req_skills):
            for j in range(len(people)):
                if len(set(best_choice[i]+people[j])) > choice_len:
                    choice_len = len(set(best_choice[i]+people[j]))
                    choice_index = j
            temp.append(choice_index)
            best_choice[i] = list(set(best_choice[i] + people[choice_index]))
        if len(temp) < len(ans):
            ans = temp

    return ans


print(smallestSufficientTeam(["ldq","lpah","i","ypowcknvrcuouhe","jftllvrfghmvt","svscjulmksgo","xt","mnfgnpsqhcobst"],[["lpah","xt"],["ldq","i"],["ypowcknvrcuouhe"],["lpah","jftllvrfghmvt","mnfgnpsqhcobst"],["xt"],["i","xt"],["svscjulmksgo"],["i"],["i","ypowcknvrcuouhe"],["i"],[],["svscjulmksgo","mnfgnpsqhcobst"],[],["xt","mnfgnpsqhcobst"],[],["ypowcknvrcuouhe","mnfgnpsqhcobst"],["i"],[],["jftllvrfghmvt","svscjulmksgo"],["i","mnfgnpsqhcobst"],["jftllvrfghmvt"],["jftllvrfghmvt"],[],["i"],["ypowcknvrcuouhe"],["ypowcknvrcuouhe"],[],[],[],["ldq","i"]]))




