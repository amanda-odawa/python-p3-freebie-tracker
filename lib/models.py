from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship('Freebie', backref='company')

    def retrieve_devs(self):
        # Display list of unique developers who received freebies from a company
        # Converting set to a list automatically removes duplicates
        return list({freebie.dev for freebie in self.freebies})
    
    def give_freebie(self, session, dev, item_name, value):
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        session.add(new_freebie)
        session.commit()

    def oldest_company(session):
        return session.query(Company).order_by(Company.founding_year.asc()).first()

    def __repr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    freebies = relationship('Freebie', backref='dev')

    def retrieve_companies(self):
        return list({freebie.company for freebie in self.freebies})
    
    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)
    
    def give_away(self, dev, freebie, session):
        if freebie.dev_id == self.id:
            freebie.dev = dev 
            session.commit()
            print(f"{self.name} gave away {freebie.item_name} to {dev.name}.")
        else:
            print(f"Transfer failed: {self.name} does not own {freebie.item_name}.")

    def __repr__(self):
        return f'<Dev {self.name}>'
    
class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())

    dev_id = Column(Integer(), ForeignKey('devs.id'))
    company_id = Column(Integer(), ForeignKey('companies.id'))

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}."

    def __repr__(self):
        return f'<Freebie {self.item_name}>'