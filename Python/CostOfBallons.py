testCases = input()             

for k in range(int(testCases)):
    costs = input()     
    costsArray = costs.split(" ")

    minCost = int(costsArray[0])< int(costsArray[1]) and int(costsArray[0]) or int(costsArray[1]);
    maxCost = int(costsArray[0])> int(costsArray[1]) and int(costsArray[0]) or int(costsArray[1]);
    totalCost=0;
    numberOfPartAnsweredQn1 =0;
    numberOfPartAnsweredQn2 =0;
    participants = input()     
    participantAnswers = list()
    intParticpant =list()
    for i in range(int(participants)):
        n = input()
        participantAnswers.append(str(n))
        ans=int(n.replace(" ", ""))
        intParticpant.append(ans)
        if ans == 10 or ans == 11 :
            numberOfPartAnsweredQn1+=1
        if ans == 11 or ans == 1 : 
            numberOfPartAnsweredQn2+=1
    for i in range(int(participants)):
        string = participantAnswers[i].split(" ");
       
        for j in range(2):
            ints = int(str(string[j]));
            if numberOfPartAnsweredQn1>numberOfPartAnsweredQn2 or numberOfPartAnsweredQn1==numberOfPartAnsweredQn2:
                if j==0:
                    totalCost +=minCost*ints;
                else:
                    totalCost +=maxCost*ints;
            else:
                if j==0:
                    totalCost +=maxCost*ints;
                else:
                    totalCost +=minCost*ints;
            
    print(totalCost)
    
    
