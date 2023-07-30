print("CRAPS賭博遊戲")
print("說明：CRAPS又稱花旗骰，是美國拉斯維加斯非常受歡迎的一種的桌上賭博遊戲該遊戲使用兩粒骰子")
print("玩家通過搖兩粒骰子獲得點數進行遊戲。")
print("簡單的規則是：玩家第一次搖骰子如果搖出了7點或11點，玩家勝")
print("玩家第一次如果搖出2點、3點或12點，莊家勝")
print("其他點數玩家繼續搖骰子，如果玩家搖出了7點，莊家勝")
print("如果玩家搖出了第一次搖的點數，玩家勝；其他點數，玩家繼續要骰子，直到分出勝負。")
import random                                       #導入random模組#
number=[1,2,3,4,5,6]   
money=int(input("請輸入總資產:"))
while money>=0:                                     #第一循環#
    add=0                                           #將add歸0#
    a=0                                             #將a歸0#
    b=1                                             #b為一局進行幾次#
    if money == 0:
        print("金額為0，無法繼續玩")  
        break                                       #若money等於0就跳出第一循環#
    c=int(input("請輸入要賭注的金額:"))              #c為賭注金額#
    while True:                                     #第二循環#
        if c>money:
            print("金額不足,請重新輸入賭注金額")      #賭注金額若大於總資產，就重新輸入賭注金額#
            c=int(input("請輸入要賭注的金額:"))
        else:
            break                                   #若賭注金額小於等於總資產，則跳出第二循環#
    a=random.choices(number,k=2)                    #從num串列取2個隨機元素放入a#
    add=a[0]+a[1]                                   #骰2次的點數和#
    print("你第一次的點數和為",add)
    if add ==7 or add == 11 :                       #若點數和等於7或11#
        print("第",b,"次擲骰,玩家獲勝") 
            money+=c                                #新總資產=原總資產+賭注金額#
            print("現在金額為%d\n"%money)
    elif add == 2 or add == 3 or add == 12:         #若點數和等於2、3或12#
        print("第",b,"次擲骰,莊家獲勝")
        money-=c                                    #新總資產=原總資產-賭注金額#
        print("現在金額為%d\n"%money)
    else:                                           #若第一次點數和不等於2、3、7、11或12就執行#
        while True:                                 #第三循環#
            a=0                                     #將a歸0#
            add1=0                                  #將add1歸0#
            a=random.choices(number,k=2)            #再次從num串列取2個隨機元素放入a#
            add1=a[0]+a[1]                          #add1為第b回合的點數和#
            b=b+1                                   #回合+1#
            print("第",b,"次的點數為",add1)
            if add1 ==11 or add1 == add :           #若add1等於11或第一次點數和#
                print("玩家獲勝")
                money+=c                            #新總資產=原總資產+賭注金額#
                print("現在金額為%d\n"%money)
                break                               #打破第三循環#
            elif add1 == 2 or add1 == 3 or add1 == 7 or add1 == 12:   #若add1等於2、3、7或12#
                print("莊家獲勝")
                money-=c                            #新總資產=原總資產-賭注金額#
                print("現在金額為%d\n"%money)
                break                               #打破第三循環#
            else:
                continue                            #跳過本次的迴圈，進行下一圈#
       

