from solid.models.user import User


# não respeita o principio de substituição de liskov, pois não implemeta o metodo pai
class Manager(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    @staticmethod
    def members():
        raise Exception("Member is not authorized to do this")
