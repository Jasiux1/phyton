from turtle import*
def sigma():
    print("czesc")
    print("podaj liczbe")
    x=int(input())
    if x <= 5:
        print("źle")
        pensize(3)
        penup()      
        goto(0, -100)
        pendown()
        circle(100)
        color("red")
        penup()
        goto(-70, 70)
        pendown()
        goto(70,-70)
        penup()
        goto(-70, -70)
        pendown()
        goto(70,70)
        
    else:
        print("dobrze")
        pensize(3)
        penup()      
        goto(0, -100) 
        pendown()     
        circle(100)
        color("green")
        penup()
        goto(-50, 0)  
        pendown()
        goto(-10, -40)  
        goto(50, 40)
        
    

        

        

sigma()
#