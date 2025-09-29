class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def __repr__(self) -> str:
        return f"User(name={self.username}, email={self.email})"

    def get_user_info(self):
        return {
            "username": self.username,
            "email": self.email
        }

    def set_email(self, new_email):
        self.email = new_email