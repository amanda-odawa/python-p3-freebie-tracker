#!/usr/bin/env python3

# Script goes here! Create sample data to test your models and associations
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Company, Dev, Freebie, Base

# Database engine
engine = create_engine('sqlite:///freebies.db')

# Create tables if they don't exist
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Sample companies
nvidia = Company(name='NVIDIA', founding_year=1993)
zoom = Company(name='Zoom Video Communications', founding_year=2011)
intel = Company(name='Intel', founding_year=1968)
adobe = Company(name='Adobe', founding_year=1982)
tesla = Company(name='Tesla', founding_year=2003)

# Sample developers
alice = Dev(name='Alice')
bob = Dev(name='Bob')
charlie = Dev(name='Charlie')
pancakes = Dev(name='Pancakes')
amanda = Dev(name='Amanda')

# Sample freebies
freebie1 = Freebie(item_name='T-Shirt', value=20, company=nvidia, dev=alice)  
freebie2 = Freebie(item_name='Backpack', value=50, company=zoom, dev=bob)  
freebie3 = Freebie(item_name='Wireless Mouse', value=30, company=intel, dev=charlie)  
freebie4 = Freebie(item_name='Sticker Pack', value=5, company=adobe, dev=pancakes)  
freebie5 = Freebie(item_name='Water Bottle', value=25, company=tesla, dev=amanda)  
freebie6 = Freebie(item_name='Laptop Stand', value=40, company=intel, dev=alice)  
freebie7 = Freebie(item_name='Notebook', value=15, company=adobe, dev=bob)  

# Add all data to session and commit session
session.add_all([nvidia, zoom, intel, adobe, tesla, alice, bob, charlie, pancakes, amanda, freebie1, freebie2, freebie3, freebie4, freebie5, freebie6, freebie7])
session.commit()

# Confirm seeding worked
print("\n Database successfully seeded!") 
print(f"Companies: {session.query(Company).all()}") #5
print(f"Developers: {session.query(Dev).all()}") #5
print(f"Freebies: {session.query(Freebie).all()}") #7

# Close session
session.close()
