from sqlalchemy import Column, Integer, ForeignKey, String, Numeric, DateTime

from .database import Base


class Charity(Base):
    __tablename__ = "charity"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)


class Campaign(Base):
    __tablename__ = "campaign"

    id = Column(Integer, primary_key=True)
    charity_id = Column(Integer, ForeignKey("charity.id"), nullable=False)

    name = Column(String, nullable=False)


class Donor(Base):
    __tablename__ = "donor"

    id = Column(Integer, primary_key=True)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)


class Donation(Base):
    __tablename__ = "donation"

    id = Column(Integer, primary_key=True)

    charity_id = Column(Integer, ForeignKey("charity.id"), nullable=False)
    campaign_id = Column(Integer, ForeignKey("campaign.id"), nullable=True)
    donor_id = Column(Integer, ForeignKey("donor.id"), nullable=False)

    created_at = Column(DateTime, nullable=False)

    amount = Column(Numeric(12, 2), nullable=False)
