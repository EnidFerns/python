import random
def choose():
    words=["rainbow","animal","player","crocodile","elephant","fireworks","television","search","courses","phsycology","transcript","uniform","jargon","vase","watermellon","refrigerator","laptop","desktop","seashore","application","tubelight"]
    pick=random.choice(words)
    return pick

def jumble(word):#jumble letters and join the elements of the list to get a jumbled word
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(playersname1,playersname2,pointsof1,pointsof2):
    print(playersname1,", your score is: ",pointsof1)
    print(playersname2,", your score is: ",pointsof2)
    print("thanks for playing")
    
def play():
    playersname1= input("enter player ones name: ")
    playersname2= input("enter player twos name: ")
    pointsof1=0
    pointsof2=0
    turn=0
    while(1):
        #computer choses word
        picked_word=choose()
        #creates question
        q=jumble(picked_word)
       
        #player1
        if(turn%2==0):  #odd number remainder is 1; even  number remainder is 0 '%'
            print(playersname1,", its your turn!")
            print(q)
            ans=input("whats on my mind?")
            if(ans==picked_word):
                pointsof1=pointsof1+1
                print("your score: ",pointsof1)
            else:
                print("you're wrong! the word is ",picked_word)
        
        #player2
        else:
            print(playersname2,", its your turn!")
            print(q)
            ans=input("whats on my mind?")
            if(ans==picked_word):
                pointsof1=pointsof2+1
                print("your score: ",pointsof2)
            else:
                print("you're wrong! the word is ",picked_word)
        c=int(input("press 1 to continue or 0 to quit. "))
        if c==0:
            thank(playersname1,playersname2,pointsof1,pointsof2)
            break
        turn=turn+1
play()  
