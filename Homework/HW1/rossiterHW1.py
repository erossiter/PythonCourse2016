import random

class Portfolio(object):
	
	def __init__(self):
		self.transactions = []
		self.cash = 0
		self.stocks = {}
		self.mutualFunds = {}
	
	def addCash(self, amount):
		priorBalance = self.cash
		self.cash += amount
		transaction = "$%s added. Prev balance: $%s. Existing balance: $%s." % (amount, priorBalance, self.cash)
		self.transactions.append(transaction)
	
	def withdrawCash(self, amount):
		if self.cash - amount < 0:
			raise Exception("Account does not have sufficient funds.")
		priorBalance = self.cash
		self.cash -= amount
		transaction = "$%s withdrawn. Prev balance: $%s. Existing balance: $%s." % (amount, priorBalance, self.cash)
		self.transactions.append(transaction)
		
	def buyMutualFund(self, shares, mf):
		if mf.symbol in self.mutualFunds.keys():
			self.mutualFunds[mf.symbol] += shares
		else:
			self.mutualFunds[mf.symbol] = shares
		transaction = "Purchasing %s shares of %s mutual fund at $1" % (shares, mf.symbol)
		self.transactions.append(transaction)
  		self.withdrawCash(shares)

	def buyStock(self, shares, s):
	  	if not isinstance(shares, int):
  			raise TypeError("Shares to buy must be an integer")
	
		if s.symbol in self.stocks.keys():
			self.stocks[s.symbol] += shares
		else:
			self.stocks[s.symbol] = shares
		transaction = "Purchasing %s shares of %s stock at $%s" % (shares, s.symbol, s.price)
		self.transactions.append(transaction)
  		self.withdrawCash(shares)
  		
  	def sellStock(self, shares, s):
  		if not isinstance(shares, int):
  			raise TypeError("Shares to sell must be an integer")
  			
  		if s.symbol in self.stocks.keys():
			self.stocks[s.symbol] -= shares
		else:
			raise Exception("Stock must exist in portfolio to sell.")
		sell_price = round(random.uniform(0.5 * s.price , 1.5 * s.price), 2)
		transaction = "Selling %s shares of %s stock at $%s" % (shares, s.symbol, sell_price)
		self.transactions.append(transaction)
  		self.addCash(sell_price * shares)
  		
  	def sellMutualFunds(self, shares, mf):
  		if mf.symbol in self.mutualFunds.keys():
			self.mutualFunds[mf.symbol] -= shares
		else:
			raise Exception("Mutual Fund must exist in portfolio to sell.")
		sell_price = round(random.uniform(0.9, 1.2), 2)
		transaction = "Selling %s shares of %s mutual fund at $%s" % (shares, mf.symbol, sell_price)
		self.transactions.append(transaction)
  		self.addCash(sell_price * shares, 2)

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

	def __init__(self, price, symbol):
		self.price = price
		self.symbol = symbol
		

## TESTING ##
portfolio = Portfolio()
portfolio.addCash(300.50)
portfolio.withdrawCash(200)

s = Stock(20, "HFH")
s2 = Stock(10, "ABC")
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")


portfolio.buyStock(5, s)
portfolio.buyStock(2, s)
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
portfolio.buyMutualFund(5, mf2)

portfolio.sellStock(1, s)

## All of these throw errors as expected.
#portfolio.sellStock(1, s2) 
#portfolio.sellStock(1.5, s2)
#portfolio.buyStock(1.5, s2)
#portfolio.buyStock(1000, s)

portfolio.history()
print portfolio
portfolio


		