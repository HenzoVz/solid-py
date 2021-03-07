from solid.models.user_lsp import User


class Member(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    @staticmethod
    def members():
        return ["username1", "username2", "username3"]

    def work(self):
        return "Coding..."
