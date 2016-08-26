import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

engine = sqlalchemy.create_engine('sqlite:////users/erinrossiter/Dropbox/Summer2016/pythoncourse2016/Day9/cases.db', echo=True)

Base = declarative_base() 

class Case(Base):
	__tablename__ = "cases"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	year = Column(Integer)
	court_id = Column(Integer, ForeignKey("courts.id"))
	def __init__(self, name, year, court=None):
		self.name = name
		self.year = year
		self.court = court
	def __repr__(self):
		return str(self.name)

class Court(Base):
	__tablename__ = "courts"
	id = Column(Integer, primary_key=True)
	name = Column(String)
	jurisdiction = Column(String)
	cases = relationship("Case", backref="court")
	def __init__(self, name, jurisdiction):
		self.name = name
		self.jurisdiction = jurisdiction
	def __repr__(self):
		return str(self.name)


Base.metadata.create_all(engine) 

Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
	Court("Supreme Court", "federal"),
	Court("California", "state")
])

session.commit()
