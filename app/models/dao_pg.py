import logging

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import OperationalError

from parameters import DB_PG_HOST, DB_PG_PORT, DB_PG_DATABASE, DB_PG_USERNAME, DB_PG_PASSWORD, DB_PG_SCHEMA 

Base = declarative_base()

class Lead(Base):

    __tablename__ = 'leads'

    lead_id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100))
    url_lead = Column(String(250))
    cellphone = Column(String(100))


class Campaign(Base):

    __tablename__ = 'campaigns'

    id_campaign = Column(Integer, primary_key=True)
    name_campaign = Column(String(255))


class Task(Base):

    __tablename__ = 'tasks'

    id_task = Column(Integer, primary_key=True)
    name_task = Column(String(255))


class CampaignTask(Base):

    __tablename__ = 'campaign_tasks'

    id_campaign_task = Column(Integer, primary_key=True)
    id_campaign = Column(Integer, ForeignKey('campaigns.id_campaign'))
    id_task = Column(Integer, ForeignKey('tasks.id_task'))
    order_number = Column(Integer)

    campaign = relationship("Campaign")
    task = relationship("Task")


class LeadsCampaign(Base):

    __tablename__ = 'leads_campaign'

    lead_id = Column(Integer, ForeignKey('leads.lead_id'), primary_key=True)
    campaign_id = Column(Integer, ForeignKey('campaigns.id_campaign'), primary_key=True)

    lead = relationship("Lead")
    campaign = relationship("Campaign")


class DataBase():

    def __init__(self, user=DB_PG_USERNAME, password=DB_PG_PASSWORD, host=DB_PG_HOST, port=DB_PG_PORT, name_db=DB_PG_DATABASE, schema=DB_PG_SCHEMA):

        self._url = f"postgresql://{user}:{password}@{host}:{port}/{name_db}?schema={schema}"
        self._engine = self.set_engine()
        self._Session = self.set_session()
        self.Lead = Lead
        self.Campaign = Campaign
        self.Task = Task
        self.CampaignTask = CampaignTask
        self.LeadsCampaign = LeadsCampaign

    def __enter__(self):

        self.session = self._Session()
        self._create_tables()

        return self


    def __exit__(self, exc_type):
        
        if exc_type is not None:

            self.session.rollback()

        self.session.commit()
        self.session.close()


    def set_engine(self):

        try:

            engine = create_engine(self._url)
            logging.info("Successfully connected to the database.")
            
            return engine
        
        except OperationalError as e:

            logging.critical(f"Failed to connect to the database: {e}")
            
            return None
        
    
    def set_session(self):

        if self._engine:

            return sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        
        else:

            return None
    

    def _create_tables(self):

        Base.metadata.create_all(self._engine, checkfirst=True)


    def _drop_tables(self):
 
        Base.metadata.drop_all(self._engine)



