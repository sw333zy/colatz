def colatz():
    cont = input('Would you like to play?(y/n) ')
    num = input('Enter a number: ')
    usernum = int(num)
   
       
    while (usernum!=1) & (cont=="y"):
        if usernum%2==0:
            usernum = usernum/2
            print(usernum)
            cont = input('Continue? ')

        else:
            usernum = usernum*3+1
            print(usernum)
            cont = input('Continue? ')
        

colatz()
