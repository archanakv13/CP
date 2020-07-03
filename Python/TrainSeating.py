import math as m

'''
Question URL 
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/description
Level - Very Easy


//Pbm -1
 '''
class TrainSeating:
    NoOfTestCases = int(raw_input())
    seatNumbersList = list()
    rem,i = 0,0
    seatNumber = 0
    if 1 <= NoOfTestCases and NoOfTestCases <= m.pow(10,5):
        while i < NoOfTestCases:
            seatNumbersList.append(int(raw_input()))
            i+=1
           
        for seatNumber in seatNumbersList:
            if 1<= seatNumber and seatNumber <= 108:
                rem = seatNumber % 12
                if rem ==1:
                    print'{0} {1}'.format(seatNumber+11,"WS")
                elif rem ==2:
                    print'{0} {1}'.format(seatNumber+9,"MS")
                elif rem==3:
                    print'{0} {1}'.format(seatNumber+7,"AS")
                elif rem==4:
                    print'{0} {1}'.format(seatNumber+5,"AS")
                elif rem==5:
                    print'{0} {1}'.format(seatNumber+3,"MS")
                elif rem==6:
                    print'{0} {1}'.format(seatNumber+1,"WS")
                elif rem==7:
                    print'{0} {1}'.format(seatNumber-1,"WS")
                elif rem==8:
                    print'{0} {1}'.format(seatNumber-3,"MS")
                elif rem==9:
                    print'{0} {1}'.format(seatNumber-5,"AS")
                elif rem==10:
                    print'{0} {1}'.format(seatNumber-7,"AS")
                elif rem==11:
                    print'{0} {1}'.format(seatNumber-9,"MS")
                elif rem == 0:
                    print'{0} {1}'.format(seatNumber-11,"WS")
            else:
                print("Invalid Seat Number")
    else:
        print("Test count exceeded")