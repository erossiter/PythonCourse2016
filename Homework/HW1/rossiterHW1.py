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
		transaction = "$%s added. Previous balance: $%s. Existing balance: $%s." % (amount, priorBalance, self.cash)
		self.transactions.append(transaction)
	
	def withdrawCash(self, amount):
		if self.cash - amount < 0:
			raise Exception("Account does not have sufficient funds.")
		priorBalance = self.cash
		self.cash -= amount
		transaction = "$%s withdrawn. Previous balance: $%s. Existing balance: $%s." % (amount, priorBalance, self.cash)
		self.transactions.append(transaction)
	
	def buyMutualFund(self, shares, mf):
		return mf.buy(self, shares)
	
	def sellMutualFund(self, shares, mf):
		return mf.sell(self, shares)
		
	def buyStock(self, shares, s):
		return s.buy(self, shares)
	
	def sellStock(self, shares, s):
		return s.sell(self, shares)
		
	def history(self):
		print "Transaction History:"
		print '\n'.join(portfolio.transactions)

	def __str__(self):
		stocks = ""
		mutualFunds = ""
		for s in self.stocks.keys():
			stocks += "\t %s: %s \n" % (self.stocks[s], s)
		for m in self.mutualFunds.keys():
			mutualFunds += "\t %s: %s \n" % (self.mutualFunds[m], m)
 		output = "Portfolio Summary:\n"
 		output += "Cash:\n\t %s \n" % self.cash
 		output += "Stocks:\n %s" % stocks
 		output += "MutualFunds:\n %s" % mutualFunds
		return output

	def __repr__(self):
		return self.__str__



class Asset(object):
	def __init__(self, price, symbol):
		self.price = price
		self.symbol = symbol

	def buy(self):
		raise NotImplementedError("Subclass must implement abstract method")
		
	def sell(self):
		raise NotImplementedError("Subclass must implement abstract method")


		
class MutualFund(Asset):
	def __init__(self, symbol):
		Asset.__init__(self, 1, symbol)
		
	def buy(self, portfolio, shares):
		if self.symbol in portfolio.mutualFunds.keys():
			portfolio.mutualFunds[self.symbol] += shares
		else:
			portfolio.mutualFunds[self.symbol] = shares
		transaction = "Purchasing %s shares of %s mutual fund at $1/share" % (shares, self.symbol)
		portfolio.transactions.append(transaction)
  		portfolio.withdrawCash(shares)
  	
  	def sell(self, portfolio, shares):
  		if self.symbol in portfolio.mutualFunds.keys():
			portfolio.mutualFunds[self.symbol] -= shares
		else:
			raise Exception("Mutual Fund must exist in portfolio to sell.")
		sell_price = round(random.uniform(0.9, 1.2), 2)
		transaction = "Selling %s shares of %s mutual fund at $%s/share" % (shares, self.symbol, sell_price)
		portfolio.transactions.append(transaction)
  		portfolio.addCash(sell_price * shares, 2)
		
	def __str__(self):
		return "Mutual fund %s can be purchased at $%s/share." % (self.symbol, self.price)
		
	

class Stock(Asset):
	def buy(self, portfolio, shares):
	  	if not isinstance(shares, int):
  			raise TypeError("Shares to buy must be an integer")
		if self.symbol in portfolio.stocks.keys():
			portfolio.stocks[self.symbol] += shares
		else:
			portfolio.stocks[self.symbol] = shares
		transaction = "Purchasing %s shares of %s stock at $%s/share" % (shares, self.symbol, self.price)
		portfolio.transactions.append(transaction)
  		portfolio.withdrawCash(shares * self.price)
  		
  	def sell(self, portfolio, shares):
  		if not isinstance(shares, int):
  			raise TypeError("Shares to sell must be an integer")
  			
  		if self.symbol in portfolio.stocks.keys():
			portfolio.stocks[self.symbol] -= shares
		else:
			raise Exception("Stock must exist in portfolio to sell.")
		sell_price = round(random.uniform(0.5 * self.price , 1.5 * self.price), 2)
		transaction = "Selling %s shares of %s stock at $%s/share" % (shares, self.symbol, sell_price)
		portfolio.transactions.append(transaction)
  		portfolio.addCash(sell_price * shares)

	def __str__(self):
		return "Stock %s can be purchased at $%s/share." % (self.symbol, self.price)


		




## TESTING ##
portfolio = Portfolio()
portfolio.addCash(300.50)
#portfolio.withdrawCash(200)

s = Stock(20, "HFH")
s2 = Stock(10, "ABC")
print s2
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
print mf2


portfolio.buyStock(5, s)
portfolio.buyStock(2, s)
portfolio.buyStock(3, s2)
portfolio.buyMutualFund(10, mf1)
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


		