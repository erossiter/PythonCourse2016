class Portfolio(object):
	
	def __init__(self):
		self.transactions = []
		self.cash = 0
		self.stocks = 0
		self.mutualFunds = 0
	
	def addCash(self, amount):
		priorBalance = self.cash
		self.cash += amount
		transaction = "$%s added to account. Balance was $%s.  Balance is now $%s." % (amount, priorBalance, self.cash)
		self.transactions.append(transaction)
	
	def withdrawCash(self, amount):
		priorBalance = self.cash
		self.cash -= amount
		transaction = "$%s withdrawn from account. Balance was $%s.  Balance is now $%s." % (amount, priorBalance, self.cash)
		self.transactions.append(transaction)
		
	def history(self):
		print '\n'.join(portfolio.transactions)
		
	def __str__(self):
		output = "Cash: $%s \n" % self.cash
		output += "Stocks: %s \n" % self.stocks
		output += "Mutual Funds: %s \n" % self.mutualFunds
		return output
		
class MutualFund(object):

	def __init__(self, symbol):
		self.symbol = symbol


class Stock(object):

	def __init__(self, symbol):
		self.symbol = symbol
		

portfolio = Portfolio()
portfolio.addCash(300.50)
portfolio.withdrawCash(200)
portfolio.history()
print portfolio


# 	def buy(self):
# 		lakdjfk
# 	
# 	def sell(self):
# 		slkflsdf
# 
# 

# 
# class MutualFund(object):
		
		