IntroString=input("EnterYourIntroduction")
characterCount=0
wordCount=1
for i in IntroString:
    characterCount=characterCount+1
    if(i==' '):
        wordCount=wordCount+1
print("number of word in this string")  
print(wordCount)
print("number of characters in the string") 
print(characterCount)    

    
