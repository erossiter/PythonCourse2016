from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

## This is saying I'll be reading in classes
## and using them.
Base = automap_base()

engine = create_engine('sqlite:////users/erinrossiter/Dropbox/Summer2016/pythoncourse2016/Day9/players.db')

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
Player = Base.classes.players
Team = Base.classes.teams

session = Session(engine)

for player in session.query(Player).order_by(Player.number):
  print player.number, player.name, player.id

[team.name for team in session.query(Team)]

