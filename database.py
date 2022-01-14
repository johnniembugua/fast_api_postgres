from curses import echo
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("postgresgl://postgres:john@localhost/item_db",
echo=True)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)


