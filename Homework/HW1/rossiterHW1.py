import random

class Portfolio(object):
	def __init__(self):
		self.transactions = []
		self.cash = 0
		self.stocks = {}
		self.mutualFunds = {}
	
	## When cash is added or withdrawn, a transaction is added
	## to the log and the cash variable is altered.
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
	
	## Buy and sell methods are defined in the respective
	## object classes and called here with the . operator
	def buyMutualFund(self, shares, mf):
		return mf.buy(self, shares)
	
	def sellMutualFund(self, shares, mf):
		return mf.sell(self, shares)
		
	def buyStock(self, shares, s):
		return s.buy(self, shares)
	
	def sellStock(self, shares, s):
		return s.sell(self, shares)
	
	## 'transactions' is a member variable, appended with a string
	## each time cash is added or withdrawn.  Therefore, printing each
	## element of 'transactions' on a new line orders them by time.
	def history(self):
		print "TRANSACTION HISTORY:"
		print '\n'.join(portfolio.transactions)

	def __str__(self):
		stocks = ""
		mutualFunds = ""
		for s in self.stocks.keys():
			stocks += "\t %s: %s \n" % (self.stocks[s], s)
		for m in self.mutualFunds.keys():
			mutualFunds += "\t %s: %s \n" % (self.mutualFunds[m], m)
 		output = "PORTFOLIO SUMMARY:\n"
 		output += "Cash:\n\t %s \n" % self.cash
 		output += "Stocks:\n %s" % stocks
 		output += "MutualFunds:\n %s" % mutualFunds
		return output

	def __repr__(self):
		return self.__str__


## 'Asset' class allows for other asset classes, such as bonds,
## to be added as subclasses in the future.  
class Asset(object):
	def __init__(self, price, symbol):
		self.price = price
		self.symbol = symbol

	def buy(self):
		raise NotImplementedError("Subclass must implement abstract method")
		
	def sell(self):
		raise NotImplementedError("Subclass must implement abstract method")


## 'Asset' subclasses, 'MutualFund' and 'Stock' define buy and
## sell methods, called upon in the 'Portfolio' Class.		
class MutualFund(Asset):
	## MutualFund objects are initialized to have price = $1/share.
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
  	
  	## 'sell_price' is determined by drawing from the
  	## uniform distribution in the specified range,
  	## then rounding by 2 to represent a real $$ value.
  	def sell(self, portfolio, shares):
  		if self.symbol in portfolio.mutualFunds.keys():
			portfolio.mutualFunds[self.symbol] -= shares
		else:
			raise Exception("Mutual Fund must exist in portfolio to sell.")
		sell_price = round(random.uniform(0.9, 1.2), 2)
		transaction = "Selling %s shares of %s mutual fund at $%s/share" % (shares, self.symbol, sell_price)
		portfolio.transactions.append(transaction)
  		portfolio.addCash(sell_price * shares)
		
	def __str__(self):
		return "Mutual fund %s can be purchased at $%s/share." % (self.symbol, self.price)
	
	def __repr__(self):
		return self.__str__
	

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
  	
  	## 'sell_price' is determined by drawing from the uniform distribution
  	## in the specified range, with the lower and upper bounds scaled by the
  	## price at which the stock was purchased
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

	def __repr__(self):
		return self.__str__

		




######################
###### TESTING #######
######################

portfolio = Portfolio()
portfolio.addCash(300.50)
portfolio.withdrawCash(50)

s = Stock(20, "HFH")
s2 = Stock(10, "ABC")
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")

print s2
print mf2

portfolio.buyStock(5, s)
portfolio.buyStock(2, s)
portfolio.buyStock(3, s2)
portfolio.buyMutualFund(10, mf1)
portfolio.buyMutualFund(2, mf2)
portfolio.buyMutualFund(5, mf2)
 
portfolio.sellStock(1, s)
portfolio.sellMutualFund(1, mf1)

## All of these throw errors as expected.
#portfolio.sellStock(1, s2) 
#portfolio.sellStock(1.5, s2)
#portfolio.buyStock(1.5, s2)
#portfolio.buyStock(1000, s)

portfolio.history()
print portfolio
portfolio

		