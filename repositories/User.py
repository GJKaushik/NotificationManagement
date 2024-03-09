from appconfig import config
from entities.User import UserEntity
from DBInit import db

class UserRepository:
    def __init__(self):
        self.config = config

    def insertUser(self):
        
        user = UserEntity(username='john', email='john@example.com')
        db.session.add(user)
        db.session.commit()

        # # Query all users
        # users = UserEntity.query.all()