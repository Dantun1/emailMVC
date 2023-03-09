import sqlalchemy as db
import main

engine = db.create_engine('sqlite:///emails.sqlite', echo=True)

main.Base.metadata.create_all(engine)