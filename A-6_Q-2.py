class game:

    import random
                                                                                                         
    c=random.randint(1,10)
    print("the total number of game you can play: ",c)
    count=0
    for j in range(c): 
        a= input("enter your choice from ['rock','paper','scisor']: ")
        print("your choice is: ",a)
        computer= ["rock","paper","scisor"]
        b= random.choice(computer)
        print("computer's choice is: ",b)
        for i in computer:
            if(b==a):
                print("the match is draw")
                break
            elif(a=="rock" and b=="scisor"):
                print("you win")
                count=count+1
                break
            elif(a=="rock" and b=="paper"):
                print("you lose")
                count=count - 1 
                break
            elif(a=="paper" and b=="rock"):
                print("you win")
                count=count+1
                break
            elif(a=="paper" and b=="scisor"):
                print("you lose")
                count=count - 1 
                break
            elif(a=="scisor" and b=="rock"):
                print("you lose")
                count=count - 1
                break
            elif(a=="scisor" and b=="paper"):
                print("you win")
                count=count+1
                break
    
    if(count>0):
        print("the total number of game you won: ",count)
        print("overall you win")
    elif(count<0):
       count = - count
       print("the total number of game you lose: ",count)
       print("overall computer is win")
    else:
        print("overall no one win")
rock= game()