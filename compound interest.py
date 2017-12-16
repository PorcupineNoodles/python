'''
def invest(amount,rate,time):
#    amount = input("How much are the Invest Amount?")
#    rate = input("What is the Invest Rate?")
#    time = input("How much are the InvestTime?")
    print( "principal amount:{}".format(amount))
    for t in range( 1 , time + 1):
        amount = amount * (1 + float(rate) )
        print("year {}: ${}".format(t,amount))
invest(100,0.05,5)
'''

def invest():
    Investamount = int(input("How much are the Invest Amount?"))
    Investrate = float(input("What is the Invest Rate?"))
    InvestTime =int(input("How much are the InvestTime?"))
    for i in range( 1 , InvestTime + 1):
        money = (Investamount * (1 + Investrate)) ** i
        print("year {} 总资金:${}".format(i,money))
invest()
