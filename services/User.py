from repositories.User import UserRepository
class UserService:
    def __init__(self):
        self.userRepo: UserRepository = UserRepository()

    def insertUser(self):
        self.userRepo.insertUser()