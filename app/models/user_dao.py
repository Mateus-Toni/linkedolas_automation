from pydantic import EmailStr
import logging

from app.models.dao_pg import DataBase, UserTb

class UserDao:

    @staticmethod
    def register_user_db(user):
        
        try:
        
            with DataBase() as session:
                
                user_create = UserTb(**user.dict())
                
                session.add(user_create)
                
            return True
                
        except Exception as e:
            
            logging.critical(e)
            
            return False
            
    @staticmethod
    def get_user_by_email(email: EmailStr):
        
        with DataBase() as session:
        
            return session.query(UserTb).filter_by(email=email).first()
            