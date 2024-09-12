'''
Uppgift 1
'''
# input

allowance = input("what is your allowance?")
cost_of_candy = input("how much is the candy?")

#calculation

money_left = int(allowance) - int(cost_of_candy)

#output

print("you have " + str(money_left) + "kr left")