import logging

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import OperationalError

from app.parameters import DB_PG_HOST, DB_PG_PORT, DB_PG_USERNAME, DB_PG_PASSWORD, DB_PG_DATABASE, DB_PG_SCHEMA

Base = declarative_base()

logging.basicConfig(level=logging.INFO)

class DataBase():

    def __init__(self, user=DB_PG_USERNAME, password=DB_PG_PASSWORD, host=DB_PG_HOST, port=DB_PG_PORT, name_db=DB_PG_DATABASE):

        self._url = f"postgresql://{user}:{password}@{host}:{port}/{name_db}"
        self._engine = self._set_engine()
        self._Session = self._set_session()


    def __enter__(self):

        self.session = self._Session()
        self._create_tables()

        return self.session


    def __exit__(self, exc_type, *args):
        
        if exc_type is not None:

            self.session.rollback()

        self.session.commit()
        self.session.close()


    def _set_engine(self):

        try:

            engine = create_engine(self._url)
            logging.info("Successfully connected to the database.")
            
            return engine
        
        except OperationalError as e:

            logging.critical(f"Failed to connect to the database: {e}")
            
            return None
        
    
    def _set_session(self):

        if self._engine:

            return sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        
        else:

            return None
    

    def _create_tables(self):

        Base.metadata.create_all(bind=self._engine, checkfirst=True)


    def _drop_tables(self):
 
        Base.metadata.drop_all(self._engine)


class LeadTb(Base):

    __tablename__ = 'leads'
    __table_args__ = {'schema': DB_PG_SCHEMA}

    lead_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    url_lead = Column(String(250))
    cellphone = Column(String(100))

    def __repr__(self):

        return f"lead_id = {self.lead_id}, name = {self.name}, email = {self.email}, url_lead = {self.url_lead}, cellphone = {self.cellphone}"


class CampaignTb(Base):

    __tablename__ = 'campaigns'
    __table_args__ = {'schema': DB_PG_SCHEMA}

    id_campaign = Column(Integer, primary_key=True)
    name_campaign = Column(String(255))

    def __repr__(self):

        return f"id_campaign = {self.id_campaign}, name_campaign = {self.name_campaign}"


class TaskTb(Base):   

    __tablename__ = 'tasks'
    __table_args__ = {'schema': DB_PG_SCHEMA}

    id_task = Column(Integer, primary_key=True)
    name_task = Column(String(255))

    def __repr__(self):
        
        return f"id_task = {self.id_task}, name_task = {self.name_task}"


class CampaignTaskTb(Base):    

    __tablename__ = 'campaign_tasks'
    __table_args__ = {'schema': DB_PG_SCHEMA}

    id_campaign_task = Column(Integer, primary_key=True)
    id_campaign = Column(Integer, ForeignKey(f'{DB_PG_SCHEMA}.campaigns.id_campaign'))
    id_task = Column(Integer, ForeignKey(f'{DB_PG_SCHEMA}.tasks.id_task'))
    order_number = Column(Integer)

    campaign = relationship("CampaignTb", foreign_keys=[id_campaign])
    task = relationship("TaskTb", foreign_keys=[id_task])

    def __repr__(self):
        return f"id_campaign_task = {self.id_campaign_task}, id_campaign = {self.id_campaign}, id_task = {self.id_task}, order_number = {self.order_number}"


class LeadsCampaignTb(Base):

    __tablename__ = 'leads_campaign'
    __table_args__ = {'schema': DB_PG_SCHEMA}

    lead_id = Column(Integer, ForeignKey(f'{DB_PG_SCHEMA}.leads.lead_id'), primary_key=True)
    campaign_id = Column(Integer, ForeignKey(f'{DB_PG_SCHEMA}.campaigns.id_campaign'), primary_key=True)

    lead = relationship("LeadTb")
    campaign = relationship("CampaignTb")

    def __repr__(self):

        return f"lead_id = {self.lead_id}, campaign_id = {self.campaign_id}"
    
class UserTb(Base):

    __tablename__ = 'users'
    __table_args__ = {'schema': DB_PG_SCHEMA}

    user_id = Column(Integer, primary_key=True)
    email = Column(String(255))
    password = Column(String(255))

    def __repr__(self):
        return f"user_id = {self.user_id}, name = {self.name}, email = {self.email}, username = {self.username}, password = {self.password}"
