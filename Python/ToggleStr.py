inputStr = input()  
string = str();
strArray = list(inputStr);
for i in range(int(len(strArray))):
    if ord(strArray[i])>=65 and ord(strArray[i])<=90: 
        string=string+chr(ord(strArray[i])+32)
    else :
        string=string+chr(ord(strArray[i])-32)
print(string);
